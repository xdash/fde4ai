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
      { text: '书', link: '/book/' },
      { text: '案例', link: '/cases' },
      { text: '名录', link: '/directory' },
      { text: '地图', link: '/map' },
      { text: '课程', link: '/#course' },
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
  locales: {
    root: {
      label: '中文',
      lang: 'zh-CN',
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      themeConfig: {
        nav: [
          { text: 'Book', link: '/book/' },
          { text: 'Cases', link: '/en/cases' },
          { text: 'Directory', link: '/en/directory' },
          { text: 'Map', link: '/en/map' },
          { text: 'Course', link: '/en/#course' },
        ],
      },
    },
  },
})
