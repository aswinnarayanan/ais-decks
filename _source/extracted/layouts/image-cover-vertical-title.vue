<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout flex" style="padding: 0; overflow: hidden; height: 100%;">
    <!-- Vertical title strip on left (transparent, just border) -->
    <div
      class="flex items-center justify-center vertical-title-strip flex-shrink-0"
      style="width: 56px; writing-mode: vertical-rl; transform: rotate(180deg); border-right: 1px solid var(--c-border, #EAEAEA);"
    >
      <slot />
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
    >
      <p
        v-if="$frontmatter.credit"
        class="absolute m-0"
        style="bottom: 8px; right: 12px; font-size: 11px; opacity: 0.7; background: rgba(255,255,255,0.7); padding: 2px 6px; border-radius: 4px;"
      >{{ $frontmatter.credit }}</p>
    </div>
  </div>
</template>

<style scoped>
.vertical-title-strip :deep(h1) {
  font-size: 20px !important;
  font-weight: 700 !important;
  margin: 0 !important;
  padding: 8px 0;
  color: var(--c-heading);
  letter-spacing: -0.01em;
  line-height: 1.1;
}
</style>
