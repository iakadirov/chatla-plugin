# Marketing Machine

Chatla mijozlari uchun **kontent + marketing mashinasi** — Claude plugin.
Niche o'rganish → oylik reja → produksiya → publish → analiz → optimizatsiya → hisobot.

## Hozirgi skill'lar (v0.3.0)

- **`carousel-writer`** — mavzudan slayd-slayd Instagram carousel copy yozadi (o'zbekcha,
  "Shunchaki Nega?" registrida). Save + comment→DM uchun optimallashtirilgan.
  `references/carousel-archetypes.md` — 6 ta carousel strukturasi.

- **`reels-scripter`** — **reference-driven**: uslub o'ylab topilmaydi, kreatorning o'z
  referens reellaridan **o'lchanadi**. Chiqish — kadrma-kadr raskadrovka (kadr + gap +
  ekran matni + ritm), Higgsfield produksiyasiga tayyor.
  - `referens-reels-hook/style-profile.md` — o'lchangan uslub (12 universal qoida,
    5 ta ta'lim rejimi, 14 hook formulasi, matn tizimi, yakun rejimlari)
  - `referens-reels-hook/persona-override.md` — kreator tanlovi profil **ustiga** qo'yiladi
  - `referens-reels-hook/teardowns/` — 15 ta reelning to'liq tahlili (536 KB)
  - `tools/` — ingest pipeline (ffmpeg + faster-whisper)

- **`viral-hooks`** — 99 ta hook qolipi, 5 oilaga bo'lingan, har biri registr va persona
  teglari bilan. `carousel-writer` va `reels-scripter` ikkalasi ham ishlatadi.

## O'rnatish

### A) GitHub marketplace orqali (mijozlar shu bilan o'rnatadi)
```bash
/plugin marketplace add iakadirov/chatla-plugin
/plugin install marketing-machine@chatla-plugins
```

### B) Lokal test (o'rnatishsiz)
Repo root'idan sessiya davomida yuklaydi:
```bash
claude --plugin-dir ./marketing-machine
```

### C) Lokal marketplace orqali
Repo root'ida:
```bash
claude
/plugin marketplace add .
/plugin install marketing-machine@chatla-plugins
```

> **Yangilashdan keyin:** kod `main`ga tushgani skill'ni avtomatik yangilamaydi.
> `/plugin` → `marketing-machine` → update qiling va versiya raqami o'zgarganini tekshiring.

## Tekshirish

```bash
claude plugin validate ./marketing-machine --strict
```

> ⚠️ **Diqqat:** validate o'tgani skill ro'yxatda ko'rinishini kafolatlamaydi.
> Skill ko'rinmay qolsa, ishlaydigan va ishlamaydigan `SKILL.md` larni solishtiring:
> tanadagi `---` (frontmatter ajratgichi bilan bir xil belgi), BOM, satr oxirlari,
> `name` maydoni papka nomiga mosligi. **Tanada `---` ishlatmang** — sarlavhalardan foydalaning.

## Ishlatish

Skill'lar namespace bilan chiqadi: `marketing-machine:reels-scripter`.
Mos so'rov bo'lsa Claude ularni avtomat ishga soladi, yoki `/` bilan chaqiring.

## Boyitish (keyingi bosqichlar)

Yangi skill = `skills/<nom>/SKILL.md` qo'shish. Avtomatik topiladi.
Navbatdagilar: `caption-cta-writer` (ikkala skill ham unga handoff qiladi, hali yo'q),
`month-planner`, `carousel-designer`, `client-onboarder`, `performance-analyst`, `client-reporter`.

MCP connectorlar (Chatla, Bloom, Metricool) `.mcp.json` orqali,
har mijoz tokeni `plugin.json` dagi `userConfig` orqali qo'shiladi.

## Struktura

```
marketing-machine/
├── .claude-plugin/plugin.json
├── skills/
│   ├── carousel-writer/
│   │   ├── SKILL.md
│   │   └── references/carousel-archetypes.md
│   ├── reels-scripter/
│   │   ├── SKILL.md
│   │   ├── references/{teardown-template,reels-archetypes}.md
│   │   ├── referens-reels-hook/
│   │   │   ├── style-profile.md        # o'lchangan uslub
│   │   │   ├── persona-override.md     # kreator tanlovi (ustun)
│   │   │   ├── teardowns/              # 15 ta reel tahlili
│   │   │   ├── raw/                    # xom videolar (git'da yo'q)
│   │   │   └── _work/                  # kadr + transkript (git'da yo'q)
│   │   └── tools/{ingest.py,transcribe_seq.sh,transcribe_all.py}
│   └── viral-hooks/
│       ├── SKILL.md
│       └── references/hook-library-99.md
├── marketing-machine-PRD.md
├── README.md
└── CHANGELOG.md
```

> **Eslatma:** `raw/` (240 MB) va `_work/` (76 MB) git'ga kirmaydi. O'rganilgan bilim
> `teardowns/` va `style-profile.md` da matn sifatida saqlangan, shuning uchun generatsiya
> uchun xom video kerak emas. Lekin profilni **qayta hisoblash** kerak bo'lsa — videolar kerak.
> Ular hozir faqat ishlab chiqish mashinasida.
