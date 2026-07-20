# Chatla Plugins

Chatla mijozlari uchun **Claude Code plugin marketplace'i**.

## O'rnatish

Claude Code ichida:

```bash
/plugin marketplace add iakadirov/chatla-plugin
/plugin install marketing-machine@chatla-plugins
```

## Pluginlar

| Plugin | Versiya | Tavsif |
|---|---|---|
| [marketing-machine](./marketing-machine) | 0.1.0 | Kontent + marketing mashinasi: niche o'rganish → oylik reja → produksiya → publish → analiz → optimizatsiya → hisobot. |

### marketing-machine skill'lari

- **carousel-writer** — mavzudan slayd-slayd Instagram carousel copy yozadi (o'zbekcha,
  "Shunchaki Nega?" registrida). Save + comment→DM uchun optimallashtirilgan.

## Lokal test

Push qilmasdan, papkadan to'g'ridan-to'g'ri sinash:

```bash
claude --plugin-dir ./marketing-machine
```

Yoki lokal marketplace sifatida:

```bash
/plugin marketplace add .
/plugin install marketing-machine@chatla-plugins
```

## Tekshirish

```bash
claude plugin validate ./marketing-machine
```

## Yangi plugin qo'shish

1. Repo root'da yangi papka yarating: `<plugin-nomi>/.claude-plugin/plugin.json`
2. Skill'larni `<plugin-nomi>/skills/<skill-nomi>/SKILL.md` ga qo'shing.
3. Root `.claude-plugin/marketplace.json` dagi `plugins` massiviga yozuv qo'shing.

## Struktura

```
chatla-plugin/
├── .claude-plugin/
│   └── marketplace.json          # marketplace katalogi
├── marketing-machine/            # plugin
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   └── carousel-writer/
│   │       ├── SKILL.md
│   │       └── references/carousel-archetypes.md
│   ├── README.md
│   └── CHANGELOG.md
├── LICENSE
└── README.md
```

## Litsenziya

[MIT](./LICENSE)
