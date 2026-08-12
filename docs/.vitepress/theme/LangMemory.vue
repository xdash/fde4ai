<script setup>
// 语言状态记忆：跨页面记住用户最后浏览的语言
// - 路由变化即记录（zh/en）
// - 仅首页落点（'/' ↔ '/en/'）按记忆自动跳转；深链（分享出去的 /cases 等）不劫持
import { onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vitepress'

const KEY = 'fde4-lang'
const route = useRoute()
const router = useRouter()
const langOf = (p) => (p === '/en' || p.startsWith('/en/') ? 'en' : 'zh')

onMounted(() => {
  try {
    const saved = localStorage.getItem(KEY)
    if (saved && saved !== langOf(route.path)) {
      if (route.path === '/') router.go('/en/')
      else if (route.path === '/en/' || route.path === '/en') router.go('/')
    }
  } catch {}
})

watch(
  () => route.path,
  (p) => {
    try {
      localStorage.setItem(KEY, langOf(p))
    } catch {}
  },
)
</script>

<template></template>
