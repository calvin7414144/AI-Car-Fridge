<template>
  <main class="site-shell">
    <header class="topbar">
      <a class="brand" href="/" aria-label="AI车载冰箱首页">
        <span class="brand-mark">BNO</span>
        <span class="brand-name">AI车载冰箱</span>
      </a>

      <nav class="nav-links" aria-label="主导航">
        <a
          v-for="item in navItems"
          :key="item.href"
          :href="item.href"
          :class="{ active: item.page === page }"
        >
          {{ item.label }}
        </a>
      </nav>
    </header>

    <section v-if="page === 'home'" class="page home-page section-block">
      <div class="hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">AI Car Fridge</p>
          <h1>不是“冰箱”，而是车内冷饮体验系统</h1>
          <p class="hero-lede">
            一款放在车内中控/后排区域的智能小冰箱，服务通勤、drive-thru、周末出游和长途自驾的饮品冷藏与杯托收纳。
          </p>
          <div class="hero-actions">
            <a class="primary-link" href="/product/">查看产品</a>
            <a class="text-link" href="/custom/">定制咨询</a>
          </div>
          <div class="hero-notes">
            <span>AI识别饮品</span>
            <span>精准控温</span>
            <span>双杯托收纳</span>
          </div>
        </div>

        <div class="hero-product">
          <ProductFigure class-name="hero-real-product" />
          <div class="floating-spec">
            <span>Display Temperature</span>
            <strong>4°C</strong>
          </div>
        </div>
      </div>

      <section class="content-band">
        <div class="section-title">
          <p class="eyebrow">Product Definition</p>
          <h2>面向车内高频饮品场景</h2>
        </div>
        <div class="copy-columns">
          <p>
            产品围绕咖啡、奶茶、汽水、水果和瓶装水等小体积高频使用需求设计，从普通车载小冰箱升级为饮品体验管理器。
          </p>
          <p>
            核心定位是让用户在车内持续获得稳定口感：冰咖啡不快速融化、奶茶不变温、瓶装水与水果保持清爽。
          </p>
        </div>
      </section>

      <section class="content-band">
        <div class="section-title">
          <p class="eyebrow">Audience</p>
          <h2>首批用户画像</h2>
        </div>
        <div class="card-grid three">
          <article v-for="item in personas" :key="item.title" class="info-card">
            <span class="card-kicker">{{ item.kicker }}</span>
            <h3>{{ item.title }}</h3>
            <p>{{ item.profile }}</p>
            <strong>{{ item.pain }}</strong>
          </article>
        </div>
      </section>
    </section>

    <section v-else-if="page === 'product'" class="page section-block product-page">
      <div class="page-heading split-heading">
        <div>
          <p class="eyebrow">Product</p>
          <h1>让“保持温度”变成可感知的体验</h1>
        </div>
        <p class="page-lede">
          黑色便携箱体、BNO 标识、前侧触控温控区、左右杯托和打开式上盖共同构成车内饮品系统，而不是传统大体积户外冷柜。
        </p>
      </div>

      <div class="product-detail-grid">
        <ProductFigure class-name="detail-real-product" />
        <div class="feature-list">
          <article v-for="item in publicFeatures" :key="item.title" class="feature-card">
            <span>{{ item.number }}</span>
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </div>

      <section class="content-band">
        <div class="section-title">
          <p class="eyebrow">Pain & Value</p>
          <h2>每个功能都对应真实痛点</h2>
        </div>
        <div class="card-grid two">
          <article v-for="item in functionRationales" :key="item.title" class="info-card horizontal">
            <h3>{{ item.title }}</h3>
            <p>痛点：{{ item.pain }}</p>
            <strong>价值：{{ item.value }}</strong>
          </article>
        </div>
      </section>

      <section class="content-band aftersale-section">
        <div class="section-title">
          <p class="eyebrow">After-sales Service</p>
          <h2>完整售后功能</h2>
        </div>
        <div class="card-grid three">
          <article v-for="item in afterSales" :key="item.title" class="info-card">
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </section>
    </section>

    <section v-else-if="page === 'factory'" class="page section-block factory-page">
      <div class="factory-image outdoor-scene"></div>
      <div class="factory-copy">
        <p class="eyebrow">Factory</p>
        <h1>围绕车内真实使用，建立可靠制造标准</h1>
        <p>
          从车内空间、饮品取放、低噪运行和节能使用出发，制造重点不是堆参数，而是保证通勤、drive-thru 和长途驾驶中的稳定体验。
        </p>
        <div class="factory-stats">
          <div v-for="item in factoryStats" :key="item.value">
            <strong>{{ item.value }}</strong>
            <span>{{ item.label }}</span>
          </div>
        </div>
      </div>

      <section class="content-band full-span">
        <div class="section-title">
          <p class="eyebrow">Quality Workflow</p>
          <h2>从样机到交付的质量流程</h2>
        </div>
        <div class="process-list">
          <article v-for="item in factoryProcess" :key="item.step" class="process-item">
            <span>{{ item.step }}</span>
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </section>

      <section class="content-band full-span">
        <div class="section-title">
          <p class="eyebrow">Use Scenarios</p>
          <h2>车内高频使用场景</h2>
        </div>
        <div class="card-grid three">
          <article v-for="item in useCases" :key="item.title" class="info-card">
            <h3>{{ item.title }}</h3>
            <p>{{ item.detail }}</p>
            <strong>{{ item.result }}</strong>
          </article>
        </div>
      </section>
    </section>

    <section v-else-if="page === 'custom'" class="page section-block custom-page">
      <div class="page-heading split-heading">
        <div>
          <p class="eyebrow">Customization</p>
          <h1>定制功能，服务不同车型与品牌场景</h1>
        </div>
        <p class="page-lede">
          定制宣传重点聚焦额外功能与外观指定：例如冷热一体、加热保温、品牌色、饰面纹理、功能模块和车机连接，而不是改变产品真实结构。
        </p>
      </div>

      <div class="custom-product-layout">
        <ProductFigure class-name="compact-real-product" />
        <div class="custom-grid">
          <article v-for="item in customOptions" :key="item.title" class="custom-card">
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </div>

      <section class="content-band">
        <div class="section-title">
          <p class="eyebrow">Optional Modules</p>
          <h2>可增加的功能方向</h2>
        </div>
        <div class="card-grid four">
          <article v-for="item in extraModules" :key="item.title" class="info-card">
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </section>
    </section>

    <section v-else-if="page === 'contact'" class="page section-block contact-page">
      <div class="contact-intro">
        <p class="eyebrow">Contact</p>
        <h1>提交你的车载冷藏项目需求</h1>
        <p class="page-lede">
          适用于 B2B 渠道、品牌定制、车型适配、样机评估和批量采购。填写信息后，项目顾问可据此判断容量、功能、预算和交付方案。
        </p>
        <div class="contact-notes">
          <span>车型适配</span>
          <span>OEM / ODM</span>
          <span>批量采购</span>
        </div>
      </div>

      <form class="contact-form" @submit.prevent="submitForm">
        <label v-for="field in formFields" :key="field.name" :class="{ wide: field.type === 'textarea' }">
          <span>{{ field.label }}</span>
          <textarea
            v-if="field.type === 'textarea'"
            v-model="form[field.name]"
            :placeholder="field.placeholder"
            rows="5"
          ></textarea>
          <select v-else-if="field.type === 'select'" v-model="form[field.name]">
            <option value="">请选择</option>
            <option v-for="option in field.options" :key="option" :value="option">{{ option }}</option>
          </select>
          <input
            v-else
            v-model="form[field.name]"
            :type="field.type"
            :placeholder="field.placeholder"
          />
        </label>
        <button class="primary-link submit-button" type="submit">提交需求</button>
        <p v-if="submitted" class="submit-message">已提交。我们已在前端记录你的需求信息，可继续对接后端保存或邮件通知。</p>
      </form>
    </section>
  </main>
