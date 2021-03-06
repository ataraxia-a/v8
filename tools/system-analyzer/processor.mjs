// Copyright 2020 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import {LogReader, parseString, parseVarArgs} from '../logreader.mjs';
import {Profile} from '../profile.mjs';

import {CodeLogEntry, DeoptLogEntry} from './log/code.mjs';
import {IcLogEntry} from './log/ic.mjs';
import {Edge, MapLogEntry} from './log/map.mjs';
import {Timeline} from './timeline.mjs';

// ===========================================================================

export class Processor extends LogReader {
  _profile = new Profile();
  _mapTimeline = new Timeline();
  _icTimeline = new Timeline();
  _deoptTimeline = new Timeline();
  _codeTimeline = new Timeline();
  _formatPCRegexp = /(.*):[0-9]+:[0-9]+$/;
  MAJOR_VERSION = 7;
  MINOR_VERSION = 6;
  constructor(logString) {
    super();
    const propertyICParser = [
      parseInt, parseInt, parseInt, parseInt, parseString, parseString,
      parseString, parseString, parseString, parseString
    ];
    this.dispatchTable_ = {
      __proto__: null,
      'v8-version': {
        parsers: [
          parseInt,
          parseInt,
        ],
        processor: this.processV8Version
      },
      'code-creation': {
        parsers: [
          parseString, parseInt, parseInt, parseInt, parseInt, parseString,
          parseVarArgs
        ],
        processor: this.processCodeCreation
      },
      'code-deopt': {
        parsers: [
          parseInt, parseInt, parseInt, parseInt, parseInt, parseString,
          parseString, parseString
        ],
        processor: this.processCodeDeopt
      },
      'code-move':
          {parsers: [parseInt, parseInt], processor: this.processCodeMove},
      'code-delete': {parsers: [parseInt], processor: this.processCodeDelete},
      'code-source-info': {
        parsers: [
          parseInt, parseInt, parseInt, parseInt, parseString, parseString,
          parseString
        ],
        processor: this.processCodeSourceInfo
      },
      'script-source': {
        parsers: [parseInt, parseString, parseString],
        processor: this.processScriptSource
      },
      'sfi-move':
          {parsers: [parseInt, parseInt], processor: this.processFunctionMove},
      'map-create':
          {parsers: [parseInt, parseString], processor: this.processMapCreate},
      'map': {
        parsers: [
          parseString, parseInt, parseString, parseString, parseInt, parseInt,
          parseInt, parseString, parseString
        ],
        processor: this.processMap
      },
      'map-details': {
        parsers: [parseInt, parseString, parseString],
        processor: this.processMapDetails
      },
      'LoadGlobalIC': {
        parsers: propertyICParser,
        processor: this.processPropertyIC.bind(this, 'LoadGlobalIC')
      },
      'StoreGlobalIC': {
        parsers: propertyICParser,
        processor: this.processPropertyIC.bind(this, 'StoreGlobalIC')
      },
      'LoadIC': {
        parsers: propertyICParser,
        processor: this.processPropertyIC.bind(this, 'LoadIC')
      },
      'StoreIC': {
        parsers: propertyICParser,
        processor: this.processPropertyIC.bind(this, 'StoreIC')
      },
      'KeyedLoadIC': {
        parsers: propertyICParser,
        processor: this.processPropertyIC.bind(this, 'KeyedLoadIC')
      },
      'KeyedStoreIC': {
        parsers: propertyICParser,
        processor: this.processPropertyIC.bind(this, 'KeyedStoreIC')
      },
      'StoreInArrayLiteralIC': {
        parsers: propertyICParser,
        processor: this.processPropertyIC.bind(this, 'StoreInArrayLiteralIC')
      },
    };
    if (logString) this.processString(logString);
  }

  printError(str) {
    console.error(str);
    throw str
  }

  processString(string) {
    let end = string.length;
    let current = 0;
    let next = 0;
    let line;
    let i = 0;
    let entry;
    try {
      while (current < end) {
        next = string.indexOf('\n', current);
        if (next === -1) break;
        i++;
        line = string.substring(current, next);
        current = next + 1;
        this.processLogLine(line);
      }
    } catch (e) {
      console.error(`Error occurred during parsing, trying to continue: ${e}`);
    }
    this.finalize();
  }

  processLogFile(fileName) {
    this.collectEntries = true;
    this.lastLogFileName_ = fileName;
    let i = 1;
    let line;
    try {
      while (line = readline()) {
        this.processLogLine(line);
        i++;
      }
    } catch (e) {
      console.error(
          `Error occurred during parsing line ${i}` +
          ', trying to continue: ' + e);
    }
    this.finalize();
  }

  finalize() {
    // TODO(cbruni): print stats;
    this._mapTimeline.transitions = new Map();
    let id = 0;
    this._mapTimeline.forEach(map => {
      if (map.isRoot()) id = map.finalizeRootMap(id + 1);
      if (map.edge && map.edge.name) {
        const edge = map.edge;
        const list = this._mapTimeline.transitions.get(edge.name);
        if (list === undefined) {
          this._mapTimeline.transitions.set(edge.name, [edge]);
        } else {
          list.push(edge);
        }
      }
    });
  }

  /**
   * Parser for dynamic code optimization state.
   */
  parseState(s) {
    switch (s) {
      case '':
        return Profile.CodeState.COMPILED;
      case '~':
        return Profile.CodeState.OPTIMIZABLE;
      case '*':
        return Profile.CodeState.OPTIMIZED;
    }
    throw new Error(`unknown code state: ${s}`);
  }

