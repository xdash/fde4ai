<script setup>
// FDE 生态舆图：战地部署图风格的分层大陆图。
// 纯渲染组件——区域勘界、节点坐标、关系边全部由
// fde-book/ecosystem/tools/publish_map.py 生成进 /ecosystem-map.json。
import { ref, computed, onMounted } from 'vue'
import { withBase } from 'vitepress'

const atlas = ref(null)
const tip = ref(null) // 当前悬停节点
const failed = ref(false)

onMounted(async () => {
  try {
    const res = await fetch(withBase('/ecosystem-map.json'))
    if (!res.ok) throw new Error(String(res.status))
    atlas.value = await res.json()
  } catch {
    failed.value = true
  }
})

const nodeById = computed(() =>
  Object.fromEntries((atlas.value?.nodes || []).map(n => [n.id, n])))

// 传承虚线：中点加垂直偏移画二次曲线，交替方向避免与领地重叠
function edgePath(e, i) {
  const mx = (e.x1 + e.x2) / 2, my = (e.y1 + e.y2) / 2
  const dx = e.x2 - e.x1, dy = e.y2 - e.y1
  const len = Math.hypot(dx, dy) || 1
  const off = (i % 2 === 0 ? 1 : -1) * Math.min(60, len * 0.25)
  const cx = mx - (dy / len) * off, cy = my + (dx / len) * off
  return { d: `M ${e.x1} ${e.y1} Q ${cx} ${cy} ${e.x2} ${e.y2}`, lx: (mx + cx) / 2, ly: (my + cy) / 2 }
}

const GRATICULE_COLS = 10 // 经线 A–J
const GRATICULE_ROWS = 7  // 纬线 1–7
const colLetter = i => String.fromCharCode(65 + i)

const TYPE_LABEL = { team: '组织要塞', person: '人物哨点', source: '知识源头', resource: '薪酬求职' }
</script>

