<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout flex flex-col" style="padding: 0; overflow: hidden; height: 100%;">
    <!-- Title bar flush at top: title left, credit right -->
    <div
      class="top-title-bar flex-shrink-0 flex items-center justify-between gap-4"
      style="padding: 6px 16px; border-bottom: 1px solid var(--c-border, #EAEAEA);"
    >
      <div class="title-slot">
        <slot />
      </div>
      <span
        v-if="$frontmatter.credit"
        class="opacity-60 flex-shrink-0"
        style="font-size: 14px; line-height: 1;"
      >{{ $frontmatter.credit }}</span>
    </div>

    <!-- Image fills the remaining area -->
    <div
      class="flex-1 relative overflow-hidden"
      :style="{
        backgroundImage: `url('${$frontmatter.image}')`,
        backgroundSize: 'contain',
        backgroundPosition: $frontmatter.imagePosition || 'center center',
        backgroundRepeat: 'no-repeat',
      }"
    ></div>
  </div>
</template>

<style scoped>
.title-slot :deep(h1) {
  font-size: 22px !important;
  font-weight: 700 !important;
  margin: 0 !important;
  color: var(--c-heading);
  letter-spacing: -0.01em;
  line-height: 1.2;
}
</style>