</template>

<script setup>
import { h, reactive, ref } from 'vue'

const props = defineProps({
  page: {
    type: String,
    default: 'home',
  },
})

const productImage = '/static/frontend/product-cutout.png'

const ProductFigure = {
  props: {
    className: {
      type: String,
      default: '',
    },
  },
  setup(componentProps) {
    return () => h(
      'figure',
      { class: ['real-product-frame', componentProps.className] },
      [
        h('img', {
          src: productImage,
          alt: 'BNO AI车载便携冰箱实拍图，黑色箱体、打开上盖、蓝色内仓冷光、前侧触控面板和左右杯托',
          class: 'real-product-image',
        }),
      ],
    )
  },
}

const navItems = [
  { label: '首页', href: '/', page: 'home' },
  { label: '产品', href: '/product/', page: 'product' },
  { label: '工厂', href: '/factory/', page: 'factory' },
  { label: '定制', href: '/custom/', page: 'custom' },
  { label: '联系', href: '/contact/', page: 'contact' },
]

const personas = [
  {
    kicker: 'Persona 1',
    title: '通勤冷饮党',
    profile: '22-40岁，开车上下班，常买冰咖啡、奶茶或能量饮料。',
    pain: '痛点：开到公司时冰块融化，味道变淡。',
  },
  {
    kicker: 'Persona 2',
    title: '周末出游家庭',
    profile: '25-45岁，亲子、情侣或朋友出游，喜欢 road trip。',
    pain: '痛点：路上水果、瓶装饮料、儿童饮品不够冰。',
  },
  {
    kicker: 'Persona 3',
    title: '户外与车生活用户',
    profile: 'SUV、RV、露营、海边、球赛尾门聚会等车生活场景。',
    pain: '痛点：传统 cooler 要加冰，取用麻烦，车内不整洁。',
  },
]

