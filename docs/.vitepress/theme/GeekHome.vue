<script setup>
// fde4.ai 首页 · V1 深色极客工具风（参考 dimagent.com）
// 文案真源：课程 canon v1.1（2026-08-10 锁定 + 08-12 口径增补）
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  lang: { type: String, default: 'zh' },
})

const BOOK_REPO = 'https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer'
const ORDER_FORM = 'https://zerodaybook.mikecrm.com/oc3Whb0' // 早鸟预购表单（MikeCRM，2026-08-13 上线）

// 固底条：滑到课程区（第三屏）后逐渐出现
const showDock = ref(false)
let courseEl = null
const onScroll = () => {
  if (!courseEl) courseEl = document.getElementById('course')
  const trigger = courseEl ? courseEl.offsetTop - window.innerHeight * 0.5 : window.innerHeight * 1.5
  showDock.value = window.scrollY > trigger
}
const toTop = () => window.scrollTo({ top: 0, behavior: 'smooth' })

// 早鸟倒计时（2026-08-26 21:00 开播即截止，canon 时间表）
const daysLeft = ref(0)
const saleEnded = ref(false)
const hydrated = ref(false) // SSR 首帧不渲染倒计时，防「今天截止」闪现
const calcDays = () => {
  const remain = new Date('2026-08-26T21:00:00+08:00').getTime() - Date.now()
  saleEnded.value = remain <= 0
  daysLeft.value = Math.max(0, Math.floor(remain / 86400000))
}
let daysTimer = null
onMounted(() => {
  onScroll()
  calcDays()
  hydrated.value = true
  daysTimer = setInterval(calcDays, 3600000) // 每小时重算，防长挂标签页过期
  window.addEventListener('scroll', onScroll, { passive: true })
})
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  clearInterval(daysTimer)
})

