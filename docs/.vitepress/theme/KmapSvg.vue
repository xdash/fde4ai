<script setup>
// 知识图谱 SVG 本体：缩略图（非交互）与浮层完整版（交互）共用，避免双份标记漂移。
// 数据由 KnowledgeMap.vue 静态 import 后传入；着色逻辑随 view 维度变化。
const props = defineProps({
  atlas: { type: Object, required: true },
  view: { type: String, default: 'maturity' },   // maturity | stage | ai
  interactive: { type: Boolean, default: false }, // 浮层版可点选节点
  activeId: { type: String, default: '' },
})
const emit = defineEmits(['pick'])

// 阶段视角的分类色（6 类，浅底明快高区分度）
const STAGE_COLOR = {
  foundation: '#64748b', 'pre-sale': '#f0603c', deployment: '#18a058',
  renewal: '#0284c7', expansion: '#d97706', scale: '#9333ea',
}

// 节点着色：随当前视角维度取值变化
function nodeFill(n) {
  if (props.view === 'stage') return STAGE_COLOR[n.stage] || '#94a3b8'
  if (props.view === 'ai') return { high: '#18a058', mid: '#9fb3c8', low: '#d3dee6' }[n.ai_leverage] || '#94a3b8'
  return { 1: '#bde5c8', 2: '#5cc489', 3: '#18a058' }[n.maturity]
}
</script>

<template>
  <svg :viewBox="`0 0 ${atlas.viewBox[0]} ${atlas.viewBox[1]}`"
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
       :class="{ picked: interactive && activeId === n.id, clickable: interactive }"
       :transform="`translate(${n.x},${n.y})`"
       v-bind="interactive ? { tabindex: 0 } : {}"
       @click="interactive && emit('pick', n)"
       @keydown.enter="interactive && emit('pick', n)"
       @keydown.space.prevent="interactive && emit('pick', n)">
      <circle r="8" class="post" :style="{ fill: nodeFill(n) }" />
      <text class="node-label" x="14" y="4">{{ n.name }}</text>
    </g>
  </svg>
</template>

<style scoped>
svg { width: 100%; height: auto; display: block; }

.region-border {
  fill: rgba(24, 160, 88, 0.04);
  stroke: #c2dccd;
  stroke-width: 1.2; stroke-dasharray: 6 5;
}
.region-contour { fill: none; stroke: rgba(24, 160, 88, 0.12); stroke-width: 1; }
.region-name { fill: #2f5c44; font-size: 15px; font-weight: 700; letter-spacing: 0.15em; }

.edge { stroke: #b6c6d2; stroke-width: 1; stroke-dasharray: 4 3; }
.edge-label { fill: #7d8fa0; font-size: 11px; text-anchor: middle; }

.node.clickable { cursor: pointer; outline: none; }
.node .post { transition: fill 0.25s; stroke: #fff; stroke-width: 1.5; }
.node.clickable:hover .post, .node.clickable:focus .post, .node.picked .post { stroke: #1f2d3d; stroke-width: 2; }
.node-label { fill: #1f2d3d; font-size: 13.5px; paint-order: stroke; stroke: #fff; stroke-width: 3px; }
.node.clickable:hover .node-label, .node.picked .node-label { fill: #18a058; font-weight: 600; }
</style>
