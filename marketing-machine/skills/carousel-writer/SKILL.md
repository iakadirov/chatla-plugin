---
name: carousel-writer
description: 'Turn a topic, idea, plan item, or rough note into slide-by-slide Instagram carousel copy, written in Uzbek in the credible-expert "Shunchaki Nega? / Donishmand Ustoz" voice. Produces a full swipe-engine — hook cover, one-idea-per-slide body, and a conversion CTA slide — engineered for SAVES and comment→DM. Use this skill whenever the user wants a carousel, a multi-slide Instagram post, "karusel", "slayd matni", "post yozib ber", "carousel copy", "slaydlarga matn", a list/steps/myth/framework post, or hands over a content-plan item whose format is carousel — even if they don''t say the word "carousel". Chains after viral-hooks (for slide 1) and hands off to carousel-designer (visual prompts) and caption-cta-writer (the caption).'
---

# Carousel Writer (Uzbek Instagram Carousels)

Take any topic and build it into an Instagram **carousel** — a stack of 6–10 slides that a person swipes through to the end, then **saves** and (ideally) **comments a keyword to get a DM**. Output is in **Uzbek**, in the **credible-expert voice** (the "Donishmand Ustoz / Shunchaki Nega?" register — strong, sure, honest, never cheap clickbait).

A carousel is not an article chopped into slides. It is a **swipe engine**: every slide's only job is to earn the next swipe. The metric that matters is not views — it's **save rate** and **swipe-through** (how many reach the last slide). Design for those.

```
❌ Slide as paragraph:  "Instagram algoritmi 2024-yilda o'zgardi va endi u
                         saqlash va ulashishga ko'proq e'tibor beradi, shuning
                         uchun kontentingizni shunga moslashtirishingiz kerak..."
✅ Slide as swipe unit:  🏷 "Algoritm endi 'like'ni sanamaydi"
                         📝 "U bitta narsani kuzatyapti. Keyingi slaydda —
                            aynan nimani."
```

## Core principles (why carousels get saved)

1. **One idea per slide.** If a slide has two ideas, split it. Scannable beats complete. A viewer reads a slide in ~1.5 seconds — a bold headline + 1–3 short lines, never a wall of text.
2. **Every slide earns the next swipe.** End body slides with a micro-hook, an open loop, or a "keyingi slaydda…" continuity cue. The swipe is the whole game; a slide that closes its loop kills momentum.
3. **Save-worthiness is designed, not hoped for.** People save references they'll return to: steps, checklists, frameworks, "N ta xato" lists. Make the carousel a thing worth keeping. If it isn't save-worthy, change the archetype.
4. **Slide 1 is a hook, not a title.** The cover must stop the scroll and promise a payoff — same voltage rules as `viral-hooks`. A flat title slide ("Instagram maslahatlari") is a dead carousel.
5. **The last slide converts.** The final slide is not "rahmat" — it drives one action: SAVE, SHARE, or a comment keyword that triggers a Chatla DM. Content that ends without a conversion path is a wasted reach.
6. **Honest by construction (non-negotiable).** Never invent statistics. No "90% odam" unless it's real and defensible. Reframe to honest ("Ko'pchilik bunga e'tibor bermaydi"). One fabricated stat wins one save and breaks the brand.

## Slide arc — the default spine

Most carousels follow this shape. Adapt slide count to the topic (default **7–8**):

- **Slayd 1 — HOOK (muqova):** stop the scroll, promise the payoff. Pull from `viral-hooks` if a hook wasn't supplied.
- **Slayd 2 — STAVKA / muammo:** why this matters to the viewer *now*. Open the loop wider; name the pain or the cost. Do NOT start delivering value yet.
- **Slayd 3…N-2 — QIYMAT (payoff, bosqichma-bosqich):** the promise delivered, one point per slide. Each is a self-contained, save-worthy nugget.
- **Slayd N-1 — XULOSA / aha:** tie it together — the recap, the reframe, or the single biggest takeaway.
- **Slayd N — CTA (konversiya):** one clear action. Prefer a comment-keyword → DM (feeds Chatla comment→DM), with SAVE as the fallback ask.

