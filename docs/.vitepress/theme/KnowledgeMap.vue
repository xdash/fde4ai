<script setup>
// FDE 知识图谱：页面内为适配内容栏宽度的缩略图，点击进入浮层看完整交互版。
// 数据由 fde-book/ecosystem/tools/publish_kmap.py 生成进 .vitepress/knowledge-map.json，
// 静态 import 内联进本 chunk（免一次运行时 fetch 往返）。
import { ref, computed, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { withBase } from 'vitepress'
import atlasData from '../knowledge-map.json'
import KmapSvg from './KmapSvg.vue'

const atlas = ref(atlasData)
const view = ref('maturity') // maturity | stage | ai
const active = ref(null)     // 当前选中节点（详情卡）
const open = ref(false)      // 浮层开关
const thumbBtn = ref(null)   // 缩略图按钮（关浮层时焦点归还）
const closeBtn = ref(null)   // 浮层关闭按钮（开浮层时焦点移入）

const VIEWS = [
  { key: 'maturity', label: '成熟度' },
  { key: 'stage', label: '阶段' },
  { key: 'ai', label: 'AI 杠杆' },
]

const STAGE_LABEL = {
  foundation: '全程基石', 'pre-sale': '售前获客', deployment: '部署激活',
  renewal: '续约留存', expansion: '扩展增收', scale: '规模化',
}
const AI_LABEL = { high: '高杠杆', mid: '中杠杆', low: '低杠杆' }
const MATURITY_LABEL = { 1: '入门', 2: '熟练', 3: '精通' }
const STAGE_COLOR = {
  foundation: '#64748b', 'pre-sale': '#f0603c', deployment: '#18a058',
  renewal: '#0284c7', expansion: '#d97706', scale: '#9333ea',
}

const legend = computed(() => {
  if (view.value === 'stage')
    return Object.entries(STAGE_LABEL).map(([k, v]) => ({ color: STAGE_COLOR[k], text: v }))
  if (view.value === 'ai')
    return [{ color: '#18a058', text: '高杠杆' }, { color: '#9fb3c8', text: '中杠杆' }, { color: '#d3dee6', text: '低杠杆' }]
  return [{ color: '#bde5c8', text: '入门' }, { color: '#5cc489', text: '熟练' }, { color: '#18a058', text: '精通' }]
})

function pick(n) {
  active.value = active.value?.id === n.id ? null : n
}
function closeModal() {
  open.value = false
  active.value = null
}
function onKey(e) { if (e.key === 'Escape') { open.value ? closeModal() : (active.value = null) } }

// 浮层打开时锁 body 滚动 + 焦点移入浮层；关闭时焦点归还触发按钮（组件在 ClientOnly 内，无 SSR 触雷）
watch(open, v => {
  document.body.style.overflow = v ? 'hidden' : ''
  nextTick(() => (v ? closeBtn.value : thumbBtn.value)?.focus())
})
onMounted(() => window.addEventListener('keydown', onKey))
onUnmounted(() => {
  window.removeEventListener('keydown', onKey)
  document.body.style.overflow = ''
})

const domainName = computed(() => {
  if (!active.value) return ''
  return atlas.value.regions.find(r => r.id === active.value.domain)?.name || ''
})
</script>

<template>
  <figure class="kmap">
    <figcaption class="cartouche">
      <span class="cartouche-title">FDE 知识图谱</span>
      <span class="cartouche-sub">{{ atlas.regions.length }} 个能力域 · {{ atlas.nodes.length }} 个能力点 · 勘定 {{ atlas.updated }}</span>
    </figcaption>

    <!-- 缩略图：整图等比缩进固定高度，点击进浮层 -->
    <button class="thumb" ref="thumbBtn" @click="open = true" aria-label="放大查看知识图谱">
      <span class="thumb-frame">
        <KmapSvg :atlas="atlas" :view="view" />
      </span>
      <span class="thumb-hint">🔍 点击放大，查看完整交互版图谱</span>
    </button>

    <!-- 浮层：完整交互版 -->
    <Teleport to="body">
      <div v-if="open" class="kmap-modal" @click.self="closeModal">
        <div class="kmap-panel" role="dialog" aria-modal="true" aria-label="FDE 知识图谱完整版">
          <div class="panel-head">
            <div class="view-switch" role="tablist" aria-label="视角切换">
              <button v-for="v in VIEWS" :key="v.key" role="tab"
                      :class="['view-btn', { on: view === v.key }]"
                      :aria-selected="view === v.key"
                      @click="view = v.key">{{ v.label }}</button>
            </div>
            <button class="panel-close" ref="closeBtn" @click="closeModal" aria-label="关闭">×</button>
          </div>

          <div class="panel-body">
            <div class="panel-canvas">
              <KmapSvg :atlas="atlas" :view="view" interactive :active-id="active?.id ?? ''" @pick="pick" />
            </div>

            <div class="legend">
              <span v-for="(l, i) in legend" :key="i"><i class="lg-dot" :style="{ background: l.color }"></i>{{ l.text }}</span>
              <span class="legend-hint">点击能力点查看详情</span>
            </div>

            <!-- 详情卡 -->
            <div v-if="active" class="detail">
              <div class="detail-head">
                <span class="detail-name">{{ active.name }}</span>
                <span class="detail-domain">{{ domainName }}</span>
                <button class="detail-close" @click="active = null" aria-label="关闭详情">×</button>
              </div>
              <div class="detail-desc">{{ active.desc }}</div>
              <div class="detail-badges">
                <span>成熟度 · {{ MATURITY_LABEL[active.maturity] }}</span>
                <span>阶段 · {{ STAGE_LABEL[active.stage] }}</span>
                <span>AI 杠杆 · {{ AI_LABEL[active.ai_leverage] }}</span>
              </div>
              <div class="detail-links">
                <a v-for="c in active.chapter_links" :key="c.num" :href="withBase(`/book/${c.slug}`)">阅读：{{ c.title }} →</a>
                <span v-if="active.cases.length" class="detail-cases">
                  相关案例：<a :href="withBase('/cases')">{{ active.cases.map(c => '#' + c).join('、') }}</a>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Teleport>
  </figure>
</template>

<style scoped>
/* 明亮轻快版：白底卡片 + 明快绿主色；浮层为全屏查看器 */
.kmap {
  --paper: #ffffff;
  --panel: #f4f8f5;
  --ink: #1f2d3d;
  --ink-soft: #5b6b7c;
  --ink-faint: #7d8fa0;
  --line: #dce5ec;
  --accent: #18a058;
  margin: 1.5rem 0;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: 0 4px 20px rgba(31, 45, 61, 0.07);
  padding: 20px 20px 16px;
  font-family: -apple-system, "PingFang SC", "Helvetica Neue", "Microsoft YaHei", sans-serif;
}
.cartouche { display: flex; align-items: baseline; gap: 14px; margin-bottom: 12px; }
.cartouche-title { font-size: 1.3rem; letter-spacing: 0.2em; color: var(--ink); font-weight: 700; }
.cartouche-sub { font-size: 0.8rem; color: var(--ink-faint); letter-spacing: 0.05em; }

/* 缩略图 */
.thumb {
  display: block; width: 100%; cursor: zoom-in;
  background: var(--panel);
  border: 1px dashed #c2dccd; border-radius: 10px;
  padding: 12px; font-family: inherit;
  transition: border-color 0.2s;
}
.thumb:hover { border-color: var(--accent); }
.thumb-frame {
  display: flex; justify-content: center;
  height: 440px; overflow: hidden;
}
.thumb-frame :deep(svg) { width: auto; height: 100%; }
.thumb-hint {
  display: block; margin-top: 8px;
  color: var(--accent); font-size: 0.82rem; letter-spacing: 0.05em;
}

/* 浮层（Teleport 到 body，样式仍是 scoped 可命中，因节点由本组件渲染） */
.kmap-modal {
  position: fixed; inset: 0; z-index: 100;
  background: rgba(15, 25, 35, 0.55);
  backdrop-filter: blur(3px);
  display: flex; align-items: center; justify-content: center;
  padding: 3vh 3vw;
}
.kmap-panel {
  background: #fff; border-radius: 14px;
  width: 100%; max-width: 880px; max-height: 94vh;
  display: flex; flex-direction: column;
  box-shadow: 0 16px 60px rgba(15, 25, 35, 0.35);
  overflow: hidden;
  font-family: -apple-system, "PingFang SC", "Helvetica Neue", "Microsoft YaHei", sans-serif;
}
.panel-head {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border-bottom: 1px solid var(--line);
  background: var(--panel);
}
.view-switch { display: flex; gap: 8px; }
.view-btn {
  background: #fff; color: var(--ink-soft);
  border: 1px solid var(--line);
  border-radius: 999px; padding: 4px 16px; font-size: 0.82rem; cursor: pointer;
  font-family: inherit; letter-spacing: 0.05em;
  transition: all 0.2s;
}
.view-btn:hover { border-color: var(--accent); color: var(--accent); }
.view-btn.on { color: #fff; background: var(--accent); border-color: var(--accent); font-weight: 600; }
.panel-close {
  margin-left: auto; background: none; border: none;
  color: var(--ink-faint); font-size: 1.5rem; cursor: pointer; line-height: 1;
  padding: 0 4px;
}
.panel-close:hover { color: var(--ink); }

.panel-body { overflow: auto; padding: 16px; }
.panel-canvas { max-width: 780px; margin: 0 auto; }

.legend {
  display: flex; flex-wrap: wrap; gap: 16px; margin-top: 12px;
  color: var(--ink-soft); font-size: 0.75rem; letter-spacing: 0.05em;
}
.legend span { display: inline-flex; align-items: center; gap: 6px; }
.lg-dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; }
.legend-hint { margin-left: auto; opacity: 0.75; }

.detail {
  margin-top: 12px; background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 10px; padding: 12px 16px;
  box-shadow: 0 2px 10px rgba(31, 45, 61, 0.05);
}
.detail-head { display: flex; align-items: baseline; gap: 10px; }
.detail-name { color: var(--ink); font-weight: 700; font-size: 1.05rem; }
.detail-domain { color: var(--accent); font-size: 0.72rem; letter-spacing: 0.15em; font-weight: 600; }
.detail-close {
  margin-left: auto; background: none; border: none; color: var(--ink-faint);
  font-size: 1.2rem; cursor: pointer; line-height: 1;
}
.detail-close:hover { color: var(--ink); }
.detail-desc { color: var(--ink-soft); font-size: 0.85rem; line-height: 1.65; margin: 6px 0; }
.detail-badges { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 8px; }
.detail-badges span {
  font-size: 0.72rem; color: var(--accent);
  border: 1px solid rgba(24, 160, 88, 0.35);
  background: rgba(24, 160, 88, 0.06);
  border-radius: 999px; padding: 2px 10px; letter-spacing: 0.05em;
}
.detail-links a { color: var(--accent); font-size: 0.85rem; margin-right: 14px; text-decoration: none; font-weight: 500; }
.detail-links a:hover { text-decoration: underline; }
.detail-cases { color: var(--ink-soft); font-size: 0.85rem; }

@media (max-width: 640px) {
  .cartouche { flex-direction: column; gap: 4px; }
  .thumb-frame { height: 320px; }
  .kmap-modal { padding: 0; }
  .kmap-panel { max-width: 100%; max-height: 100vh; border-radius: 0; }
  .panel-canvas { max-width: none; min-width: 620px; }
}
</style>
