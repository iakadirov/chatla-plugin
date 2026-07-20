# Marketing Machine

Chatla mijozlari uchun **kontent + marketing mashinasi** — Claude plugin.
Niche o'rganish → oylik reja → produksiya → publish → analiz → optimizatsiya → hisobot.
Bu skelet **carousel-writer** skill'i bilan boshlanadi va bosqichma-bosqich boyib boradi.

## Hozirgi skill'lar (v0.1.0)

- **carousel-writer** — mavzudan slayd-slayd Instagram carousel copy yozadi (o'zbekcha,
  "Shunchaki Nega?" registrida). Save + comment→DM uchun optimallashtirilgan.
  `references/carousel-archetypes.md` — 6 ta carousel strukturasi.

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

## Tekshirish
Repo root'idan:
```bash
claude plugin validate ./marketing-machine
```

## Ishlatish
Skill'lar namespace bilan chiqadi: `marketing-machine:carousel-writer`.
Carousel so'rasangiz Claude uni avtomat ishga soladi.

## Boyitish (keyingi bosqichlar)
Yangi skill = `skills/<nom>/SKILL.md` qo'shish. Avtomatik topiladi.
Reja: `month-planner`, `reels-scripter`, `carousel-designer`, `client-onboarder`,
`performance-analyst`, `client-reporter` va h.k.
MCP connectorlar (Chatla, Bloom, Metricool) `.mcp.json` orqali,
har mijoz tokeni `plugin.json` dagi `userConfig` orqali qo'shiladi.

## Struktura
```
marketing-machine/
├── .claude-plugin/
│   └── plugin.json          # plugin manifesti
├── skills/
│   └── carousel-writer/
│       ├── SKILL.md
│       └── references/carousel-archetypes.md
├── README.md
└── CHANGELOG.md
```
