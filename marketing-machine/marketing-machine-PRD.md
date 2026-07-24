# PRD — Marketing Machine (Claude Plugin)

| | |
|---|---|
| **Mahsulot** | `marketing-machine` — Chatla mijozlari uchun kontent + marketing mashinasi (Claude plugin) |
| **Egasi** | Ibrohim |
| **Holat** | Draft · v0.1 (skelet qurilgan, `carousel-writer` skill'i tayyor) |
| **Yo'nalish** | Chatla mijozlariga xizmat/mahsulot (productized service), multi-tenant |
| **Umurtqa** | Chatla MCP (system-of-record: brain · plan · publish · DM · analitika) |

---

## 1. Problem Statement

O'zbekistondagi bizneslar Instagram/Telegram'da izchil, sifatli kontent chiqara olmaydi: kopirayter + dizayner + SMM + analitik jamoasi qimmat va sekin. Natijada kontent tartibsiz, generik va o'lchanmaydigan bo'ladi — reach bo'lsa ham, u DM va sotuvga aylanmaydi. Chatla allaqachon mijozning DM'larini konversiya qiladi, lekin o'sha DM'larni **keltiradigan kontent** bo'shliq bo'lib qolgan. Bu bo'shliqni to'ldirmaslik — Chatla mijozlarining o'sishini cheklaydi va raqobat riski tug'diradi.

## 2. Goals

1. **Mijozga o'lchanadigan ROI:** mashina ishlab chiqargan kontent orqali har mijozda oyiga DM/lead sonini ko'paytirish (asosiy metrika — reach yoki like emas).
2. **Produksiya tannarxi va vaqtini keskin tushirish:** bir mijozning oylik kontent rejasi + carousel produksiyasi soatlar emas, daqiqalarda; tannarx (kredit/USD) o'lchanadigan va bashoratli.
3. **Sifatni tizim orqali kafolatlash:** har asset publish'gacha brend voice + visual DNA'ga tekshiriladi (guardrail + approval gate), shuning uchun avtomatizatsiya sifatni pasaytirmaydi.
4. **Kompaunding aql:** har oy `learnings` o'sadi — mashina vaqt o'tgani sayin har mijoz auditoriyasi uchun aqlliroq bo'ladi.
5. **Chatla uchun yangi daromad qatlami:** "Content add-on" — Chatla'ga tabiiy sotiladigan, marja beradigan xizmat.

## 3. Non-Goals

1. **O'z generatsiya modelimizni qurmaymiz.** Rasm — Bloom, video — Higgsfield. Sabab: qayta ixtiro qilish behuda.
2. **Cross-network analitikani noldan qurmaymiz (v1'da).** Metricool plug-in bo'lib qoladi; Chatla native analitika keyingi bosqich.
3. **v1 to'liq avtonom emas.** Mijoz brendida approval gate majburiy — bitta yomon post munosabatni buzadi.
4. **v1 masshtabli multi-tenant emas.** Bitta pilot mijozdan boshlanadi; `conductor` (ko'p mijoz parallel) — keyingi to'lqin.
5. **`hashtag-seo` kiritilmaydi.** Ta'siri past deb baholandi, scope'dan chiqarildi.
6. **Umumiy ochiq bozor mahsuloti emas.** Chatla ekotizimiga bog'langan — mustaqil SMM tool sifatida pozitsiyalanmaydi.

## 4. Target Users & Personas

- **Operator (Ibrohim / Chatla jamoasi):** mashinani yuritadi, mijozlarni onboard qiladi, rejani nazorat qiladi, hisobot beradi.
- **Mijoz (biznes egasi):** kontent xizmatini sotib oladi; rejani/assetlarni tasdiqlaydi; DM/lead natijasini oladi. Texnik emas.
- **Sotuv (yangi mijoz):** proposal/case study orqali yangi mijoz yutish (keyingi to'lqin).

## 5. Value Proposition (Product Story)

*"Chatla sizning DM'ingizni pulga aylantiradi — endi Chatla o'sha DM'larni keltiradigan kontentni ham o'zi ishlab beradi."*
Content → komment→DM → lead → sotuv: yopiq ROI halqasi. Har hisobotning markaziy KPI'si — **DM va lead**.

## 6. Architecture (qisqacha)

**Falsafa:** "content scheduler" emas, **Marketing OS** — mutaxassislar agentligi. Har skill = bir mutaxassis; Chatla = system-of-record; generatsiya engine'lari plug-in; Claude plugin orkestr qiladi.

| Qatlam | Engine | Roli |
|---|---|---|
| Niche + feedback + DM + **publish** | **Chatla** (native quriladi) | Brain, reja, publish, DM, analitika — system-of-record |
| Karusel / statik rasm | **Trybloom (Bloom)** | Brendga mos rasm |
| Reels / video | **Higgsfield** | Video, shorts, motion |
| Cross-network analitika | **Metricool** | Best-time + ko'p platforma analitikasi (plug-in) |
| Orkestr + copy + reja | **Claude plugin** | Skills + commands + sub-agents + brain fayllar |

**Qaror (belgilangan):** publishing Chatla'da **native** quriladi (Metricool wrap emas) — to'liq nazorat uchun.

**Brain (kompaunding xotira):** per-mijoz namespacing —
`/brain/registry.csv` + `/brain/clients/<id>/{niche, voice, content-plan, published-log, performance, learnings, reports}`.

**Sifatni ushlab turadigan 3 tamoyil:** (1) brain birinchi; (2) `brand-guardian` guardrail har doim; (3) approval gate mijoz xizmatida majburiy.

## 7. Functional Requirements

Skill kutubxonasi 9 qatlam / ~44 skill. Ustuvorlik to'lqinlar bo'yicha. **★ = mavjud** (`viral-hooks`, `oson-tushuntirish`, `higgsfield-content-factory`).

### P0 — Must-Have (v1 / To'lqin 1: bitta pilot mijozda uchidan-uchiga ROI)
Bitta mijozda quyidagi zanjir ishlashi shart: **onboard → niche → oylik reja → carousel produksiya → guardrail → publish → hisobot + tannarx**.
- `client-onboarder` — Chatla + Bloom (+ Metricool) ulash, brain qurish
- `niche-intelligence` — Chatla profil + reels'dan pozitsiya/ICP/offer
- `month-planner` — 30 kunlik kalendar (mavzu × format × goal × sana)
- `carousel-writer` ✅ **(qurilgan)** — slayd-slayd copy
- `carousel-designer` — Bloom promptlari + layout
- `brand-guardian` — voice + visual DNA guardrail
- `scheduler` — best-time bilan publish (Chatla native)
- `performance-analyst` — post/format bo'yicha tahlil
- `client-reporter` — DM/ROI-markazli mijoz hisoboti
- `cost-tracker` — kredit + USD (COGS o'lchash)

**Acceptance (P0):**
- Given pilot mijoz onboard qilingan · When operator `month-planner`ni ishga soladi · Then mijoz tasdig'iga tayyor 30-kunlik carousel-asosli reja chiqadi.
- Given tasdiqlangan reja bandi · When `carousel-writer` + `carousel-designer` ishlaydi · Then slayd-slayd copy + Bloom rasm assetlari, `brand-guardian`dan o'tgan holda, chiqadi.
- Given tayyor asset · When `scheduler` ishlaydi · Then post Chatla orqali best-time'ga rejalanadi va `published-log`ga yoziladi.
- Given oy yakuni · When `client-reporter` ishlaydi · Then DM/lead-markazli hisobot + `cost-tracker` kredit/USD qatori chiqadi.

### P1 — Should-Have (To'lqin 2: ko'paytir + konversiya)
`reels-scripter` ✅ **(qurilgan)** · `story-writer` · `caption-cta-writer` · `angle-generator` · `localizer` · `video-producer`★ · `atomizer` · `winner-recycler` · `comment-to-dm` · `telegram-broadcaster` · `optimizer`
→ ko'p format, atomizatsiya, DM konversiya (Chatla reel_automation), o'rganish halqasi yopiladi.

### P2 — Future (To'lqin 3–4: intellekt, o'sish, masshtab)
- Intelligence: `audience-profiler` · `competitor-radar` · `trend-scout` · `comment-miner` · `offer-funnel-mapper`
- Strategy: `content-pillars` · `campaign-architect` · `series-designer` · `content-mix-balancer`
- Visual: `thumbnail-cover` · `voiceover-audio` · `ugc-generator` · `ad-creative`
- Distribution/Growth: `multi-channel-publisher` · `paid-amplifier` · `lead-magnet-maker` · `landing-page-gen`
- Analytics: `funnel-analytics` · `attribution` · `experiment-runner` · `sentiment-tracker` · `benchmark`
- Ops/Scale: `conductor` (multi-tenant orkestr) · `proposal-generator` · `qbr` · `community-manager` · `dm-sales-sequences`

## 8. Plugin & Distribution Requirements

- **Struktura (P0):** `.claude-plugin/{plugin.json, marketplace.json (source "./")}` + `skills/<name>/SKILL.md`. ✅ qurilgan.
- **Ishlash muhiti:** skill'lar chatda (web), Claude Desktop Chat tab va Cowork'da ishlaydi. Sub-agent/hook faqat Cowork'da — chatda kulrang. v1 skill-only bo'lgani uchun chatda to'liq ishlaydi.
- **O'rnatish:** (a) `Upload plugin` orqali zip; (b) GitHub marketplace → `Customize → Plugins → Add marketplace → Add from a repository` → Install.
- **Multi-tenant auth (P1):** MCP connectorlar `.mcp.json` orqali jamlanadi; har mijoz tokeni `plugin.json` `userConfig` (`sensitive: true`) orqali enable paytida so'raladi.
- **Tarqatish:** pullik tarif (Pro/Max/Team/Enterprise) talab qilinadi; bepul tarifda o'rnatilmaydi.

## 9. Constraints & Risks (non-functional)

1. **Kredit = real COGS.** Bloom/Higgsfield har mijozga oyiga pul yeydi → per-mijoz budjet cap + har hisobotda kredit/USD qatori. Narx tannarxsiz belgilanmaydi (shuning uchun To'lqin 1 tannarxni o'lchaydi).
2. **Brend riski.** Birovning brendida bitta yomon post — munosabatni buzadi → approval gate majburiy.
3. **Akkaunt kirish friction.** Har mijoz IG'sini Chatla + engine'larga ulashi kerak; egalik oldindan hal qilinadi.
4. **Platforma API limitlari.** IG publishing kvotasi, Meta review — Chatla native publishing quriladiganda hisobga olinadi.
5. **Metricool brend limiti.** 20 mijoz = 20 brend slot (agar Metricool ishlatilsa) — native publishing bu bog'liqlikni kamaytiradi.
6. **Xavfsizlik.** Plugin lokal MCP ishga tushirishi mumkin — mijozlarga faqat ishonchli manba, deb aytiladi.
7. **Backbone alohida mehnat.** Chatla native publishing/analytics/brain tool'lari plugin'dan ajralgan, lekin kritik yo'l.

## 10. Success Metrics

**North Star:** har mijozda oyiga mashina-kontenti orqali kelgan **DM/lead soni**.

**Leading (tez o'zgaradi):**
- Bir mijozning oylik carousel rejasi + produksiyasi vaqti (target: soatlar emas, < ~30 daq/mijoz)
- Post uchun asset tannarxi (kredit/USD) — o'lchanadigan va cap ostida
- Carousel save rate va swipe-through (mashina kontenti bo'yicha)
- Approval turnaround (mijoz tasdig'i vaqti)

**Lagging (vaqt bilan):**
- Mijozga oylik DM/lead o'sishi (asosiy ROI)
- Mijoz retention (xizmatda qolishi)
- COGS (kredit) vs daromad marjasi
- Parallel yuritilayotgan mijozlar soni

**O'lchash:** ko'rsatkichlar Chatla analitika + `performance.csv` + `cost-tracker`dan; baseline pilot mijozda o'rnatiladi (hozircha targetlar gipoteza).

## 11. Roadmap (phasing)

- **To'lqin 1 (P0):** bitta pilot mijozda uchidan-uchiga ROI + tannarx o'lchash. → birinchi case study.
- **To'lqin 2 (P1):** ko'p format + atomizatsiya + DM konversiya + o'rganish halqasi.
- **To'lqin 3 (P2):** intellekt (raqib/trend/comment-mining) + o'sish (proposal, landing, paid).
- **To'lqin 4 (P2):** multi-tenant `conductor`, to'liq atribut, QBR — 10+ mijoz parallel.

*Qattiq tashqi deadline yo'q; boyitish inkremental — yangi skill = `skills/<name>/SKILL.md` qo'shish, rebuild kerak emas.*

## 12. Open Questions

- **[Biznes — Ibrohim]** Qaysi pilot mijoz? (afzal: IG'si ulanган, DM konversiya undan foyda ko'radigan biznes) — *blocking* To'lqin 1.
- **[Muhandislik — Chatla]** Chatla native publishing/brain/analytics tool'lari qancha mehnat/vaqt talab qiladi? — *blocking* P0'ning publish qismi.
- **[Moliya]** Per-mijoz kredit budjeti va narx modeli? — To'lqin 1 COGS datasiga bog'liq (non-blocking hozircha).
- **[Ops/Legal]** Mijoz IG akkaunt egaligi va ulanishi kim orqali? — To'lqin 1'gacha hal qilinsin.
- **[Mahsulot]** Har mijoz uchun avtonomiya darajasi (approval qamrovi)? — default: reja + asset partiyasi tasdiqlanadi.
- **[Muhandislik]** Tarqatish: bitta umumiy marketplace vs mijozga alohida; `userConfig` orqali token — qaysi model?

## 13. Appendix — Hozirgi holat (v0.1)

- ✅ Plugin skeleti: `marketing-machine` (marketplace: `chatla-plugins`, install: `marketing-machine@chatla-plugins`).
- ✅ `carousel-writer` skill'i + `references/carousel-archetypes.md` (6 arxetip).
- ✅ `viral-hooks` skill'i — 99 ta hook qolipi (5 oila), registr va persona teglari bilan. `carousel-writer` va `reels-scripter` ikkalasi ham ishlatadi.
- ✅ `reels-scripter` skill'i (P1) — **reference-driven**: uslub o'ylab topilmaydi, kreatorning o'z referens reellaridan o'lchanadi.
  - Ingest pipeline (`tools/`): ffmpeg (vaqt belgili contact sheet, hook kadrlari, kesim tahlili) + faster-whisper large-v3 (so'zma-so'z transkript).
  - 15 ta referens reel to'liq teardown qilindi (536 KB) → `style-profile.md` (o'lchangan uslub) + `persona-override.md` (kreator tanlovi).
  - Chiqish: beat-by-beat raskadrovka, Higgsfield produksiyasiga tayyor; yakun rejimi komment→DM (Chatla) yoki aforizm.
  - ⚠️ Bu **bitta kreatorning** uslubi, universal "viral formula" emas — profilda shunday yozilgan.
- ⏳ `plugin.json` `repository`/`homepage`da `USERNAME` placeholder — GitHub'ga almashtirilishi kerak.
- ⏳ `.mcp.json` (connector jamlash) hali yo'q — v1 mavjud ulanishlarga tayanadi.
