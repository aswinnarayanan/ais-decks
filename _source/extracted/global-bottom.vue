<script setup>
import { computed } from 'vue'
import { useNav } from '@slidev/client'
const { currentSlideRoute } = useNav()
const logos = computed(() => currentSlideRoute.value?.meta?.slide?.frontmatter?.logos ?? [])
</script>

<template>
  <div>
    <div
      v-if="logos.length"
      class="absolute bottom-4 right-4 flex items-center bg-white rounded-lg px-4 py-2 gap-4 border border-gray-200 shadow-sm"
    >
      <img
        v-for="(logo, i) in logos"
        :key="i"
        :src="logo"
        :class="['h-7 max-w-[120px] object-contain', i > 0 ? 'border-l border-gray-200 pl-4' : '']"
      />
    </div>
  </div>
</template>
