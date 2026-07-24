---
name: reels-scripter
description: 'Turn any topic into a beat-by-beat Instagram Reels script in the creator''s own style — sentence length, hook formulas, on-screen text, cut cadence and ending mode all come from a measured reference profile, not from taste. Output is a shot-list a video engine (Higgsfield) can produce directly. Use whenever the user wants a reel, a short video, a Reels/TikTok/Shorts script, "reels yozib ber", "reels ssenariy", "video skript", "ssenariy yoz", says they added reference videos, or hands over a plan item whose format is reels/video — even without the word "reel". Chains after viral-hooks; hands off to higgsfield-content-factory and caption-cta-writer.'
---

# Reels Scripter (reference-driven, RU → UZ)

Take any topic and build it into an Instagram **Reel** whose style is **learned from the user's own reference corpus**, not invented.

The corpus (`referens-reels-hook/`) is **15 reels by one Russian creator** — 20 minutes of video, fully transcribed with `large-v3` and torn down frame-by-frame. Every rule below is a measurement, not an opinion.

## Language

- **Default output: RUSSIAN.** The style profile is derived from Russian reels; sentence rhythm, connectives and text cards only reproduce faithfully in the source language.
- **Uzbek adaptation is a separate final pass**, done only when the user asks. Adapt *meaning and rhythm*, not word-for-word — Uzbek sentence lengths must land in the same 8–12 word band.
- Section labels in the output template stay in Uzbek (the operator is Uzbek); **script lines, on-screen text and captions are Russian**.

## Load order — read these before writing anything

Three layers, applied in this order. **Later layers override earlier ones.**

| # | File | What it is | If missing |
|---|---|---|---|
| 1 | `referens-reels-hook/style-profile.md` | **Measured facts** from the 15-reel corpus — the authority on style | Fall back to the retention principles at the bottom, and tell the user the output is generic |
| 2 | `referens-reels-hook/persona-override.md` | **The creator's own choices** — register, pacing, teaching mode | Skip; use the profile's own averages |
| 3 | `brain/clients/<id>/voice.md` | Per-client voice, if this is client work | Skip |

**Precedence: persona-override beats style-profile beats your own taste.** The profile measures what the *reference creator* does; the persona says what *this* creator does. When they conflict, the persona wins — and say so in the fidelity check.

⚠️ **Never skip step 2.** A persona override typically changes cut cadence, sentence length, teaching mode and whether imperatives are allowed. Generating without it produces a script in the wrong voice even though every profile rule passes.


# Phase 1 — Ingest new references (only when the user adds videos)

```bash
cd marketing-machine/skills/reels-scripter
python tools/ingest.py referens-reels-hook/raw/<VIDEO> --frames-only   # fast
bash  tools/transcribe_seq.sh                                          # slow, resumable
```
Produces per video in `_work/<stem>/`: `analysis.json`, `sheets/` (timestamped contact sheets, 1 thumb/sec), `hook/` (first 6s at 0.5s steps), `cuts/`, `transcript.txt`.

**Then:** read the contact sheets **with your eyes**, write a teardown per `references/teardown-template.md` into `teardowns/`, and **rebuild `style-profile.md`** (a pattern is a rule only at ≥60% of the corpus).

> ⚠️ Two hard-won operational facts, both verified:
> - **Scene-detect lied in 13 of 15 videos** — both over- and under-counting. Contact sheets are the ground truth for montage rhythm.
> - **`cpu_threads` must stay at 4** and each video needs its own fresh process, or faster-whisper dies with `mkl_malloc: failed to allocate memory`. Loading `large-v3` also needs **~600 MB free disk**; `transcribe_seq.sh` aborts below 1.2 GB rather than thrash a full volume.


# Phase 2 — Generate a script