<template>
  <figure class="atlas" role="img" aria-label="FDE 生态舆图">
    <figcaption class="cartouche">
      <span class="cartouche-title">FDE 生态舆图</span>
      <span class="cartouche-sub">七块领地 · {{ atlas?.nodes.length ?? '…' }} 处据点 · 勘定 {{ atlas?.updated ?? '' }}</span>
    </figcaption>

    <div v-if="failed" class="atlas-fallback">舆图数据加载失败，请直接阅读下方文字版分层。</div>

    <div v-else class="atlas-canvas">
      <svg :viewBox="`0 0 ${atlas?.viewBox?.[0] ?? 1200} ${atlas?.viewBox?.[1] ?? 860}`" v-if="atlas">
        <!-- 经纬网 -->
        <g class="graticule">
          <template v-for="i in GRATICULE_COLS - 1" :key="'v' + i">
            <line :x1="120 * i" y1="0" :x2="120 * i" :y2="860" />
          </template>
          <template v-for="i in GRATICULE_ROWS - 1" :key="'h' + i">
            <line x1="0" :y1="120 * i" x2="1200" :y2="120 * i" />
          </template>
          <text v-for="i in GRATICULE_COLS" :key="'cl' + i" class="coord"
                :x="120 * (i - 1) + 6" y="18">{{ colLetter(i - 1) }}</text>
          <text v-for="i in GRATICULE_ROWS" :key="'rl' + i" class="coord"
                x="6" :y="120 * (i - 1) + 34">{{ i }}</text>
        </g>

        <!-- 罗盘玫瑰 -->
        <g class="compass" transform="translate(1146,818)">
          <circle r="26" /><line x1="0" y1="-26" x2="0" y2="26" /><line x1="-26" y1="0" x2="26" y2="0" />
          <path d="M 0 -26 L 6 0 L 0 6 L -6 0 Z" class="needle" />
          <text y="-32">北</text>
        </g>

        <!-- 领地 -->
        <g v-for="r in atlas.regions" :key="r.id" class="region">
          <rect :x="r.x" :y="r.y" :width="r.w" :height="r.h" rx="26" class="region-border" />
          <rect :x="r.x + 9" :y="r.y + 9" :width="r.w - 18" :height="r.h - 18" rx="20" class="region-contour" />
          <text :x="r.x + 22" :y="r.y + 30" class="region-name">{{ r.name }}</text>
        </g>

        <!-- 关系边 -->
        <g class="edges">
          <template v-for="(e, i) in atlas.edges" :key="i">
            <path v-if="e.kind === 'alumni'" :d="edgePath(e, i).d" class="edge-alumni" />
            <line v-else :x1="e.x1" :y1="e.y1" :x2="e.x2" :y2="e.y2" class="edge-member" />
            <text v-if="e.kind === 'alumni' && e.label" class="edge-label"
                  :x="edgePath(e, i).lx" :y="edgePath(e, i).ly">{{ e.label }}</text>
          </template>
        </g>

        <!-- 据点 -->
        <g v-for="n in atlas.nodes" :key="n.id" class="node" :class="'node-' + n.type"
           :transform="`translate(${n.x},${n.y})`" tabindex="0"
           @mouseenter="tip = n" @mouseleave="tip = null"
           @focus="tip = n" @blur="tip = null">
          <template v-if="n.type === 'team'">
            <circle r="12" class="fort-outer" /><circle r="4.5" class="fort-inner" />
          </template>
          <template v-else-if="n.type === 'source'">
            <line x1="0" y1="0" x2="0" y2="-14" class="flag-pole" />
            <path d="M 0 -14 L 12 -10 L 0 -6 Z" class="flag-cloth" />
          </template>
          <template v-else-if="n.type === 'resource'">
            <text class="anchor" y="5">⚓</text>
          </template>
          <circle v-else r="5.5" class="post" />
          <text class="node-label" x="15" y="4">{{ n.label || n.name }}</text>
        </g>
      </svg>

      <!-- 悬停简介卡 -->
      <div v-if="tip" class="tip" :style="{ left: tip.x / 12 + '%', top: tip.y / 8.6 + '%' }">
        <div class="tip-name">{{ tip.name }}</div>
        <div class="tip-type">{{ TYPE_LABEL[tip.type] || tip.type }}</div>
        <div class="tip-summary">{{ tip.summary }}</div>
      </div>
    </div>

    <div class="legend">
      <span><i class="lg lg-fort"></i>组织要塞</span>
      <span><i class="lg lg-post"></i>人物哨点</span>
      <span><i class="lg lg-flag"></i>知识源头</span>
      <span><i class="lg lg-anchor">⚓</i>薪酬求职</span>
      <span><i class="lg lg-line"></i>隶属</span>
      <span><i class="lg lg-dash"></i>出身传承</span>
    </div>
  </figure>
</template>

<style scoped>
.atlas {
  --ink: #101c28;
  --ink-panel: #18293a;
  --sand: #d8c9a3;
  --sand-bright: #e8dcc0;
  --signal: #e05d3a;
  margin: 1.5rem 0;
  background: var(--ink);
  border: 1px solid color-mix(in srgb, var(--sand) 40%, transparent);
  border-radius: 12px;
  padding: 20px 20px 12px;
  font-family: "Songti SC", "STSong", "Noto Serif CJK SC", serif;
}
.cartouche { display: flex; align-items: baseline; gap: 14px; margin-bottom: 12px; }
.cartouche-title {
  font-size: 1.35rem; letter-spacing: 0.35em; color: var(--sand-bright); font-weight: 700;
}
.cartouche-sub { font-size: 0.8rem; color: color-mix(in srgb, var(--sand) 70%, transparent); letter-spacing: 0.1em; }
.atlas-fallback { color: var(--sand); padding: 2rem; text-align: center; }
.atlas-canvas { position: relative; }
svg { width: 100%; height: auto; display: block; }

.graticule line { stroke: color-mix(in srgb, var(--sand) 9%, transparent); stroke-width: 1; }
.coord { fill: color-mix(in srgb, var(--sand) 30%, transparent); font-size: 10px; letter-spacing: 0.1em; }

.compass circle { fill: none; stroke: color-mix(in srgb, var(--sand) 45%, transparent); stroke-width: 1.2; }
.compass line { stroke: color-mix(in srgb, var(--sand) 45%, transparent); stroke-width: 1; }
.compass .needle { fill: var(--signal); }
.compass text { fill: var(--sand); font-size: 11px; text-anchor: middle; }

