# Changelog

## 0.2.0
- **`reels-scripter` skill'i** (P1) — reference-driven: uslub o'ylab topilmaydi, referens reellardan o'lchanadi.
- **Ingest pipeline** (`tools/`): `ffmpeg` bilan vaqt belgili contact sheet + hook kadrlari + kesim tahlili, `faster-whisper large-v3` bilan so'zma-so'z transkript.
- **15 ta referens reel** to'liq teardown qilindi (536 KB) — kadrma-kadr montaj + so'zma-so'z transkript + jumla statistikasi.
- **`style-profile.md`** — o'lchangan uslub: 12 universal qoida, 14 hook formulasi, matn tizimi, montaj, yakun rejimlari.
- **`persona-override.md`** — kreatorning shaxsiy tanlovi profil ustiga qo'yiladi (registr, ritm, ta'lim rejimi).

### Tuzatilgan xatolar
- `style-profile` §1.7 «butun ssenariyda 1 ta buyruq fe'l (13/15)» — **noto'g'ri edi**. `DZj-s3dt8sn` da 7 ta buyruq bor. Sabab: hikoyadagi buyruq va bo'lim sarlavhasidagi buyruq ajratilmagan edi.
- Shart mayli («men qilgan bo'lardim») universal deb ko'rsatilgandi — aslida korpusda **2/15 (13%)**, ya'ni eng kam uchraydigan rejim. §5b da beshta ta'lim rejimi taksonomiyasi qo'shildi.
- `SKILL.md` `persona-override.md` ni o'qimasdi — persona e'tiborga olinmay qolardi. Load order qo'shildi.

### Ma'lum cheklovlar
- Scene-detect 15 tadan 13 tasida noto'g'ri sanadi (ham ortiqcha, ham kam) — montaj ritmi contact sheet orqali ko'z bilan tekshiriladi.
- `faster-whisper` uchun `cpu_threads=4` va har videoga alohida jarayon shart; `large-v3` yuklanishi ~600 MB bo'sh disk talab qiladi.
- Audio/beat tahlili cheklangan — ko'p teardownda `[noaniq]` deb belgilangan.

## 0.1.0
- Dastlabki skelet: marketplace-ready plugin strukturasi.
- `carousel-writer` skill'i + `carousel-archetypes` referens kutubxonasi.
