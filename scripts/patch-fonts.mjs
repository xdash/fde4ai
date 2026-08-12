// 性能补丁（2026-08-13）：用 ASCII+Latin-1 子集（wght 400-700，39KB）替换 VitePress 默认主题的
// 全量 Inter latin（66KB）。原因：VitePress 对默认主题字体硬编码 preload 且无关闭开关，
// 子集化只能直捣字体源文件。postinstall 钩子保证本地与 CI（npm ci）每次安装后自动重打。
// 影响面：超出 U+0020-00FF 的拉丁字符（如某些变音符号）回退系统字体——本站内容几乎不出现。
import { copyFileSync, existsSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'

const root = join(dirname(fileURLToPath(import.meta.url)), '..')
const src = join(root, 'scripts/assets/inter-roman-latin.woff2')
const dest = join(root, 'node_modules/vitepress/dist/client/theme-default/fonts/inter-roman-latin.woff2')

if (!existsSync(dest)) {
  console.warn('[patch-fonts] vitepress 字体路径不存在，跳过（版本可能已变，请检查）')
  process.exit(0)
}
copyFileSync(src, dest)
console.log('[patch-fonts] Inter 子集已应用（66KB → 39KB）')
