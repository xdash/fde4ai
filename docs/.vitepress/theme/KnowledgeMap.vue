<script setup>
// FDE 知识图谱：能力域分区 + 三视角滤镜（成熟度/阶段/AI 杠杆）。
// 纯渲染组件——区域勘界、节点坐标、关系边全部由
// fde-book/ecosystem/tools/publish_kmap.py 生成进 .vitepress/knowledge-map.json，
// 此处静态 import 由 Vite 内联进本 chunk（免一次运行时 fetch 往返）。
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { withBase } from 'vitepress'
import atlasData from '../knowledge-map.json'

const atlas = ref(atlasData)
const view = ref('maturity') // maturity | stage | ai
const active = ref(null)     // 当前选中节点（详情卡）

onMounted(() => {
  window.addEventListener('keydown', onKey)
})

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

// 阶段视角的分类色（6 类，暗底高区分度）
const STAGE_COLOR = {
  foundation: '#d8c9a3', 'pre-sale': '#e05d3a', deployment: '#18F050',
  renewal: '#5ac8fa', expansion: '#ffd60a', scale: '#bf5af2',
}

// 节点着色：随当前视角维度取值变化
function nodeFill(n) {
  if (view.value === 'stage') return STAGE_COLOR[n.stage] || '#d8c9a3'
  if (view.value === 'ai') return { high: '#18F050', mid: '#d8c9a3', low: '#6b7a8c' }[n.ai_leverage] || '#d8c9a3'
  return { 1: 'rgba(216,201,163,0.45)', 2: 'rgba(216,201,163,0.8)', 3: '#e8dcc0' }[n.maturity]
}

const legend = computed(() => {
  if (view.value === 'stage')
    return Object.entries(STAGE_LABEL).map(([k, v]) => ({ color: STAGE_COLOR[k], text: v }))
  if (view.value === 'ai')
    return [{ color: '#18F050', text: '高杠杆' }, { color: '#d8c9a3', text: '中杠杆' }, { color: '#6b7a8c', text: '低杠杆' }]
  return [{ color: 'rgba(216,201,163,0.45)', text: '入门' }, { color: 'rgba(216,201,163,0.8)', text: '熟练' }, { color: '#e8dcc0', text: '精通' }]
})

function pick(n) {
  active.value = active.value?.id === n.id ? null : n
}
function onKey(e) { if (e.key === 'Escape') active.value = null }

onUnmounted(() => window.removeEventListener('keydown', onKey))
const domainName = computed(() => {
  if (!active.value || !atlas.value) return ''
  return atlas.value.regions.find(r => r.id === active.value.domain)?.name || ''
})
</script>

<template>
  <figure class="kmap">
    <figcaption class="cartouche">
      <span class="cartouche-title">FDE 知识图谱</span>
      <span class="cartouche-sub">{{ atlas?.regions.length ?? '…' }} 个能力域 · {{ atlas?.nodes.length ?? '…' }} 个能力点 · 勘定 {{ atlas?.updated ?? '' }}</span>
    </figcaption>

    <div class="view-switch" role="tablist" aria-label="视角切换">
      <button v-for="v in VIEWS" :key="v.key" role="tab"
              :class="['view-btn', { on: view === v.key }]"
              :aria-selected="view === v.key"
              @click="view = v.key">{{ v.label }}</button>
    </div>

    <div class="kmap-canvas">
      <svg :viewBox="`0 0 ${atlas?.viewBox?.[0] ?? 1200} ${atlas?.viewBox?.[1] ?? 1010}`" v-if="atlas"
           role="group" aria-label="FDE 知识图谱">
        <!-- 领地 -->
        <g v-for="r in atlas.regions" :key="r.id" class="region">
          <rect :x="r.x" :y="r.y" :width="r.w" :height="r.h" rx="20" class="region-border" />
          <rect :x="r.x + 8" :y="r.y + 8" :width="r.w - 16" :height="r.h - 16" rx="14" class="region-contour" />
          <text :x="r.x + 20" :y="r.y + 30" class="region-name">{{ r.name }}</text>
        </g>

        <!-- 关系边 -->
        <g class="edges">
          <template v-for="(e, i) in atlas.edges" :key="i">
            <line :x1="e.x1" :y1="e.y1" :x2="e.x2" :y2="e.y2" class="edge" />
            <text v-if="e.label" class="edge-label"
                  :x="(e.x1 + e.x2) / 2" :y="(e.y1 + e.y2) / 2 - 4">{{ e.label }}</text>
          </template>
        </g>

        <!-- 能力点 -->
        <g v-for="n in atlas.nodes" :key="n.id" class="node"
           :class="{ picked: active?.id === n.id }"
           :transform="`translate(${n.x},${n.y})`" tabindex="0"
           @click="pick(n)" @keydown.enter="pick(n)" @keydown.space.prevent="pick(n)">
          <circle r="8" class="post" :style="{ fill: nodeFill(n) }" />
          <text class="node-label" x="14" y="4">{{ n.name }}</text>
        </g>
      </svg>

      <div class="legend" v-if="atlas">
        <span v-for="(l, i) in legend" :key="i"><i class="lg-dot" :style="{ background: l.color }"></i>{{ l.text }}</span>
        <span class="legend-hint">点击能力点查看详情</span>
      </div>

      <!-- 详情卡 -->
      <div v-if="active" class="detail">
        <div class="detail-head">
          <span class="detail-name">{{ active.name }}</span>
          <span class="detail-domain">{{ domainName }}</span>
          <button class="detail-close" @click="active = null" aria-label="关闭">×</button>
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
  </figure>