const publicFeatures = [
  {
    number: '01',
    title: 'AI识别饮品',
    description: '自动识别咖啡、奶茶、汽水、水果等，并匹配推荐温度。',
  },
  {
    number: '02',
    title: '精准控温',
    description: '减少冰饮变淡、奶茶变温、咖啡失去口感的问题。',
  },
  {
    number: '03',
    title: '双杯托设计',
    description: 'Drive-thru 之后不用马上喝完，杯子也能稳固放置。',
  },
  {
    number: '04',
    title: '车载场景优化',
    description: '低噪、节能、易取用，适合通勤和长途驾驶。',
  },
]

const functionRationales = [
  { title: 'AI视觉识别', pain: '不知道不同饮品该放几度', value: '降低使用门槛，制造科技感' },
  { title: '精准控温', pain: '冰饮变淡、奶饮变温、咖啡口感下降', value: '把保持最佳口感变成核心承诺' },
  { title: '双杯托', pain: 'drive-thru 杯子太高、易倒、没地方放', value: '连接美国外带饮品习惯' },
  { title: '分区冷藏', pain: '水果、瓶装水、杯装饮料混放', value: '提升整洁度和多场景适配' },
  { title: '异常提醒', pain: '开盖、温差、耗电用户无感知', value: '提升安心感和售后满意度' },
  { title: '节能低噪', pain: '车内空间小，噪音和耗电敏感', value: '适合日常通勤，降低顾虑' },
]

const afterSales = [
  { title: '质保登记', description: '支持序列号、购买渠道、客户信息和保修起止时间登记，便于后续追踪。' },
  { title: '远程诊断', description: '记录温控异常、开盖异常、电压异常和压缩机运行状态，辅助售后判断。' },
  { title: '配件更换', description: '杯托、密封件、电源线、收纳配件等可按型号建立备件清单。' },
  { title: '维修工单', description: '支持客户问题、检测结果、处理进度、物流状态和售后反馈闭环。' },
  { title: '使用指导', description: '提供饮品温度建议、车内摆放建议、清洁保养和安全使用指南。' },
  { title: '客户回访', description: '围绕噪音、控温、耗电、杯托稳定性和复购配件进行满意度回访。' },
]

