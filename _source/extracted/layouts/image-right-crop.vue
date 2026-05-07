<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout grid grid-cols-2 h-full p-0">
    <div class="my-auto px-14 py-10 relative">
      <slot />
      <img
        v-if="$frontmatter.mascot"
        :src="$frontmatter.mascot"
        class="absolute"
        style="bottom: 1.5rem; right: 1.5rem; height: 100px; object-fit: contain;"
      />
    </div>
    <div class="h-full overflow-hidden relative">
      <img
        :src="$frontmatter.image"
        :style="{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          objectPosition: $frontmatter.imagePosition || 'right center',
        }"
      />
      <span
        v-if="$frontmatter.credit"
        class="absolute opacity-70"
        style="bottom: 4px; right: 8px; font-size: 11px; line-height: 1; padding: 2px 6px; background: rgba(255,255,255,0.7); border-radius: 4px;"
      >{{ $frontmatter.credit }}</span>
    </div>
  </div>
</template>