  processCodeCreation(type, kind, timestamp, start, size, name, maybe_func) {
    let entry;
    if (maybe_func.length) {
      const funcAddr = parseInt(maybe_func[0]);
      const state = this.parseState(maybe_func[1]);
      entry = this._profile.addFuncCode(
          type, name, timestamp, start, size, funcAddr, state);
    } else {
      entry = this._profile.addCode(type, name, timestamp, start, size);
    }
    this._codeTimeline.push(new CodeLogEntry(type, timestamp, kind, entry));
  }

  processCodeDeopt(
      timestamp, codeSize, instructionStart, inliningId, scriptOffset,
      deoptKind, deoptLocation, deoptReason) {
    this._deoptTimeline.push(new DeoptLogEntry(
        deoptKind, timestamp, deoptReason, deoptLocation, scriptOffset,
        instructionStart, codeSize, inliningId));
  }

  processV8Version(majorVersion, minorVersion) {
    if ((majorVersion == this.MAJOR_VERSION &&
         minorVersion <= this.MINOR_VERSION) ||
        (majorVersion < this.MAJOR_VERSION)) {
      window.alert(
          `Unsupported version ${majorVersion}.${minorVersion}. \n` +
          `Please use the matching tool for given the V8 version.`);
    }
  }

  processScriptSource(scriptId, url, source) {
    this._profile.addScriptSource(scriptId, url, source);
  }

  processCodeMove(from, to) {
    this._profile.moveCode(from, to);
  }

  processCodeDelete(start) {
    this._profile.deleteCode(start);
  }

  processFunctionMove(from, to) {
    this._profile.moveFunc(from, to);
  }

  processCodeSourceInfo(
      start, script, startPos, endPos, sourcePositions, inliningPositions,
      inlinedFunctions) {
    this._profile.addSourcePositions(
        start, script, startPos, endPos, sourcePositions, inliningPositions,
        inlinedFunctions);
  }

  processPropertyIC(
      type, pc, time, line, column, old_state, new_state, map, key, modifier,
      slow_reason) {
    let profileEntry = this._profile.findEntry(pc);
    let fnName = this.formatProfileEntry(profileEntry);
    let script = this.getProfileEntryScript(profileEntry);
    // TODO: Use SourcePosition here directly
    let entry = new IcLogEntry(
        type, fnName, time, line, column, key, old_state, new_state, map,
        slow_reason, script, modifier);
    if (script) {
      entry.sourcePosition = script.addSourcePosition(line, column, entry);
    }
    this._icTimeline.push(entry);
  }

  formatProfileEntry(profileEntry, line, column) {
    if (!profileEntry) return '<unknown>';
    if (profileEntry.type === 'Builtin') return profileEntry.name;
    const name = profileEntry.func.getName();
    const array = this._formatPCRegexp.exec(name);
    const formatted =
        (array === null) ? name : profileEntry.getState() + array[1];
    if (line === undefined || column === undefined) return formatted;
    return `${formatted}:${line}:${column}`;
  }

  getProfileEntryScript(profileEntry) {
    if (!profileEntry) return undefined;
    if (profileEntry.type === 'Builtin') return undefined;
    const script = profileEntry.source?.script;
    if (script !== undefined) return script;
    // Slow path, try to get the script from the url:
    const fnName = this.formatProfileEntry(profileEntry);
    let parts = fnName.split(' ');
    let fileName = parts[parts.length - 1];
    return this.getScript(fileName);
  }

  processMap(type, time, from, to, pc, line, column, reason, name) {
    let time_ = parseInt(time);
    if (type === 'Deprecate') return this.deprecateMap(type, time_, from);
    let from_ = this.getExistingMapEntry(from, time_);
    let to_ = this.getExistingMapEntry(to, time_);
    // TODO: use SourcePosition directly.
    let edge = new Edge(type, name, reason, time, from_, to_);
    const profileEntry = this._profile.findEntry(pc)
    to_.filePosition = this.formatProfileEntry(profileEntry, line, column);
    let script = this.getProfileEntryScript(profileEntry);
    if (script) {
      to_.script = script;
      to_.sourcePosition = to_.script.addSourcePosition(line, column, to_)
    }
    edge.finishSetup();
  }

  deprecateMap(type, time, id) {
    this.getExistingMapEntry(id, time).deprecate();
  }

  processMapCreate(time, id) {
    // map-create events might override existing maps if the addresses get
    // recycled. Hence we do not check for existing maps.
    let map = this.createMapEntry(id, time);
  }

  processMapDetails(time, id, string) {
    // TODO(cbruni): fix initial map logging.
    let map = this.getExistingMapEntry(id, time);
    map.description = string;
  }

  createMapEntry(id, time) {
    let map = new MapLogEntry(id, time);
    this._mapTimeline.push(map);
    return map;
  }

  getExistingMapEntry(id, time) {
    if (id === '0x000000000000') return undefined;
    let map = MapLogEntry.get(id, time);
    if (map === undefined) {
      console.error(`No map details provided: id=${id}`);
      // Manually patch in a map to continue running.
      return this.createMapEntry(id, time);
    };
    return map;
  }

  getScript(url) {
    const script = this._profile.getScript(url);
    // TODO create placeholder script for empty urls.
    if (script === undefined) {
      console.error(`Could not find script for url: '${url}'`)
    }
    return script;
  }

  get icTimeline() {
    return this._icTimeline;
  }

  get mapTimeline() {
    return this._mapTimeline;
  }

  get deoptTimeline() {
    return this._deoptTimeline;
  }

  get codeTimeline() {
    return this._codeTimeline;
  }

  get scripts() {
    return this._profile.scripts_.filter(script => script !== undefined);
  }
}
