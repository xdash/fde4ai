import { defineConfig } from 'vitepress'
import bookSidebar from './book-sidebar.json'

const BOOK_REPO = 'https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer'

export default defineConfig({
  title: 'FDE4.AI',
  description: '前线部署工程师开源指南 | The FDE Field Guide',
  lang: 'zh-CN',
  cleanUrls: true,
  themeConfig: {
    nav: [
      { text: 'Book 书', link: '/book/' },
      { text: 'Cases 案例', link: '/cases' },
      { text: 'Directory 名录', link: '/directory' },
      { text: 'Map 地图', link: '/map' },
      { text: 'Course 课程', link: '/#course' },
    ],
    sidebar: {
      '/book/': bookSidebar,
    },
    socialLinks: [
      { icon: 'github', link: BOOK_REPO },
    ],
    footer: {
      message: 'Book content open-sourced on GitHub',
      copyright: '© 2026 FDE4.AI',
    },
  },
})