## Slide length — the #1 formatting rule

- **Sarlavha (headline):** ≤ 6 words. Big, bold, scannable.
- **Matn (body):** ≤ 3 short lines, ~ ≤ 20 words total. Fragments are fine. White space is your friend.
- If a slide needs more than that, it's two slides. Split it.

```
❌ Uzun, tushuntiradi:   🏷 "Kontent rejasi qanday tuziladi"
                          📝 "Avval auditoriyangizni tahlil qiling, keyin
                             ustunlarni belgilang, so'ng har bir ustun uchun
                             mavzular ro'yxatini yozing va formatni tanlang."
✅ Bitta g'oya, ochiq loop: 🏷 "Reja 3 ta ustundan boshlanadi"
                          📝 "Ko'pchilik 4-chisini o'tkazib yuboradi.
                             O'sha eng muhimi."
```

## Voice: credible expert, punchy (same register as viral-hooks)

- **Authority through brevity.** A sure expert doesn't over-explain. Short, certain lines read as *more* credible.
- **Strong, not screamy.** No ALL CAPS, no "SHOK!!!". Power is in certainty, not volume.
- **Talk to one person.** "Siz/sen", not "hammangiz". A carousel is a 1-on-1 whisper, not a stage announcement.
- If a client voice profile exists (`brain/clients/<id>/voice.md`), read it and match tone, dos/donts, and forbidden claims. Otherwise use the default Shunchaki Nega register.

## Workflow

