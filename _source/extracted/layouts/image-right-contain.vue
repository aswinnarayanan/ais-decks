<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout grid grid-cols-2 gap-4 py-10 h-full" style="padding-left: 3.5rem; padding-right: 1.75rem;">
    <div class="my-auto">
      <slot />
    </div>
    <div class="my-auto h-full flex items-center justify-center">
      <img :src="$frontmatter.image" class="max-h-full max-w-full object-contain" />
    </div>
  </div>
</template>
