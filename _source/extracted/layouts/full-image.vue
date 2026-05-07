<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout">
    <div
      style="
        position: absolute;
        inset: 0;
        display: flex;
        align-items: center;
        justify-content: center;
      "
    >
      <img
        :src="$frontmatter.image"
        style="max-height: 100%; max-width: 100%; object-fit: contain;"
      />
    </div>
    <span
      v-if="$frontmatter.credit"
      class="absolute opacity-70"
      style="bottom: 4px; right: 8px; font-size: 12px; line-height: 1; padding: 2px 6px; background: rgba(255,255,255,0.7); border-radius: 4px;"
    >{{ $frontmatter.credit }}</span>
  </div>
</template>
