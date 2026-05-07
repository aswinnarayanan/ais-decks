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
  </div>
</template>