1. **Extract the core.** One line: what's the genuinely useful/surprising/save-worthy thing here? If the topic is flat, dig for the angle the viewer doesn't expect. This becomes the promise the whole carousel keeps.
2. **Pick the archetype.** Read `references/carousel-archetypes.md` and choose the structure that fits the core (list / steps / myth-bust / framework / mistakes / story). The archetype decides the slide arc.
3. **Get the hook.** If a hook was handed over (from `viral-hooks` or the plan), use it for Slide 1. If not, build one now from the **99-template library**: `../viral-hooks/references/hook-library-99.md` — five families, each tagged with the register it carries and which creator persona it fits.
   - Pick the family the persona allows (the library's persona table); **family 4 (provocation) is wrong for the calm-expert voice** this skill uses by default.
   - Fill `[kvadrat qavs]` with **concrete specifics** — real numbers, real names. A template filled with vague words reads as generic and kills the cover.
   - Respect the ⚠️ markers: those templates demand real proof. **Discard the template rather than invent a claim.**
   - Unlike `reels-scripter` (which re-casts the angle into a measured formula), carousels use the library template **directly** — there is no measured cadence profile to protect here.
4. **Outline the slides** before writing prose: assign one idea to each slide along the arc. Verify swipe-through — does each slide give a reason to swipe on?
5. **Write each slide:** headline ≤6 words + body ≤3 lines. Apply the continuity cue to body slides. Keep the payoff honest and concrete.
6. **Engineer the last slide** as a conversion: pick ONE action. If a comment→DM keyword fits, propose it (this wires into Chatla). Otherwise SAVE.
7. **Add a visual brief per slide** — a one-line note for `carousel-designer` (what the image/layout should show). This is the handoff, not final design.
8. **Run the checks:** honesty (no fake numbers), save test (would someone keep this?), swipe test (does slide 1 earn slide 2, and so on to the end).

## Output format

ALWAYS use this exact structure so the downstream skills can consume it:

```
## 🎯 Yadro
[One line: the save-worthy core promise this carousel keeps.]

## 📐 Arxetip
[Chosen type] · [slide count] slayd

## Slaydlar

**Slayd 1 — HOOK (muqova)**
🏷 Sarlavha: "..."
📝 Matn: "..."
🎨 Visual: [one-line brief for carousel-designer]

**Slayd 2 — STAVKA / muammo**
🏷 Sarlavha: "..."
📝 Matn: "..."
🎨 Visual: [...]

[... QIYMAT slaydlari, har biri bitta g'oya, swipe cue bilan ...]

**Slayd N-1 — XULOSA / aha**
🏷 Sarlavha: "..."
📝 Matn: "..."
🎨 Visual: [...]

**Slayd N — CTA (konversiya)**
🏷 Sarlavha: "..."
📝 Matn: "..."
💬 DM kaliti: "[keyword]"   ← comment→DM uchun (Chatla); mos kelmasa "Saqlab qo'ying"
🎨 Visual: [...]

## → Keyingi bosqich
- caption-cta-writer: caption + birinchi izoh yozadi (DM kaliti bilan)
- localizer: RU varianti kerak bo'lsa
```

If the user asks for only the copy (no visual briefs) or a specific slide count, honor that. If unspecified, default to 7–8 slides with visual briefs.

## Worked example

**Mavzu (rejadan):** "Ko'p biznes Instagram'da mijozni qo'ldan boy beradi."

**🎯 Yadro:** Reach bor, lekin DM'da javob sekin/yo'q — mijoz kutmaydi, raqibga ketadi. Buni tizim hal qiladi.

**📐 Arxetip:** Xato / Mistakes · 7 slayd

**Slayd 1 — HOOK (muqova)**
🏷 Sarlavha: "Reach bor. Mijoz yo'q."
📝 Matn: "Sabab postda emas. Keyingi slaydda — aynan qayerda."
🎨 Visual: to'q fon, katta oq sarlavha, past qismda ozgina DM ikonkasi

**Slayd 2 — STAVKA / muammo**
🏷 Sarlavha: "Mijoz 5 daqiqa kutmaydi"
📝 Matn: "DM'ga javob kechiksa — u allaqachon raqibda. Siz sezmaysiz ham."
🎨 Visual: soat + o'qilmagan xabar ko'rsatkichi

**Slayd 3 — QIYMAT**
🏷 Sarlavha: "Xato #1: qo'lda javob"
📝 Matn: "Tunda, dam olishda savol keladi. Odam uxlaydi — savdo o'ladi."
🎨 Visual: kechqurun telefon, javobsiz xabar

**Slayd 4 — QIYMAT**
🏷 Sarlavha: "Xato #2: bir xil savol, 100 marta"
📝 Matn: "Narx? Manzil? Har kuni qayta yozasiz. Vaqt yonadi."
🎨 Visual: takrorlanuvchi bir xil xabar bulutlari

**Slayd 5 — QIYMAT**
🏷 Sarlavha: "Xato #3: izoh — o'lik yer"
📝 Matn: "Odam 'narxi?' deb izoh yozadi. Javob DM'da bo'lishi kerak edi."
🎨 Visual: izoh → strelka → DM

**Slayd 6 — XULOSA / aha**
🏷 Sarlavha: "Yechim: avtomatik DM"
📝 Matn: "Izoh kelsa — bot darhol DM yozadi, savolga javob beradi, sizni chaqiradi."
🎨 Visual: izoh → avtomatik DM oqimi (2 qadam)

**Slayd 7 — CTA (konversiya)**
🏷 Sarlavha: "Buni sizga sozlab beramiz"
📝 Matn: "Qanday ishlashini ko'rmoqchimisiz?"
💬 DM kaliti: "DM"   ← "Kommentga 'DM' yozing — botni ko'rsatamiz"
🎨 Visual: sokin CTA slayd, katta 'DM' so'zi

**→ Keyingi bosqich**
- caption-cta-writer: caption + "DM" kaliti bilan birinchi izoh
- localizer: RU varianti (mijoz auditoriyasi aralash bo'lsa)

## Libraries

- `references/carousel-archetypes.md` — 6 carousel structures (list, steps, myth-bust, framework, mistakes, story), each with its slide arc and when to use it. Read it in step 2 to pick the right shape; don't rely on memory.
- `../viral-hooks/references/hook-library-99.md` — 99 hook templates in five families for Slide 1. Read it in step 3. Templates are numbered and stable, so a content plan can specify "hook #47" and this skill will produce it.

## Note on edits
Instructions are in English (clearer for the model); all slide copy and output are in Uzbek. To change the default slide count, voice, or output structure, edit the relevant section above.
