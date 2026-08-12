<script setup>
// fde4.ai 首页 · V1 深色极客工具风（参考 dimagent.com）
// 文案真源：课程 canon v1.1（2026-08-10 锁定 + 08-12 口径增补）
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  lang: { type: String, default: 'zh' },
})

const BOOK_REPO = 'https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer'

// 固底条：滑到课程区（第三屏）后逐渐出现
const showDock = ref(false)
let courseEl = null
const onScroll = () => {
  if (!courseEl) courseEl = document.getElementById('course')
  const trigger = courseEl ? courseEl.offsetTop - window.innerHeight * 0.5 : window.innerHeight * 1.5
  showDock.value = window.scrollY > trigger
}
const toTop = () => window.scrollTo({ top: 0, behavior: 'smooth' })

// 早鸟倒计时（2026-08-18 截止，canon 时间表）
const daysLeft = ref(0)
const calcDays = () => {
  const end = new Date('2026-08-18T23:59:59+08:00').getTime()
  daysLeft.value = Math.max(0, Math.ceil((end - Date.now()) / 86400000))
}
onMounted(() => {
  onScroll()
  calcDays()
  window.addEventListener('scroll', onScroll, { passive: true })
})
onUnmounted(() => window.removeEventListener('scroll', onScroll))

const copy = {
  zh: {
    badge: '开源手册 · 全文免费 · GitHub 4k+ Star',
    titleDim: '前线部署工程师',
    titleEm: 'FDE',
    heroSub: '开源手册 · 付费课程/社群',
    tagMono: 'THE OPEN-SOURCE FIELD GUIDE FOR FORWARD DEPLOYED ENGINEERS',
    tagPre: '一本写给 AI 交付者的实战手册：从岗位全貌、赢得客户到激活部署，讲清 FDE 怎么',
    tagShimmer: '在客户一线把 AI 项目做成',
    tagPost: '。',
    ctaGh: 'GitHub 项目 ↗',
    ctaRead: '免费阅读手册 →',
    ctaCourse: '付费课程/社群 ↓',
    info: [['范冰 著', ''], ['全文免费', ''], ['GitHub ', '4k+ Star'], ['持续版本化更新', '']],
    features: [
      { ico: '📖', h: '开源免费', p: '全文在线免费阅读，欢迎在 GitHub 上纠错与共建' },
      { ico: '🛠️', h: '实战导向', p: '来自客户一线的部署方法论与真实案例' },
      { ico: '🔄', h: '持续更新', p: '版本化迭代，站点与 GitHub 仓库自动同步' },
    ],
    bookEyebrow: 'THE HANDBOOK · 手册内容',
    bookTitle: '这本手册讲了什么',
    bookLead: '从岗位崛起到规模化复制——一个 FDE 的完整作战周期，八章走完。',
    chapters: [
      ['01', 'FDE 的崛起'],
      ['02', '解决正确的问题'],
      ['03', '赢得客户'],
      ['04', '激活部署'],
      ['05', '守住续约'],
      ['06', '扩大收入'],
      ['07', '规模化复制'],
      ['08', '完整案例集'],
    ],
    bookOutro: '另有自序、后记《FDE 的职业道德》与三份附录：常用指标清单 / FDE 人物与团队名单 / 全书案例索引与资料出处',
    bookCta: '免费阅读手册 →',
    courseEyebrow: '付费课程 · FDE 线上课程（2026）· 早鸟预购中',
    courseTitle1: '一个人读书，',
    courseTitle2: '一群人实战',
    lead1: '开源手册解决「知道」：岗位全貌、方法论主干、落地框架——全文免费，读到够用就到此为止。',
    lead2: '但如果你要的是「做到」——这门付费课程是手册的实战延伸：与书的重合度不到 20%，其余 80% 全是书里没有的东西。',
    lead3: '实战为主：作者本人的亲身顾问经验与失败复盘、一手源案例（Bob McGrew 的 YC 原版、Palantir 官方、各厂 FDE 负责人亲述）、能带走的工具包与答疑库，外加 90 天高强度学员社群——中文圈的 FDE 课全是二手转述，这门课不是。',
    stats: [
      { num: '4k', unit: '+ STAR', lbl: '开源书 GitHub' },
      { num: '90', unit: 'MIN 总时长', lbl: '7 节核心视频讲练结合' },
      { num: '5', unit: '件工具包', lbl: '带走就能用 K1–K5' },
      { num: '50', unit: '单启动', lbl: '预售门槛 不满全退' },
    ],
    cards: [
      { idx: '01 / CORE', h: '核心视频', p: '7 节，共约 90 分钟，讲练结合' },
      { idx: '02 / TOOLKIT', h: '工具包 5 件', p: '带走就能用的模板（K1-K5）' },
      { idx: '03 / PRACTICE', h: '实操作业', p: '用 DROP5 五问法拆解你身边的真实业务，填出人生第一张《企业 AI 项目可行性一页纸》' },
      { idx: '04 / MATERIAL', h: '双层课件', p: '购课即得观看版 PDF；完课 48 小时内发带你姓名水印的精排《复习手册》' },
      { idx: '05 / Q&A', h: '答疑', p: '主体录播 + 首期群内直播答疑（录屏归档，不承诺定期直播）' },
      { idx: '06 / COMMUNITY', h: '学员群', p: '90 天高强度运营，结业转长期校友群' },
    ],
    kitHead: 'Toolkit · K1 — K5 一览',
    kits: [
      ['K1', '《FDE 岗位能力自测表》'],
      ['K2', '《企业 AI 项目可行性一页纸》'],
      ['K3', '《交付三关检查清单》'],
      ['K4', '《FDE 入场前 30 天准备清单》'],
      ['K5', '《FDE 面试题库与备战清单》'],
    ],
    syllTitle: '七节大纲',
    syllTag: 'SYLLABUS · 90 MIN TOTAL',
    syllHead: ['No.', '标题', '时长', '一句话'],
    syllabus: [
      ['01', 'FDE 岗位全貌：为什么是现在，以及泼一盆冷水', '13 min', '需求数据之外，讲清中国真实岗位盘子；教的是可迁移技能，不是空头 title'],
      ['02', '边界澄清：FDE 不是什么', '10 min', 'vs 售前/交付/咨询/外包，附假 FDE 识别法'],
      ['03', '方法论：一个主干、一个印证、一个能带走的框架', '14 min', '全课只精讲 DROP5 五问法一个框架'],
      ['04', '书里书外：出版后的实战修正', '12 min', '中美差异、信任周期、落地三道坎'],
      ['05', '案例：我的顾问现场', '18 min', '本人失败复盘 + 交付实证，DROP5 完整走一遍'],
      ['06', '入场双轨：进企业 or 独立接单', '14 min', '能力模型与面试备战 / 接单五步评估与客户筛选'],
      ['07', '第 1 / 3 / 7 天行动清单 + 你的第一张一页纸', '10 min', '实操作业发布，第 7 天带回群打卡'],
    ],
    priceEyebrow: 'Pricing · Early Bird Ends Aug 18',
    priceTitle: '早鸟 ¥199，8 月 18 日后恢复 ¥299',
    priceLead: '¥299 即全部——无后端升单、不加微信卖咨询。透明本身就是卖点。',
    countPre: '距早鸟截止还有 ',
    countPost: ' 天',
    tiers: [
      { hot: true, corner: '推荐 · 早鸟', name: '早鸟预售', price: '199', desc: '开售后 7 天内或前 100 名 · 独享「创始学员」权益', cta: '立即预订' },
      { hot: false, name: '正式价', price: '299', desc: '8 月 18 日预售截止后生效 · 明码标价，不议价', cta: '预售期买早鸟更划算 →' },
      { hot: false, name: '老客户', price: '269', desc: '知识星球会员 / 既往学员专属（专属链接 + 微信返现）', cta: '预售期买早鸟更划算 →' },
    ],
    tierNote: '（收款通道接入中 · 即将开放）',
    tierPerkPre: '附注：购课后 ',
    tierPerkB1: '30 天内',
    tierPerkMid: '可领星球 ',
    tierPerkB2: '85 折',
    tierPerkPost: '优惠码',
    founderTag: '创始学员权益',
    founderHtml: '<b>创始学员群</b> + 群内答疑优先提问权；名字写入<b>课程致谢页</b>；预售表单问题进<b>首期答疑题库</b>',
    fitYes: '适合谁',
    fitYesList: [
      '默认你有现场经验——我们不从「Token 是什么」讲起',
      '想转型做 FDE 的工程师 / 交付顾问 / 解决方案人员',
      '刚开始接触 FDE 业务的一线从业者',
      '有企业软件 / 交付 / 客户现场经验，想切入 FDE 岗位',
    ],
    fitNo: '不适合谁 · 劝退即筛选',
    fitNoList: [
      '想找「速成保 offer」捷径的人',
      '完全没有企业软件 / 交付 / 客户现场经验的人',
      '企业老板 / 决策者——那是万元档线下老板课的受众，请移步',
    ],
    proof: [['开源书 ', '4k+ Star'], ['作者', '一线企业顾问', '履历'], ['真实交付案例（交易所 RFM、政务 72 项原子事务等）', '']],
    authorTag: '讲师 · YOUR INSTRUCTOR',
    authorName: '范冰',
    authorLines: [
      '《前线部署工程师》开源手册作者',
      '一线企业 AI 交付顾问：交易所 RFM、政务 72 项原子事务等真实交付',
      '书里写方法论，课里讲我是怎么摔的',
    ],
    faqEyebrow: 'FAQ · 你可能想问',
    faqs: [
      ['课程什么时候能看？', '8 月 18 日预售截止，满 50 单即启动全量制作，8 月 25 日前交付全部视频与工具包。'],
      ['录播还是直播？', '主体录播，随时看。首期做一次群内直播答疑（录屏归档），后续视群内需求择机做，不承诺频次。'],
      ['和万元档老板课有什么区别？', '本课面向从业者：怎么上岗、怎么交付。老板课面向决策者：怎么选 FDE、怎么谈合同——别买错。'],
      ['我读过开源手册了，还需要买课吗？', '重合度不到 20%。手册给方法论主干，课程给实战案例、亲身复盘、工具包与社群。'],
    ],
    mech1Tag: '预售机制',
    mech1Html: '预售满 <b>50 单</b>即启动全量制作，不满<b>全额退款</b>；8 月 18 日预售截止，8 月 25 日前交付全部视频与工具包，9 月第一周首期群内直播答疑',
    mech2Tag: '预售表单 · 开放题预告',
    mech2Q: '「你最希望这门课回答的一个问题是什么？」',
    mech2P: '——你的问题会进首期答疑题库',
    finalCta: '立即预订 · 早鸟 ¥199 →',
    finalRisk: '不满 50 单，全额退款——你没有任何风险',
    finalFine: '（收款通道接入中 · 即将开放）',
    footBrand: '《前线部署工程师》开源书 · 作者范冰',
    footGh: 'GitHub 开源共建',
    footNote: '课程咨询：预售表单内留言',
    dockTop: '返回顶部 ↑',
    dockCta: '立即预订 · 早鸟 ¥199',
  },
  en: {
    badge: 'Open-source Handbook · Free to Read · 4k+ GitHub Stars',
    titleDim: 'Forward Deployed Engineer',
    titleEm: 'FDE',
    heroSub: 'Open-source Handbook · Paid Course & Community',
    tagMono: '前线部署工程师的开源实战手册',
    tagPre: 'A field guide for AI builders: from the FDE landscape and winning customers to activating deployments — how FDEs ',
    tagShimmer: 'get AI projects done on the customer frontline',
    tagPost: '.',
    ctaGh: 'GitHub Project ↗',
    ctaRead: 'Read the Handbook Free →',
    ctaCourse: 'Paid Course & Community ↓',
    info: [['By Fan Bing', ''], ['Free to Read', ''], ['GitHub · ', '4k+ Stars'], ['Versioned, Continuously Updated', '']],
    features: [
      { ico: '📖', h: 'Open Source', p: 'Free to read online; corrections & contributions welcome on GitHub' },
      { ico: '🛠️', h: 'Battle-tested', p: 'Field methodology and real cases from the customer frontline' },
      { ico: '🔄', h: 'Continuously Updated', p: 'Versioned releases, auto-synced with the GitHub repo' },
    ],
    bookEyebrow: 'THE HANDBOOK · CONTENTS',
    bookTitle: 'What\'s in the handbook',
    bookLead: 'From the rise of the role to scaling what works — a complete FDE campaign cycle in eight chapters.',
    chapters: [
      ['01', 'The Rise of FDE'],
      ['02', 'Solving the Right Problems'],
      ['03', 'Winning the Customer'],
      ['04', 'Activating the Deployment'],
      ['05', 'Keeping the Renewal'],
      ['06', 'Expanding Revenue'],
      ['07', 'Scaling What Works'],
      ['08', 'The Complete Case Files'],
    ],
    bookOutro: 'Plus a preface, an afterword on FDE professional ethics, and three appendices: key metrics / people & teams / full case index & sources',
    bookCta: 'Read the Handbook Free →',
    courseEyebrow: 'PAID COURSE · FDE ONLINE COURSE (2026) · EARLY-BIRD PRE-SALE',
    courseTitle1: 'Don\'t read alone —',
    courseTitle2: 'join the cohort',
    lead1: 'The free handbook covers the "what": the role, the methodology backbone, the landing frameworks — free forever, and enough for many.',
    lead2: 'But if you want to get from "knowing" to "doing" — this paid course is the hands-on extension of the handbook: less than 20% overlap with the book, the other 80% is all new material.',
    lead3: 'Practice-first: the author\'s own consulting experience and failure post-mortems, first-hand sources (Bob McGrew\'s original YC talk, Palantir official materials, FDE leads\' own accounts), take-away toolkits and a Q&A bank — plus a 90-day intensive student community.',
    stats: [
      { num: '4k', unit: '+ STARS', lbl: 'Open-source Book' },
      { num: '90', unit: 'MIN TOTAL', lbl: '7 Core Video Sessions' },
      { num: '5', unit: 'TOOLKITS', lbl: 'Ready-to-use K1–K5' },
      { num: '50', unit: 'SEATS', lbl: 'Pre-sale Threshold, Full Refund' },
    ],
    cards: [
      { idx: '01 / CORE', h: 'Core Videos', p: '7 sessions, ~90 min total, learn by doing' },
      { idx: '02 / TOOLKIT', h: 'Toolkit × 5', p: 'Take-away templates that work out of the box (K1–K5)' },
      { idx: '03 / PRACTICE', h: 'Hands-on Assignment', p: 'Dissect a real business scenario around you with the DROP5 five questions, and produce your first Enterprise AI Feasibility One-Pager' },
      { idx: '04 / MATERIAL', h: 'Two-tier Materials', p: 'Viewing PDF on purchase; a typeset Review Handbook with your name watermarked, within 48h of completion' },
      { idx: '05 / Q&A', h: 'Q&A', p: 'Recorded course + first live group Q&A (archived; no recurring live commitment)' },
      { idx: '06 / COMMUNITY', h: 'Cohort', p: '90-day intensive community, graduating into a long-term alumni group' },
    ],
    kitHead: 'Toolkit · K1 — K5',
    kits: [
      ['K1', 'FDE Competency Self-Assessment'],
      ['K2', 'Enterprise AI Feasibility One-Pager'],
      ['K3', 'Delivery Three-Gate Checklist'],
      ['K4', '30-Day Pre-Entry Checklist'],
      ['K5', 'FDE Interview Bank & Prep Plan'],
    ],
    syllTitle: 'Syllabus',
    syllTag: '7 SESSIONS · 90 MIN TOTAL',
    syllHead: ['No.', 'Title', 'Length', 'In one line'],
    syllabus: [
      ['01', 'The FDE Landscape: Why Now, with a Cold Shower', '13 min', 'Beyond demand data: the real hiring landscape; transferable skills, not an empty title'],
      ['02', 'Boundaries: What FDE Is Not', '10 min', 'vs pre-sales / delivery / consulting / outsourcing, plus how to spot a fake FDE'],
      ['03', 'Methodology: One Backbone, One Corroboration, One Framework', '14 min', 'The whole course teaches exactly one framework: the DROP5 five questions'],
      ['04', 'Beyond the Book: Field Corrections Since Publication', '12 min', 'China–US differences, trust cycles, three hurdles to landing'],
      ['05', 'Cases: My Consulting Frontline', '18 min', 'My own failure post-mortem + delivery evidence, DROP5 in full action'],
      ['06', 'Two Tracks In: Join a Company or Go Independent', '14 min', 'Competency model & interview prep / five-step project & client screening'],
      ['07', 'Day 1 / 3 / 7 Action List + Your First One-Pager', '10 min', 'Assignment kickoff; report back to the group on day 7'],
    ],
    priceEyebrow: 'Pricing · Early Bird Ends Aug 18',
    priceTitle: 'Early Bird ¥199 — back to ¥299 after Aug 18',
    priceLead: '¥299 is all-inclusive — no upsells, no WeChat consulting funnel. Transparency is the point.',
    countPre: 'Only ',
    countPost: ' days left before early bird ends',
    tiers: [
      { hot: true, corner: 'EARLY BIRD', name: 'Early Bird Pre-sale', price: '199', desc: 'First 7 days or first 100 seats · exclusive Founder Member perks', cta: 'Reserve Now' },
      { hot: false, name: 'Standard', price: '299', desc: 'Effective after the Aug 18 pre-sale · flat price, no bargaining', cta: 'Early bird ¥199 is better →' },
      { hot: false, name: 'Alumni', price: '269', desc: 'For Planet members / past students (exclusive link + WeChat cashback)', cta: 'Early bird ¥199 is better →' },
    ],
    tierNote: '(Payment gateway being connected — opening soon)',
    tierPerkPre: 'Note: a ',
    tierPerkB1: '15%-off',
    tierPerkMid: ' Planet coupon within ',
    tierPerkB2: '30 days',
    tierPerkPost: ' of purchase',
    founderTag: 'FOUNDER PERKS',
    founderHtml: '<b>Founder group</b> with priority Q&A · your name on the <b>credits page</b> · pre-sale questions feed the <b>first Q&A session</b>',
    fitYes: 'Who it\'s for',
    fitYesList: [
      'We assume frontline experience — we don\'t start from "what is a token"',
      'Engineers / delivery consultants / solution folks moving into FDE',
      'Frontline practitioners new to FDE work',
      'Enterprise software / delivery / on-site experience, aiming at an FDE role',
    ],
    fitNo: 'Who it\'s not for',
    fitNoList: [
      'Anyone hunting a "guaranteed offer" shortcut',
      'Zero enterprise software / delivery / on-site experience',
      'Business owners / decision-makers — that\'s the executive offline course',
    ],
    proof: [['Open-source book · ', '4k+ Stars'], ['Author\'s ', 'frontline consulting', ' track record'], ['Real delivery cases (exchange RFM, 72 atomic government workflows, etc.)', '']],
    authorTag: 'YOUR INSTRUCTOR',
    authorName: 'Fan Bing',
    authorLines: [
      'Author of the open-source FDE Field Guide',
      'Frontline AI delivery consultant — exchange RFM, 72 atomic government workflows, and more',
      'The book teaches the methodology; the course shows how I fell',
    ],
    faqEyebrow: 'FAQ · YOU MAY WONDER',
    faqs: [
      ['When do I get access?', 'Pre-sale closes Aug 18; production starts at 50 orders; all videos & toolkits delivered by Aug 25.'],
      ['Live or recorded?', 'Recorded — watch anytime. One live group Q&A for the first cohort (archived); no recurring commitment.'],
      ['How is this different from the executive course?', 'This course is for practitioners: landing the job, delivering the work. The executive course is for decision-makers: choosing FDEs and negotiating contracts.'],
      ['I already read the handbook. Do I need the course?', 'Less than 20% overlap. The handbook gives the methodology; the course gives cases, first-hand post-mortems, toolkits, and community.'],
    ],
    mech1Tag: 'PRE-SALE MECHANICS',
    mech1Html: 'Production starts at <b>50 pre-orders</b>, <b>full refund</b> otherwise; pre-sale closes <b>Aug 18</b>; all videos & toolkits delivered by <b>Aug 25</b>; first live Q&A in the first week of September',
    mech2Tag: 'PRE-SALE FORM · OPEN QUESTION',
    mech2Q: '"What\'s the one question you want this course to answer?"',
    mech2P: '— your question feeds the first Q&A session',
    finalCta: 'Reserve · Early Bird ¥199 →',
    finalRisk: 'Fewer than 50 pre-orders? Full refund — zero risk for you',
    finalFine: '(Payment gateway being connected — opening soon)',
    footBrand: 'The FDE Field Guide (open source) · by Fan Bing',
    footGh: 'GitHub',
    footNote: 'Course inquiries via the pre-sale form',
    dockTop: 'Back to Top ↑',
    dockCta: 'Reserve · Early Bird ¥199',
  },
}

