// Copyright 2020 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "src/heap/cppgc/visitor.h"
#include "include/cppgc/garbage-collected.h"
#include "include/cppgc/trace-trait.h"
#include "src/base/macros.h"
#include "testing/gtest/include/gtest/gtest.h"

namespace cppgc {
namespace internal {

namespace {

class GCed : public GarbageCollected<GCed> {
 public:
  static size_t trace_callcount;

  GCed() { trace_callcount = 0; }

  virtual void Trace(cppgc::Visitor* visitor) { trace_callcount++; }
};

size_t GCed::trace_callcount;

class GCedMixin : public GarbageCollectedMixin {};

class OtherPayload {
 public:
  virtual void* GetDummy() const { return nullptr; }
};

class GCedMixinApplication : public GCed,
                             public OtherPayload,
                             public GCedMixin {
  USING_GARBAGE_COLLECTED_MIXIN();

 public:
  void Trace(cppgc::Visitor* visitor) override {
    GCed::Trace(visitor);
    GCedMixin::Trace(visitor);
  }
};

class DispatchingVisitor final : public VisitorBase {
 public:
  DispatchingVisitor(const void* object, const void* payload)
      : object_(object), payload_(payload) {}

 protected:
  void Visit(const void* t, TraceDescriptor desc) final {
    EXPECT_EQ(object_, t);
    EXPECT_EQ(payload_, desc.base_object_payload);
    desc.callback(this, desc.base_object_payload);
  }

 private:
  const void* object_;
  const void* payload_;
};

}  // namespace

TEST(TraceTraitTest, GetObjectStartGCed) {
  GCed gced;
  EXPECT_EQ(&gced,
            TraceTrait<GCed>::GetTraceDescriptor(&gced).base_object_payload);
}

TEST(TraceTraitTest, GetObjectStartGCedMixin) {
  GCedMixinApplication gced_mixin_app;
  GCedMixin* gced_mixin = static_cast<GCedMixin*>(&gced_mixin_app);
  EXPECT_EQ(&gced_mixin_app,
            TraceTrait<GCedMixin>::GetTraceDescriptor(gced_mixin)
                .base_object_payload);
}

TEST(TraceTraitTest, TraceGCed) {
  GCed gced;
  EXPECT_EQ(0u, GCed::trace_callcount);
  TraceTrait<GCed>::Trace(nullptr, &gced);
  EXPECT_EQ(1u, GCed::trace_callcount);
}

TEST(TraceTraitTest, TraceGCedMixin) {
  GCedMixinApplication gced_mixin_app;
  GCedMixin* gced_mixin = static_cast<GCedMixin*>(&gced_mixin_app);
  EXPECT_EQ(0u, GCed::trace_callcount);
  TraceTrait<GCedMixin>::Trace(nullptr, gced_mixin);
  EXPECT_EQ(1u, GCed::trace_callcount);
}

TEST(TraceTraitTest, TraceGCedThroughTraceDescriptor) {
  GCed gced;
  EXPECT_EQ(0u, GCed::trace_callcount);
  TraceDescriptor desc = TraceTrait<GCed>::GetTraceDescriptor(&gced);
  desc.callback(nullptr, desc.base_object_payload);
  EXPECT_EQ(1u, GCed::trace_callcount);
}

TEST(TraceTraitTest, TraceGCedMixinThroughTraceDescriptor) {
  GCedMixinApplication gced_mixin_app;
  GCedMixin* gced_mixin = static_cast<GCedMixin*>(&gced_mixin_app);
  EXPECT_EQ(0u, GCed::trace_callcount);
  TraceDescriptor desc = TraceTrait<GCedMixin>::GetTraceDescriptor(gced_mixin);
  desc.callback(nullptr, desc.base_object_payload);
  EXPECT_EQ(1u, GCed::trace_callcount);
}

TEST(VisitorTest, DispatchTraceGCed) {
  GCed gced;
  Member<GCed> ref(&gced);
  DispatchingVisitor visitor(&gced, &gced);
  EXPECT_EQ(0u, GCed::trace_callcount);
  visitor.Trace(ref);
  EXPECT_EQ(1u, GCed::trace_callcount);
}

TEST(VisitorTest, DispatchTraceGCedMixin) {
  GCedMixinApplication gced_mixin_app;
  GCedMixin* gced_mixin = static_cast<GCedMixin*>(&gced_mixin_app);
  // Ensure that we indeed test dispatching an inner object.
  EXPECT_NE(static_cast<void*>(&gced_mixin_app),
            static_cast<void*>(gced_mixin));
  Member<GCedMixin> ref(gced_mixin);
  DispatchingVisitor visitor(gced_mixin, &gced_mixin_app);
  EXPECT_EQ(0u, GCed::trace_callcount);
  visitor.Trace(ref);
  EXPECT_EQ(1u, GCed::trace_callcount);
}

}  // namespace internal
}  // namespace cppgc
