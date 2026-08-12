import DefaultTheme from 'vitepress/theme'
import './custom.css'
import EcosystemMap from './EcosystemMap.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('EcosystemMap', EcosystemMap)
  },
}
