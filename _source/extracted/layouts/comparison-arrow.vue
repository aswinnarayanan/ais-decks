<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout flex flex-col h-full px-14 py-10">
    <slot />
    <div class="flex-1 flex items-center justify-center gap-4 mt-4 min-h-0">
      <div class="flex-1 min-w-0 h-full flex items-center justify-center">
        <img :src="$frontmatter.image1" class="max-h-full max-w-full object-contain border border-gray-200 rounded" />
      </div>
      <span class="text-5xl text-gray-400 flex-shrink-0">→</span>
      <div class="flex-1 min-w-0 h-full flex items-center justify-center">
        <img :src="$frontmatter.image2" class="max-h-full max-w-full object-contain border border-gray-200 rounded" />
      </div>
    </div>
    <img
      v-if="$frontmatter.cornerImage"
      :src="$frontmatter.cornerImage"
      class="absolute top-4 right-4 h-24 object-contain !opacity-90"
    />
  </div>
</template>