const copy = {
  zh: {
    badge: '开源手册 · 全文免费 · GitHub 4k+ Star',
    titleDim: '前线部署工程师',
    titleEm: 'FDE',
    heroSub: '免费开源手册 + 付费课程·社群',
    authorLine: '范冰 著',
    tagMono: 'THE OPEN-SOURCE FIELD GUIDE FOR FORWARD DEPLOYED ENGINEERS',
    tagPre: '一本写给 AI 交付者的实战手册：从岗位全貌、赢得客户到激活部署，讲清 FDE 怎么',
    tagShimmer: '在客户一线把 AI 项目做成',
    tagPost: '。',
    ctaGh: 'GitHub 项目 ↗',
    ctaRead: '免费阅读手册 →',
    ctaCourse: '付费课程/社群 ↓',
    info: [['全文免费', ''], ['GitHub ', '4k+ Star'], ['持续版本化更新', '']],
    features: [],
    whyEyebrow: 'WHY FDE · 岗位背景',
    whyTitle: 'Palantir 开创的岗位，AI 时代的刚需',
    whyLead1: 'FDE（Forward Deployed Engineer，前线部署工程师）由 Palantir 开创：把工程师派到客户一线，在现场把平台能力变成真实的业务结果。',
    whyLead2: '大模型时代，「买模型容易、落地难」是所有企业的共同瓶颈——这个角色正从硅谷的小众工种变成 AI 交付的标配：OpenAI、Anthropic、微软、Sierra、Harvey 都在组建 FDE 团队。',
    whyStats: [
      { num: '+1165', unit: '%', lbl: 'FDE 岗位需求年增幅 · 据公开报道' },
      { num: '8,900', unit: '人', lbl: 'TCS 单家拟招 FDE · 据公开报道' },
      { num: '巨头抢人', unit: '', lbl: 'OpenAI / Anthropic / 微软 / Sierra / Harvey' },
      { num: '落地刚需', unit: '', lbl: '买模型容易，把模型变成结果难' },
    ],
    bookEyebrow: 'THE HANDBOOK · 手册内容',
    bookTitle: '这本免费开源手册讲了什么',
    bookLead: '从岗位崛起到规模化复制——一个 FDE 的完整作战周期，八章走完。',
    chapters: [
      ['01', 'FDE 的崛起', '/book/01-第1章-FDE的崛起'],
      ['02', '解决正确的问题', '/book/02-第2章-解决正确的问题'],
      ['03', '赢得客户', '/book/03-第3章-赢得客户'],
      ['04', '激活部署', '/book/04-第4章-激活部署'],
      ['05', '守住续约', '/book/05-第5章-守住续约'],
      ['06', '扩大收入', '/book/06-第6章-扩大收入'],
      ['07', '规模化复制', '/book/07-第7章-规模化复制'],
      ['08', '完整案例集', '/book/08-第8章-完整案例集'],
    ],
    outroParts: [
      ['text', '另有'], ['link', '自序', '/book/00-自序'], ['text', '、'],
      ['link', '后记《FDE 的职业道德》', '/book/09-后记-FDE的职业道德'], ['text', ' 与三份附录：'],
      ['link', 'A · 常用指标清单', '/book/10-附录A-FDE应当关注的常用指标'], ['text', ' / '],
      ['link', 'B · FDE 人物与团队名单', '/book/11-附录B-FDE人物与团队名单'], ['text', ' / '],
      ['link', 'C · 全书案例索引与资料出处', '/book/12-附录C-全书案例索引与资料出处'],
    ],
    bookCta: '免费阅读手册 →',
    courseEyebrow: '付费课程 · FDE 线上课程（2026）· 早鸟预购中',
    courseTitle1: '一个人读书，',
    courseTitle2: '一群人实战',
    lead1: '开源手册解决「知道」：岗位全貌、方法论主干、落地框架——全文免费，读到够用就到此为止。',
    lead2: '但如果你要的是「做到」——这门付费课程是手册的实战延伸：与书的重合度不到 20%，其余 80% 全是书里没有的东西。',
    lead3: '实战为主：大量一手源案例（Bob McGrew 的 YC 原版、Palantir 官方、各厂 FDE 负责人亲述）打底，加上作者本人的亲身顾问经验与失败复盘，再配能带走的工具包，和直播前即可加入的学习社群。',
    stats: [
      { num: '100', unit: 'MIN+', lbl: '核心视频 只多不少' },
      { num: '80', unit: '%', lbl: '免费手册里没有的增量内容' },
      { num: '5', unit: '件', lbl: '工具包 带走就能用' },
      { num: '直播', unit: '+ 录屏', lbl: '社群内首发 · 群内观看' },
    ],
    courseCta: '立即购买课程并加入学习社群·早鸟 ¥199 →',
    cards: [
      { idx: '01 / CORE', h: '核心视频', p: '100min+，讲练结合，只多不少' },
      { idx: '02 / TOOLKIT', h: '工具包 5 件', p: '带走就能用的模板' },
      { idx: '03 / PRACTICE', h: '实操拆解', p: '课程现场抛出问题、逐步讲解，带你拆解一个真实业务场景，当堂完成你的第一张《企业 AI 项目可行性一页纸》' },
      { idx: '04 / MATERIAL', h: '课件与回放', p: '购课即得观看版 PDF；直播后提供完整视频回放' },
      { idx: '05 / LIVE', h: '直播与答疑', p: '学习社群内直播首发（8 月 26 日周三 21:00，仅限群内观看）+ 事后提供直播录屏' },
      { idx: '06 / COMMUNITY', h: '学习社群', p: '直播前即可入群交流；首发直播仅限群内观看——社群也是同路人的天然过滤器' },
    ],
    kitHead: 'TOOLKIT · 五件一览',
    kits: [
      '《FDE 岗位能力自测表》',
      '《企业 AI 项目可行性一页纸》',
      '《交付三关检查清单》',
      '《FDE 入场前 30 天准备清单》',
      '《FDE 面试题库与备战清单》',
    ],
    syllTitle: '大纲（暂定）',
    syllTag: '以实际交付为准 · TENTATIVE',
    syllHead: ['No.', '标题', '一句话'],
    syllabus: [
      ['01', 'FDE 岗位全貌：为什么是现在，以及泼一盆冷水', '需求数据之外，讲清中国真实岗位盘子；教的是可迁移技能，不是空头 title'],
      ['02', '边界澄清：FDE 不是什么', 'vs 售前/交付/咨询/外包，附假 FDE 识别法'],
      ['03', '方法论：一个主干、一个印证、一个能带走的框架', '全课只精讲 DROP5 五问法一个框架'],
      ['04', '书里书外：出版后的实战修正', '中美差异、信任周期、落地三道坎'],
      ['05', '案例：我的顾问现场', '本人失败复盘 + 交付实证，DROP5 完整走一遍'],
      ['06', '入场双轨：进企业 or 独立接单', '能力模型与面试备战 / 接单五步评估与客户筛选'],
      ['07', '第 1 / 3 / 7 天行动清单 + 你的第一张一页纸', '实操拆解收束：当堂产出你的第一张可行性一页纸'],
    ],
    priceEyebrow: 'Pricing · 早鸟截止 8 月 26 日',
    priceTitle: '早鸟 ¥199，8 月 26 日开播后恢复 ¥299',
    priceLead: '¥299 即全部——无后端升单、不加微信卖咨询。',
    countPre: '距早鸟截止还有 ',
    countPost: ' 天',
    countToday: '今天截止，最后机会',
    tiers: [
      { hot: false, name: '正式价', price: '299', desc: '8 月 26 日开播后生效 · 明码标价，不议价', cta: '预售期买早鸟更划算 →' },
      { hot: true, corner: '优选 · 早鸟', name: '早鸟预售', price: '199', desc: '预售价 ¥199 · 8 月 26 日 21:00 开播前有效，之后恢复 ¥299', cta: '立即预订' },
      { hot: false, name: '老客户红包', price: '99', desc: '知识星球（ZengZhang.AI VIP）成员购买后，微信联络我并出示购买成功截图，派发 99 元红包', cta: '去我知识星球看看 →', link: 'https://wx.zsxq.com/group/15528815482422' },
    ],
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
      '还处于了解 AI 早期阶段的老板 / 决策者——更适合你的线下课我正在制作中，这门课的实操浓度对你可能太高',
    ],
    proof: [['开源书 ', '4k+ Star'], ['《增长黑客》作者 · ', 'ZengZhang.AI 主理人'], ['真实交付案例（东风汽车 / 华为荣耀 / 金融机构 / 直播 MCN 等）', '']],
    authorTag: '讲师 · YOUR INSTRUCTOR',
    authorName: '范冰',
    authorLines: [
      '《增长黑客》作者、ZengZhang.AI 主理人',
      '10 年+ 营销咨询顾问经验，AI 前沿玩家',
      '服务过东风汽车、华为荣耀、金融机构、直播 MCN 等企业客户',
      '书里写方法论，课里讲实操经验与案例干货',
    ],
    faqEyebrow: 'FAQ · 你可能想问',
    faqs: [
      ['我读过开源手册了，还需要买课吗？', '重合度不到 20%。手册给方法论主干，课程给实战案例、亲身复盘、工具包与社群。'],
      ['直播还是录播？', '直播首发 + 事后录屏。入群可看首发直播并现场交流；不入群也能在两天内通过 Email 收到全部课件。'],
      ['课程什么时候能看？', '8 月 26 日（周三）21:00 学习社群内首发直播，仅限群内观看；直播后两天内，无论是否入群，都会通过 Email 收到课件（PDF + 视频回放）。'],
      ['怎么加入学习社群（微信群）？', '购买表单里会要求您留下微信号，我会主动加您——一般在工作时间处理；晚间和周末要带娃，回复可能不及时，请见谅。等人数达到一定规模后集体拉群。另外声明：您也可以选择不进群——不进群就看不到 8 月 26 日的首发直播，但课程视频、课件资料等都会在直播后两天内通过 Email 照常发给您，一样不少。'],
      ['课件怎么交付？', '首播后两天内，课件 PDF 与视频回放（网盘 / YouTube 链接）统一通过 Email 发送——建议优先使用 Gmail、iCloud 等国际邮箱，QQ、163 等国产邮箱可能误过滤；开课后第一时间没收到，请先检查垃圾箱。客服邮箱：xdash@duck.com'],
      ['可以开发票吗？购买后能退款吗？', '发票：本课程为个人数字内容产品，无企业主体，无法开具发票，介意请慎拍。退款：虚拟数字内容一经售出，概不退款——下单前如有任何疑问，欢迎先发邮件到 xdash@duck.com 问清楚再买。'],
      ['我是企业经营决策者 / 老板 / 非一线业务人士，适合学吗？', '看您的学习目标：如果您对业务细节感兴趣、希望身先士卒搞清楚一线怎么把 AI 项目做成，可以学——这门课教的就是一线实操；如果您只想建立概念、把握方向，这门课的实操浓度对您可能太高——更适合您的线下课我正在制作中。'],
    ],
    perksTag: '预购专享 · 开播后绝版',
    perksTitle: '现在预购，独享三项福利',
    perksNote: '三项福利均为预购专享——8 月 26 日开播后购买，只有回放与课件，不再享有',
    perks: [
      { t: '首发直播入场券', p: '8 月 26 日（周三）21:00 学习社群内直播，仅限群内观看，现场提问现场答；开播后购买只能看回放' },
      { t: '你的问题进课堂', p: '提交购买表单时留下你最感兴趣的问题——我大概率会在课程内直接解答' },
      { t: '让我认识你', p: '表单里留下你的背景信息 / 业务介绍：为你介绍适合的项目；信息足够真实优质，收录进 fde4.ai 生态地图、行业名录、案例库，向行业公开展示' },
    ],
    finalCta: '立即预订 · 早鸟 ¥199 →',
    finalRisk: '直播后两天内 Email 收到课件（PDF + 视频回放），不依赖任何第三方平台',
    closingEyebrow: 'WHY NOW · 写在最后',
    closingTitle: 'AI 时代最稀缺的，不是模型，是把模型变成结果的人',
    closingLead: '技术贬值越来越快，一线交付能力越来越贵。FDE 是这轮 AI 浪潮里少数「离钱最近」的技术岗位——手册给你地图，课程和社群陪你走第一程。',
    closingRead: '免费阅读手册',
    footBrand: '《前线部署工程师》开源书 · 作者范冰',
    footGh: 'GitHub 开源共建',
    footNote: '课程咨询：xdash@duck.com',
    footLinks: '友情链接',
    dockTop: '返回顶部 ↑',
    dockCta: '立即预订 · 早鸟 ¥199',
  },
  en: {
    badge: 'Open-source Handbook · Free to Read · 4k+ GitHub Stars',
    titleDim: 'Forward Deployed Engineer',
    titleEm: 'FDE',
    heroSub: 'Free Open Handbook + Paid Course & Community',
    authorLine: 'by Fan Bing',
    tagMono: '前线部署工程师的开源实战手册',
    tagPre: 'A field guide for AI builders: from the FDE landscape and winning customers to activating deployments — how FDEs ',
    tagShimmer: 'get AI projects done on the customer frontline',
    tagPost: '.',
    ctaGh: 'GitHub Project ↗',
    ctaRead: 'Read the Handbook Free →',
    ctaCourse: 'Paid Course & Community ↓',
    info: [['Free to Read', ''], ['GitHub · ', '4k+ Stars'], ['Versioned, Continuously Updated', '']],
    features: [],
    whyEyebrow: 'WHY FDE · THE ROLE',
    whyTitle: 'A role pioneered by Palantir. A necessity of the AI era.',
    whyLead1: 'FDE (Forward Deployed Engineer) was pioneered by Palantir: engineers embedded on the customer frontline, turning platform capabilities into real business outcomes.',
    whyLead2: 'In the LLM era, "easy to buy models, hard to land them" is every enterprise\'s bottleneck — and OpenAI, Anthropic, Microsoft, Sierra, and Harvey are all building FDE teams.',
    whyStats: [
      { num: '+1165', unit: '%', lbl: 'YoY growth in FDE job postings · public reports' },
      { num: '8,900', unit: '', lbl: 'FDEs TCS plans to hire · public reports' },
      { num: 'Big players hiring', unit: '', lbl: 'OpenAI / Anthropic / Microsoft / Sierra / Harvey' },
      { num: 'Landing is the moat', unit: '', lbl: 'Buying models is easy; turning them into results is hard' },
    ],
    bookEyebrow: 'THE HANDBOOK · CONTENTS',
    bookTitle: 'What\'s in this free, open handbook',
    bookLead: 'From the rise of the role to scaling what works — a complete FDE campaign cycle in eight chapters.',
    chapters: [
      ['01', 'The Rise of FDE', '/book/01-第1章-FDE的崛起'],
      ['02', 'Solving the Right Problems', '/book/02-第2章-解决正确的问题'],
      ['03', 'Winning the Customer', '/book/03-第3章-赢得客户'],
      ['04', 'Activating the Deployment', '/book/04-第4章-激活部署'],
      ['05', 'Keeping the Renewal', '/book/05-第5章-守住续约'],
      ['06', 'Expanding Revenue', '/book/06-第6章-扩大收入'],
      ['07', 'Scaling What Works', '/book/07-第7章-规模化复制'],
      ['08', 'The Complete Case Files', '/book/08-第8章-完整案例集'],
    ],
    outroParts: [
      ['text', 'Also: '], ['link', 'Preface', '/book/00-自序'], ['text', ' · '],
      ['link', 'Afterword: FDE Professional Ethics', '/book/09-后记-FDE的职业道德'], ['text', ' · Appendices: '],
      ['link', 'A · Key Metrics', '/book/10-附录A-FDE应当关注的常用指标'], ['text', ' / '],
      ['link', 'B · People & Teams', '/book/11-附录B-FDE人物与团队名单'], ['text', ' / '],
      ['link', 'C · Case Index & Sources', '/book/12-附录C-全书案例索引与资料出处'],
    ],
    bookCta: 'Read the Handbook Free →',
    courseEyebrow: 'PAID COURSE · FDE ONLINE COURSE (2026) · EARLY-BIRD PRE-SALE',
    courseTitle1: 'Don\'t read alone —',
    courseTitle2: 'join the cohort',
    lead1: 'The free handbook covers the "what": the role, the methodology backbone, the landing frameworks — free forever, and enough for many.',
    lead2: 'But if you want to get from "knowing" to "doing" — this paid course is the hands-on extension of the handbook: less than 20% overlap with the book, the other 80% is all new material.',
    lead3: 'Practice-first: the author\'s own consulting experience and failure post-mortems, first-hand sources (Bob McGrew\'s original YC talk, Palantir official materials, FDE leads\' own accounts), take-away toolkits — plus a learning community you can join before the live premiere.',
    stats: [
      { num: '100', unit: 'MIN+', lbl: 'Core Video, More if Anything' },
      { num: '80', unit: '%', lbl: 'New Beyond the Free Handbook' },
      { num: '5', unit: '', lbl: 'Take-away Toolkits' },
      { num: 'Live', unit: '+ Replay', lbl: 'Community Premiere' },
    ],
    courseCta: 'Buy the Course & Join the Community · Early Bird ¥199 →',
    cards: [
      { idx: '01 / CORE', h: 'Core Videos', p: '100min+ core videos, learn by doing — more if anything' },
      { idx: '02 / TOOLKIT', h: 'Toolkit × 5', p: 'Take-away templates that work out of the box' },
      { idx: '03 / PRACTICE', h: 'Live Teardown', p: 'A real business scenario is posed and worked through in class — you finish your first Enterprise AI Feasibility One-Pager on the spot' },
      { idx: '04 / MATERIAL', h: 'Materials & Replay', p: 'Viewing PDF on purchase; full video replay after the live session' },
      { idx: '05 / LIVE', h: 'Live & Q&A', p: 'Premiere live in the community (Aug 26, Wed 21:00, members only) + recording afterwards' },
      { idx: '06 / COMMUNITY', h: 'Learning Community', p: 'Join and chat before the premiere; the live premiere is members-only — the community is a natural filter for fellow travelers' },
    ],
    kitHead: 'TOOLKIT · ALL FIVE',
    kits: [
      'FDE Competency Self-Assessment',
      'Enterprise AI Feasibility One-Pager',
      'Delivery Three-Gate Checklist',
      '30-Day Pre-Entry Checklist',
      'FDE Interview Bank & Prep Plan',
    ],
    syllTitle: 'Syllabus (Tentative)',
    syllTag: 'SUBJECT TO CHANGE',
    syllHead: ['No.', 'Title', 'In one line'],
    syllabus: [
      ['01', 'The FDE Landscape: Why Now, with a Cold Shower', 'Beyond demand data: the real hiring landscape; transferable skills, not an empty title'],
      ['02', 'Boundaries: What FDE Is Not', 'vs pre-sales / delivery / consulting / outsourcing, plus how to spot a fake FDE'],
      ['03', 'Methodology: One Backbone, One Corroboration, One Framework', 'The whole course teaches exactly one framework: the DROP5 five questions'],
      ['04', 'Beyond the Book: Field Corrections Since Publication', 'China–US differences, trust cycles, three hurdles to landing'],
      ['05', 'Cases: My Consulting Frontline', 'My own failure post-mortem + delivery evidence, DROP5 in full action'],
      ['06', 'Two Tracks In: Join a Company or Go Independent', 'Competency model & interview prep / five-step project & client screening'],
      ['07', 'Day 1 / 3 / 7 Action List + Your First One-Pager', 'Live teardown finale: produce your first feasibility one-pager in class'],
    ],
    priceEyebrow: 'Pricing · Early Bird Ends Aug 26',
    priceTitle: 'Early Bird ¥199 — back to ¥299 once we go live Aug 26',
    priceLead: '¥299 is all-inclusive — no upsells, no WeChat consulting funnel.',
    countPre: 'Only ',
    countPost: ' days left before early bird ends',
    countToday: 'Ends today — last chance',
    tiers: [
      { hot: false, name: 'Standard', price: '299', desc: 'Effective after the Aug 26 premiere · flat price, no bargaining', cta: 'Early bird ¥199 is better →' },
      { hot: true, corner: 'BEST PICK', name: 'Early Bird Pre-sale', price: '199', desc: '¥199 until the Aug 26 premiere (21:00 GMT+8), then ¥299', cta: 'Reserve Now' },
      { hot: false, name: 'Alumni Red Packet', price: '99', desc: 'Planet (ZengZhang.AI VIP) members: after purchase, message me on WeChat with your receipt screenshot for a ¥99 red packet', cta: 'Visit my Planet →', link: 'https://wx.zsxq.com/group/15528815482422' },
    ],
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
      'Owners / decision-makers still early in their AI journey — a course designed for you is in the works; this one may be too hands-on',
    ],
    proof: [['Open-source book · ', '4k+ Stars'], ['Author of ', 'Growth Hacker', ' · founder of ZengZhang.AI'], ['Real delivery cases (Dongfeng Motor / Huawei Honor / financial institutions / live-commerce MCN)', '']],
    authorTag: 'YOUR INSTRUCTOR',
    authorName: 'Fan Bing',
    authorLines: [
      'Author of Growth Hacker, founder of ZengZhang.AI',
      '10+ years in marketing consulting, AI frontier practitioner',
      'Served Dongfeng Motor, Huawei Honor, financial institutions, live-commerce MCNs, and more',
      'The book gives the methodology; the course gives hands-on experience and real cases',
    ],
    faqEyebrow: 'FAQ · YOU MAY WONDER',
    faqs: [
      ['I already read the handbook. Do I need the course?', 'Less than 20% overlap. The handbook gives the methodology; the course gives cases, first-hand post-mortems, toolkits, and community.'],
      ['Live or recorded?', 'Live premiere + recording afterwards. Members watch live and interact; non-members get everything by email within two days.'],
      ['When do I get access?', 'Premiere live in the community on Aug 26 (Wed) 21:00, members only; within two days, everyone receives the materials (PDF + video replay) by email.'],
      ['How do I join the community (WeChat group)?', 'The order form asks for your WeChat ID, and I\'ll add you myself — usually during work hours; evenings and weekends are family time, so replies may be slow. Once enough people have joined, I\'ll invite everyone into the group together. Note: you can also choose not to join — you\'d miss the Aug 26 live premiere, but all videos and materials still arrive by email within two days, nothing lost.'],
      ['How are materials delivered?', 'Within two days of the premiere, the PDF and video replay (cloud drive / YouTube link) are sent by email — Gmail / iCloud recommended; QQ / 163 and other domestic providers may misfilter. If nothing arrives, check spam first. Support: xdash@duck.com'],
      ['Can I get an invoice? Is it refundable?', 'Invoice: this is a personal digital product with no corporate entity, so no invoice (fapiao) can be issued — please don\'t buy if you need one. Refund: digital content is final sale, no refunds once purchased — if you have any doubts, email xdash@duck.com and ask before ordering.'],
      ['I\'m a business owner / decision-maker, not a frontline practitioner. Is this for me?', 'It depends on your goal: if you enjoy getting into the details and want to lead from the front — to understand how AI projects actually land on the ground — yes, that\'s exactly what this course teaches. If you only want concepts and direction, it\'s probably too hands-on for you — a course designed for you is in the works.'],
    ],
    perksTag: 'PRE-ORDER ONLY · GONE AFTER LAUNCH',
    perksTitle: 'Three perks you only get by pre-ordering',
    perksNote: 'All three are pre-order exclusives — buy after the Aug 26 premiere and you get the replay and materials only',
    perks: [
      { t: 'Seat at the Premiere', p: 'Live in the community on Aug 26 (Wed) 21:00, members only — ask questions in real time; later buyers get the replay only' },
      { t: 'Your Question in Class', p: 'Leave the question you care about most in the order form — chances are I\'ll answer it directly in the course' },
      { t: 'Let Me Know You', p: 'Share your background / business in the form: I\'ll point you to fitting projects; authentic, strong profiles get featured in fde4.ai\'s ecosystem map, industry directory, and case library' },
    ],
    finalCta: 'Reserve · Early Bird ¥199 →',
    finalRisk: 'Materials (PDF + video replay) arrive by email within two days of the live session — no third-party platform required',
    closingEyebrow: 'WHY NOW · PARTING WORDS',
    closingTitle: 'The scarcest thing in the AI era is not models — it\'s people who turn models into results',
    closingLead: 'Tech depreciates fast; frontline delivery appreciates. FDE is one of the closest-to-revenue technical roles of this wave — the handbook gives you the map; the course and community walk the first mile with you.',
    closingRead: 'Read the Handbook Free',
    footBrand: 'The FDE Field Guide (open source) · by Fan Bing',
    footGh: 'GitHub',
    footNote: 'Course inquiries: xdash@duck.com',
    footLinks: 'Links',
    dockTop: 'Back to Top ↑',
    dockCta: 'Reserve · Early Bird ¥199',
  },
}

