<script setup>
// book/ 章节页底部：返回手册目录索引（主题层注入，不改动 CI 同步的书稿文件）
import { computed } from 'vue'
import { useRoute } from 'vitepress'

const route = useRoute()
const show = computed(() => /^\/book\/.+/.test(route.path) && !/^\/book\/(index\.html)?$/.test(route.path))
</script>

<template>
  <div v-if="show" class="back-to-index">
    <a href="/book/">← 返回手册目录</a>
  </div>
</template>

<style scoped>
.back-to-index {
  margin-top: 2.5rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--vp-c-divider);
}
.back-to-index a {
  font-family: 'Menlo', 'JetBrains Mono', 'SF Mono', monospace;
  font-size: 13px;
  letter-spacing: 0.04em;
  color: var(--vp-c-brand-1);
  text-decoration: none;
}
.back-to-index a:hover {
  text-decoration: underline;
}
</style>