.region-border {
  fill: color-mix(in srgb, var(--sand) 4%, transparent);
  stroke: color-mix(in srgb, var(--sand) 55%, transparent);
  stroke-width: 1.4; stroke-dasharray: 7 5;
}
.region-contour {
  fill: none;
  stroke: color-mix(in srgb, var(--sand) 18%, transparent);
  stroke-width: 1;
}
.region-name {
  fill: var(--sand); font-size: 14px; font-weight: 700; letter-spacing: 0.18em;
}

.edge-member { stroke: color-mix(in srgb, var(--sand) 28%, transparent); stroke-width: 1; }
.edge-alumni { fill: none; stroke: var(--signal); stroke-width: 1.4; stroke-dasharray: 5 4; opacity: 0.85; }
.edge-label { fill: var(--signal); font-size: 10.5px; text-anchor: middle; opacity: 0.9; }

.node { cursor: pointer; outline: none; }
.node .fort-outer { fill: none; stroke: var(--sand-bright); stroke-width: 1.6; }
.node .fort-inner { fill: var(--signal); }
.node .post { fill: var(--sand-bright); }
.node .flag-pole { stroke: var(--sand-bright); stroke-width: 1.4; }
.node .flag-cloth { fill: var(--sand); }
.node .anchor { fill: var(--sand-bright); font-size: 15px; text-anchor: middle; }
.node-label { fill: var(--sand-bright); font-size: 12.5px; paint-order: stroke; stroke: var(--ink); stroke-width: 3px; }
.node:hover .fort-outer, .node:focus .fort-outer,
.node:hover .post, .node:focus .post,
.node:hover .flag-cloth, .node:focus .flag-cloth { stroke: var(--signal); }
.node:hover .post, .node:focus .post { fill: var(--signal); }
.node:hover .node-label, .node:focus .node-label { fill: #fff; }

.tip {
  position: absolute; transform: translate(-50%, calc(-100% - 16px));
  width: 260px; background: var(--ink-panel);
  border: 1px solid color-mix(in srgb, var(--sand) 45%, transparent);
  border-radius: 8px; padding: 10px 12px; pointer-events: none; z-index: 10;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
}
.tip-name { color: var(--sand-bright); font-weight: 700; font-size: 0.9rem; margin-bottom: 2px; }
.tip-type { color: var(--signal); font-size: 0.7rem; letter-spacing: 0.2em; margin-bottom: 6px; }
.tip-summary { color: color-mix(in srgb, var(--sand-bright) 85%, transparent); font-size: 0.78rem; line-height: 1.55; }

.legend {
  display: flex; flex-wrap: wrap; gap: 18px; margin-top: 10px;
  color: color-mix(in srgb, var(--sand) 75%, transparent); font-size: 0.75rem; letter-spacing: 0.08em;
}
.legend span { display: inline-flex; align-items: center; gap: 6px; }
.lg { display: inline-block; width: 16px; height: 12px; position: relative; }
.lg-fort::before { content: ""; position: absolute; inset: 1px; border: 1.5px solid var(--sand-bright); border-radius: 50%; }
.lg-fort::after { content: ""; position: absolute; left: 5px; top: 3.5px; width: 5px; height: 5px; background: var(--signal); border-radius: 50%; }
.lg-post::before { content: ""; position: absolute; left: 4px; top: 2px; width: 8px; height: 8px; background: var(--sand-bright); border-radius: 50%; }
.lg-flag::before { content: ""; position: absolute; left: 3px; top: 0; width: 1.5px; height: 12px; background: var(--sand-bright); }
.lg-flag::after { content: ""; position: absolute; left: 4.5px; top: 0; border-left: 9px solid var(--sand); border-top: 3px solid transparent; border-bottom: 3px solid transparent; }
.lg-anchor { font-size: 12px; color: var(--sand-bright); text-align: center; line-height: 12px; }
.lg-line::before { content: ""; position: absolute; left: 0; top: 5.5px; width: 16px; height: 1px; background: color-mix(in srgb, var(--sand) 40%, transparent); }
.lg-dash::before { content: ""; position: absolute; left: 0; top: 5.5px; width: 16px; border-top: 1.5px dashed var(--signal); }

@media (max-width: 640px) {
  .cartouche { flex-direction: column; gap: 4px; }
  .tip { width: 200px; }
}
</style>
