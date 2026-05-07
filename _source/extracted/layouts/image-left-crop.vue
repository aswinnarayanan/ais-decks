<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout grid grid-cols-2 h-full p-0">
    <div class="h-full overflow-hidden">
      <img
        :src="$frontmatter.image"
        style="width: 100%; height: 100%; object-fit: cover; object-position: left center;"
      />
    </div>
    <div class="my-auto px-14 py-10">
      <slot />
    </div>
  </div>
</template>
