# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "SHORT_EXTERNAL_STRING_TYPE",
  106: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ALLOCATION_SITE_TYPE",
  159: "ASYNC_GENERATOR_REQUEST_TYPE",
  160: "DEBUG_INFO_TYPE",
  161: "FUNCTION_TEMPLATE_INFO_TYPE",
  162: "INTERCEPTOR_INFO_TYPE",
  163: "INTERPRETER_DATA_TYPE",
  164: "MODULE_INFO_ENTRY_TYPE",
  165: "MODULE_TYPE",
  166: "OBJECT_TEMPLATE_INFO_TYPE",
  167: "PROMISE_CAPABILITY_TYPE",
  168: "PROMISE_REACTION_TYPE",
  169: "PROTOTYPE_INFO_TYPE",
  170: "SCRIPT_TYPE",
  171: "STACK_FRAME_INFO_TYPE",
  172: "TUPLE2_TYPE",
  173: "TUPLE3_TYPE",
  174: "WASM_COMPILED_MODULE_TYPE",
  175: "WASM_DEBUG_INFO_TYPE",
  176: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  177: "WASM_SHARED_MODULE_DATA_TYPE",
  178: "CALLABLE_TASK_TYPE",
  179: "CALLBACK_TASK_TYPE",
  180: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  181: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  182: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  183: "FIXED_ARRAY_TYPE",
  184: "BOILERPLATE_DESCRIPTION_TYPE",
  185: "HASH_TABLE_TYPE",
  186: "SCOPE_INFO_TYPE",
  187: "BLOCK_CONTEXT_TYPE",
  188: "CATCH_CONTEXT_TYPE",
  189: "DEBUG_EVALUATE_CONTEXT_TYPE",
  190: "EVAL_CONTEXT_TYPE",
  191: "FUNCTION_CONTEXT_TYPE",
  192: "MODULE_CONTEXT_TYPE",
  193: "NATIVE_CONTEXT_TYPE",
  194: "SCRIPT_CONTEXT_TYPE",
  195: "WITH_CONTEXT_TYPE",
  196: "WEAK_FIXED_ARRAY_TYPE",
  197: "DESCRIPTOR_ARRAY_TYPE",
  198: "TRANSITION_ARRAY_TYPE",
  199: "CALL_HANDLER_INFO_TYPE",
  200: "CELL_TYPE",
  201: "CODE_DATA_CONTAINER_TYPE",
  202: "FEEDBACK_CELL_TYPE",
  203: "FEEDBACK_VECTOR_TYPE",
  204: "LOAD_HANDLER_TYPE",
  205: "PROPERTY_ARRAY_TYPE",
  206: "PROPERTY_CELL_TYPE",
  207: "SHARED_FUNCTION_INFO_TYPE",
  208: "SMALL_ORDERED_HASH_MAP_TYPE",
  209: "SMALL_ORDERED_HASH_SET_TYPE",
  210: "STORE_HANDLER_TYPE",
  211: "WEAK_CELL_TYPE",
  212: "WEAK_ARRAY_LIST_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_ERROR_TYPE",
  1067: "JS_GENERATOR_OBJECT_TYPE",
  1068: "JS_MAP_TYPE",
  1069: "JS_MAP_KEY_ITERATOR_TYPE",
  1070: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1071: "JS_MAP_VALUE_ITERATOR_TYPE",
  1072: "JS_MESSAGE_OBJECT_TYPE",
  1073: "JS_PROMISE_TYPE",
  1074: "JS_REGEXP_TYPE",
  1075: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1076: "JS_SET_TYPE",
  1077: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1078: "JS_SET_VALUE_ITERATOR_TYPE",
  1079: "JS_STRING_ITERATOR_TYPE",
  1080: "JS_WEAK_MAP_TYPE",
  1081: "JS_WEAK_SET_TYPE",
  1082: "JS_TYPED_ARRAY_TYPE",
  1083: "JS_DATA_VIEW_TYPE",
  1084: "JS_INTL_LOCALE_TYPE",
  1085: "WASM_GLOBAL_TYPE",
  1086: "WASM_INSTANCE_TYPE",
  1087: "WASM_MEMORY_TYPE",
  1088: "WASM_MODULE_TYPE",
  1089: "WASM_TABLE_TYPE",
  1090: "JS_BOUND_FUNCTION_TYPE",
  1091: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x02201): (138, "FreeSpaceMap"),
  ("RO_SPACE", 0x02259): (132, "MetaMap"),
  ("RO_SPACE", 0x022e1): (131, "NullMap"),
  ("RO_SPACE", 0x02359): (197, "DescriptorArrayMap"),
  ("RO_SPACE", 0x023c1): (183, "FixedArrayMap"),
  ("RO_SPACE", 0x02429): (211, "WeakCellMap"),
  ("RO_SPACE", 0x024d1): (152, "OnePointerFillerMap"),
  ("RO_SPACE", 0x02539): (152, "TwoPointerFillerMap"),
  ("RO_SPACE", 0x025d1): (131, "UninitializedMap"),
  ("RO_SPACE", 0x02661): (8, "OneByteInternalizedStringMap"),
  ("RO_SPACE", 0x02721): (131, "UndefinedMap"),
  ("RO_SPACE", 0x02799): (129, "HeapNumberMap"),
  ("RO_SPACE", 0x02831): (131, "TheHoleMap"),
  ("RO_SPACE", 0x028f9): (131, "BooleanMap"),
  ("RO_SPACE", 0x02a09): (136, "ByteArrayMap"),
  ("RO_SPACE", 0x02a71): (183, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x02ad9): (185, "HashTableMap"),
  ("RO_SPACE", 0x02b41): (128, "SymbolMap"),
  ("RO_SPACE", 0x02ba9): (72, "OneByteStringMap"),
  ("RO_SPACE", 0x02c11): (186, "ScopeInfoMap"),
  ("RO_SPACE", 0x02c79): (207, "SharedFunctionInfoMap"),
  ("RO_SPACE", 0x02ce1): (133, "CodeMap"),
  ("RO_SPACE", 0x02d49): (191, "FunctionContextMap"),
  ("RO_SPACE", 0x02db1): (200, "CellMap"),
  ("RO_SPACE", 0x02e19): (206, "GlobalPropertyCellMap"),
  ("RO_SPACE", 0x02e81): (135, "ForeignMap"),
  ("RO_SPACE", 0x02ee9): (198, "TransitionArrayMap"),
  ("RO_SPACE", 0x02f51): (203, "FeedbackVectorMap"),
  ("RO_SPACE", 0x02ff9): (131, "ArgumentsMarkerMap"),
  ("RO_SPACE", 0x030b9): (131, "ExceptionMap"),
  ("RO_SPACE", 0x03179): (131, "TerminationExceptionMap"),
  ("RO_SPACE", 0x03241): (131, "OptimizedOutMap"),
  ("RO_SPACE", 0x03301): (131, "StaleRegisterMap"),
  ("RO_SPACE", 0x03391): (193, "NativeContextMap"),
  ("RO_SPACE", 0x033f9): (192, "ModuleContextMap"),
  ("RO_SPACE", 0x03461): (190, "EvalContextMap"),
  ("RO_SPACE", 0x034c9): (194, "ScriptContextMap"),
  ("RO_SPACE", 0x03531): (187, "BlockContextMap"),
  ("RO_SPACE", 0x03599): (188, "CatchContextMap"),
  ("RO_SPACE", 0x03601): (195, "WithContextMap"),
  ("RO_SPACE", 0x03669): (189, "DebugEvaluateContextMap"),
  ("RO_SPACE", 0x036d1): (183, "ScriptContextTableMap"),
  ("RO_SPACE", 0x03739): (151, "FeedbackMetadataArrayMap"),
  ("RO_SPACE", 0x037a1): (183, "ArrayListMap"),
  ("RO_SPACE", 0x03809): (130, "BigIntMap"),
  ("RO_SPACE", 0x03871): (184, "BoilerplateDescriptionMap"),
  ("RO_SPACE", 0x038d9): (137, "BytecodeArrayMap"),
  ("RO_SPACE", 0x03941): (201, "CodeDataContainerMap"),
  ("RO_SPACE", 0x039a9): (150, "FixedDoubleArrayMap"),
  ("RO_SPACE", 0x03a11): (185, "GlobalDictionaryMap"),
  ("RO_SPACE", 0x03a79): (202, "ManyClosuresCellMap"),
  ("RO_SPACE", 0x03ae1): (183, "ModuleInfoMap"),
  ("RO_SPACE", 0x03b49): (134, "MutableHeapNumberMap"),
  ("RO_SPACE", 0x03bb1): (185, "NameDictionaryMap"),
  ("RO_SPACE", 0x03c19): (202, "NoClosuresCellMap"),
  ("RO_SPACE", 0x03c81): (185, "NumberDictionaryMap"),
  ("RO_SPACE", 0x03ce9): (202, "OneClosureCellMap"),
  ("RO_SPACE", 0x03d51): (185, "OrderedHashMapMap"),
  ("RO_SPACE", 0x03db9): (185, "OrderedHashSetMap"),
  ("RO_SPACE", 0x03e21): (205, "PropertyArrayMap"),
  ("RO_SPACE", 0x03e89): (199, "SideEffectCallHandlerInfoMap"),
  ("RO_SPACE", 0x03ef1): (199, "SideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x03f59): (199, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x03fc1): (185, "SimpleNumberDictionaryMap"),
  ("RO_SPACE", 0x04029): (183, "SloppyArgumentsElementsMap"),
  ("RO_SPACE", 0x04091): (208, "SmallOrderedHashMapMap"),
  ("RO_SPACE", 0x040f9): (209, "SmallOrderedHashSetMap"),
  ("RO_SPACE", 0x04161): (185, "StringTableMap"),
  ("RO_SPACE", 0x041c9): (196, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x04231): (212, "WeakArrayListMap"),
  ("RO_SPACE", 0x04299): (106, "NativeSourceStringMap"),
  ("RO_SPACE", 0x04301): (64, "StringMap"),
  ("RO_SPACE", 0x04369): (73, "ConsOneByteStringMap"),
  ("RO_SPACE", 0x043d1): (65, "ConsStringMap"),
  ("RO_SPACE", 0x04439): (77, "ThinOneByteStringMap"),
  ("RO_SPACE", 0x044a1): (69, "ThinStringMap"),
  ("RO_SPACE", 0x04509): (67, "SlicedStringMap"),
  ("RO_SPACE", 0x04571): (75, "SlicedOneByteStringMap"),
  ("RO_SPACE", 0x045d9): (66, "ExternalStringMap"),
  ("RO_SPACE", 0x04641): (82, "ExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x046a9): (74, "ExternalOneByteStringMap"),
  ("RO_SPACE", 0x04711): (98, "ShortExternalStringMap"),
  ("RO_SPACE", 0x04779): (114, "ShortExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x047e1): (0, "InternalizedStringMap"),
  ("RO_SPACE", 0x04849): (2, "ExternalInternalizedStringMap"),
  ("RO_SPACE", 0x048b1): (18, "ExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04919): (10, "ExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x04981): (34, "ShortExternalInternalizedStringMap"),
  ("RO_SPACE", 0x049e9): (50, "ShortExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04a51): (42, "ShortExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x04ab9): (106, "ShortExternalOneByteStringMap"),
  ("RO_SPACE", 0x04b21): (140, "FixedUint8ArrayMap"),
  ("RO_SPACE", 0x04b89): (139, "FixedInt8ArrayMap"),
  ("RO_SPACE", 0x04bf1): (142, "FixedUint16ArrayMap"),
  ("RO_SPACE", 0x04c59): (141, "FixedInt16ArrayMap"),
  ("RO_SPACE", 0x04cc1): (144, "FixedUint32ArrayMap"),
  ("RO_SPACE", 0x04d29): (143, "FixedInt32ArrayMap"),
  ("RO_SPACE", 0x04d91): (145, "FixedFloat32ArrayMap"),
  ("RO_SPACE", 0x04df9): (146, "FixedFloat64ArrayMap"),
  ("RO_SPACE", 0x04e61): (147, "FixedUint8ClampedArrayMap"),
  ("RO_SPACE", 0x04ec9): (149, "FixedBigUint64ArrayMap"),
  ("RO_SPACE", 0x04f31): (148, "FixedBigInt64ArrayMap"),
  ("RO_SPACE", 0x04f99): (131, "SelfReferenceMarkerMap"),
  ("RO_SPACE", 0x05019): (172, "Tuple2Map"),
  ("RO_SPACE", 0x05211): (170, "ScriptMap"),
  ("RO_SPACE", 0x053d9): (162, "InterceptorInfoMap"),
  ("RO_SPACE", 0x09d59): (154, "AccessorInfoMap"),
  ("RO_SPACE", 0x09f69): (153, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x09fd1): (155, "AccessorPairMap"),
  ("RO_SPACE", 0x0a039): (156, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x0a0a1): (157, "AllocationMementoMap"),
  ("RO_SPACE", 0x0a109): (158, "AllocationSiteMap"),
  ("RO_SPACE", 0x0a171): (159, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x0a1d9): (160, "DebugInfoMap"),
  ("RO_SPACE", 0x0a241): (161, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x0a2a9): (163, "InterpreterDataMap"),
  ("RO_SPACE", 0x0a311): (164, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x0a379): (165, "ModuleMap"),
  ("RO_SPACE", 0x0a3e1): (166, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x0a449): (167, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x0a4b1): (168, "PromiseReactionMap"),
  ("RO_SPACE", 0x0a519): (169, "PrototypeInfoMap"),
  ("RO_SPACE", 0x0a581): (171, "StackFrameInfoMap"),
  ("RO_SPACE", 0x0a5e9): (173, "Tuple3Map"),
  ("RO_SPACE", 0x0a651): (174, "WasmCompiledModuleMap"),
  ("RO_SPACE", 0x0a6b9): (175, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x0a721): (176, "WasmExportedFunctionDataMap"),
  ("RO_SPACE", 0x0a789): (177, "WasmSharedModuleDataMap"),
  ("RO_SPACE", 0x0a7f1): (178, "CallableTaskMap"),
  ("RO_SPACE", 0x0a859): (179, "CallbackTaskMap"),
  ("RO_SPACE", 0x0a8c1): (180, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x0a929): (181, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x0a991): (182, "PromiseResolveThenableJobTaskMap"),
  ("MAP_SPACE", 0x02201): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x02259): (1072, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x022b1): "NullValue",
  ("RO_SPACE", 0x02339): "EmptyDescriptorArray",
  ("RO_SPACE", 0x023b1): "EmptyFixedArray",
  ("RO_SPACE", 0x025a1): "UninitializedValue",
  ("RO_SPACE", 0x026f1): "UndefinedValue",
  ("RO_SPACE", 0x02789): "NanValue",
  ("RO_SPACE", 0x02801): "TheHoleValue",
  ("RO_SPACE", 0x028b9): "HoleNanValue",
  ("RO_SPACE", 0x028c9): "TrueValue",
  ("RO_SPACE", 0x029a1): "FalseValue",
  ("RO_SPACE", 0x029f1): "empty_string",
  ("RO_SPACE", 0x02fb9): "EmptyScopeInfo",
  ("RO_SPACE", 0x02fc9): "ArgumentsMarker",
  ("RO_SPACE", 0x03089): "Exception",
  ("RO_SPACE", 0x03149): "TerminationException",
  ("RO_SPACE", 0x03211): "OptimizedOut",
  ("RO_SPACE", 0x032d1): "StaleRegister",
  ("RO_SPACE", 0x05091): "EmptyByteArray",
  ("RO_SPACE", 0x050b1): "EmptyFixedUint8Array",
  ("RO_SPACE", 0x050d1): "EmptyFixedInt8Array",
  ("RO_SPACE", 0x050f1): "EmptyFixedUint16Array",
  ("RO_SPACE", 0x05111): "EmptyFixedInt16Array",
  ("RO_SPACE", 0x05131): "EmptyFixedUint32Array",
  ("RO_SPACE", 0x05151): "EmptyFixedInt32Array",
  ("RO_SPACE", 0x05171): "EmptyFixedFloat32Array",
  ("RO_SPACE", 0x05191): "EmptyFixedFloat64Array",
  ("RO_SPACE", 0x051b1): "EmptyFixedUint8ClampedArray",
  ("RO_SPACE", 0x05289): "EmptySloppyArgumentsElements",
  ("RO_SPACE", 0x052a9): "EmptySlowElementDictionary",
  ("RO_SPACE", 0x052f1): "EmptyOrderedHashMap",
  ("RO_SPACE", 0x05319): "EmptyOrderedHashSet",
  ("RO_SPACE", 0x05351): "EmptyPropertyCell",
  ("RO_SPACE", 0x05379): "EmptyWeakCell",
  ("RO_SPACE", 0x05459): "InfinityValue",
  ("RO_SPACE", 0x05469): "MinusZeroValue",
  ("RO_SPACE", 0x05479): "MinusInfinityValue",
  ("RO_SPACE", 0x05489): "SelfReferenceMarker",
  ("OLD_SPACE", 0x02211): "EmptyScript",
  ("OLD_SPACE", 0x02299): "ManyClosuresCell",
  ("OLD_SPACE", 0x022b9): "NoElementsProtector",
  ("OLD_SPACE", 0x022e1): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x022f1): "ArraySpeciesProtector",
  ("OLD_SPACE", 0x02319): "TypedArraySpeciesProtector",
  ("OLD_SPACE", 0x02341): "PromiseSpeciesProtector",
  ("OLD_SPACE", 0x02369): "StringLengthProtector",
  ("OLD_SPACE", 0x02379): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x023a1): "ArrayBufferNeuteringProtector",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
