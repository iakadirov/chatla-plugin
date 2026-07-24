# referens-reels-hook — referens video korpusi

Bu papka `reels-scripter` skill'ining **uslub maktabi**. Bu yerga tashlangan videolar o'rganiladi va skill keyingi barcha ssenariylarni **aynan shu uslubda** yozadi.

## 📥 Videolarni qayerga tashlaysiz

```
referens-reels-hook/
├── raw/            ← 🎬 VIDEOLARNI SHU YERGA TASHLANG
├── _work/          ← avtomatik: kadrlar, contact sheet, transkript (git'ga kirmaydi)
├── teardowns/      ← avtomatik: har video uchun bitta tahlil fayli (.md)
└── style-profile.md ← avtomatik: barcha videolardan chiqarilgan "uy uslubi"
```

**Faqat `raw/` papkasiga tashlang.** Qolgani avtomatik quriladi.

## ✅ Qanday video kerak

| Talab | Izoh |
|---|---|
| **Format** | `.mp4`, `.mov`, `.webm` — Instagram'dan yuklab olingan bo'lsa ham bo'ladi |
| **Soni** | Kamida **3 ta**, ideal **6–12 ta**. Kam bo'lsa uslub aniqlanmaydi, ko'p bo'lsa aniqroq |
| **Sifat** | Ovoz eshitilsin (transkript uchun). Ovozsiz bo'lsa — ekran matni bo'yicha o'rganiladi |
| **Tanlov** | Faqat **sizga yoqqan / natija bergan** reel'lar. Bu korpus = "men shunday xohlayman"ning ta'rifi |

### Nomlash (ixtiyoriy, lekin foydali)
Fayl nomiga qisqa belgi qo'ysangiz, tahlil aniqroq bo'ladi:
```
hook-shok_ai-agentlar.mp4
story_mijoz-kesi.mp4
listicle_3-xato.mp4
```
Nomlamasangiz ham ishlaydi — skill o'zi aniqlaydi.

## ⚙️ Video tashlagandan keyin nima bo'ladi

Menga *"videolarni tashladim"* deb ayting. Keyin har bir video uchun avtomatik:

1. **Ingest** (`tools/ingest.py`) —
   - `ffprobe` → davomiylik, fps, o'lcham, 9:16 tekshiruvi
   - kesim (scene-cut) vaqtlari + o'rtacha kesim oralig'i → **montaj ritmi**
   - **contact sheet** → butun videoning montaji bitta rasmda (men buni ko'z bilan o'rganaman)
   - **hook kadrlari** → birinchi 3 soniya, 0.5s qadam bilan (eng muhim qism)
   - **faster-whisper** → o'zbekcha **so'zma-so'z transkript**, vaqt belgilari bilan

2. **Teardown** → `teardowns/<video>.md`
   Har bir video so'zma-so'z va kadrma-kadr yoriladi: nima deyilgan, qanday jumla tuzilgan, qanday montaj qilingan, matn qanday chiqqan, ritm qanday.

3. **Style profile** → `style-profile.md`
   Barcha teardown'lardan **takrorlanuvchi naqshlar** ajratiladi: hook shablonlari, jumla uzunligi va ritmi, kesim tezligi, ekran matni uslubi, ton, tugatish usuli. **Generatsiya aynan shu fayldan ishlaydi.**

## 🔒 Git haqida

- `raw/` (videolar) va `_work/` (kadrlar) **git'ga kirmaydi** — hajmi katta, kerak ham emas.
- `teardowns/` va `style-profile.md` **git'ga kiradi** — asl qiymat shularda. Videolar o'chsa ham uslub saqlanib qoladi.

## 🛠 Qo'lda ishga tushirish (kerak bo'lsa)

```bash
cd marketing-machine/skills/reels-scripter
python tools/ingest.py referens-reels-hook/raw/VIDEO.mp4
```
Foydali flaglar:
- `--model medium` → tezroq (aniqlik biroz past). Default `large-v3` (o'zbekcha uchun eng aniq, birinchi safar ~1.5GB yuklaydi)
- `--scene 0.15` → kesimlar kam topilsa, sezgirlikni oshiradi
- `--no-transcribe` → faqat kadr/montaj tahlili

> **Eslatma:** scene-detect 100% ishonchli emas (sinovda tasdiqlandi). Shuning uchun montaj ritmi **contact sheet orqali ko'z bilan** tasdiqlanadi, scene-detect raqami esa yordamchi sifatida ishlatiladi.
