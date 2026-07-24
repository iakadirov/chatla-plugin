# Teardown Template — how to study one reference reel

Fill this template **once per reference video**, saved to `referens-reels-hook/teardowns/<video-stem>.md`.

The purpose is not to describe the video. It is to extract **reproducible rules** — patterns specific enough that a new script written from them would be indistinguishable in style from the reference. Vague notes ("energetic, fast-paced") are useless. Numbers, exact words, and counts are the deliverable.

## Hard rules for filling this out

1. **Transcribe verbatim.** Never paraphrase, never clean up grammar. Filler words, repetitions, broken sentences, and slang are *the style* — they are the most valuable data here. If whisper mis-heard a word, correct it against the burned-in captions visible in the frames.
2. **Count, don't feel.** Sentence length in words. Cut interval in seconds. Text-card duration. Number of shots. Every impression must be backed by a number.
3. **Verify montage with your eyes.** Read `contact_sheet.jpg` and the `hook_frames/`. The scene-detect number in `analysis.json` is a *hint only* — it has been proven to miss cuts. The contact sheet is the ground truth.
4. **Separate the repeatable from the one-off.** A joke about a specific event is not a pattern. "Opens with a 2-word fragment, then a pause, then the promise" is a pattern. Only patterns transfer.
5. **Never invent.** If the audio is unclear or a frame is ambiguous, write `[noaniq]`. A guessed line poisons the style profile.

---

# Teardown: `<video filename>`

## 1. Meta
| | |
|---|---|
| Davomiylik | `__s` |
| O'lcham / orientatsiya | `__x__` · 9:16? |
| Kesimlar soni (ko'z bilan, contact sheet) | `__` |
| O'rtacha kesim oralig'i | `__s` |
| Scene-detect raqami (yordamchi) | `__` |
| Arxetip (reels-archetypes.md dan) | `__` |
| Ovoz | VO / musiqa / ikkalasi / ovozsiz |

## 2. So'zma-so'z transkript (vaqt belgilari bilan)
> Verbatim. Filler, takror, buzilgan jumla — hammasi saqlanadi.

```
0.0–2.1  "..."
2.1–4.6  "..."
...
```

## 3. Hook teardown (0–3s) — eng muhim blok
Frame-by-frame, `hook_frames/` asosida:

| Vaqt | Ekranda nima | Aytilgan so'z | Ekran matni |
|---|---|---|---|
| 0.0s | | | |
| 0.5s | | | |
| 1.0s | | | |
| 1.5s | | | |
| 2.0s | | | |
| 2.5s | | | |

- **Pattern interrupt nima?** (harakat / yaqin plan / kutilmagan kadr / matn / ovoz)
- **Birinchi aytilgan jumla, so'zma-so'z:** "..."  → **necha so'z:** `__`
- **Ochilgan loop nima?** (tomoshabin qaysi savolga javob kutib qoladi)
- **Va'da nima?** (qolsa nima oladi)
- **Mute'da ishlaydimi?** (birinchi ekran matni yolg'iz o'zi hook'ni beradimi)

## 4. Beat map (butun video, montaj bilan)
| Vaqt | Kadr turi | Ekranda | Aytilgan gap (verbatim) | Ekran matni | Kesim? |
|---|---|---|---|---|---|
| | | | | | |

Kadr turi: talking-head / b-roll / ekran yozuvi / screen-record / arxiv / matn-kartochka / split

## 5. Jumla tuzilishi (eng qimmatli qism)
Bu blok "jumlalar qanday tuzilmoqda" degan savolga raqam bilan javob beradi.

- **Jumla uzunliklari (so'zda), ketma-ket:** `[4, 7, 3, 9, 5, ...]`
- **O'rtacha / mediana:** `__ / __`
- **Eng uzun jumla:** `__` so'z · **eng qisqa:** `__` so'z
- **Fragment (to'liq bo'lmagan gap) ulushi:** `__%`
- **Jumla boshlanish naqshlari** (takrorlanadiganlari): masalan "Mana...", "Lekin...", "Sen...", raqam bilan boshlash
- **Bog'lovchilar / ko'prik so'zlar:** ("lekin", "shuning uchun", "mana shu yerda", "endi eng muhimi")
- **Murojaat:** sen / siz / hamma / men-tili? Qaysi shaxs ustun?
- **Fe'l zamoni va shakli:** hozirgi / o'tgan / buyruq. Buyruq gap ulushi `__%`
- **Ritm naqshi:** qisqa-qisqa-uzun? savol→javob? tasdiq→rad?
- **Filler siyosati:** "aa", "ya'ni", "umuman olganda" bormi yoki toza kesilganmi?
- **Takrorlash usuli:** bir so'zni qayta ishlatish, uch marta takror, anafora?
- **Raqam ishlatish:** aniq raqamlar bormi? qanday joylashtirilgan?
- **Ko'chirib olinadigan 5 ta jumla qolipi** (yangi mavzuga moslanadigan shablon):
  1. `"____ , lekin ____"`
  2. ...

## 6. Montaj barmoq izi
- **Kesim tezligi:** har `__s` da (min `__`, maks `__`)
- **Eng tez blok qayerda?** (odatda hook yoki payoff)
- **Shot turlari ulushi:** talking-head `__%` · b-roll `__%` · matn `__%` · boshqa `__%`
- **O'tishlar:** hard cut / jump cut / whip / match cut / zoom punch-in — qaysi biri, necha marta
- **Zoom/punch-in ishlatiladimi?** qachon (urg'u paytida?)
- **Ekran matni uslubi:** shrift turi (qalin sans?), joylashuv (markaz/yuqori/past), rang, fon (qora plashka?), bir kartochkada necha so'z `__`, ekranda necha soniya `__s`
- **Matn subtitr-mi yoki urg'u-mi?** (har so'z chiqadimi yoki faqat kalit iboralar)
- **Emoji / stiker / strelka ishlatiladimi?**
- **Rang/look:** issiq/sovuq, kontrast, grain, natural?
- **B-roll bilan gapning bog'lanishi:** aytilgan narsa ekranda ko'rsatiladimi (literal) yoki metafora?

## 7. Audio
- VO bormi, musiqa turi, balandlik nisbati
- **Beat sync:** kesimlar musiqa zarbiga tushadimi?
- Sound effect (whoosh, pop, riser) — qayerda ishlatilgan
- Sukut (pauza) ishlatiladimi? qayerda va necha soniya

## 8. Struktura va yakun
- **Arxetip:** `__`
- **Spine:** hook `0–__s` → stavka `__–__s` → qiymat beats `__` ta → payoff `__s` → yakun `__s`
- **Loop qayerda ochiladi / yopiladi?**
- **Payoff nima?** (aniq)
- **Yakun turi:** loop-back / CTA / keskin kesim / cliffhanger
- **CTA bormi?** so'zma-so'z: "..."

## 9. ✅ Ko'chiriladigan qoidalar (bu videodan nima o'rganildi)
> Faqat **takrorlanadigan**, yangi mavzuga o'tadigan qoidalar. Har biri buyruq shaklida.
1.
2.
3.

## 10. ❌ Ko'chirilmaydigan (bu videoga xos, bir martalik)
1.
2.