</template>

<style scoped>
.kmap {
  --ink: #101c28;
  --ink-panel: #18293a;
  --sand: #d8c9a3;
  --sand-bright: #e8dcc0;
  --signal: #e05d3a;
  --neon: #18F050;
  margin: 1.5rem 0;
  background: var(--ink);
  border: 1px solid color-mix(in srgb, var(--sand) 40%, transparent);
  border-radius: 12px;
  padding: 20px 20px 12px;
  font-family: "Songti SC", "STSong", "Noto Serif CJK SC", serif;
}
.cartouche { display: flex; align-items: baseline; gap: 14px; margin-bottom: 12px; }
.cartouche-title { font-size: 1.35rem; letter-spacing: 0.35em; color: var(--sand-bright); font-weight: 700; }
.cartouche-sub { font-size: 0.8rem; color: color-mix(in srgb, var(--sand) 70%, transparent); letter-spacing: 0.1em; }

.view-switch { display: flex; gap: 8px; margin-bottom: 12px; }
.view-btn {
  background: transparent; color: color-mix(in srgb, var(--sand) 70%, transparent);
  border: 1px solid color-mix(in srgb, var(--sand) 35%, transparent);
  border-radius: 999px; padding: 4px 16px; font-size: 0.82rem; cursor: pointer;
  font-family: inherit; letter-spacing: 0.1em;
}
.view-btn.on { color: var(--ink); background: var(--neon); border-color: var(--neon); font-weight: 700; }

.kmap-fallback { color: var(--sand); padding: 2rem; text-align: center; }
.kmap-canvas { position: relative; overflow-x: auto; }
svg { width: 100%; height: auto; display: block; min-width: 880px; }

.region-border {
  fill: color-mix(in srgb, var(--sand) 4%, transparent);
  stroke: color-mix(in srgb, var(--sand) 55%, transparent);
  stroke-width: 1.4; stroke-dasharray: 7 5;
}
.region-contour { fill: none; stroke: color-mix(in srgb, var(--sand) 18%, transparent); stroke-width: 1; }
.region-name { fill: var(--sand); font-size: 15px; font-weight: 700; letter-spacing: 0.18em; }

.edge { stroke: color-mix(in srgb, var(--sand) 30%, transparent); stroke-width: 1; stroke-dasharray: 4 3; }
.edge-label { fill: color-mix(in srgb, var(--sand) 55%, transparent); font-size: 11px; text-anchor: middle; }

.node { cursor: pointer; outline: none; }
.node .post { transition: fill 0.25s; }
.node:hover .post, .node:focus .post, .node.picked .post { stroke: var(--neon); stroke-width: 2; }
.node-label { fill: var(--sand-bright); font-size: 13.5px; paint-order: stroke; stroke: var(--ink); stroke-width: 3px; }
.node:hover .node-label, .node.picked .node-label { fill: #fff; }

.legend {
  display: flex; flex-wrap: wrap; gap: 16px; margin-top: 10px;
  color: color-mix(in srgb, var(--sand) 75%, transparent); font-size: 0.75rem; letter-spacing: 0.08em;
}
.legend span { display: inline-flex; align-items: center; gap: 6px; }
.lg-dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; }
.legend-hint { margin-left: auto; opacity: 0.7; }

.detail {
  margin-top: 12px; background: var(--ink-panel);
  border: 1px solid color-mix(in srgb, var(--sand) 45%, transparent);
  border-radius: 8px; padding: 12px 16px;
}
.detail-head { display: flex; align-items: baseline; gap: 10px; }
.detail-name { color: var(--sand-bright); font-weight: 700; font-size: 1.05rem; }
.detail-domain { color: var(--signal); font-size: 0.72rem; letter-spacing: 0.2em; }
.detail-close {
  margin-left: auto; background: none; border: none; color: var(--sand);
  font-size: 1.2rem; cursor: pointer; line-height: 1;
}
.detail-desc { color: color-mix(in srgb, var(--sand-bright) 88%, transparent); font-size: 0.85rem; line-height: 1.6; margin: 6px 0; }
.detail-badges { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 8px; }
.detail-badges span {
  font-size: 0.72rem; color: var(--neon);
  border: 1px solid color-mix(in srgb, var(--neon) 45%, transparent);
  border-radius: 999px; padding: 2px 10px; letter-spacing: 0.06em;
}
.detail-links a { color: var(--neon); font-size: 0.85rem; margin-right: 14px; text-decoration: none; }
.detail-links a:hover { text-decoration: underline; }
.detail-cases { color: color-mix(in srgb, var(--sand) 80%, transparent); font-size: 0.85rem; }

@media (max-width: 640px) {
  .cartouche { flex-direction: column; gap: 4px; }
}
</style>
