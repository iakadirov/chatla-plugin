# Teardown: `DVLS6-Pjd0f.mp4`

## 1. Meta
| | |
|---|---|
| Davomiylik | **75.14s** |
| O'lcham | 1080×1920 · 9:16 · 30fps · vp9 + aac |
| Kesimlar (ko'z bilan tasdiqlangan) | **23 kesim → 24 kadr** |
| O'rtacha kadr | **3.13s** · mediana **2.90s** · min **1.10s** · maks **8.10s** |
| Scene-detect raqami (yordamchi) | 24 @0.15 · 19 @0.25 — **ikkalasi ham noto'g'ri** (pastga qarang) |
| Arxetip | **Framework / Listicle ("4 ТИПА") + Comparison** — har bir tip bir xil skorkarta bo'yicha o'lchanadi |
| Ovoz | VO (kreator o'zi), uzluksiz + doimiy fon qatlami |
| Produksiya rejimi | **Bitta kvartira + bitta flipchart doska + kostyum almashishi** |
| Asosiy artefakt | **Qo'lda yozilgan flipchart skorkarta** (4 marta takrorlanadi) |

### Scene-detect vs ko'z — nima o'tkazib yuborilgan
`analysis.json` @0.15 24 ta kesim beradi, lekin ular ichida **43.23 va 43.27 bitta kesim** (dublikat), ya'ni real 23. Detektor umuman ko'rmagan kesim: **2.47s** (hook ichidagi jump-cut — hook_05 va hook_06 kadrlari butunlay boshqa plan). Detektor kesim deb hisoblagan, lekin kesim BO'LMAGAN nuqtalar: **25.10s** va **50.9s** — bular kamera kesimi emas, **doskadagi mini-skrinshotning almashishi** (grafik almashinuvi, kadr o'zi qimirlamaydi). Shuningdek **44.07s** — bu telefon ekranini barmoq bilan scroll qilish, kesim emas.

**Yakuniy kesim ro'yxati (23):**
`2.47 · 6.73 · 8.17 · 10.40 · 13.33 · 17.43 · 20.37 · 24.17 · 26.27 · 27.90 · 29.63 · 30.73 · 32.50 · 35.67 · 36.87 · 39.73 · 43.27 · 46.73 · 48.13 · 53.90 · 61.20 · 63.00 · 71.10`

## 2. So'zma-so'z transkript (vaqt belgilari bilan)
> Verbatim, whisper large-v3. Grammatika tuzatilmagan — "релсе / рилсе / рилс" xatosi ham, "держались в высокий охват" buzuq konstruksiyasi ham asl holida.

```
 0.00– 6.64  Я потратил 7 лет для того, чтобы сейчас за 60 секунд рассказать вам, как делать контент, который приносит подписки и продажи.
 6.68– 8.00  Всего есть 4 типа контента.
 8.10–10.28  Первый, охватный, это тренды и юмор.
10.36–13.22  Тут много просмотров, но он не дает подписчиков и денег.
13.32–17.30  И если ты пытаешься снимать тренды, у тебя нет шансов развить блог.
17.42–20.28  Но есть еще 3 типа контента, которые тебя спасут.
20.36–21.82  Второй тип, экспертный.
21.88–23.92  Делимся полезной информацией или обучаем.
24.04–26.24  Он дает больше всего подписчиков.
26.26–29.58  На этом релсе 500 тысяч просмотров и он принес мне 5000 подписчиков.
29.58–32.24  А на этом рилсе 1,8 миллионов и он мне принес 20 тысяч
32.24–35.58  А этот рилс набрал 3 миллиона и принес 17 тысяч подписчиков
35.58–36.70  Третий, личный
36.70–39.52  Делимся историями из жизни и раскрываемся как человек
39.52–43.12  Это нужно, чтобы люди долго оставались в блоге и держались в высокий охват
43.12–46.52  Я делаю много личного контента и мои сторис смотрят под 100 тысяч человек
46.52–48.10  И четвертый тип, продающий
48.10–51.02  Рассказываем о своем продукте и получаем заявки с продажами
51.02–53.76  Набирает меньше всего просмотров, но приносит деньги
53.76–54.54  И вот идеальный план
54.54–57.18  Я бы не вел сторис, пока не наберу хотя бы 5 тысяч подписчиков
57.18–61.14  Чтобы их набрать, я бы снимал по 10-15 хороших релсов в месяц
61.14–62.88  И снимал бы их вот в такой пропорции
62.88–67.06  Чтобы делать большие продажи, вы можете объединять экспертный и личный контент с продажами
67.06–68.34  Прямо в одном ролике
68.34–71.00  И тогда даже продающий ролик может набрать миллион просмотров
71.00–73.20  Мои ученики так развивают блог даже с нуля
73.20–75.06  Так что это работает, попробуй
```

- **Jumla soni:** 28 · **so'z soni:** 243
- **Nutq tezligi:** 243 / 75.06s = **3.24 so'z/s ≈ 194 so'z/min**
- **O'lik havo (pauza):** jami **0.72s** = davomiylikning **0.96%i**. Eng uzun pauza 0.12s (17.30→17.42 va 23.92→24.04). 26.26s dan keyin jumlalar orasida **nol pauza** — segmentlar tutash.

## 3. Hook teardown (0–6.73s) — eng muhim blok

Frame-by-frame, `hook/` (0.5s qadam) asosida:

| Vaqt | Ekranda | Aytilgan (verbatim) | Ekran matni |
|---|---|---|---|
| 0.0s | Talking-head, bel-plan, keng burchak (shift buzilishi ko'rinadi), bej kurtka + oq futbolka, jigar parda + deraza | "Я потратил…" | **Я ПОТРАТИЛ** (oq, YUQORI) |
| 0.5s | Push-in boshlandi — ko'krak-plan | "…потратил 7…" | Я ПОТРАТИЛ |
| 1.0s | Push-in tugadi — yuz kadrni to'ldiradi | "…7 лет…" | Я ПОТРАТИЛ / **7 ЛЕТ** (SARIQ) |
| 1.5s | Sama yaqin plan | "…для того…" | Я ПОТРАТИЛ / 7 ЛЕТ *(yuqori)* + **для того** *(past-markaz, kichik oq)* |
| 2.0s | Sama | "…чтобы сейчас…" | Я ПОТРАТИЛ / 7 ЛЕТ + **чтобы сейчас** |
| **2.47s** | **KESIM** → keng planga qaytish | | |
| 2.5s | Keng plan, qo'l harakatda | "…за 60 секунд…" | **ЗА 60 СЕКУНД** (oq) |
| 3.0s | Sama | "…секунд…" | ЗА 60 СЕКУНД |
| 3.5s | Sama, barmoq bilan ko'rsatadi | "…рассказать вам…" | ЗА 60 СЕКУНД / **РАССКАЗАТЬ ВАМ** (SARIQ) |
| 4.0s | Sama | "…как делать…" | **КАК ДЕЛАТЬ** (oq) |
| 4.5s | Sama | "…контент…" | КАК ДЕЛАТЬ / **КОНТЕНТ** (SARIQ) |
| 5.0s | Kadr yuqorisida **birinchi isbot kartochkasi** paydo bo'ladi | "…который приносит…" | **приносит** (kichik oq, markaz) |
| 5.5s | **Ikkita isbot kartochkasi**: «Действия в профиле ⓘ **2,493** / Подписки 2,493» + «**2550** платных заказов *133 626 489 руб.* / **2411** оплачено 94.55% **103 138 177 руб.**» | "…подписки…" | **ПОДПИСКИ** (oq) |
| 6.6s | Kartochkalardagi raqamlar o'zgargan: «Подписки **19,422**» + «**8376** платных заказов *123 780 730 руб.* / **8294** оплачено 99.02% **101 475 137 руб.**» | "…и продажи." | **и продажи** (kichik oq) |

- **Pattern interrupt nima?** Vizual gimmik yo'q — oddiy talking-head. Zarba uchta narsada: **(1)** 0.0→1.0s ichidagi **tez raqamli push-in** (bel-plan → yuz kadrni to'ldiradi, ~1.2s), **(2)** 1.0s da sariq **«7 ЛЕТ»** portlashi, **(3)** leksik — **vaqt savdosi**.
- **Birinchi aytilgan jumla, so'zma-so'z:**
  > "Я потратил 7 лет для того, чтобы сейчас за 60 секунд рассказать вам, как делать контент, который приносит подписки и продажи."
  → **21 so'z.** Bu videodagi **eng uzun jumla** (o'rtacha 8.7 so'z, ya'ni 2.4×). Uzunligiga qaramay 6.64s da aytiladi (3.16 so'z/s — umumiy tezlik bilan bir xil).
- **Hook dvigateli — VAQT SAVDOSI:** `[MEN SARFLAGAN KATTA VAQT] ↔ [SENGA KETADIGAN KICHIK VAQT] ↔ [ANIQ NATIJA]` = **7 лет ↔ 60 секунд ↔ подписки и продажи**. Nisbat ≈ 3.7 mln : 1.
- **Ochilgan loop:** *"kontent qanday qilib obuna va sotuv keltiradi?"* — to'liq javob faqat **63.00–71.10s** da (birlashtirish formulasi) beriladi, ya'ni videoning **84%idan keyin**.
- **Isbot birinchi 7 soniyada:** 5.0–6.7s da ikkita yarim shaffof iOS-uslubidagi skrinshot kartochkasi. **Ya'ni da'vo aytilgan zahoti hujjatlashtiriladi** (`DS7rlXjja9c` dagi eski post skrinshoti bilan bir xil qoida).
- **Mute'da ishlaydimi?** ⚠️ **Qisman.** 0.0s dagi «Я ПОТРАТИЛ» (2 so'z) yolg'iz o'zi hook bermaydi. Mute-hook **1.0s** da to'liq bo'ladi («Я ПОТРАТИЛ 7 ЛЕТ» = 4 so'z) va **4.5s** da va'da yopiladi («КАК ДЕЛАТЬ КОНТЕНТ»). Butun video esa 63% subtitr qamrovi bilan mute'da to'liq o'qiladi.
- **«60 секунд» va'dasi bajarilmaydi:** video **75.14s**, ya'ni va'dadan **25% uzun**. Kreator buni oxirida eslatmaydi.

## 4. Struktura — spine (vaqt belgilari bilan)

```
 0.00– 6.73s  HOOK              vaqt savdosi + 2 ta isbot skrinshoti           6.73s · 21 so'z
 6.73– 8.17s  RO'YXAT VA'DASI   "Всего есть 4 типа контента."                  1.44s ·  5 so'z
 8.17–17.43s  TIP 1 · ОХВАТНЫЙ  [1/4] skorkarta + trend-raqs b-roll            9.26s · 28 so'z
17.43–20.37s  RE-HOOK           "Но есть еще 3 типа контента, которые тебя спасут."  2.94s · 9 so'z
20.37–35.67s  TIP 2 · ЭКСПЕРТНЫЙ [2/4] skorkarta + 3 ta rils isboti           15.30s · 48 so'z
35.67–46.73s  TIP 3 · ЛИЧНЫЙ    [3/4] skorkarta + qiz bola + storis isboti    11.06s · 36 so'z
46.73–53.90s  TIP 4 · ПРОДАЮЩИЙ [4/4] skorkarta, isbotsiz                      7.17s · 20 so'z
53.90–63.00s  ИДЕАЛЬНЫЙ ПЛАН    3 bandli ro'yxat + 50/30/20 doiraviy diagramma 9.10s · 37 so'z
63.00–71.10s  SINTEZ/FORMULA    экспертный+личный+продажи → 1 МЛН              8.10s · 26 so'z
71.10–75.14s  ISBOT + YAKUN     3 juft o'quvchi "oldin→keyin" + "попробуй"     4.04s · 13 so'z
```

> ### 🔑 Eng muhim strukturaviy topilma — vaqt taqsimoti aytmoqchi bo'lgan narsani ko'rsatadi
> Kreator **eng ko'p vaqtni tavsiya qiladigan tipga** beradi va **eng kam vaqtni pasaytiradigan tipga**:
> | Tip | Davomiylik | So'z | Isbot ekrani |
> |---|---|---|---|
> | 1 · Охватный (rad etiladi) | 9.26s | 28 | yo'q |
> | **2 · Экспертный (asosiy tavsiya)** | **15.30s** | **48** | **9.40s telefon** |
> | 3 · Личный | 11.06s | 36 | 3.46s telefon |
> | 4 · Продающий | **7.17s** | **20** | yo'q |
>
> Ya'ni **bo'limlar teng emas** — 15.30s vs 7.17s (2.1×). Ro'yxat "4 ta teng punkt" emas, **ierarxiya**.

> ### 🔑 Ikkinchi topilma — RE-HOOK 17.43s da
> 1-tipni "o'ldirgandan" keyin (*"у тебя нет шансов развить блог"*) darhol yangi va'da qo'yiladi:
> > "Но есть еще 3 типа контента, **которые тебя спасут**."
>
> Bu videoning **23%ida** joylashgan — ya'ni birinchi katta tashlab ketish nuqtasida. Loop qayta ochiladi. `DQ19FfMDfer` va `DS7rlXjja9c` da bunday o'rta-re-hook yo'q edi.

## 5. Uchta signature qurilma (bu formatning yuragi)

### ⭐ A. Katta yarim shaffof bo'lim hisoblagichi `N/4`

| Hisoblagich | Ko'rinish oynasi | Rangi | Bir vaqtda chiqadigan sariq matn |
|---|---|---|---|
| **1/4** | ~8.2 – 9.5s (**~1.3s**) | oq-shaffof | **ОХВАТНЫЙ** (9.2s) |
| **2/4** | ~20.4 – 22.0s (**~1.6s**) | **to'q kulrang-shaffof** | **ЭКСПЕРТНЫЙ** (21.8s) |
| **3/4** | ~35.9 – 37.0s (**~1.1s**) | oq-shaffof | **ЛИЧНЫЙ** (36.6s) |
| **4/4** | ~46.8 – 48.3s (**~1.5s**) | oq-shaffof | **ПРОДАЮЩИЙ** (48.0s) |

- **Joylashuv:** kadrning **pastki yarmi**, deyarli butun kenglik, balandligi kadrning ~35%i.
- **Qatlam tartibi:** videodan yuqorida, lekin **sarlavha matnidan pastda** — matn hisoblagich ustiga chiqadi.
- ⭐ **Rangi kontrastga moslashadi:** 2/4 to'q kulrang, chunki o'sha kadrda kreator **qora smoking**da — oq hisoblagich ko'rinmay qolardi. Boshqa uchtasi oq.
- ⭐ **Har doim bo'lim boshlanish kesimidan keyingi birinchi 0–1.5s ichida**, keyin butunlay yo'qoladi. Doimiy "progress bar" emas — **bir martalik zarba**.

### ⭐ B. Takrorlanuvchi flipchart SKORKARTA shabloni

Har bir tip uchun **aynan bir xil** qo'lda yozilgan shablon (qora marker, sarlavha tagi chizilgan, chapda mini-ekran/foto biriktirilgan):

```
┌──────────────────────────────┐
│  [mini-ekran /  N. Название  │
│   skrinshot]   ──────────    │
│                              │
│                ПРОСМОТРЫ: ↑/↓│
│                ПОДПИСКИ:  ↑/↓│
│                ПРОДАЖИ:   ↑/↓│
│                ДОВЕРИЕ:   ↑/↓│
└──────────────────────────────┘
```

| # | Doskadagi sarlavha | Vaqt | ПРОСМОТРЫ | ПОДПИСКИ | ПРОДАЖИ | ДОВЕРИЕ | Yashil |
|---|---|---|---|---|---|---|---|
| 1 | `1.Охватный` | 9.0–13.33s | 🟢↑ | 🔴↓ | 🔴↓ | 🔴↓ | **1/4** |
| 2 | `2.Экспертный` | 21.0–26.27s | 🔴↓ | 🟢↑ | 🟢↑ | 🟢↑ | **3/4** |
| 3 | `3.Личный` | 36.2–39.73s | 🟢↑ | 🔴↓ | 🔴↓ | 🟢↑ | **2/4** |
| 4 | `4.Продающий` | 47.0–53.90s | 🔴↓ | 🔴↓ | 🟢↑ | 🔴↓ | **1/4** |

- **4 ta o'q, 4 ta tip = 16 ta binar baho.** Butun freymvork bitta rasmda siqilgan.
- **Yashil o'q sanog'i 1 → 3 → 2 → 1** — 2-tip yutuvchi, va aynan unga eng ko'p vaqt berilgan (§4 ga qarang).
- **Mini-ekran har tipni jismonan isbotlaydi:** 1-tipda — kreatorning telefonga raqsga tushayotgan klipi; 2-tipda — 3 ta rils muqovasi (*«СМОТРЯТ 3 ТАКИХ СТАДИОНА»*), **25.10s da bitta muqovaga almashadi**; 3-tipda — selfi-storis (*«я соберу тебя со вкусом»*); 4-tipda — Instagram profil/DM skrinshoti, **~50.9s da «СПОСОБЫ» kadriga almashadi**.
- ⭐ **Grafik almashinuvi kesim o'rnini bosadi.** Kamera qimirlamaydi, faqat doskadagi rasm o'zgaradi — scene-detect buni "kesim" deb o'qiydi, lekin bu **montaj emas, animatsiya**.

### ⭐ C. Kostyum/prop almashishi = tip belgisi

| Tip | Vaqt | Kostyum / prop | Nimani anglatadi |
|---|---|---|---|
| — (hook, narrator) | 0.00–13.33 | **Bej kurtka + oq futbolka** | asosiy "muallif" holati |
| **1 · Охватный** | **13.33–20.37** | **Oq futbolka + qora shim, raqsga tushadi, oldida telefon o'zini suratga oladi** | "trend olish" — masxara |
| **2 · Экспертный** | **20.37–24.17** | **Qora smoking + oq ko'ylak + qora ko'zoynak + qo'lda chupa-chups** | "professor" |
| **3 · Личный** | **35.67–36.87** | Bej kurtka + **qo'lida qizchasi** | shaxsiy hayot |
| **4 · Продающий** | **63.00–71.10** | Bej kurtka + **doskaga yopishtirilgan 5000₽ banknot** | pul |

- ⭐ **Qoida: har bo'lim uchun aytilgan tushunchani jismonan gavdalantiruvchi bitta prop yoki kostyum.** Aytilmaydi — **ko'rsatiladi** (`DS7rlXjja9c` dagi "stikerlarni olib tashlash = fokus" bilan bir xil printsip).
- Kostyum almashishi **har doim bo'lim kesimi bilan bir vaqtda** (13.33 · 20.37 · 35.67).
- Bej kurtka **default** — hikoyachi rejimiga qaytish belgisi (39.73–43.27, 46.73–63.00, 71.10–75.14).

## 6. Jumla tuzilishi (raqamlar bilan)

- **Jumlalar:** 28
- **So'z uzunliklari, ketma-ket:**
  `[21, 5, 6, 10, 12, 9, 3, 5, 5, 12, 12, 11, 2, 8, 13, 13, 4, 9, 7, 4, 13, 12, 8, 13, 4, 9, 8, 5]`
- **Jami:** 243 so'z · **o'rtacha:** **8.68** · **mediana:** **8.5**
- **Eng uzun:** **21** so'z (1-jumla, hook) · **eng qisqa:** **2** so'z ("Третий, личный")
- **Hook'siz o'rtacha:** 222/27 = **8.22** — ya'ni hook o'rtachani sezilarli ko'taradi
- **Fragment (fe'lsiz to'liq bo'lmagan gap):** 5 ta — "Второй тип, экспертный" · "Третий, личный" · "И четвертый тип, продающий" · "И вот идеальный план" · "Прямо в одном ролике" = **17.9%**. Nominal "Первый, охватный, это тренды и юмор" ni qo'shsak — **21.4%**.
- **Buyruq gaplar:** **1 ta** ("попробуй") = **3.6%**. Va u **videoning eng oxirgi so'zi**.

### ⭐ Har bir tip uchun QAT'IY 3-beat mikro-shabloni

| Beat | Shakl | Tip 1 | Tip 2 | Tip 3 | Tip 4 |
|---|---|---|---|---|---|
| **(a) NOM** | tartib son + [тип] + nomi · **2–4 so'z** | "Первый, охватный" | "Второй тип, экспертный." | "Третий, личный" | "И четвертый тип, продающий" |
| **(b) TA'RIF** | 1-shaxs ko'plik fe'l · **5–9 so'z** | *(yo'q — "это тренды и юмор")* | "Делимся полезной информацией или обучаем." | "Делимся историями из жизни и раскрываемся как человек" | "Рассказываем о своем продукте и получаем заявки с продажами" |
| **(c) NATIJA** | "Он дает…" / "Набирает…" · **5–13 so'z** | "Тут много просмотров, но он не дает подписчиков и денег." | "Он дает больше всего подписчиков." | "Это нужно, чтобы люди долго оставались в блоге и держались в высокий охват" | "Набирает меньше всего просмотров, но приносит деньги" |
| **(d) ISBOT** | real ekran + raqam | — | 3 ta rils (500к/5000, 1,8 млн/20 тыс, 3 млн/17 тыс) | storis (под 100 тысяч) | — |

⭐ **1-tip qasddan shablondan chiqariladi:** unda "мы"-fe'l yo'q ("это тренды и юмор" — nominal). Ya'ni **«делимся / рассказываем» faqat QILISH KERAK bo'lgan tiplarga beriladi.** Rad etilgan tip grammatik jihatdan ham "biz"dan chiqarib tashlanadi.

### ⭐ Aynalgan juftlik — 1-tip va 4-tip bir xil qolipda, teskari mazmun bilan

> 10.36s — "Тут **много просмотров**, **но** он не дает подписчиков и **денег**."
> 51.02s — "Набирает **меньше всего просмотров**, **но** приносит **деньги**."

Bir xil `X, но Y` konstruksiyasi, bir xil leksika (просмотры / деньги), teskari qutb. Bu freymvorkni **ramkaga oladi** — birinchi va oxirgi tip bir-birining oynasi.

### ⭐ "Я бы …" — maslahat shaxsiy tanlov qilib berilgan

54.54–62.88s da uchta ketma-ket shart maylidagi jumla:
> "**Я бы не вел** сторис, пока не наберу хотя бы 5 тысяч подписчиков"
> "Чтобы их набрать, **я бы снимал** по 10-15 хороших релсов в месяц"
> "И **снимал бы** их вот в такой пропорции"

**3× «бы» 8.3 soniyada.** "Sen shunday qil" emas — "men bo'lganimda shunday qilardim". Buyruqni yumshatadi, lekin aynan reja beradi.

### Murojaat — 5 marta almashadi

| Blok | Vaqt | Shaxs | Dalil |
|---|---|---|---|
| Hook | 0.00–6.64 | **я → вам** | "**Я** потратил… рассказать **вам**" |
| Tip 1 ogohlantirish | 13.32–20.28 | **ты** | "если **ты** пытаешься… у **тебя** нет шансов… **тебя** спасут" |
| Tip 2–4 ta'riflar | 21.88–51.02 | **мы** | "**Делимся**… **раскрываемся**… **Рассказываем**… **получаем**" |
| Shaxsiy isbot | 43.12–46.52 | **я** | "**Я** делаю много личного контента… **мои** сторис" |
| Ideal reja | 54.54–62.88 | **я бы** (shart) | "**Я бы** не вел… **я бы** снимал" |
| Sintez | 62.88–67.06 | **вы** | "**вы** можете объединять" |
| Yakun | 73.20–75.06 | **ты** (buyruq) | "**попробуй**" |

⭐ **Naqsh: `я → вам → ты → мы → я → вы → ты`.** `DQ19FfMDfer` (я→ты) va `DS7rlXjja9c` (я→ты→мы) dan farqli — bu yerda **«мы» o'rtada**, ta'riflar uchun ishlatiladi, «вы»/«ты» esa boshi va oxirida. Ya'ni: **ta'rif — "biz", tanbeh va chaqiriq — "sen", isbot — "men"**.

### Bo'lim ochuvchi markerlar
| Marker | Uchrashi |
|---|---|
| Tartib son + nom | 4× (8.10 · 20.36 · 35.58 · 46.52) |
| "**И вот…**" | 1× (53.76 — "И вот идеальный план") — `DQ19FfMDfer` dagi bilan bir xil marker |
| "**Но…**" (burilish) | 3× (10.36 ichida · 17.42 re-hook · 51.02) |
| "**А на этом / А этот…**" | 2× (29.58 · 32.24) — isbot zanjirini davom ettiradi |
| "**Чтобы…**" (maqsad) | 4× (0.00 ichida · 39.52 · 57.18 · 62.88) |
| "**И тогда…**" | 1× (68.34 — natija) |

### Raqam siyosati
14 ta aniq raqam 75s da = **har 5.4s da bitta**:
`7 лет · 60 секунд · 4 типа · 3 типа · 500 тысяч · 5000 · 1,8 миллионов · 20 тысяч · 3 миллиона · 17 тысяч · 100 тысяч · 5 тысяч · 10-15 · миллион`

⭐ **Isbot zanjiri o'sib boradi:** `500 тысяч → 1,8 миллионов → 3 миллиона` (ko'rish) va `5000 → 20 тысяч → 17 тысяч` (obuna). Ko'rish monoton o'sadi, obuna **oxirida tushadi** — bu qasddan: "ko'rish ≠ obuna" degan asosiy tezisni raqam bilan tasdiqlaydi.

### Filler siyosati
**Nol.** "ну", "как бы", "то есть", "вот это самое" — yo'q. Yagona og'zaki g'adir-budurlik: **"релсе / рилсе / рилс"** so'zining uch xil talaffuzi (26.26 · 29.58 · 32.24 · 57.18) va **"держались в высокий охват"** buzuq boshqaruvi (39.52). **Bular tuzatilmaydi — jonli nutq belgisi.**

### Ko'chirib olinadigan 5 ta jumla qolipi
1. `"Я потратил <KATTA VAQT> для того, чтобы сейчас за <KICHIK VAQT> рассказать вам, как <NATIJA>."`
2. `"Всего есть <N> типа <NARSA>."`
3. `"<Tartib son> тип, <nom>. Делимся/Рассказываем <nima>. Он дает <natija>."`
4. `"Тут много <A>, но он не дает <B>."` ↔ `"Набирает меньше всего <A>, но приносит <B>."`
5. `"Я бы не <X>, пока не <Y>."` / `"Чтобы <Y>, я бы <Z>."`

## 7. Montaj barmoq izi

- **Kesim tezligi:** o'rtacha **3.13s**, mediana **2.90s**, min **1.10s**, maks **8.10s**
- ⭐ **Eng TEZ blok — payoff emas, ISBOT:** 26.27–32.50s (2-tipning rils isboti) — 4 kesim 6.23s ichida = **1.56s/kadr**. Hook (2 kadr / 6.73s = 3.37s) undan **2.2× sekinroq**.
- ⭐ **Eng SEKIN blok — 53.90–71.10s** (idealniy plan + formula): 17.2s da atigi 3 kadr = **5.73s/kadr**. Ya'ni **freymvorkning yechimi sekinlashadi** — tomoshabinga o'qishga vaqt beriladi. Bu `DQ19FfMDfer`/`DS7rlXjja9c` dagi "payoffda tezlashadi" qoidasining **teskarisi**.

### ⭐ Montaj gapga bo'ysunadi, musiqaga emas — o'lchangan
23 ta kesimdan **19 tasi (83%)** jumla chegarasiga ±0.25s aniqlikda tushadi. Faqat 4 ta istisno: **2.47s** (hook ichidagi jump-cut) va **27.90 / 30.73 / 32.50** (rils isboti montaji — bu yerda kesim **har bir raqamga** tushadi, gapga emas).

### Shot turlari ulushi (davomiylik bo'yicha)
| Tur | Soniya | % |
|---|---|---|
| Doska yaqin plani (grafika) | 23.56s | **31.4%** |
| Talking-head (doskasiz) | 18.69s | **24.9%** |
| Odam + doska (o'rta/keng) | 15.93s | **21.2%** |
| Telefon ekrani (isbot) | 12.86s | **17.1%** |
| Kostyum b-roll (trend raqsi) | 4.10s | **5.5%** |

- **Doska (yaqin + o'rta) = 39.49s = 52.6%** — ya'ni videoning yarmidan ko'pi **flipchart**. Doska formatning o'zi.
- **Hujjatlashtirilgan isbot** (telefon 12.86 + hook skrinshotlari ~1.7 + finaldagi o'quvchi kartochkalari 4.04) = **~18.6s = 24.8%**. Har to'rtinchi soniya — isbot.

### O'tishlar va kamera
- **Hammasi hard cut.** Whip, dissolve, match-cut — **yo'q** (0 ta).
- **Zoom/punch-in:** **1 marta** — hook'da 0.0→1.2s, raqamli push-in (bel-plan → yuz). Boshqa joyda yo'q.
- **Kamera:** doska sahnalarida qat'iy statik shtativ; talking-head'da qo'lda, keng burchak (shift buzilishi shipda ko'rinadi).
- **Yorug'lik/look:** tabiiy deraza yorug'ligi, iliq-neytral, kontrast past, grain yo'q, toza. Bir xil kvartira (jigar parda, oq deraza) butun video davomida.

### Ekran matni tizimi
```
┌─────────────────────────────┐
│   KATTA OQ / SARIQ          │  ← faqat HOOK'da (0–4.5s), YUQORI zona
│                             │
│         [kadr]              │
│                             │
│   kichik oq  yoki           │  ← 5s dan keyin FAQAT markaz/past-markaz
│   KATTA OQ + SARIQ          │
└─────────────────────────────┘
```
- **Shrift:** qalin siqilgan sans, yengil soya. Urg'uli so'zlar **BOSH HARF**, bog'lovchilar **kichik harf**.
- **Ranglar:** oq (bog'lovchi/kontekst) + **sariq** (payload). Uchinchi rang yo'q.
- **Sariq nimaga beriladi:** (a) raqamlar (`7 ЛЕТ`, `3 ТИПА`, `5 ТЫСЯЧ`, `20 ТЫСЯЧ`, `17 ТЫСЯЧ`), (b) **4 ta tip nomi** (`ОХВАТНЫЙ`, `ЭКСПЕРТНЫЙ`, `ЛИЧНЫЙ`, `ПРОДАЮЩИЙ`), (c) yakun zarbalari (`РАБОТАЕТ`, `ПОПРОБУЙ`). Bog'lovchiga **hech qachon** berilmaydi. ~24 sariq kartochka / ~88 holat = **27%**.
- **Kartochka hajmi:** **1–4 so'z**, o'rtacha **1.74 so'z**.
- **Almashish tezligi:** kamida **88 ta matn holati** 75.14s da = **har ~0.85s da yangi holat**. (1 soniyalik kontakt-varaq bo'yicha sanaldi; oraliqdagilari qo'shimcha kadrlardan topildi — masalan `500 тысяч` 26.9s, `личного` 44.3s, `С ПРОДАЖАМИ` 50.7s. Real son ~90–100.)
- **Ikki zona bir vaqtda:** faqat **1.5–2.2s** oralig'ida (yuqorida `Я ПОТРАТИЛ / 7 ЛЕТ`, pastda `для того` → `чтобы сейчас`). Undan keyin hech qachon.

### ⭐ Matn SUBTITR-mi yoki QISQARTMA-mi? — o'lchangan
**Bu videoda — QISQARTILGAN SUBTITR (yaqin-subtitr), `DQ19FfMDfer`/`DS7rlXjja9c` dagi sof qisqartmadan farq qiladi.**

| Jumla | Aytilgan so'z | Ekranda so'z | Qamrov |
|---|---|---|---|
| #1 (hook) | 21 | 19 (faqat "который" tushib qolgan) | **90%** |
| #10 ("На этом релсе 500 тысяч…") | 12 | 12 | **100%** |
| #15 ("Это нужно, чтобы люди…") | 13 | 9 ("долго", "в высокий охват" tushgan) | 69% |
| #22 ("Чтобы их набрать…") | 12 | 8 | 67% |
| #24 ("Чтобы делать большие продажи…") | 13 | 6 | **46%** |

**Umumiy: ~153 ekran so'zi / 243 aytilgan so'z = 63%.**
⭐ **Qoida shundan chiqadi: raqam va isbot jumlalari 100% subtitr qilinadi; tushuntirish jumlalari 50–70% gacha qisqartiriladi.** Ya'ni **raqam hech qachon ekrandan tushmaydi**.

### ⭐ Progressiv yig'ilish — TASDIQLANDI, 3 qatorgacha
Matn ekranda so'zma-so'z **o'sib boradi**, avvalgi qator o'chmaydi:
- `Я ПОТРАТИЛ` → `+ 7 ЛЕТ` → `+ для того` → `+ чтобы сейчас` (4 bosqich, 0.0–2.2s)
- `ЗА 60 СЕКУНД` → `+ РАССКАЗАТЬ ВАМ`
- `КАК ДЕЛАТЬ` → `+ КОНТЕНТ`
- `ТУТ МНОГО` → `+ ПРОСМОТРОВ`
- `У ТЕБЯ` → `+ НЕТ ШАНСОВ`
- `ДЕЛИМСЯ` → `+ ПОЛЕЗНОЙ`
- `И РАСКРЫВАЕМСЯ` → `+ КАК ЧЕЛОВЕК`
- `ОСТАВАЛИСЬ` → `+ В БЛОГЕ`
- `ПРИНЕС` → `+ 20 ТЫСЯЧ`
- `17 ТЫСЯЧ` → `+ ПОДПИСЧИКОВ`
- `И ПОЛУЧАЕМ` → `+ ЗАЯВКИ` → `+ С ПРОДАЖАМИ` ← **yagona 3 qatorli yig'ilish, 49.5–51.0s**
- `ХОРОШИХ` → `+ РИЛСОВ`
- `ТАК ЧТО ЭТО` → `+ РАБОТАЕТ`

**Naqsh: 1-qator oq (kontekst) → 2-qator sariq (payload).** Maksimum 3 qator; keyin butunlay tozalanadi.

## 8. Audio

- **VO doimiy va pauzasiz:** o'lik havo jami **0.72s = 0.96%**. 26.26s dan keyin jumlalar orasida umuman pauza yo'q.
- **Fon qatlami bor:** pauzalarda RMS **−27.3 dB** (peak −16.3 dB), nutq paytida RMS **−13.0…−13.7 dB**. Ya'ni ost qatlam nutqdan **~14 dB past**, lekin sukut emas. Oxirgi 0.08s da RMS −31.2 dB.
- **Bu musiqami yoki xona shovqinimi — kadrlardan aniqlab bo'lmaydi:** `[noaniq]`.
- **Beat-sync yo'q:** kesimlarning 83%i **jumla chegarasiga** tushadi (§7), musiqa zarbiga emas.
- **Sound effect (whoosh / pop / riser) — kadrlar bo'yicha aniqlab bo'lmaydi:** `[noaniq]`.
- **Sukut/pauza dramatik qurilma sifatida ishlatilmaydi** — eng uzun pauza 0.12s.

## 9. Yakun va loop yopilishi

```
71.10–75.14s  6 ta Instagram profil kartochkasi = 3 juft "oldin → keyin"
```

| Juft | OLDIN | KEYIN | O'sish |
|---|---|---|---|
| 1 | `Станислав` — 4 публикации · **138 подписчики** · 4 подписки (71.1–71.9) | `ozonseller77` — Станислав \| Селлер на озон \| Маркетплейсы — 81 публикации · **15,8 тыс. подписчики** (72.0–72.4) | ×114 |
| 2 | `Женя \| Репетитор по английскому · разговорный · онлайн` — 34 posts · **128 followers** (72.5–73.1) | `evgeshark` — Женя \| Репетитор по английскому — 32 публикации · **11 тыс. подписчики** (73.2–73.8) | ×86 |
| 3 | `✨ Katya \| motivation & discipline ✨` — 26 публикации · **46 подписчики** (73.9–74.4) | `ekateriina_kruz` — Катя kruz. Саморазвитие & Мышление — 31 публикации · **5 004 подписчики** (74.5–75.14) | ×109 |

- **Kartochka almashish tezligi:** 6 kartochka / 4.04s = **~0.67s har biriga**. Kadr o'zi bitta (71.10 dan keyin kesim yo'q) — faqat overleylar almashadi.
- **Yakun turi:** **isbot + yumshoq buyruq.** Oxirgi jumla: *"Так что это работает, попробуй"* (5 so'z), oxirgi ekran so'zi — **sariq `ПОПРОБУЙ`**.

### CTA bormi?
⛔ **Klassik CTA YO'Q.** "Подпишись", "сохрани", "напиши в комментах", "пиши слово в директ" — **hech biri yo'q**. Videodagi yagona buyruq — oxirgi so'z **"попробуй"**, va u mahsulotga emas, **usulga** qaratilgan. Bu korpusning uchinchi tasdig'i: **bu kreator CTA bilan tugatmaydi.**

### Hook detallari finalda qaytadimi?
⚠️ **Qisman — va bu `DS7rlXjja9c` dan farq qiladi.**

| Hook detali | Finalda qaytadimi |
|---|---|
| **«7 лет»** | ❌ Yo'q. Boshqa hech qayerda eslanmaydi. |
| **«за 60 секунд»** | ❌ Yo'q — video 75.14s (va'dadan 25% uzun), lekin bu tan olinmaydi. |
| **«подписки и продажи»** | ✅ **Ha, strukturaviy:** `ПОДПИСКИ` va `ПРОДАЖИ` — 4 ta skorkartaning 4 qatoridan 2 tasi; 63–71s dagi formula aynan shu ikkisini birlashtiradi. |
| **Hook'dagi isbot skrinshotlari** (19,422 подписки · 8376 платных заказов) | ✅ **Ha, oynali:** 71–75s da **o'quvchilarning** obunachi raqamlari bilan qaytadi — "menda ishlaydi" → "ularda ham ishlaydi". |

⭐ **Ya'ni bu videoda callback RAQAMLI emas, KONSEPTUAL.** Hook'dagi aniq sonlar (7 yil, 60 soniya) yopilmaydi — faqat va'da qilingan **natija turlari** (подписки/продажи) va **isbot janri** (skrinshot) yopiladi.

## 10. ✅ Ko'chiriladigan qoidalar

1. **Hook'ni VAQT SAVDOSI qilib qur:** `"Я потратил <KATTA VAQT>, чтобы за <KICHIK VAQT> рассказать, как <NATIJA>"`. Nisbat qanchalik keskin bo'lsa, shunchalik yaxshi (bu yerda 7 yil ↔ 60 soniya).
2. **Hook jumlasi uzun bo'lishi mumkin (21 so'z), lekin ekranda 1–2 so'zli 8 ta kartochkaga bo'linadi.** Quloq uzun eshitadi, ko'z qisqa o'qiydi.
3. **Da'voni birinchi 7 soniyada skrinshot bilan hujjatlashtir** (5.0–6.7s). Raqamli isbot hook ichida bo'lsin, keyin emas.
4. **Ro'yxat sonini darhol e'lon qil:** "Всего есть 4 типа контента" — hook'dan keyingi 1.44 soniya, 5 so'z.
5. **Har bo'lim boshida katta yarim shaffof `N/4` hisoblagichini 1–1.5 soniyaga chiqar** va u bilan bir vaqtda **tip nomini SARIQ bosh harfda** ber. Hisoblagich doimiy turmasin.
6. **Bir xil o'lchov shablonini har bo'limda takrorla** (bu yerda: ПРОСМОТРЫ / ПОДПИСКИ / ПРОДАЖИ / ДОВЕРИЕ + yashil↑/qizil↓). Bir xil 4 mezon × N variant = butun freymvork bitta rasmda.
7. **Har bo'limga aytilgan tushunchani gavdalantiruvchi bitta kostyum yoki prop ber** (trend → raqs + oq futbolka; ekspert → smoking + ko'zoynak; shaxsiy → bola qo'lda; sotuv → banknot doskada). Aytma — kiyib chiq.
8. **Bo'lim mikro-shabloni: NOM (2–4 so'z) → TA'RIF ("Делимся/Рассказываем…", 5–9 so'z) → NATIJA ("Он дает…", 5–13 so'z) → ISBOT (ixtiyoriy).**
9. **Rad etadigan variantni grammatik jihatdan "biz"dan chiqarib tashla** — unga "делимся" bermay, "это тренды и юмор" deb nominal ta'rifla.
10. **Birinchi va oxirgi bandni bir xil qolipda, teskari mazmun bilan yoz:** `"Много X, но не дает Y"` ↔ `"Меньше всего X, но приносит Y"`. Freymvork ramkaga olinadi.
11. **Videoning ~23%ida RE-HOOK qo'y:** birinchi bandni "o'ldirgandan" keyin darhol `"Но есть еще <N-1> …, которые тебя спасут"`.
12. **Bo'limlarga TENG vaqt berma.** Tavsiya qiladiganingga 2× ko'proq vaqt va butun isbot montajini ber (bu yerda 15.3s vs 7.2s).
13. **Isbot montajini eng tez blok qil (1.5–1.6s/kadr), yechim blokini eng sekin (5–8s/kadr).** Tezlik isbotga, sokinlik xulosaga.
14. **Kesimlarni jumla chegarasiga tushir (83%),** faqat raqamlar sanalayotgan isbot montajida — har raqamga.
15. **Isbot raqamlarini o'suvchi zanjir qilib ber, lekin ikkinchi ustunni monoton qilma:** ko'rish 500к → 1,8 млн → 3 млн, obuna 5000 → 20 тыс → 17 тыс. Tushish tezisni isbotlaydi.
16. **Maslahatni "Я бы…" shart maylida ber** ("Я бы не вел сторис, пока не наберу…"). Buyruqdan yumshoq, tavsiyadan aniqroq.
17. **Shaxsni bosqichma-bosqich almashtir: я → вам → ты → мы → я → вы → ты.** Ta'rif — "biz", tanbeh — "sen", isbot — "men".
18. **Ekran matni — qisqartilgan subtitr, 60–70% qamrov. Lekin raqamli jumlalarni 100% subtitr qil.** Raqam hech qachon ekrandan tushmaydi.
19. **Matnni progressiv yig': 1-qator oq (kontekst) → 2-qator SARIQ (payload). Maksimum 3 qator, keyin tozala.** Har ~0.85s da yangi holat.
20. **Sariqni faqat uch narsaga ber:** raqamlar, bo'lim nomlari, yakun zarbasi. Bog'lovchiga hech qachon.
21. **Grafik almashinuvini kesim o'rniga ishlat:** kamera qotgan, doskadagi mini-skrinshot almashadi (25.1s, 50.9s). Bepul "kesim" hissi.
22. **Finalni o'quvchilarning "oldin→keyin" juftliklari bilan yop** — 3 juft, har kartochka ~0.67s, bitta kadr ichida overley sifatida.
23. **CTA bilan tugatma.** Yagona buyruq — usulga qaratilgan bitta so'z (`попробуй`), va u videoning eng oxirgi so'zi bo'lsin.
24. **Fillerni nolga tushir, lekin og'zaki g'adir-budurlikni tuzatma** ("релсе/рилсе/рилс", "держались в высокий охват") — u jonlilik beradi.

## 11. ❌ Ko'chirilmaydigan (bu videoga xos, bir martalik)

1. **Aniq shaxsiy raqamlar** — 19,422 подписки, 8376 платных заказов на 123 780 730 руб., 500к/1,8 млн/3 млн ko'rishlar. Faqat haqiqiy bo'lsa. **To'qib chiqarilmasin.**
2. **O'quvchilarning haqiqiy akkauntlari va raqamlari** (`ozonseller77` 15,8 тыс., `evgeshark` 11 тыс., `ekateriina_kruz` 5 004) — bu real odamlar; ruxsatsiz va tekshirilmagan holda ishlatilmaydi.
3. **Qizchani kadrga olib chiqish** — "личный контент" tipini ko'rsatishning eng kuchli usuli, lekin u kreatorning shaxsiy hayotiga bog'liq. Har brend uchun mos emas.
4. **Qora smoking + ko'zoynak + chupa-chups** — aynan "экспертный" so'ziga bog'langan vizual hazil. Boshqa freymvorkda boshqa prop kerak.
5. **50% / 30% / 20% proporsiyasi va "10-15 Reels/мес"** — bu kreatorning o'z ish rejimi, universal me'yor emas.
6. **«за 60 секунд» deb va'da qilib 75.14s olish** — bu videoda jazosiz o'tgan, lekin qoida sifatida ko'chirilmaydi. Va'da qilingan vaqtga rioya qil yoki umuman vaqt aytma.
7. **Trend-raqsni masxara qilish sahnasi (13.33–17.43s)** — kreatorning pozitsiyasiga bog'liq. Trendlarni tavsiya qiladigan brendda teskari ishlaydi.