const c = copy[props.lang] || copy.zh
const bookLink = '/book/'
const friendLinks = [
  { label: 'diy-jarvis.com', href: 'https://diy-jarvis.com' },
  { label: 'zengzhangheike.com', href: 'https://www.zengzhangheike.com' },
  { label: 'xdash.me', href: 'https://xdash.me' },
]
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
        <div class="hero-author rv d2">{{ c.authorLine }}</div>

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

    <div class="divider"></div>

    <!-- WHY FDE · 岗位背景区（深色分层带） -->
    <section class="block why-band">
      <div class="wrap">
        <div class="eyebrow rv d1">{{ c.whyEyebrow }}</div>
        <h2 class="sec-title rv d2">{{ c.whyTitle }}</h2>
        <p class="lead rv d3">{{ c.whyLead1 }}</p>
        <p class="lead rv d4">{{ c.whyLead2 }}</p>

        <div class="stats why-stats rv d5">
          <div class="stat" v-for="(s, i) in c.whyStats" :key="i">
            <div class="num">{{ s.num }}<span class="u" v-if="s.unit"> {{ s.unit }}</span></div>
            <div class="lbl">{{ s.lbl }}</div>
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
          <a class="chap" v-for="(ch, i) in c.chapters" :key="i" :href="ch[2]" target="_blank" rel="noopener">
            <div class="ch-no">{{ ch[0] }}</div>
            <div class="ch-tt">{{ ch[1] }}</div>
          </a>
        </div>

        <p class="book-outro rv d4">
          <template v-for="(p, i) in c.outroParts" :key="i">
            <a v-if="p[0] === 'link'" :href="p[2]" target="_blank" rel="noopener">{{ p[1] }}</a>
            <span v-else>{{ p[1] }}</span>
          </template>
        </p>

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
        <div class="cta-row lead-cta rv d6">
          <a class="btn btn-primary" :href="ORDER_FORM" target="_blank" rel="noopener">{{ c.courseCta }}</a>
        </div>

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
            <li v-for="(k, i) in c.kits" :key="i">{{ k }}</li>
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
                <th style="width:44%">{{ c.syllHead[2] }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, i) in c.syllabus" :key="i">
                <td class="no">{{ row[0] }}</td>
                <td class="tt">{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <!-- 屏 3 · 定价与门槛 -->
    <section class="block pricing">
      <div class="wrap">
        <div class="eyebrow rv d1">{{ c.priceEyebrow }}</div>

        <!-- 预购专享福利带（开播后绝版） -->
        <div class="perks rv d2">
          <div class="perks-head">
            <span class="perks-tag">{{ c.perksTag }}</span>
            <span class="perks-title">{{ c.perksTitle }}</span>
          </div>
          <div class="perks-grid">
            <div class="perk" v-for="(p, i) in c.perks" :key="i">
              <div class="perk-no">0{{ i + 1 }}</div>
              <div class="perk-t">{{ p.t }}</div>
              <div class="perk-p">{{ p.p }}</div>
            </div>
          </div>
          <div class="perks-note">{{ c.perksNote }}</div>
        </div>

        <h2 class="sec-title rv d2" id="pricing">{{ c.priceTitle }}</h2>
        <p class="countdown rv d2" v-if="hydrated && !saleEnded">
          <template v-if="daysLeft > 0">{{ c.countPre }}<b>{{ daysLeft }}</b>{{ c.countPost }}</template>
          <template v-else><b>{{ c.countToday }}</b></template>
        </p>
        <p class="lead rv d2">{{ c.priceLead }}</p>

        <div class="tiers">
          <div class="tier rv" :class="[{ hot: t.hot }, 'd' + (i + 2)]" v-for="(t, i) in c.tiers" :key="i">
            <div class="corner" v-if="t.corner">{{ t.corner }}</div>
            <div class="t-name">{{ t.name }}</div>
            <div class="t-price"><span class="cur">¥</span>{{ t.price }}</div>
            <div class="t-desc">{{ t.desc }}</div>
            <a class="t-cta" :href="t.link || ORDER_FORM" target="_blank" rel="noopener">{{ t.cta }}</a>
          </div>
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

        <div class="final-cta rv d3">
          <a class="btn btn-primary" :href="ORDER_FORM" target="_blank" rel="noopener">{{ c.finalCta }}</a>
          <p class="cta-risk">{{ c.finalRisk }}</p>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <!-- 收尾升华区 -->
    <section class="block closing">
      <div class="wrap">
        <div class="eyebrow eyebrow-center rv d1">{{ c.closingEyebrow }}</div>
        <h2 class="closing-title rv d2">{{ c.closingTitle }}</h2>
        <p class="closing-lead rv d3">{{ c.closingLead }}</p>
        <div class="cta-row rv d4">
          <a class="btn btn-primary" :href="ORDER_FORM" target="_blank" rel="noopener">{{ c.finalCta }}</a>
          <a class="btn btn-ghost" :href="bookLink" target="_blank" rel="noopener">{{ c.closingRead }}</a>
        </div>
      </div>
    </section>

    <!-- 固底条：滑到课程区后逐渐出现 -->
    <div class="dock" :class="{ show: showDock }">
      <div class="dock-inner">
        <button class="dock-btn" type="button" @click="toTop">{{ c.dockTop }}</button>
        <a class="dock-btn dock-hot" :href="ORDER_FORM" target="_blank" rel="noopener">{{ c.dockCta }}</a>
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
        <div class="f-links">
          {{ c.footLinks }}<span class="sep">｜</span><template v-for="(l, i) in friendLinks" :key="l.href"><a :href="l.href" target="_blank" rel="noopener">{{ l.label }}</a><span v-if="i < friendLinks.length - 1" class="sep">｜</span></template>
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
.hero-author{
  margin-top:10px;
  font-family:var(--font-mono);
  font-size:12.5px;letter-spacing:.28em;
  color:var(--ink-3);
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

/* ============ WHY 背景区（特性条移除后的深色分层带） ============ */
.why-band{background:var(--bg-1)}

/* 锚点落点补偿 sticky 导航高度 */
#course,#pricing{scroll-margin-top:84px}

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
.lead-cta{margin-top:32px;justify-content:flex-start}

/* ============ Stats 数字墙 ============ */
.stats{
  display:grid;grid-template-columns:repeat(4,1fr);
  border:1px solid var(--line);border-radius:var(--radius);
  margin:52px 0 64px;overflow:hidden;
  background:var(--bg-1);
}
.why-stats .stat .num{font-size:clamp(22px,2.6vw,32px)}
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
  box-shadow:0 0 48px rgba(24,240,80,.22),inset 0 0 0 1px rgba(24,240,80,.15);
  background:linear-gradient(180deg,rgba(24,240,80,.07),var(--bg-0) 55%);
  transform:scale(1.05);
  z-index:1;
}
.tier.hot:hover{transform:scale(1.05) translateY(-3px);box-shadow:0 0 64px rgba(24,240,80,.3),inset 0 0 0 1px rgba(24,240,80,.2)}
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

/* 预购专享福利带 */
.perks{
  position:relative;
  margin:8px 0 52px;
  border:1px solid rgba(24,240,80,.45);
  border-radius:20px;
  padding:40px 40px 30px;
  background:linear-gradient(180deg,rgba(24,240,80,.09),rgba(24,240,80,.015) 60%,transparent);
  box-shadow:0 0 60px rgba(24,240,80,.08),inset 0 0 0 1px rgba(24,240,80,.06);
  overflow:hidden;
}
.perks::before{
  content:"";
  position:absolute;top:-40%;right:-8%;
  width:420px;height:420px;
  background:radial-gradient(circle,rgba(24,240,80,.12) 0%,transparent 65%);
  pointer-events:none;
}
.perks-head{
  position:relative;z-index:2;
  display:flex;align-items:center;gap:18px;flex-wrap:wrap;
  margin-bottom:28px;
}
.perks-tag{
  font-family:var(--font-mono);font-size:12px;
  letter-spacing:.22em;text-transform:uppercase;
  color:#060806;font-weight:700;
  background:var(--neon);
  border-radius:999px;padding:6px 16px;
  white-space:nowrap;
  box-shadow:0 0 20px rgba(24,240,80,.35);
}
.perks-title{
  font-size:clamp(28px,4.2vw,44px);
  font-weight:800;letter-spacing:-.02em;line-height:1.15;
  color:var(--ink);
}
.perks-grid{
  position:relative;z-index:2;
  display:grid;grid-template-columns:repeat(3,1fr);gap:20px;
}
.perk{
  background:rgba(10,10,10,.72);
  border:1px solid var(--line-strong);border-radius:14px;
  padding:26px 26px;
  transition:border-color .25s,box-shadow .25s,transform .2s;
}
.perk:hover{border-color:rgba(24,240,80,.55);box-shadow:0 0 26px rgba(24,240,80,.12);transform:translateY(-3px)}
.perk-no{
  font-family:var(--font-mono);font-size:12px;
  letter-spacing:.22em;color:var(--neon);margin-bottom:12px;
}
.perk-t{font-size:17px;font-weight:800;color:var(--ink);margin-bottom:10px}
.perk-p{font-size:14px;color:var(--ink-2);line-height:1.85}
.perks-note{
  position:relative;z-index:2;
  margin-top:24px;
  font-family:var(--font-mono);font-size:13px;letter-spacing:.05em;
  color:var(--ink-2);
}
.perks-note::before{content:"⏳ ";font-size:12px}

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
  padding:38px 0 110px; /* 底部余量补偿固底条遮挡 */
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
.foot-inner .f-links{font-family:var(--font-mono);letter-spacing:.04em}
.foot-inner .f-links a{color:var(--ink-3)}

/* ============ 收尾升华区 ============ */
.closing{
  position:relative;
  text-align:center;
  overflow:hidden;
}
.closing::before{
  content:"";
  position:absolute;bottom:-30%;left:50%;
  transform:translateX(-50%);
  width:720px;height:520px;
  background:radial-gradient(ellipse,rgba(24,240,80,.10) 0%,transparent 65%);
  pointer-events:none;
}
.closing .wrap{position:relative;z-index:2}
.eyebrow-center{justify-content:center}
.eyebrow-center::before{display:none}
.closing-title{
  font-size:clamp(28px,4.6vw,48px);
  font-weight:800;letter-spacing:-.02em;line-height:1.2;
  max-width:880px;margin:0 auto;
  border:none;padding:0;
  background:linear-gradient(100deg,#F2F2F2 55%,#18F050 85%);
  background-size:200% 100%;
  -webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent;
}
.closing-lead{
  max-width:640px;margin:26px auto 0;
  font-size:16.5px;color:var(--ink-2);line-height:1.9;
}
.closing .cta-row{justify-content:center}

/* ============ 手册章节流 ============ */
.chaps{
  display:grid;grid-template-columns:repeat(4,1fr);gap:16px;
  margin-top:44px;
}
.chap{
  display:block;
  border:1px solid var(--line);border-radius:12px;
  padding:20px 22px;background:var(--bg-1);
  transition:border-color .25s,box-shadow .25s,transform .2s;
}
.chap:hover{
  border-color:rgba(24,240,80,.45);
  box-shadow:0 0 20px rgba(24,240,80,.08);
  transform:translateY(-2px);
}
.chap:hover .ch-tt{color:var(--neon)}
.chap .ch-no{
  font-family:var(--font-mono);font-size:12px;
  letter-spacing:.2em;color:var(--neon);margin-bottom:8px;
}
.chap .ch-no::after{content:" ↗"}
.chap .ch-tt{font-size:15px;font-weight:700;color:var(--ink);line-height:1.5;transition:color .2s}
.book-outro{
  margin-top:28px;font-size:13.5px;color:var(--ink-3);line-height:1.9;
  max-width:760px;
}
.book-outro a{
  color:var(--ink-2);
  border-bottom:1px dashed rgba(24,240,80,.4);
  transition:color .2s,border-color .2s;
}
.book-outro a:hover{color:var(--neon);border-bottom-color:var(--neon)}
.book-cta{margin-top:36px}

/* ============ 固底条 ============ */
.dock{
  position:fixed;left:0;right:0;bottom:0;z-index:20; /* 低于 VPNav(30)，不压移动端全屏菜单 */
  transform:translateY(110%);
  opacity:0;
  visibility:hidden;
  transition:transform .45s cubic-bezier(.22,.68,.28,1),opacity .45s,visibility .45s;
  pointer-events:none;
}
.dock.show{
  transform:translateY(0);
  opacity:1;
  visibility:visible;
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
  .tier.hot{transform:none}
  .tier.hot:hover{transform:translateY(-3px)}
  .fit-grid{grid-template-columns:1fr}
  .perks-grid{grid-template-columns:1fr}
  .perks{padding:30px 24px 22px}
}
@media (max-width:720px){
  .hero{padding:76px 0 64px}
  .chaps{grid-template-columns:1fr 1fr}
  .dock-inner{max-width:calc(100% - 24px)}
  .cards{grid-template-columns:1fr}
  section.block{padding:68px 0}
  .syll-table th:nth-child(3),.syll-table td:nth-child(3){display:none}
  .author{flex-direction:column;gap:10px}
}
@media (prefers-reduced-motion:reduce){
  .geek-home *,.geek-home *::before,.geek-home *::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
  .rv{opacity:1}
}
</style>