1. **Load the style.** Read `style-profile.md`, then `persona-override.md` (load order above).
2. **Extract the core.** One line: the genuinely useful / surprising thing here. If flat, find the unexpected angle.
3. **Pick the teaching mode** — profile §5b. This decides *how advice is delivered* and is the single biggest driver of how the script sounds. The persona file usually names it; if not, pick from the persona's register.

   | Rejim | Korpusda | Ovoz |
   |---|---|---|
   | **A** To'g'ridan buyruq | 4/15 | «Держи фокус» — energiyali ekspert |
   | **B** Mexanizm tushuntirish | 4/15 | «Bu shunday ishlaydi» — 3-shaxs, buyruqsiz. **Ustoz registri** |
   | **C** Qoida + shaxsiy isbot | 3/15 | qoida («ты») → isbot («я», o'tgan zamon) |
   | **D** Nominal / fe'lsiz | 2/15 | «Birinchi qadam — g'oya izlash» |
   | **E** Shart mayli | 2/15 | «Men bo'lsam shunday qilardim» — eng yumshoq |

   ⚠️ **Do not default to E.** It is the rarest mode (13%) and reads as hesitant. Earlier versions of this skill wrongly treated it as universal.
   ⭐ **Never mix modes inside one script** — the CTA is the only exception (always imperative).
4. **Pick the archetype** from the profile's §11 table (Hikoya / Listicle / Freymvork / Tutorial / Myth-bust / Anafora). The archetype sets length, promise timing, b-roll type and ending mode — **do not mix these settings across archetypes**. Cut cadence comes from the persona if one is set, otherwise from the archetype.
5. **Build the hook — two sources, two jobs.**
   - **Angle** (what we lean on): pick from `../viral-hooks/references/hook-library-99.md` — 99 templates in five families, each tagged by register and persona fit. Respect its ⚠️ markers (templates needing real proof) and its persona table (family 4 is wrong for a calm-teacher persona).
   - **Shape** (rhythm and length): cast that angle into one of the **14 measured formulas** in profile §3. These carry the corpus's actual sentence length and cadence.

   ⭐ **Never paste a library template straight into a reel script** — it breaks the measured sentence-length and cadence work. Library finds the angle; profile §3 gives it the shape.

   First word at t=0.00, no greeting. Hook text must be **85–100% on screen** (mute-proof).
6. **Plant documentary proof in the first ~10s** — screenshot, archive frame, real interface. Never a bare claim.
7. **Write the body** to the profile's sentence rules: median 10–12 words, `И/А/Но` openers, historical present for past events, verb chains, `НЕ X, А Y` antithesis, numbers escalating.
8. **Design the on-screen text**: two registers (small white lowercase bridge + BIG CAPS, yellow = payload only), 1–3 words per card, a new card every **0.6–1.2s** — i.e. **2–4× faster than the cuts**. Build lines progressively. Numbers as digits.
9. **Set the cut rhythm to meaning**: 4–6s hold on the central claim, 0.3–0.9s bursts on lists/proof, ~2.3s average. Cuts land on sentence boundaries, never on the beat.
10. **Give every abstract idea a physical demonstration** — one prop/action per 6–9s.
11. **Spend the imperative once.** Everywhere else: infinitive, inclusive «мы», or conditional «Я бы…».
12. **Engineer the ending** by the archetype: universal aphorism / status line (default, 9/15) **or** the comment-keyword CTA formula (profile §8b) when a DM conversion is wanted — proof → reward named → `«Пиши [KALIT]»`, keyword derived from the topic.
13. **Run the fidelity check.** Fix failures *before* showing the user.

## Fidelity check — every time

Report as a table with three columns: **profil talabi · persona talabi · bu ssenariy**. Where the persona deliberately deviates from the profile, mark it `ataylab` rather than as a failure.

- [ ] **Teaching mode** — one mode throughout, matching the persona? Zero imperatives outside the CTA if the mode forbids them?
- [ ] **Persona pacing** — cut cadence and sentence length match `persona-override.md`, not the profile average?
- [ ] Sentence word counts: median **10–12** (or the persona's own band), section headers **3–5**?
- [ ] Hook built from a profile formula, first word at 0.00, no greeting, mute-proof?
- [ ] Proof inside the first ~10s?
- [ ] Text cards 1–3 words, new card every 0.6–1.2s, **2–4× faster than cuts**?
- [ ] Yellow used **only** for payload (number / money / loss / decision verb)?
- [ ] Numbers written as digits on screen, spoken as words?
- [ ] Exactly **one** imperative, at the end or in the CTA?
- [ ] One physical demonstration per 6–9s?
- [ ] Cut cadence bound to meaning; nothing beat-locked?
- [ ] Ending matches the archetype's mode?
- [ ] Nothing from profile §9 (⛔ Hech qachon) present — no greeting, no «подпишись», no dead air?
- [ ] **Honesty:** every number real. Never fabricate a statistic, result or personal story.

State the result briefly with numbers, e.g. *"jumla mediana 11 so'z ✅ · matn/kesim nisbati 2.8× ✅ · 1 buyruq ✅"*.


# Output format

```
## 🎯 Yadro
[One line: the promise this reel keeps.]

## 📐 Format
[Arxetip] · ~[N]s · 9:16 · Hook formulasi: [№ + nomi profil §3 dan]
🎨 Uslub manbasi: style-profile.md (15 referens)
🏁 Yakun rejimi: [aforizm | komment-kalit CTA]

## 🎬 Skript (beat-by-beat)

**HOOK (0–Xs)**
🎥 Kadr: [...]
🗣 Gap (RU): "..."           [so'z: N]
✍️ Ekran: kichik oq "..." / **KATTA SARIQ "..."**

**[BO'LIM] (X–Ys)**
🎥 Kadr: [...]
🗣 Gap (RU): "..."           [N]
✍️ Ekran: [...]
🔨 Jismoniy ko'rsatish: [rekvizit / harakat]

[... beat'lar, har biri bitta g'oya ...]

**YAKUN**
🗣 Gap (RU): "..."
✍️ Ekran: [...]
💬 CTA: «Пиши [KALIT]» — [mukofot]     ← faqat CTA rejimida

## 📊 Ritm xaritasi
kesim: o'rtacha ~X.Xs · eng sekin [qayerda] · portlash [qayerda]
matn: har ~X.Xs (kesimdan X.X× tez)

## ✅ Fidelity check
[raqamlar bilan]

## → Keyingi bosqich
- higgsfield-content-factory / video-producer: skriptdan video
- caption-cta-writer: caption + birinchi izoh
- 🇺🇿 O'zbekcha adaptatsiya: so'rasangiz alohida pass
```


# Retention physics (Mode B floor / the "why")

Instagram ranks Reels on **watch time**, then **sends per reach**, then **likes per reach** (Mosseri, 2025).

1. **First 3 seconds decide everything** — up to 50% leave; a >60% 3-second hold reaches 5–10× further.
2. **Retention % beats length.** Never pad.
3. **Keep the loop open** until the payoff.
4. **The payoff must pay** — a weak ending trains viewers to skip you next time.
5. **Design for sends** — ask why someone would DM this to a friend.
6. **85%+ watch on mute** → on-screen text carries the narrative.
7. **Original by construction** — Instagram down-ranks reposts and watermarks.
8. **Honest by construction** — never invent statistics.

**Mode B spine:** HOOK (0–3s) → STAVKA → QIYMAT beats (1.5–3s each) → PAYOFF → LOOP/CTA.


# Files

- `referens-reels-hook/style-profile.md` — **measured facts.** 12 universal rules, §5b teaching-mode taxonomy, 14 hook formulas, sentence stats, montage, text system, endings, forbidden list, 15 copy-ready sentence molds, archetype→settings table.
- `referens-reels-hook/persona-override.md` — **the creator's own choices**, layered on top of the profile. Read it every time; it wins on conflicts.
- `referens-reels-hook/teardowns/` — 15 per-video forensic teardowns (536 KB).
- `referens-reels-hook/README.md` — where the user drops new videos.
- `tools/ingest.py` · `tools/transcribe_seq.sh` · `tools/transcribe_all.py` — the ingest pipeline.
- `references/teardown-template.md` — the strict per-video analysis template.
- `references/reels-archetypes.md` — generic archetype library (Mode B).

# Note on edits
Instructions are in English. Script output is **Russian**; Uzbek only on request, as a separate adaptation pass. To change how scripts sound, add reference videos and rebuild `style-profile.md` — don't hand-edit prose here.
