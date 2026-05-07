<script setup>
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const SECTIONS = [
  'The problems',
  'Existing solutions',
  "What's needed",
  'Proposed architecture',
  'Discussion & outlook',
]

const { currentSlideRoute } = useNav()
const active = computed(() => currentSlideRoute.value?.meta?.slide?.frontmatter?.section ?? null)
</script>

<template>
  <div
    v-if="active"
    class="absolute bottom-6 left-6 text-xs font-semibold uppercase tracking-wider opacity-60"
  >
    {{ active }}
  </div>
</template>