const c = copy[props.lang] || copy.zh
const bookLink = '/book/'
</script>

<template>
  <div class="geek-home">
    <!-- 屏 1 · Hero -->
    <header class="hero">
      <div class="wrap">
        <div class="badge rv d1"><span class="dot"></span>{{ c.badge }}</div>

        <h1 class="hero-title rv d2">
          <span class="dim">{{ c.titleDim }}</span>
          <span class="em">{{ c.titleEm }}</span>
        </h1>
        <div class="hero-sub rv d2">{{ c.heroSub }}</div>

        <p class="tagline rv d3">
          <span class="en">{{ c.tagMono }}</span>
          {{ c.tagPre }}<span class="shimmer">{{ c.tagShimmer }}</span>{{ c.tagPost }}
        </p>

        <div class="cta-row rv d4">
          <a class="btn btn-ghost mono" :href="BOOK_REPO" target="_blank" rel="noopener">{{ c.ctaGh }}</a>
          <a class="btn btn-primary" :href="bookLink" target="_blank" rel="noopener">{{ c.ctaRead }}</a>
          <a class="btn btn-ghost" href="#course">{{ c.ctaCourse }}</a>
        </div>

        <div class="hero-infobar rv d5">
          <span v-for="(item, i) in c.info" :key="i">{{ item[0] }}<b v-if="item[1]">{{ item[1] }}</b>{{ item[2] || '' }}</span>
        </div>
      </div>
    </header>

    <!-- 书籍特性条 -->
    <section class="features">
      <div class="wrap">
        <div class="features-grid">
          <div class="feat rv" :class="'d' + (i + 1)" v-for="(f, i) in c.features" :key="i">
            <div class="ico">{{ f.ico }}</div>
            <div>
              <h3>{{ f.h }}</h3>
              <p>{{ f.p }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <!-- 手册内容区 -->
    <section class="block">
      <div class="wrap">
        <div class="eyebrow rv d1">{{ c.bookEyebrow }}</div>
        <h2 class="sec-title rv d2">{{ c.bookTitle }}</h2>
        <p class="lead rv d3">{{ c.bookLead }}</p>

        <div class="chaps rv d4">
          <div class="chap" v-for="(ch, i) in c.chapters" :key="i">
            <div class="ch-no">{{ ch[0] }}</div>
            <div class="ch-tt">{{ ch[1] }}</div>
          </div>
        </div>

        <p class="book-outro rv d4">{{ c.bookOutro }}</p>

        <div class="book-cta rv d5">
          <a class="btn btn-primary" :href="bookLink" target="_blank" rel="noopener">{{ c.bookCta }}</a>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <!-- 屏 2 · 课程总览 -->
    <section class="block" id="course">
      <div class="wrap">
        <div class="eyebrow rv d1">{{ c.courseEyebrow }}</div>
        <h2 class="sec-title rv d2">{{ c.courseTitle1 }}<br>{{ c.courseTitle2 }}</h2>

        <p class="lead rv d3">{{ c.lead1 }}</p>
        <p class="lead rv d4">{{ c.lead2 }}</p>
        <p class="lead rv d5">{{ c.lead3 }}</p>

        <div class="stats rv d4">
          <div class="stat" v-for="(s, i) in c.stats" :key="i">
            <div class="num">{{ s.num }}<span class="u"> {{ s.unit }}</span></div>
            <div class="lbl">{{ s.lbl }}</div>
          </div>
        </div>

        <div class="cards">
          <div class="card rv" :class="'d' + (i + 1)" v-for="(card, i) in c.cards" :key="i">
            <div class="idx">{{ card.idx }}</div>
            <h3>{{ card.h }}</h3>
            <p>{{ card.p }}</p>
          </div>
        </div>

        <div class="kit rv d3">
          <div class="kit-head">{{ c.kitHead }}</div>
          <ul>
            <li v-for="(k, i) in c.kits" :key="i"><b>{{ k[0] }}</b>{{ k[1] }}</li>
          </ul>
        </div>

        <div class="syllabus rv d3">
          <div class="syll-head">
            <h3>{{ c.syllTitle }}</h3>
            <span class="tag"><span class="accent">{{ c.syllTag }}</span></span>
          </div>
          <table class="syll-table">
            <thead>
              <tr>
                <th style="width:56px">{{ c.syllHead[0] }}</th>
                <th>{{ c.syllHead[1] }}</th>
                <th style="width:96px">{{ c.syllHead[2] }}</th>
                <th style="width:44%">{{ c.syllHead[3] }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, i) in c.syllabus" :key="i">
                <td class="no">{{ row[0] }}</td>
                <td class="tt">{{ row[1] }}</td>
                <td class="min">{{ row[2] }}</td>
                <td>{{ row[3] }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <!-- 屏 3 · 定价与门槛 -->
    <section class="block pricing" id="pricing">
      <div class="wrap">
        <div class="eyebrow rv d1">{{ c.priceEyebrow }}</div>
        <h2 class="sec-title rv d2">{{ c.priceTitle }}</h2>
        <p class="countdown rv d2" v-if="daysLeft > 0">{{ c.countPre }}<b>{{ daysLeft }}</b>{{ c.countPost }}</p>
        <p class="lead rv d2">{{ c.priceLead }}</p>

        <div class="tiers">
          <div class="tier rv" :class="[{ hot: t.hot }, 'd' + (i + 2)]" v-for="(t, i) in c.tiers" :key="i">
            <div class="corner" v-if="t.corner">{{ t.corner }}</div>
            <div class="t-name">{{ t.name }}</div>
            <div class="t-price"><span class="cur">¥</span>{{ t.price }}</div>
            <div class="t-desc">{{ t.desc }}</div>
            <a class="t-cta" href="#pricing">{{ t.cta }}</a>
          </div>
        </div>
        <p class="tier-note rv d4">{{ c.tierNote }}</p>
        <p class="tier-perk-note rv d4">{{ c.tierPerkPre }}<b>{{ c.tierPerkB1 }}</b>{{ c.tierPerkMid }}<b>{{ c.tierPerkB2 }}</b>{{ c.tierPerkPost }}</p>

        <div class="founder rv d3">
          <div class="f-tag">{{ c.founderTag }}</div>
          <p v-html="c.founderHtml"></p>
        </div>

        <div class="fit-grid">
          <div class="fit yes rv d2">
            <h4>{{ c.fitYes }}</h4>
            <ul>
              <li v-for="(li, i) in c.fitYesList" :key="i">{{ li }}</li>
            </ul>
          </div>
          <div class="fit no rv d3">
            <h4>{{ c.fitNo }}</h4>
            <ul>
              <li v-for="(li, i) in c.fitNoList" :key="i">{{ li }}</li>
            </ul>
          </div>
        </div>

        <div class="proof rv d3">
          <span v-for="(p, i) in c.proof" :key="i">{{ p[0] }}<b v-if="p[1]">{{ p[1] }}</b>{{ p[2] || '' }}</span>
        </div>

        <!-- 作者卡 -->
        <div class="author rv d3">
          <div class="a-tag">{{ c.authorTag }}</div>
          <div class="a-body">
            <div class="a-name">{{ c.authorName }}</div>
            <ul>
              <li v-for="(li, i) in c.authorLines" :key="i">{{ li }}</li>
            </ul>
          </div>
        </div>

        <!-- FAQ -->
        <div class="faq rv d3">
          <div class="faq-eyebrow">{{ c.faqEyebrow }}</div>
          <div class="faq-item" v-for="(f, i) in c.faqs" :key="i">
            <div class="faq-q">{{ f[0] }}</div>
            <div class="faq-a">{{ f[1] }}</div>
          </div>
        </div>

        <div class="mech">
          <div class="mech-item rv d2">
            <div class="m-tag">{{ c.mech1Tag }}</div>
            <p v-html="c.mech1Html"></p>
          </div>
          <div class="mech-item rv d3">
            <div class="m-tag">{{ c.mech2Tag }}</div>
            <p class="q">{{ c.mech2Q }}</p>
            <p>{{ c.mech2P }}</p>
          </div>
        </div>

        <div class="final-cta rv d3">
          <a class="btn btn-primary" href="#pricing">{{ c.finalCta }}</a>
          <p class="cta-risk">{{ c.finalRisk }}</p>
          <p class="cta-fine">{{ c.finalFine }}</p>
        </div>
      </div>
    </section>

    <!-- 固底条：滑到课程区后逐渐出现 -->
    <div class="dock" :class="{ show: showDock }">
      <div class="dock-inner">
        <button class="dock-btn" type="button" @click="toTop">{{ c.dockTop }}</button>
        <a class="dock-btn dock-hot" href="#pricing">{{ c.dockCta }}</a>
      </div>
    </div>

    <!-- 页脚 -->
    <footer class="geek-footer">
      <div class="wrap foot-inner">
        <div class="f-brand"><span class="prompt">$</span> fde4.ai · {{ c.footBrand }}</div>
        <div>
          <a :href="BOOK_REPO" target="_blank" rel="noopener">{{ c.footGh }}</a>
          <span class="sep">｜</span>
          {{ c.footNote }}
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* ============ 基础与变量 ============ */
.geek-home{
  --bg-0:#0A0A0A;
  --bg-1:#0F0F0F;
  --bg-2:#131313;
  --ink:#F2F2F2;
  --ink-2:#B8B8B8;
  --ink-3:#5A5A5A;
  --neon:#18F050;
  --neon-dim:rgba(24,240,80,.14);
  --line:rgba(255,255,255,.08);
  --line-strong:rgba(255,255,255,.14);
  --font-display:"Avenir Next","Futura","PingFang SC","Hiragino Sans GB",sans-serif;
  --font-mono:"Menlo","JetBrains Mono","SF Mono",monospace;
  --radius:16px;
  background:var(--bg-0);
  color:var(--ink);
  font-family:var(--font-display);
  font-size:16px;
  line-height:1.75;
  -webkit-font-smoothing:antialiased;
  overflow-x:hidden;
}
.geek-home *{margin:0;padding:0;box-sizing:border-box}
.geek-home ::selection{background:var(--neon);color:#0A0A0A}
/* 注意：不要给 .geek-home a 设 color——scoped attr 会抬高特异性，压过 .btn-primary 等单类色规则（白字压荧光绿事故） */
.geek-home a{text-decoration:none}

/* 噪点纹理（inline SVG feTurbulence） */
.geek-home::after{
  content:"";
  position:fixed;inset:0;
  pointer-events:none;z-index:999;
  opacity:.035;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

.wrap{max-width:1120px;margin:0 auto;padding:0 28px}

/* 加载 staggered reveal */
@keyframes rise{
  from{opacity:0;transform:translateY(22px)}
  to{opacity:1;transform:translateY(0)}
}
.rv{opacity:0;animation:rise .8s cubic-bezier(.22,.68,.28,1) forwards}
.d1{animation-delay:.05s}.d2{animation-delay:.15s}.d3{animation-delay:.25s}
.d4{animation-delay:.35s}.d5{animation-delay:.45s}.d6{animation-delay:.55s}
.d7{animation-delay:.65s}.d8{animation-delay:.75s}

/* 装饰 mono 标签 */
.tag{
  font-family:var(--font-mono);
  font-size:11px;
  letter-spacing:.26em;
  text-transform:uppercase;
  color:var(--ink-3);
}
.tag .accent{color:var(--neon)}

/* ============ Hero ============ */
.hero{
  position:relative;
  padding:120px 0 90px;
  overflow:hidden;
  text-align:center;
}
.hero::before{
  content:"";
  position:absolute;top:-22%;left:50%;
  transform:translateX(-50%);
  width:720px;height:720px;
  background:radial-gradient(circle,rgba(24,240,80,.13) 0%,rgba(24,240,80,.045) 42%,transparent 70%);
  pointer-events:none;
}
.hero::after{
  content:"";
  position:absolute;inset:0;
  background-image:
    linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);
  background-size:56px 56px;
  mask-image:radial-gradient(ellipse 75% 75% at 50% 28%,#000 20%,transparent 75%);
  -webkit-mask-image:radial-gradient(ellipse 75% 75% at 50% 28%,#000 20%,transparent 75%);
  pointer-events:none;
}
.hero .wrap{position:relative;z-index:2}

.badge{
  display:inline-flex;align-items:center;gap:10px;
  font-family:var(--font-mono);font-size:12px;letter-spacing:.12em;
  color:var(--neon);
  border:1px solid rgba(24,240,80,.4);
  background:var(--neon-dim);
  border-radius:999px;
  padding:7px 16px;
  margin-bottom:34px;
}
.badge .dot{
  width:6px;height:6px;border-radius:50%;background:var(--neon);
  box-shadow:0 0 8px var(--neon);
  animation:pulse 1.8s ease-in-out infinite;
}
@keyframes pulse{50%{opacity:.35}}

h1.hero-title{
  font-size:clamp(42px,7.4vw,80px);
  font-weight:800;
  letter-spacing:-.025em;
  line-height:1.03;
  margin-bottom:10px;
  border:none;
  padding:0;
}
h1 .dim{color:var(--ink-3);display:block}
h1 .em{
  display:block;
  font-family:var(--font-mono);
  letter-spacing:-.01em;
  background:linear-gradient(100deg,#18F050 20%,#8BFFA9 40%,#18F050 60%);
  background-size:200% 100%;
  -webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent;
  animation:flow 5s linear infinite;
}
@keyframes flow{
  0%{background-position:0% 0}
  100%{background-position:-200% 0}
}
.hero-sub{
  font-size:clamp(19px,2.8vw,30px);
  font-weight:700;letter-spacing:-.01em;
  color:var(--ink);
  margin-top:14px;
}

.tagline{
  max-width:640px;
  margin:28px auto 0;
  font-size:17px;color:var(--ink-2);line-height:1.8;
}
.tagline .en{
  font-family:var(--font-mono);
  font-size:14px;color:var(--ink-3);
  display:block;margin-bottom:6px;letter-spacing:.02em;
}
.tagline .shimmer{
  background:linear-gradient(100deg,var(--ink) 30%,var(--neon) 50%,var(--ink) 70%);
  background-size:200% 100%;
  -webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent;
  animation:flow 6s linear infinite;
  font-weight:600;
}

.cta-row{display:flex;gap:14px;margin-top:40px;flex-wrap:wrap;justify-content:center}
.btn{
  display:inline-flex;align-items:center;gap:8px;
  font-size:15px;font-weight:600;
  padding:14px 28px;border-radius:12px;
  transition:transform .18s,box-shadow .25s,background .2s,border-color .2s;
  letter-spacing:.02em;
}
.btn-primary{
  background:var(--neon);color:#060806;
  box-shadow:0 0 0 rgba(24,240,80,0);
}
.btn-primary:hover{
  transform:translateY(-2px);
  box-shadow:0 8px 32px rgba(24,240,80,.35);
}
.btn-ghost{
  border:1px solid var(--line-strong);color:var(--ink);
  background:rgba(255,255,255,.02);
}
.btn-ghost:hover{border-color:rgba(24,240,80,.55);color:var(--neon);transform:translateY(-2px)}
.btn-ghost.mono{font-family:var(--font-mono);font-size:13px}

.hero-infobar{
  margin-top:56px;
  padding-top:22px;
  border-top:1px solid var(--line);
  font-family:var(--font-mono);
  font-size:12.5px;letter-spacing:.06em;
  color:var(--ink-3);
  display:flex;gap:0;flex-wrap:wrap;
  justify-content:center;
}
.hero-infobar span{padding:0 18px;border-left:1px solid var(--line)}
.hero-infobar span:first-child{padding-left:0;border-left:none}
.hero-infobar b{color:var(--neon);font-weight:600}

/* 分隔线 */
.divider{height:1px;background:var(--line);max-width:1120px;margin:0 auto}

/* ============ 书籍特性条 ============ */
.features{background:var(--bg-1);padding:56px 0}
.features-grid{
  display:grid;grid-template-columns:repeat(3,1fr);gap:22px;
}
.feat{
  display:flex;gap:16px;align-items:flex-start;
  padding:24px 26px;
  background:var(--bg-2);
  border:1px solid var(--line);
  border-radius:var(--radius);
  transition:border-color .25s,box-shadow .25s;
}
.feat:hover{border-color:rgba(24,240,80,.4);box-shadow:0 0 24px rgba(24,240,80,.08)}
.feat .ico{font-size:22px;line-height:1.4}
.feat h3{font-size:15.5px;font-weight:700;margin-bottom:4px}
.feat p{font-size:13.5px;color:var(--ink-2);line-height:1.7}

/* ============ 区块通用 ============ */
section.block{padding:96px 0}
.eyebrow{
  font-family:var(--font-mono);
  font-size:12px;letter-spacing:.28em;text-transform:uppercase;
  color:var(--neon);
  margin-bottom:16px;
  display:flex;align-items:center;gap:12px;
}
.eyebrow::before{content:"";width:28px;height:1px;background:var(--neon)}
h2.sec-title{
  font-size:clamp(28px,4.2vw,44px);
  font-weight:800;letter-spacing:-.02em;line-height:1.15;
  margin-bottom:22px;
  border:none;padding:0;
}
.lead{font-size:16.5px;color:var(--ink-2);max-width:780px;line-height:1.9}
.lead + .lead{margin-top:16px}

/* ============ Stats 数字墙 ============ */
.stats{
  display:grid;grid-template-columns:repeat(4,1fr);
  border:1px solid var(--line);border-radius:var(--radius);
  margin:52px 0 64px;overflow:hidden;
  background:var(--bg-1);
}
.stat{
  padding:30px 26px;
  border-left:1px solid var(--line);
}
.stat:first-child{border-left:none}
.stat .num{
  font-size:clamp(26px,3.2vw,38px);font-weight:800;letter-spacing:-.02em;
  color:var(--ink);
}
.stat .num .u{color:var(--neon);font-size:.6em;font-family:var(--font-mono);margin-left:2px}
.stat .lbl{
  font-family:var(--font-mono);font-size:11px;
  letter-spacing:.22em;text-transform:uppercase;
  color:var(--ink-3);margin-top:6px;
}

/* ============ 课程包 6 卡 ============ */
.cards{
  display:grid;grid-template-columns:repeat(3,1fr);gap:20px;
  margin-top:12px;
}
.card{
  background:var(--bg-1);
  border:1px solid var(--line);
  border-radius:var(--radius);
  padding:28px 26px;
  position:relative;
  transition:border-color .25s,box-shadow .25s,transform .2s;
}
.card:hover{
  border-color:rgba(24,240,80,.5);
  box-shadow:0 0 28px rgba(24,240,80,.10),inset 0 0 0 1px rgba(24,240,80,.12);
  transform:translateY(-3px);
}
.card .idx{
  font-family:var(--font-mono);font-size:11px;
  letter-spacing:.24em;color:var(--neon);
  margin-bottom:14px;
}
.card h3{font-size:17px;font-weight:700;margin-bottom:8px}
.card p{font-size:13.8px;color:var(--ink-2);line-height:1.75}

/* ============ 工具包 K1-K5 ============ */
.kit{
  margin-top:56px;
  border:1px dashed rgba(24,240,80,.3);
  border-radius:var(--radius);
  padding:26px 30px;
  background:linear-gradient(180deg,rgba(24,240,80,.04),transparent);
}
.kit .kit-head{
  font-family:var(--font-mono);font-size:12px;
  letter-spacing:.24em;text-transform:uppercase;color:var(--neon);
  margin-bottom:14px;
}
.kit ul{list-style:none;display:flex;flex-wrap:wrap;gap:10px 26px}
.kit li{
  font-size:13.5px;color:var(--ink-2);
  font-family:var(--font-mono);letter-spacing:.01em;
}
.kit li b{color:var(--neon);font-weight:600;margin-right:6px}

/* ============ 七节大纲 ============ */
.syllabus{margin-top:64px}
.syll-head{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:20px}
.syll-head h3{font-size:20px;font-weight:700}
table.syll-table{width:100%;border-collapse:collapse;font-size:14px}
.syll-table th{
  font-family:var(--font-mono);font-size:11px;
  letter-spacing:.22em;text-transform:uppercase;
  color:var(--ink-3);text-align:left;
  padding:12px 16px;border-bottom:1px solid var(--line-strong);
}
.syll-table td{
  padding:16px;vertical-align:top;
  border-bottom:1px solid var(--line);
  color:var(--ink-2);line-height:1.7;
}
.syll-table tr{transition:background .2s}
.syll-table tbody tr:hover{background:rgba(24,240,80,.035)}
.syll-table .no{
  font-family:var(--font-mono);color:var(--neon);
  font-size:13px;white-space:nowrap;
}
.syll-table .tt{color:var(--ink);font-weight:600;white-space:normal}
.syll-table .min{
  font-family:var(--font-mono);font-size:12.5px;
  color:var(--ink-2);white-space:nowrap;
}

/* ============ 定价区 ============ */
.pricing{background:var(--bg-1)}
.tiers{
  display:grid;grid-template-columns:repeat(3,1fr);gap:20px;
  margin:48px 0 20px;
}
.tier{
  background:var(--bg-0);
  border:1px solid var(--line);
  border-radius:18px;
  padding:34px 30px;
  display:flex;flex-direction:column;
  transition:border-color .25s,box-shadow .25s,transform .2s;
  position:relative;
}
.tier:hover{transform:translateY(-3px);border-color:var(--line-strong)}
.tier.hot{
  border:1px solid var(--neon);
  box-shadow:0 0 40px rgba(24,240,80,.16),inset 0 0 0 1px rgba(24,240,80,.15);
  background:linear-gradient(180deg,rgba(24,240,80,.05),var(--bg-0) 55%);
}
.tier.hot:hover{box-shadow:0 0 56px rgba(24,240,80,.26),inset 0 0 0 1px rgba(24,240,80,.2)}
.tier .corner{
  position:absolute;top:-11px;left:26px;
  font-family:var(--font-mono);font-size:10.5px;
  letter-spacing:.24em;text-transform:uppercase;
  background:var(--neon);color:#060806;font-weight:700;
  padding:4px 12px;border-radius:999px;
}
.tier .t-name{font-size:15px;font-weight:700;color:var(--ink-2);margin-bottom:10px}
.tier.hot .t-name{color:var(--neon)}
.tier .t-price{
  font-size:clamp(38px,4vw,52px);font-weight:800;letter-spacing:-.03em;line-height:1;
  margin-bottom:14px;
}
.tier .t-price .cur{font-size:.45em;color:var(--ink-3);margin-right:2px;font-weight:600}
.tier .t-desc{font-size:13.8px;color:var(--ink-2);line-height:1.75;flex:1}
.tier .t-cta{
  margin-top:24px;text-align:center;
  font-size:14px;font-weight:600;
  padding:12px;border-radius:10px;
  border:1px solid var(--line-strong);color:var(--ink);
  transition:border-color .2s,color .2s,background .2s,box-shadow .25s;
}
.tier .t-cta:hover{border-color:var(--neon);color:var(--neon)}
.tier.hot .t-cta{background:var(--neon);border-color:var(--neon);color:#060806}
.tier.hot .t-cta:hover{box-shadow:0 6px 26px rgba(24,240,80,.35);color:#060806}
.tier-note{
  font-size:12.5px;color:var(--ink-3);
  font-family:var(--font-mono);letter-spacing:.03em;
  margin-bottom:8px;
}
.tier-perk-note{font-size:13px;color:var(--ink-3);margin-top:6px}
.tier-perk-note b{color:var(--ink-2)}

/* 创始学员权益 */
.founder{
  margin-top:36px;
  border:1px solid var(--line);border-radius:var(--radius);
  padding:26px 30px;background:var(--bg-0);
  display:flex;gap:18px;align-items:flex-start;
}
.founder .f-tag{
  font-family:var(--font-mono);font-size:11px;letter-spacing:.22em;
  text-transform:uppercase;color:var(--neon);white-space:nowrap;
  padding-top:4px;
}
.founder p{font-size:14px;color:var(--ink-2);line-height:1.85}
.founder :deep(b){color:var(--ink)}

/* 适合 / 不适合 */
.fit-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:24px}
.fit{
  border:1px solid var(--line);border-radius:var(--radius);
  padding:28px 30px;background:var(--bg-0);
}
.fit h4{
  font-family:var(--font-mono);font-size:12px;
  letter-spacing:.24em;text-transform:uppercase;
  margin-bottom:16px;
}
.fit.yes h4{color:var(--neon)}
.fit.no h4{color:var(--ink-3)}
.fit ul{list-style:none}
.fit li{
  font-size:14px;color:var(--ink-2);line-height:1.8;
  padding-left:24px;position:relative;margin-bottom:8px;
}
.fit.yes li::before{content:"→";position:absolute;left:0;color:var(--neon);font-family:var(--font-mono)}
.fit.no li::before{content:"×";position:absolute;left:2px;color:var(--ink-3);font-family:var(--font-mono)}
.fit.no li{color:var(--ink-3)}

/* 背书条 */
.proof{
  margin-top:44px;
  border-top:1px solid var(--line);border-bottom:1px solid var(--line);
  padding:20px 0;
  display:flex;flex-wrap:wrap;gap:10px 34px;
  font-family:var(--font-mono);font-size:12.5px;letter-spacing:.05em;
  color:var(--ink-3);
}
.proof b{color:var(--neon);font-weight:600}

/* 倒计时 */
.countdown{
  font-family:var(--font-mono);font-size:13px;letter-spacing:.1em;
  color:var(--neon);margin:-8px 0 18px;
}
.countdown b{font-size:16px}

/* 作者卡 */
.author{
  margin-top:44px;
  border:1px solid var(--line);border-radius:var(--radius);
  padding:28px 30px;background:var(--bg-0);
  display:flex;gap:22px;align-items:flex-start;
}
.author .a-tag{
  font-family:var(--font-mono);font-size:11px;letter-spacing:.22em;
  text-transform:uppercase;color:var(--neon);white-space:nowrap;
  padding-top:6px;
}
.author .a-name{font-size:22px;font-weight:800;letter-spacing:-.01em;margin-bottom:10px}
.author ul{list-style:none}
.author li{
  font-size:14px;color:var(--ink-2);line-height:1.9;
  padding-left:22px;position:relative;
}
.author li::before{content:"→";position:absolute;left:0;color:var(--neon);font-family:var(--font-mono)}

/* FAQ */
.faq{margin-top:44px}
.faq-eyebrow{
  font-family:var(--font-mono);font-size:11px;
  letter-spacing:.24em;text-transform:uppercase;
  color:var(--ink-3);margin-bottom:18px;
}
.faq-item{
  border-top:1px solid var(--line);
  padding:18px 0;
}
.faq-item:last-child{border-bottom:1px solid var(--line)}
.faq-q{font-size:15px;font-weight:700;color:var(--ink);margin-bottom:6px}
.faq-q::before{content:"Q ";color:var(--neon);font-family:var(--font-mono);margin-right:6px}
.faq-a{font-size:14px;color:var(--ink-2);line-height:1.85;padding-left:24px}

/* 预售机制 */
.mech{
  margin-top:44px;
  display:grid;grid-template-columns:repeat(2,1fr);gap:20px;
}
.mech-item{
  border:1px solid var(--line);border-radius:var(--radius);
  padding:26px 28px;background:var(--bg-0);
  transition:border-color .25s,box-shadow .25s;
}
.mech-item:hover{border-color:rgba(24,240,80,.35);box-shadow:0 0 20px rgba(24,240,80,.07)}
.mech-item .m-tag{
  font-family:var(--font-mono);font-size:11px;
  letter-spacing:.24em;text-transform:uppercase;
  color:var(--neon);margin-bottom:12px;
}
.mech-item p{font-size:14px;color:var(--ink-2);line-height:1.85}
.mech-item :deep(b){color:var(--ink)}
.mech-item .q{
  color:var(--ink);font-weight:600;
}

/* 主 CTA */
.final-cta{margin-top:56px;text-align:center}
.final-cta .btn{font-size:16px;padding:17px 44px}
.cta-risk{
  margin-top:16px;font-size:14px;font-weight:600;color:var(--ink-2);
}
.cta-risk::before{content:"✓ ";color:var(--neon);font-family:var(--font-mono)}
.cta-fine{
  margin-top:14px;font-size:12.5px;color:var(--ink-3);
  font-family:var(--font-mono);letter-spacing:.03em;
}

/* ============ 页脚 ============ */
.geek-footer{
  border-top:1px solid var(--line);
  padding:38px 0 46px;
  background:var(--bg-0);
}
.foot-inner{
  display:flex;justify-content:space-between;align-items:center;
  flex-wrap:wrap;gap:14px;
  font-size:13px;color:var(--ink-3);
}
.foot-inner .f-brand{font-family:var(--font-mono);letter-spacing:.04em}
.foot-inner .f-brand .prompt{color:var(--neon)}
.foot-inner a{transition:color .2s}
.foot-inner a:hover{color:var(--neon)}
.foot-inner .sep{margin:0 12px;color:var(--line-strong)}

/* ============ 手册章节流 ============ */
.chaps{
  display:grid;grid-template-columns:repeat(4,1fr);gap:16px;
  margin-top:44px;
}
.chap{
  border:1px solid var(--line);border-radius:12px;
  padding:20px 22px;background:var(--bg-1);
  transition:border-color .25s,box-shadow .25s,transform .2s;
}
.chap:hover{
  border-color:rgba(24,240,80,.45);
  box-shadow:0 0 20px rgba(24,240,80,.08);
  transform:translateY(-2px);
}
.chap .ch-no{
  font-family:var(--font-mono);font-size:12px;
  letter-spacing:.2em;color:var(--neon);margin-bottom:8px;
}
.chap .ch-tt{font-size:15px;font-weight:700;color:var(--ink);line-height:1.5}
.book-outro{
  margin-top:28px;font-size:13.5px;color:var(--ink-3);line-height:1.9;
  max-width:760px;
}
.book-cta{margin-top:36px}

/* ============ 固底条 ============ */
.dock{
  position:fixed;left:0;right:0;bottom:0;z-index:90;
  transform:translateY(110%);
  opacity:0;
  transition:transform .45s cubic-bezier(.22,.68,.28,1),opacity .45s;
  pointer-events:none;
}
.dock.show{
  transform:translateY(0);
  opacity:1;
  pointer-events:auto;
}
.dock-inner{
  max-width:560px;margin:0 auto 18px;
  display:flex;gap:12px;justify-content:center;
  padding:12px 16px;
  background:rgba(15,15,15,.88);
  backdrop-filter:blur(14px);
  -webkit-backdrop-filter:blur(14px);
  border:1px solid var(--line-strong);
  border-radius:16px;
  box-shadow:0 12px 40px rgba(0,0,0,.55);
}
.dock-btn{
  font-family:var(--font-mono);font-size:13px;letter-spacing:.04em;
  padding:11px 22px;border-radius:10px;cursor:pointer;
  border:1px solid var(--line-strong);
  background:transparent;color:var(--ink);
  transition:border-color .2s,color .2s,box-shadow .25s,transform .18s;
}
.dock-btn:hover{border-color:rgba(24,240,80,.55);color:var(--neon)}
.dock-btn.dock-hot{
  background:var(--neon);border-color:var(--neon);color:#060806;font-weight:700;
}
.dock-btn.dock-hot:hover{
  color:#060806;
  box-shadow:0 6px 26px rgba(24,240,80,.4);
  transform:translateY(-1px);
}
@supports (padding: env(safe-area-inset-bottom)){
  .dock-inner{margin-bottom:calc(18px + env(safe-area-inset-bottom))}
}

/* ============ 响应式 ============ */
@media (max-width:960px){
  .chaps{grid-template-columns:repeat(2,1fr)}
  .cards{grid-template-columns:repeat(2,1fr)}
  .stats{grid-template-columns:repeat(2,1fr)}
  .stat:nth-child(3){border-left:none}
  .stat:nth-child(n+3){border-top:1px solid var(--line)}
  .tiers{grid-template-columns:1fr;max-width:480px;margin-left:auto;margin-right:auto}
  .fit-grid{grid-template-columns:1fr}
  .mech{grid-template-columns:1fr}
}
@media (max-width:720px){
  .hero{padding:76px 0 64px}
  .chaps{grid-template-columns:1fr 1fr}
  .dock-inner{max-width:calc(100% - 24px)}
  .features-grid{grid-template-columns:1fr}
  .cards{grid-template-columns:1fr}
  section.block{padding:68px 0}
  .syll-table th:nth-child(4),.syll-table td:nth-child(4){display:none}
  .founder{flex-direction:column;gap:8px}
  .author{flex-direction:column;gap:10px}
}
@media (prefers-reduced-motion:reduce){
  .geek-home *,.geek-home *::before,.geek-home *::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
  .rv{opacity:1}
}
</style>
