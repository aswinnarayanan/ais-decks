<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout flex flex-col h-full p-0">
    <div class="overflow-hidden relative" style="height: 70%;">
      <img
        :src="$frontmatter.image"
        :style="{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          objectPosition: $frontmatter.imagePosition || 'center center',
        }"
      />
    </div>
    <div class="flex-1 flex flex-col justify-center px-14 py-6 relative">
      <slot />
      <span
        v-if="$frontmatter.credit"
        class="absolute opacity-50"
        style="bottom: 4px; right: 12px; font-size: 11px; line-height: 1;"
      >{{ $frontmatter.credit }}</span>
    </div>
  </div>
</template>
