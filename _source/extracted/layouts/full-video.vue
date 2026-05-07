<script setup>
import { useSlideContext } from '@slidev/client'
const { $frontmatter } = useSlideContext()
</script>

<template>
  <div class="slidev-layout">
    <div
      style="
        position: absolute;
        top: 24px;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        align-items: center;
        justify-content: center;
      "
    >
      <SlidevVideo
        controls
        :poster="$frontmatter.poster"
        style="max-height: 100%; max-width: 100%;"
      >
        <source :src="$frontmatter.video" :type="$frontmatter.video?.endsWith('.mov') ? 'video/quicktime' : 'video/mp4'" />
      </SlidevVideo>
    </div>
    <span
      v-if="$frontmatter.link"
      class="absolute opacity-60"
      style="top: 0; right: 0; padding: 4px 8px; font-size: 14px; line-height: 1;"
    >🔗 {{ $frontmatter.link }}</span>
  </div>
</template>
