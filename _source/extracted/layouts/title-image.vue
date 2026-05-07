<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout flex flex-col h-full px-14 py-8">
    <slot />
    <div class="flex-1 flex items-center justify-center min-h-0 mt-4 mb-12">
      <img :src="$frontmatter.image" class="max-h-full max-w-full object-contain" />
    </div>
  </div>
</template>
