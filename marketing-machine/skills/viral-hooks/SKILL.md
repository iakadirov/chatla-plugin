---
name: viral-hooks
description: 'Generate scroll-stopping Instagram hooks in Uzbek from a library of 99 proven templates, organised into five families (curiosity/exposure, personal experience, educational, provocation, personal-catchy). Picks the family that matches the creator persona, fills the template with concrete specifics, and returns several ranked options with the reasoning. Use this skill whenever the user asks for a hook, a headline, an opening line, a cover line, "hook yozib ber", "sarlavha", "ilmoq", "birinchi qator", "muqova matni", or when another skill needs an opening it does not already have. Feeds carousel-writer (slide 1) and reels-scripter (the opening beat); those skills read references/hook-library-99.md directly.'
---

# Viral Hooks (Uzbek)

Turn any topic into an opening line that stops the scroll. Output is in **Uzbek**.

A hook is not a title. A title *labels* the content; a hook **opens a loop** the viewer needs closed. `«Instagram maslahatlari»` is a title. `«Sen har kuni buni qilasan — aynan shuning uchun reach yo'q»` is a hook.

## The library

`references/hook-library-99.md` — 99 templates in five families, each tagged with the register it carries and which creator persona it fits. **Read it every time; do not generate hooks from memory.** The library also carries the ⚠️ markers for templates that require real proof.

## Three rules that override everything

1. **Fill with specifics, not fillers.** `[soha]` → «Instagram'da xizmat sotadiganlar», not «biznesda». A template filled with vague words is worse than no hook — it reads as generic and the viewer scrolls.
2. **Honesty beats the template.** If a template demands a claim you cannot back (a number, a result, a personal story), **discard that template**. Templates marked ⚠️ only work with real proof. Never invent a statistic, a result, or an experience to satisfy a shape.
3. **Register must match the persona.** Family 4 (provocation) is built on pressure and hype. It is **wrong** for a calm-teacher persona no matter how catchy the line. Check the persona table at the end of the library.

## Workflow

1. **Read the library** (`references/hook-library-99.md`).
2. **Read the persona** if one exists — `referens-reels-hook/persona-override.md` for reels work, or `brain/clients/<id>/voice.md` for client work. The persona decides which families are allowed.
3. **Extract the sharp edge of the topic.** What is genuinely surprising, costly, or counterintuitive here? A hook can only be as interesting as the idea under it — if the idea is flat, say so and fix the idea first.
4. **Pick 2–3 families** the persona allows, and take candidate templates from each.
5. **Fill them with concrete specifics** — real numbers, real names, real timeframes.
6. **Rank and return 5 options**, each labelled with its library number and family, plus one line on why it works for this topic.
7. **Flag every honesty risk.** If an option needs proof the creator may not have, say so on that option.

## Output format

```
## 🎯 Burchak
[One line: the sharp edge this hook leans on.]

## Variantlar

**1. «[hook matni]»**
   `#[raqam] · [oila nomi]` — [nega bu mavzuga mos, bir qator]
   ⚠️ [agar dalil kerak bo'lsa — nima kerakligi]

**2. «[hook matni]»**
   ...

[5 tagacha]

## 💡 Tavsiya
[Qaysi birini va nega — bitta xatboshi.]

## → Keyingi bosqich
- carousel-writer: 1-slayd muqovasi sifatida
- reels-scripter: profil §3 formulasiga quyiladi (ko'prik qoidasi)
```

## Bridge rule — how this feeds the other skills

The library finds the **angle**. It does not decide the **shape**.

- **`reels-scripter`** has its own 14 hook formulas measured from the reference corpus (`style-profile.md` §3). Those carry the creator's actual rhythm and length. So: take the angle from the library, then **cast it into a measured formula**. Never paste a library template straight into a reel script — it will break the sentence-length and cadence work.
- **`carousel-writer`** has no measured profile, so the library is used **directly** for slide 1.

## Note on edits
Instructions are in English; all hook output is in Uzbek. To add or retire templates, edit `references/hook-library-99.md` — keep the existing numbering stable so other skills and past plans can still reference hooks by number.
