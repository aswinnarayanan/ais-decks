<script setup>
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const HIDE_FOR_LAYOUTS = ['full-video', 'full-image', 'cover', 'image-cover-top-title', 'image-cover-vertical-title']

const { currentSlideRoute } = useNav()
const active = computed(() => currentSlideRoute.value?.meta?.slide?.frontmatter?.section ?? null)
const layout = computed(() => currentSlideRoute.value?.meta?.slide?.frontmatter?.layout ?? null)
const visible = computed(() => active.value && !HIDE_FOR_LAYOUTS.includes(layout.value))
</script>

<template>
  <div
    v-if="visible"
    class="absolute bottom-6 left-6 text-xs font-semibold uppercase tracking-wider opacity-60"
  >
    {{ active }}
  </div>
</template>