const factoryStats = [
  { value: '低噪', label: '车内空间友好' },
  { value: '节能', label: '适合日常通勤' },
  { value: '易取用', label: '驾驶与后排兼顾' },
]

const factoryProcess = [
  { step: '01', title: '结构适配', description: '围绕中控、后排区域和车内杯托习惯验证尺寸与取放动线。' },
  { step: '02', title: '制冷测试', description: '测试不同饮品、瓶装水、水果和杯装饮料在车内环境中的温度保持。' },
  { step: '03', title: '噪音与功耗', description: '针对小车内空间验证低噪运行、节能策略和长时间使用稳定性。' },
  { step: '04', title: '交付检验', description: '对触控面板、杯托、上盖、密封、蓝色内仓灯和电源接口逐项检查。' },
]

const useCases = [
  { title: '通勤', detail: '美国平均单程通勤约 27.2 分钟，往返接近 1 小时。', result: '冰咖啡、奶茶、能量饮料不会在路上快速变温。' },
  { title: 'Drive-thru之后', detail: '早餐、咖啡、午餐和冰饮都是快速取餐高频场景。', result: '杯托与冷藏让饮品不用马上喝完。' },
  { title: 'Road trip/周末出游', detail: '长途自驾常伴随瓶装水、水果、汽水和儿童饮品。', result: '一路保持清爽，减少传统 cooler 加冰负担。' },
]

const customOptions = [
  { title: '加热保温功能', description: '为冬季通勤、热咖啡、热奶和保温餐食预留冷热一体方案。' },
  { title: '颜色指定', description: '支持黑色、香槟金、车企品牌色和限定色外观开发。' },
  { title: '饰面材料', description: '可指定钢琴黑、磨砂黑、金属拉丝、皮纹或木纹饰面。' },
  { title: '杯托规格', description: '根据美式大杯、奶茶杯、咖啡杯和瓶装水调整杯托深度与直径。' },
]

const extraModules = [
  { title: '冷热双模式', description: '冷藏与加热保温切换，覆盖夏季冷饮与冬季热饮。' },
  { title: '专属品牌灯效', description: '指定冷光颜色、开机动效和品牌迎宾灯效。' },
  { title: '车机联动', description: '预留车机接口、App 控制、温度记录和异常提醒。' },
  { title: '配件套装', description: '定制电源线、固定支架、清洁包、杯架适配件和储物盒。' },
]

const formFields = [
  { name: 'contactName', label: '联系人', type: 'text', placeholder: '请输入联系人姓名' },
  { name: 'phone', label: '联系电话', type: 'tel', placeholder: '请输入联系电话' },
  { name: 'company', label: '公司/品牌', type: 'text', placeholder: '请输入公司或品牌名称' },
  { name: 'projectType', label: '项目类型', type: 'select', options: ['B2B渠道合作', 'OEM/ODM定制', '车型适配', '样机评估', '批量采购'] },
  { name: 'quantity', label: '预计订购数量', type: 'select', options: ['1-50台', '51-300台', '301-1000台', '1000台以上'] },
  { name: 'city', label: '交付城市', type: 'text', placeholder: '例如：上海 / Los Angeles' },
  { name: 'budget', label: '预算区间', type: 'select', options: ['待评估', '10万以内', '10-50万', '50-200万', '200万以上'] },
  { name: 'requirements', label: '需求说明', type: 'textarea', placeholder: '请描述车型、使用场景、功能定制、颜色要求或交付时间' },
]

const form = reactive(Object.fromEntries(formFields.map((field) => [field.name, ''])))
const submitted = ref(false)

function submitForm() {
  submitted.value = true
  console.info('Contact form submitted', { ...form })
}
</script>
