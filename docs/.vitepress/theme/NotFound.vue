<script setup>
// 双语 404：book 正文仅中文，英文站切到书页会落到这里，给两个出口
const BOOK = '/book/'
</script>

<template>
  <div class="nf">
    <div class="nf-code">404</div>
    <p class="nf-zh">这个页面不存在。手册正文目前只有中文版。</p>
    <p class="nf-en">Page not found. The handbook is currently available in Chinese only.</p>
    <div class="nf-links">
      <a href="/">回到首页</a>
      <a :href="BOOK">阅读手册（中文）</a>
      <a href="/en/">English Home</a>
    </div>
  </div>
</template>

<style scoped>
.nf {
  min-height: 60vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 48px 24px;
  color: var(--vp-c-text-1);
}
.nf-code {
  font-family: 'Menlo', 'JetBrains Mono', 'SF Mono', monospace;
  font-size: 64px;
  font-weight: 800;
  color: var(--vp-c-brand-1);
  letter-spacing: 0.08em;
  margin-bottom: 18px;
}
.nf-zh { font-size: 16px; margin-bottom: 6px; }
.nf-en { font-size: 14px; color: var(--vp-c-text-2); margin-bottom: 26px; }
.nf-links { display: flex; gap: 22px; flex-wrap: wrap; justify-content: center; }
.nf-links a {
  font-family: 'Menlo', 'JetBrains Mono', 'SF Mono', monospace;
  font-size: 13px;
  color: var(--vp-c-brand-1);
  text-decoration: none;
  border-bottom: 1px dashed var(--vp-c-brand-1);
  padding-bottom: 2px;
}
</style>
