import DefaultTheme from 'vitepress/theme'
import { h, defineAsyncComponent } from 'vue'
import './custom.css'
import GeekHome from './GeekHome.vue'
import BackToBookIndex from './BackToBookIndex.vue'
import LangMemory from './LangMemory.vue'
import NotFound from './NotFound.vue'

// 生态地图仅 /map 页使用，异步拆出关键路径（首页/书页不再加载它）
const EcosystemMap = defineAsyncComponent(() => import('./EcosystemMap.vue'))

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // book/ 章节页底部注入「返回手册目录」（doc-bottom slot，不触碰 CI 同步的书稿）
      'doc-bottom': () => h(BackToBookIndex),
      // 语言状态记忆（挂载于全站）
      'layout-top': () => h(LangMemory),
      // 双语 404（book 仅中文的兜底出口）
      'not-found': () => h(NotFound),
    })
  },
  enhanceApp({ app }) {
    app.component('EcosystemMap', EcosystemMap)
    app.component('GeekHome', GeekHome)
  },
}
