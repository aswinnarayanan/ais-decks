<script setup>
defineProps({
  cols: { type: [Number, String], default: 3 },
})
</script>

<template>
  <div :class="`grid grid-cols-${cols} gap-x-12 gap-y-10 mt-12 text-current justify-items-center`">
    <slot />
  </div>
</template>
