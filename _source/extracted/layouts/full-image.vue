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
      v-if="$frontmatter.link"
      class="absolute"
      style="top: 12px; right: 16px; font-size: 14px; line-height: 1.2; padding: 4px 10px; color: #1a1a1a; background: rgba(255,255,255,0.92); border-radius: 4px; z-index: 10;"
    >🔗 {{ $frontmatter.link }}</span>
    <span
      v-if="$frontmatter.credit"
      class="absolute opacity-70"
      style="bottom: 4px; right: 8px; font-size: 12px; line-height: 1; padding: 2px 6px; background: rgba(255,255,255,0.7); border-radius: 4px;"
    >{{ $frontmatter.credit }}</span>
  </div>
</template>
