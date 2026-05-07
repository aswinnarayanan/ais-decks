<script setup>
defineProps({
  caption: String,
  size: { type: String, default: 'text-6xl' },
})
</script>

<template>
  <figure class="text-center">
    <div :class="[size, 'mx-auto inline-block']">
      <slot />
    </div>
    <figcaption class="text-xs mt-3 font-medium leading-snug">{{ caption }}</figcaption>
  </figure>
</template>
