# Teardown: `DUxbSgyDTck.mp4`

## 1. Meta
| | |
|---|---|
| Davomiylik | **71.07s** |
| O'lcham | 1080×1920 · 9:16 · 30fps |
| Kesimlar (ko'z bilan, contact sheet) | **~37 kadr** · o'rtacha **1.92s** |
| Scene-detect raqami (yordamchi) | @0.25 → 52 "hodisa" · avg 1.26s — **noto'g'ri** (pastga qarang) |
| Haqiqiy o'tish soni | **36** (12 ta oq flash + 24 ta hard cut) |
| Eng qisqa kadr | **0.56s** (55.17–55.73 — erkak→ayol almashuvi) |
| Eng uzun kadr | **6.60s** (43.73–50.33 — quti xonasi) |
| Arxetip | **Tutorial (4 qadam)** × "noldan qayta boshlash" freymi → **Reality-teaser payoff + keyword CTA** |
| Ovoz | VO (kreator o'zi), 220 so'z / 70.8s = **3.11 so'z/s** · fon musiqa `[noaniq]` |
| Produksiya rejimi | **Gibrid: AI-kartun hook (0–6.5s) → jonli s'yomka + arxiv + oq doska + AI-fotoreal ayol avatar** |

> ### ⚠️ Scene-detect raqami nega yaroqsiz
> `analysis.json` @0.25 da 52 ta hodisa beradi (avg 1.26s). Lekin ulardan **12 tasi 3–4 kadrlik klasterlar** (masalan `6.47 / 6.50 / 6.57` yoki `60.47 / 60.50 / 60.53 / 60.57`) — bu bitta **oq flash o'tishi**, uch marta sanalgan.
> Teskari tomondan: **50.43–55.17 oralig'ida detektor 0 ta kesim topgan**, contact sheet esa 50s / 51s / 52s / 53s da **to'rt xil fon** ko'rsatadi (ko'k divan → koridor+javon → keng plan → qizil kreslo) — ya'ni kamida **3 ta kesim o'tkazib yuborilgan**.
> Ko'z bilan sanalgan haqiqiy raqam: **~37 kadr, o'rtacha 1.92s**.

## 2. So'zma-so'z transkript (vaqt belgilari bilan)
> Verbatim, whisper. `[✎]` = ekrandagi yozuv bo'yicha tuzatilgan.

```
 0.00– 6.20  Если бы у меня в кармане осталось 1000 рублей, я лишился бы блога, оказался в общаге, в теле девушки
 6.20–10.82  То вот что я бы делал, чтобы съехать с общаги и начать получать деньги онлайн
10.82–18.24  Первое, я бы точно завел свой блог, потому что именно благодаря блогу у меня уже получилось пройти путь от хостела до вот такого дома
18.24–20.62  Дальше я бы выбрал две основные темы для блога
20.62–25.30  Первое, мое дело, я бы показывал, чем могу быть полезен людям и какие услуги у меня можно купить
25.30–29.52  А вторая тема, моя жизнь, я бы показывал свой путь, даже если не все идеально
29.52–33.16  Как я съезжаю с общаги, ищу отношения и исполняю мечты
33.16–35.24  Это принесет лояльных подписчиков
35.24–39.76  Третье, я бы не вкладывал деньги в рекламу, а делал по 15-20 релсов в месяц
39.76–43.64  И чтобы набрать первую тысячу подписчиков, мне бы хватило около 10 релсов
43.64–47.98  И, наконец, когда есть тысяча подписчиков, можно начать сотрудничать с брендами по бартеру
47.98–50.24  И стабильно получать клиентов с блога
50.24–54.52  На словах всегда все звучит красиво, но я решил показать на деле и провести эксперимент
       ⟨0.50s PAUZA — butun videodagi yagona⟩
55.02–58.20  Я стану девушкой на 30 дней, заведу[✎ whisper: «загаду»] блог с нуля
58.20–60.18  И пройду каждый шаг из этого видео
60.18–64.30  От нуля подписчиков до первого бартера и первых денег
64.30–66.24  А чтобы получить первую серию реалити
66.24–68.56  И посмотреть, как я создал свою женскую версию
68.56–70.82  Пиши слово «Аватар» в комментарии
```

**Sanoq izchilligi buzilgan (verbatim saqlandi):** og'zaki "Первое" **ikki marta** ishlatiladi — 10.82 da (1-qadam) va 20.62 da (2-qadamning ichidagi 1-mavzu). "Второе" umuman yo'q — o'rniga "Дальше". Bu chalkashlikni **ekrandagi raqamlar tuzatadi**: `1/4`, `2/4`, `3/4`.

## 3. Hook teardown (0–6.5s) — eng muhim blok

`hook/` (0.5s qadam) + contact sheet bo'yicha, frame-by-frame:

| Vaqt | Ekranda nima | Aytilgan so'z | Ekran matni |
|---|---|---|---|
| 0.0s | **AI-kartun**: yigit stulda, oldida tripodda telefon; devor yorilib, pul va parchalar uchmoqda | "Если бы…" | **ЕСЛИ БЫ** (oq, katta) |
| 0.5s | Sama kadr, parchalar yuzini yopib o'tadi | "…у меня в кармане…" | ЕСЛИ БЫ / У МЕНЯ **В КАРМАНЕ** (sariq) |
| 1.0s | Xona butun, tepada 1000 rublik kupyura suzib turibdi | "…осталось…" | **ОСТАЛАСЬ** (oq) |
| 1.5s | Kupyura yaqinlashadi | "…1000 рублей…" | **1 000 РУБЛЕЙ** (sariq) |
| 2.0s | Sama | (pauza) | 1 000 РУБЛЕЙ (sariq) |
| 2.5s | Punch-in: tripod kadr markazida, plan yaqinroq | "я лишился бы…" | **Я ЛИШИЛСЯ БЫ** (oq) |
| 3.0s | Yanada yaqin, tripod pastga tushgan | (davomi) | Я ЛИШИЛСЯ БЫ (oq) |
| 3.5s | Tripod umuman yo'q — "blogdan mahrum bo'ldi" vizual | "…блога…" | Я ЛИШИЛСЯ БЫ / **БЛОГА** (sariq) |
| 4.0s | **ECU: kaft ob'ektivni yopadi** (eski xona hali orqada) | "…оказался…" | **ОКАЗАЛСЯ** (oq) |
| 4.5s | Kaft ochiladi — **boshqa xona**: iflos, mog'orlagan oshxona | "…в общаге…" | ОКАЗАЛСЯ / **В ОБЩАГЕ** (sariq) |
| 5.0s | Erkak o'sha stulda, iflos oshxonada | "…в теле…" | **В ТЕЛЕ ДЕВУШКИ** (sariq) |
| 5.5s | **Aynan shu kadrda erkak ayolga aylanadi** (uzun soch, gulli ko'ylak) | "…девушки" | В ТЕЛЕ ДЕВУШКИ (sariq) |
| 6.5s | Oq flash → jonli s'yomkaga o'tish | "То вот что…" | (flash) |

- **Pattern interrupt nima:** **format**. Birinchi 6.5 soniya butunlay **AI-illyustratsiya (kartun)** — lentadagi hech bir boshqa video bunday ko'rinmaydi. Vizual zarba emas, **rendering uslubining o'zi** to'xtatadi.
- **Birinchi aytilgan jumla, so'zma-so'z:** *"Если бы у меня в кармане осталось 1000 рублей, я лишился бы блога, оказался в общаге, в теле девушки"* → **19 so'z**
  Ammo bu jumla **6.20 soniya davom etadi** va grammatik jihatdan tugallanmagan — "то" bo'lagi 6.20 da keladi. To'liq shart gap = **34 so'z / 10.82s**.
- **Hook'ning ichki tuzilishi — 4 zarbali eskalatsiya:**
  1. shart + raqam → `1000 рублей`
  2. yo'qotish 1 → `блога`
  3. yo'qotish 2 → `в общаге`
  4. yo'qotish 3 (absurd) → `в теле девушки` ← eng kutilmagani oxirida
  Har zarba ~1.5s. Uchinchi yo'qotish **mantiqan kerak emas** — u faqat "bu nima ekan?" degan savol uchun qo'yilgan.
- **Ochilgan loop:** *nega aynan "в теле девушки"? Bu qanday qilib bo'ladi?* — bu **55.02 gacha**, ya'ni videoning **77%igacha** yopilmaydi.
- **Va'da:** 6.20–10.82 — *"То вот что я бы делал, чтобы съехать с общаги и начать получать деньги онлайн"*
- **Mute'da ishlaydimi:** ✅ **ha, 95%**. Hook'da aytilgan 19 so'zdan **18 tasi ekranda ham bor**. Bu videoning yagona joyi bunday zich — qolgan qismida ekran matni 53–60% ga tushadi (5-bo'limga qarang).

## 4. Struktura — spine

```
 0.00– 6.20s  HOOK          "Если бы… 1000 рублей" → 3 ta yo'qotish, oxirgisi absurd
 6.20–10.82s  STAVKA/VA'DA  "То вот что я бы делал, чтобы съехать с общаги…"
10.82–18.24s  QADAM 1  1/4  завести блог  + isbot: ОТ ХОСТЕЛА → ДО ВОТ ТАКОГО
18.24–35.24s  QADAM 2  2/4  две темы: (а) мое дело  (б) моя жизнь
35.24–43.64s  QADAM 3  3/4  не реклама, а 15-20 рилсов; 1000 подписчиков ≈ 10 рилсов
43.64–50.24s  QADAM 4  [4/4 `[noaniq]`]  бартер → клиенты
50.24–55.02s  KO'PRIK       "На словах всегда все звучит красиво, но я решил показать на деле"
       ⟨0.50s SUKUT⟩
55.02–64.30s  PAYOFF        "Я стану девушкой на 30 дней" → LOOP YOPILADI
64.30–70.82s  CTA           "Пиши слово «Аватар» в комментарии"
```

> ### 🔑 Eng muhim topilma — **gipoteza → real eksperiment burilishi**
> Birinchi **50.24 soniya butunlay shart maylida**: "я **бы** завел", "я **бы** выбрал", "я **бы** показывал", "мне **бы** хватило" — **9 marta «бы»**.
> 50.24 da bitta jumla butun videoni ag'daradi: *"На словах всегда все звучит красиво, **но я решил показать на деле** и провести эксперимент"*.
> Shundan keyin fe'llar **real kelasi zamonga** o'tadi: "Я **стану**", "**заведу**", "**пройду**".
> Ya'ni: **maslahat berilmaydi — maslahatni bajarish va'da qilinadi.** Kontent seriyaga aylanadi, CTA esa keyingi seriyani sotadi.

> ### 🔑 Ikkinchi topilma — **raqamli callback: 1000 рублей → 1000 подписчиков**
> Hook'da: `1 000 РУБЛЕЙ` (sariq, katta, markaz — 1.5–2.5s)
> 45-soniyada: `1000` (katta oq) / `ПОДПИСЧИКОВ` (sariq) — **aynan o'sha tipografik qolip**.
> Yo'qotilgan 1000 rubl → orttiriladigan 1000 obunachi. Raqam o'zgarmaydi, birligi o'zgaradi.

### Hook detallarining yopilishi (hammasi tekshirildi)
| Hook'da aytilgan | Qayerda qaytadi | Yopildimi |
|---|---|---|
| `1000 рублей` | 39.76 "первую тысячу подписчиков" · 43.64 "тысяча подписчиков" · ekranda `1000` (45s) | ✅ raqam qayta ishlatilgan |
| `блога` | 10.82 "я бы точно завел свой блог" · 47.98 "клиентов с блога" · 55.02 "заведу блог с нуля" | ✅ 3× |
| `в общаге` | 6.20 "чтобы съехать с общаги" · 29.52 "Как я съезжаю с общаги" · vizual: 16s va 30s da xostel arxivi | ✅ 2× og'zaki + 2× vizual |
| `в теле девушки` | 55.02 "Я стану девушкой на 30 дней" · 66.24 "как я создал свою женскую версию" | ✅ oxirgi 16 soniyada |

**Qoida:** hook'da nomlangan **4 ta konkret detalning 4 tasi ham** finalda yopiladi. Bittasi ham osilib qolmaydi.

## 5. Jumla tuzilishi (raqamlar bilan)

- **Nutq birliklari (whisper segmentlari):** 19
- **So'z sanog'i ketma-ket:** `[19, 15, 24, 9, 18, 15, 10, 4, 15, 12, 13, 6, 15, 10, 7, 9, 6, 8, 5]`
- **Jami:** 220 so'z (analysis.json: 221) · **O'rtacha:** 11.6 · **Mediana:** 10
- **Eng uzun:** 24 so'z (10.82–18.24, 1-qadam) · **eng qisqa:** 4 so'z (*"Это принесет лояльных подписчиков"*)
- **Nutq tezligi:** 3.11 so'z/s ≈ 186 so'z/min — **butun video davomida deyarli o'zgarmaydi** (hook 3.06 · tana 3.20 · payoff 2.85). Tezlashish nutqda emas, **montajda**.
- **Fragment (grammatik jihatdan mustaqil bo'lmagan davom) ulushi:** 7/19 = **36.8%**
  Fragmentlar: *"То вот что я бы делал…"*, *"Как я съезжаю с общаги…"*, *"И стабильно получать клиентов с блога"*, *"И пройду каждый шаг…"*, *"От нуля подписчиков до первого бартера и первых денег"*, *"А чтобы получить первую серию реалити"*, *"И посмотреть, как я создал…"*

### ⭐ Signature qurilma: shart mayli ("Если бы… я бы…")
| Ko'rsatkich | Qiymat |
|---|---|
| «бы» soni | **9** (0.00–43.64 oralig'ida) |
| «бы» zichligi shart blokida | har 4.8 soniyada 1 marta |
| Shart bloki uzunligi | 0.00–50.24 = **50.24s = 71%** |
| Real zamonga o'tish nuqtasi | **50.24** ("но я решил показать на деле") |

Bu korpusdagi boshqa ikki videodan (`DQ19FfMDfer`, `DS7rlXjja9c` — ikkalasi ham o'tgan zamon hikoyasi) **tubdan farq qiladi**. Bu yerda hikoya yo'q — **stsenariy** bor: "agar hozir noldan boshlasam".

### ⭐ Bo'lim ochuvchi markerlar
| Marker | Vaqt | So'z soni |
|---|---|---|
| "Первое, …" | 10.82 | 1 |
| "Дальше…" | 18.24 | 1 |
| "Первое, мое дело" | 20.62 | 3 |
| "А вторая тема, моя жизнь" | 25.30 | 4 |
| "Третье, …" | 35.24 | 1 |
| "И, наконец, …" | 43.64 | 2 |

Har bir marker **1–4 so'z** va gapning **eng boshida**. `DS7rlXjja9c` dagi "Первое. Держи фокус." qolipi bilan bir xil oila, lekin bu yerda **buyruq fe'l yo'q** — chunki hamma narsa "я бы" da.

### ⭐ Uch a'zoli sanoq — kesim ritmini boshqaradi
> *"Как я съезжаю с общаги, **ищу отношения** и **исполняю мечты**"* (29.52–33.16)
> *"…я лишился бы **блога**, оказался **в общаге**, **в теле девушки**"* (0.00–6.20)

Ikkala holatda ham **har element uchun alohida kadr** beriladi (29.83, 30.57, 31.20 — uchta 0.6–0.7s lik kadr). Ya'ni: **sanoq aytilsa — sanoq montaj qilinadi.**

### Bog'lovchilar / ko'prik so'zlar
| So'z | Uchrashi |
|---|---|
| "И…" jumla boshida | **5×** (39.76, 43.64, 47.98, 58.20, 66.24) |
| "А…" jumla boshida | **2×** (25.30, 64.30) |
| "потому что / именно благодаря" | 1× (sabab ko'prigi, 10.82 ichida) |
| "но" (burilish) | **1×** — va u aynan videoning eng muhim burilishida (50.24) |
| "даже если" (yon berish) | 1× (25.30) |

### Murojaat (shaxs) — bu videoning eng qat'iy qoidasi
| Blok | Vaqt | Shaxs |
|---|---|---|
| Hook + butun freymvork + payoff | **0.00–68.56** | **я** (100%) |
| CTA | **68.56–70.82** | **ты** (buyruq: "Пиши") |

- **"ты" birinchi marta 68.56 da paydo bo'ladi** — ya'ni videoning **96.5%i faqat "я"da**.
- **"мы" umuman yo'q** (`DS7rlXjja9c` dagi я→ты→мы uch bosqichidan farqli).
- **Buyruq gaplar:** **1 ta** — "Пиши" (1/19 = 5.3%), oxirgi 2.3 soniyada.
- ⭐ **Qoida: freymvork "sen shuni qil" emas, "men shuni qilardim" tarzida beriladi.** O'qituvchi ohangi nolga tushadi — tomoshabin maslahat emas, **rejani kuzatadi**.

### Raqam ishlatish
`1000 рублей` · `две основные темы` (ekranda `2`) · `15-20 релсов` · `около 10 релсов` · `первую тысячу подписчиков` · `тысяча подписчиков` · `30 дней` · `первую серию` · `от нуля`
= **9 ta raqamli lang'ar / 70.8s** → har **7.9 soniyada bitta raqam**.
Naqsh: **katta noaniq raqam → kichik aniq raqam** (1000 подписчиков → всего 10 рилсов). Bu "bajarish mumkin" hissini beradi.

### Filler siyosati
Nolga yaqin. "ну", "как бы", "то есть", "вот это самое" — **yo'q**. Yagona og'zaki yumshatgichlar: "вот такого" (17s), "точно" (10.82), "всегда все" (50.24).

### Sukut
Butun 71 soniyada **bitta pauza**: **54.52 → 55.02 = 0.50s**, aynan *"Я стану девушкой на 30 дней"* dan **oldin**. Payoff'ni "havoda" ushlab turadi.

### Ko'chirib olinadigan 5 ta jumla qolipi
1. `"Если бы у меня ____ , я лишился бы ____ , оказался ____ , ____"` — shart + 3 ta yo'qotish, uchinchisi absurd
2. `"То вот что я бы делал, чтобы ____ и начать ____"` — va'da ko'prigi
3. `"Первое, я бы точно ____ , потому что именно благодаря ____ у меня уже получилось пройти путь от ____ до ____"` — qadam + sabab + before/after
4. `"Я бы не ____ , а делал по ____ в месяц"` — inkor → tasdiq juftligi (zid qo'yish)
5. `"На словах всегда все звучит красиво, но я решил показать на деле"` — gipotezadan amaliyotga burilish
6. `"А чтобы получить ____ и посмотреть ____ , пиши слово «____» в комментарии"` — mukofot avval, so'rov keyin

## 6. Montaj barmoq izi

### Kesim tezligi — **ikki yarimga bo'lingan**
| Blok | Kadrlar | Davomiylik | O'rtacha |
|---|---|---|---|
| Birinchi yarim (0.00–35.30) | ~23 | 35.30s | **1.53s** |
| Ikkinchi yarim (35.40–71.07) | ~14 | 35.67s | **2.55s** |

**Kesim ikkinchi yarimda 67% ga sekinlashadi** — bu intuitsiyaga zid, lekin ishlaydi (sabab: pastda "diqqatni nima ushlaydi").

### Kadr uzunliklari — **bimodal, o'rtachasi yo'q**
- **Qisqa portlashlar (<1.0s), 5 ta:** 0.33 · 0.57 · 0.63 · 0.74 · **0.56** — hammasi **sanoq/ro'yxat** aytilayotgan joyda
- **Uzun ushlashlar (>3.5s), 7 ta:** 3.80 · 3.93 · 4.20 · 4.47 · 4.74 · 4.74 · **6.60** — **hammasi 35s dan keyin**
- 1.0–3.5s oralig'ida atigi ~12 kadr

### ⭐ Kesimlar nutqqa sinxron, musiqaga emas — o'lchandi
19 ta jumla chegarasidan **11 tasida oq flash**, yana 4 tasida hard cut turadi. Flash **jumla tugagandan keyin 0.10–0.32s** ichida tushadi:

| Jumla tugashi | Flash | Kechikish |
|---|---|---|
| 6.20 | 6.47 | +0.27 |
| 10.82 | 10.93 | +0.11 |
| 18.24 | 18.43 | +0.19 |
| 20.62 | 20.73 | +0.11 |
| 25.30 | 25.37 | +0.07 |
| 35.24 | 35.30 | +0.06 |
| 39.76 | 39.87 | +0.11 |
| 50.24 | 50.33 | +0.09 |
| 60.18 | 60.47 | +0.29 |
| 64.30 | 64.50 | +0.20 |
| 68.56 | 68.80 | +0.24 |

**O'rtacha kechikish: +0.16s.** Beat-sync belgisi topilmadi — kesim **gapga bo'ysunadi**.

### Ichki kesimlar — uzun jumla ichida
| Jumla | So'z | Davomiylik | Ichki kesimlar | Kadr uzunligi | Kadr / so'z |
|---|---|---|---|---|---|
| 10.82–18.24 | 24 | 7.42s | 13.07 · 16.27 · 16.70 · 17.27 (4 ta) | 1.48s | 4.8 |
| 25.30–29.52 | 15 | 4.22s | 26.93 (1 ta) | 2.11s | 7.5 |
| 29.52–33.16 | 10 | 3.64s | 30.57 · 31.20 (2 ta) | 1.21s | 3.3 |
| 50.24–54.52 | 15 | 4.28s | ~3 ta (detektor topmagan) | 1.07s | 3.8 |

⭐ **Qoida: 10 so'zdan uzun jumla ichida har 1–2 soniyada (≈ har 3–7 so'zda, o'rtacha 4.9) kadr almashadi.** Jumla tugamaydi — kadr tugaydi.

### Shot turlari ulushi (~37 kadrdan)
| Tur | Kadrlar | Ulush |
|---|---|---|
| Talking-head (jonli, kreator) | ~13 | 35% |
| Arxiv / eski selfie video | ~6 | 16% |
| AI-kartun (0–6.5s) | ~6 | 16% |
| Oq doska / flipchart (marker bilan chizish) | ~4 | 11% |
| Telefon ekrani / screen-record | ~4 | 11% |
| AI-fotoreal ayol avatar | ~3 | 8% |
| B-roll (manikyur, kechqurun sayr) | ~3 | 8% |

### O'tishlar
- **Oq flash: 12 ta** (33%) — asosiy bo'lim ajratgich, har biri ~0.10s
- **Hard cut: 24 ta** (67%)
- **Kaft-wipe (hand-over-lens match cut): 1 ta** — 3.9–4.5s da kaft ob'ektivni yopadi (chiroyli xona) va ochiladi (iflos oshxona). **Bir kaft harakati bilan ikki dunyo almashadi.**
- **Morph (o'sha kadrda jinsni almashtirish): 2 ta** — 5.5s (kartun erkak→ayol) va **55.17→55.73** (jonli erkak→AI ayol, **aynan bir xil kreslo, bir xil rakurs**)
- **Negativ/invert freym: 1 ta** (~18s, "дальше") — 0.3–0.5s lik "shovqin" o'tishi
- **Zoom / punch-in:** 2 marta — hook ichida (0.5→3.5s asta yaqinlashuv) va 11.03–13.07 da (qo'l ob'ektivga cho'ziladi, plan keskin kattalashadi)

### ⭐ Uzun kadrlarda kesim o'rnini bosuvchi 4 ta qurilma
Bu videoning asosiy siri: 3 soniyadan uzun **har bir** kadrda **kadr ichida uzluksiz harakat** bor.

| Kadr | Uzunlik | Kadr ichidagi harakat |
|---|---|---|
| 35.40–39.87 | 4.47s | Flipchart oldida yuradi, **qizil ✗** yopishtiradi, keyin **yashil ✓** qo'yadi (statik kamera) |
| 39.93–43.73 | 3.80s | Yashil marker **jonli chizadi**: ✓ → strelka → `1000` → odamcha → `10` |
| **43.73–50.33** | **6.60s** | **Stop-motion: brend qutilari birma-bir kadrga "sakrab" chiqadi** (1 → 3 → 5 → 6 → 7 ta) — kamera qimirlamaydi, lekin har soniyada kadr o'zgaradi |
| 60.57–64.50 | 3.93s | Marker `БАРТЕР` yozadi, strelka tortadi, oxirida **haqiqiy pul dastasi** doskaga qo'yiladi |

⭐ **Qoida: uzun kadr = statik kamera + kadr ichida bosqichma-bosqich o'sib boradigan ob'ekt.** Kesim o'rniga **jismoniy o'zgarish**.

### Vizual metaforalar — abstrakt tushuncha jismoniy ko'rsatiladi
| Aytilgan | Ekranda ko'rsatilgan |
|---|---|
| "я лишился бы блога" | tripoddagi telefon kadrdan **yo'qoladi** (2.5s → 3.5s) |
| "оказался в общаге" | chiroyli xona → **mog'orlagan oshxona** (kaft-wipe orqali) |
| "от хостела до вот такого дома" | **arxiv**: xostel oynasidagi selfi (16s) → **kechqurun katta uy oldida yurish** (17s) |
| "какие услуги у меня можно купить" | kreator **haqiqatan manikyur qiladi** (21–24s) — "услуга" so'zi emas, xizmatning o'zi |
| "ищу отношения и исполняю мечты" | telefonda qiz profili va konsert fotolari **varaqlanadi** (31–33s) |
| "лояльных подписчиков" | **to'lib ketgan Instagram Direct** ekrani (34s) |
| "не вкладывал деньги в рекламу, а делал релсы" | doskada **✗ (pul) / ✓ (telefon)** yonma-yon (37–39s) |
| "сотрудничать с брендами по бартеру" | **haqiqiy PR-qutilar** atrofida ko'payadi (44–49s) |
| "от нуля подписчиков" | doskada **0 obunachili haqiqiy IG profil skrinshoti** (61s) |
| "первых денег" | doskaga **haqiqiy 5000₽ dastasi** qo'yiladi (64s) |

⭐ **Bitta so'z hech qachon ekranda takrorlanmaydi — u ijro etiladi.** "Бартер" so'zi kaptsiyada yo'q, chunki uni **marker doskaga yozib beradi**.

## 7. Ekran matni tizimi — **uch qavatli**

```
┌───────────────────────────────┐
│                               │
│      [kadr — odatda odam]     │
│                               │
│   kichik oq lowercase         │  ← 1-qavat: ko'prik / davom
│   KATTA OQ UPPERCASE          │  ← 2-qavat: gapning setup'i
│   KATTA SARIQ UPPERCASE       │  ← 3-qavat: PAYLOAD (raqam / pul / zarba)
│                               │
│        3/4  (katta kulrang)   │  ← bob raqami, shaffof, orqada
└───────────────────────────────┘
```

| Parametr | Qiymat |
|---|---|
| Joylashuv | **kadr markazi–pastki markaz oralig'i** (~40–55% balandlik), odam ko'kragi ustida — `DQ19FfMDfer` dagi past-markazdan **balandroq** |
| Shrift | qalin siqilgan grotesk, ALL CAPS; ko'prik satrlar kichik harflar |
| Fon plashka | **yo'q** — qora kontur/soya bilan ajratilgan |
| Ranglar | oq + **#FFE24A tipidagi sariq** (faqat 2 rang) |
| Jami matn kartochkasi | **~59 ta / 71.07s** → har **1.20s da yangi kartochka** |
| Kartochkadagi so'z | o'rtacha **2.7**, min **1**, maks **6** |
| Sariq payload kartochkalari | **19 ta** (32%) |
| Progressiv yig'ilish | **14 marta** (pastga qarang) |
| Bob raqamlari | `1/4` (11–12s) · `2/4` (19–20s) · `3/4` (35–36s) · **`4/4` — `[noaniq]`, 1fps namunada topilmadi** |

### ⭐ Matn — SUBTITR EMAS, QISQARTMA (o'lchandi)
| Blok | Aytilgan so'z | Ekrandagi so'z | Ulush |
|---|---|---|---|
| **Hook 0.00–6.20** | 19 | 18 | **95%** ← deyarli to'liq |
| 18.24–20.62 | 9 | 5 | 56% |
| 43.64–50.24 | 19 | 10 | **53%** |
| 50.24–54.52 | 15 | 9 | 60% |

⭐ **Qoida: hook'da matn to'liq (mute uchun), tanada 53–60% ga tushadi.** Faqat hook mute'da o'z-o'zidan tushunarli bo'lishi kerak — qolgani ovoz bilan ishlaydi.

Misollar (tashlab yuborilgan so'zlar qavsda):
- Ovozda: *"Дальше я бы выбрал две основные темы для блога"* → ekranda: **2 ОСНОВНЫЕ ТЕМЫ / ДЛЯ БЛОГА** (~~Дальше я бы выбрал~~; "две" → **2**)
- Ovozda: *"…можно начать сотрудничать с брендами по бартеру"* → ekranda: **сотрудничать / по бартеру** (~~можно начать~~, ~~с брендами~~)
- Ovozda: *"На словах всегда все звучит красиво"* → ekranda: **на словах / звучит красиво** (~~всегда все~~)

### ⭐ Progressiv yig'ilish — 14 ta tasdiqlangan holat
Naqsh **har safar bir xil**: avval oq satr, keyin **pastiga sariq payload qo'shiladi** (oq satr o'chmaydi).

| Bosqich 1 (oq) | Bosqich 2 (+sariq) |
|---|---|
| `ЕСЛИ БЫ` | `+ У МЕНЯ В КАРМАНЕ` |
| `Я ЛИШИЛСЯ БЫ` | `+ БЛОГА` |
| `ОКАЗАЛСЯ` | `+ В ОБЩАГЕ` |
| `2 ОСНОВНЫЕ ТЕМЫ` | `+ ДЛЯ БЛОГА` |
| `даже если` | `+ НЕ ВСЕ ИДЕАЛЬНО` |
| `И ИСПОЛНЯЮ` | `+ МЕЧТЫ` |
| `я бы не вкладывал` | `+ ДЕНЬГИ` |
| `по 15-20 рилсов` | `+ В МЕСЯЦ` |
| `ОКОЛО` | `+ 10 РИЛСОВ` |
| `1000` | `+ ПОДПИСЧИКОВ` |
| `Я СТАНУ` | `+ ДЕВУШКОЙ / НА 30 ДНЕЙ` |
| `а чтобы получить` | `+ 1 СЕРИЮ` |
| `как я создал свою` | `+ ЖЕНСКУЮ ВЕРСИЮ` |
| `ПИШИ СЛОВО` | `+ АВАТАР` (+ `в комментарии` kichik oq) |

### Sariq nimaga beriladi (leksik qoida)
`В КАРМАНЕ` · `1 000 РУБЛЕЙ` · `БЛОГА` · `В ОБЩАГЕ` · `В ТЕЛЕ ДЕВУШКИ` · `ДО ВОТ ТАКОГО` · `НЕ ВСЕ ИДЕАЛЬНО` · `МЕЧТЫ` · `ДЕНЬГИ` · `В МЕСЯЦ` · `10 РИЛСОВ` · `ПОДПИСЧИКОВ` · `ДЕВУШКОЙ НА 30 ДНЕЙ` · `1 СЕРИЮ` · `ЖЕНСКУЮ ВЕРСИЮ` · `АВАТАР`

→ **Sariq faqat: raqam, pul, yo'qotish yoki kutilmagan so'z.** Hech qachon bog'lovchi, olmosh yoki fe'l-yordamchi sariq bo'lmaydi.

### Emoji / stiker
Raqamli emoji **yo'q**. O'rniga **jismoniy rekvizit**: qog'ozdan kesilgan **yashil ✓** va **qizil ✗** doskaga yopishtiriladi (37–43s), yashil marker chizmalari (40–43s, 61–64s). Grafik qatlam **qo'lda va kadr ichida** yaratiladi.

### Rang / look
Iliq, past kontrast, biroz sarg'ish grading. Arxiv kadrlar ataylab **past sifatli va donador** qoldirilgan (25–30s) — "haqiqiy 2018-yil" hissi. AI-kartun bloki **eng issiq va eng to'yingan**; jonli s'yomka undan sovuqroq. Iflos oshxona — sarg'ish-yashil, iflos.

## 8. Audio
- **VO:** kreator o'zi, doimiy, 3.11 so'z/s, tekis temp
- **Fon musiqa / SFX:** `[noaniq]` — audio tinglanmadi. Ammo **strukturaviy dalil bor**: 11 ta flash 11 ta jumla chegarasidan +0.16s o'rtacha kechikish bilan tushadi, musiqa zarbasiga bog'lanish belgisi topilmadi → **kesim nutqqa sinxron**
- **Sukut:** **1 ta, 0.50s** (54.52–55.02), payoff jumlasidan oldin

## 9. Yakun va CTA — **bu videoning korpusdan farqi**

| | `DQ19FfMDfer` | `DS7rlXjja9c` | **`DUxbSgyDTck`** |
|---|---|---|---|
| Yakun turi | maslahat + istiqbol | universal aforizm | **cliffhanger + keyword CTA** |
| CTA | ❌ yo'q | ❌ yo'q | ✅ **bor** |

- **CTA bloki:** 64.30–70.82 = **6.52s = runtime'ning 9.2%i**
- **So'zma-so'z:** *"А чтобы получить первую серию реалити, и посмотреть, как я создал свою женскую версию — **Пиши слово «Аватар» в комментарии**"*
- **Ekranda:** `ПИШИ СЛОВО` (katta oq) / **`АВАТАР`** (katta sariq) / `в комментарии` (kichik oq)
- ⭐ **Tuzilishi: mukofot avval, so'rov keyin.** So'rovdan **4.26 soniya oldin** ikkita mukofot nomlanadi ("первую серию реалити" + "как я создал свою женскую версию"). Buyruq fe'l ("Пиши") **butun videodagi yagona buyruq** va oxirgi 2.3 soniyada turadi.
- **Vizual qo'llab-quvvatlash:** 69–70s da kreator ko'kragiga **screen-record oynasi** kompozitsiya qilinadi — unda `NANO BANANA PRO` interfeysi va ayol avatar ko'rinadi. Ya'ni "qanday qilganman" degan va'da **ekranda bir soniya ko'rsatiladi**, lekin tushuntirilmaydi → qiziqish CTA'ga haydaladi.
- **Loop yopilishi:** hook'dagi eng g'alati detal (`в теле девушки`) **CTA kaliti bo'lib qaytadi** (`АВАТАР`). Ya'ni **hook = CTA uchun setup**.

## 10. ✅ Ko'chiriladigan qoidalar

1. **Hook'ni shart maylida qur:** `"Если бы у меня ____ , я лишился бы ____ , оказался ____ , ____"`. Uch yo'qotish sana, **uchinchisi mantiqan keraksiz va absurd** bo'lsin — loop aynan shundan ochiladi.
2. **Birinchi jumlani 6 soniyaga cho'z, lekin grammatik jihatdan tugatma.** "то…" bo'lagini 6-soniyaga qoldir — tomoshabin gapni tugatish uchun qoladi.
3. **Hook'da 3–4 ta konkret detal ayt va hammasini finalda yop.** Bu videoda 4/4 yopilgan. Bitta ham osilib qolmasin.
4. **Hook'dagi raqamni oxirida birligini almashtirib qaytar** (`1000 рублей` → `1000 подписчиков`), **aynan bir xil tipografiya bilan**.
5. **Butun freymvorkni "я бы"da ayt, "ты"ga o'tma.** Buyruq gap butun videoda **1 ta** bo'lsin va faqat CTA'da. O'qituvchi ohangi = past retention.
6. **Gipotezadan amaliyotga burilish jumlasini qo'y:** `"На словах всегда все звучит красиво, но я решил показать на деле"`. Undan keyin fe'llarni **real kelasi zamonga** o'tkaz ("я стану", "заведу", "пройду").
7. **Payoff jumlasidan oldin 0.5s sukut qoldir.** Butun videodagi yagona pauza shu joyda bo'lsin.
8. **Ekrandagi bob raqamlarini (`1/4`, `2/4`, `3/4`) katta shaffof kulrang qilib qo'y** — og'zaki sanoq chalkashsa ham (bu videoda "Первое" ikki marta aytilgan) ekran tuzatib turadi.
9. **Matn uch qavatli bo'lsin:** kichik oq lowercase (ko'prik) → KATTA OQ CAPS (setup) → **KATTA SARIQ CAPS (payload)**. Sariq faqat raqam / pul / yo'qotish / kutilmagan so'zga beriladi.
10. **Har ~1.2 soniyada yangi matn kartochkasi, o'rtacha 2.7 so'z.** Matn kadrdan tez almashsin — kesim sekin bo'lsa ham ekran tirik qoladi.
11. **Hook'da matn 95% subtitr, tanada 53–60% qisqartma.** Faqat hook mute'da mustaqil ishlashi shart.
12. **Matnni progressiv yig':** oq satr qoladi, pastiga sariq payload qo'shiladi. Hech qachon butun jumlani birdan chiqarma.
13. **Kesimni jumla tugagandan +0.1…+0.3s keyin qo'y** (o'rtacha +0.16s), musiqa zarbasiga emas. Har jumla chegarasi = o'tish.
14. **10 so'zdan uzun jumla ichida har 1–2 soniyada kadr almashtir** (≈ har 3–7 so'zda). Jumlani tugatma — kadrni tugat.
15. **Sanoq aytilsa — sanoqni montaj qil:** ro'yxatning har elementiga **0.3–0.8s** lik alohida kadr.
16. **Kadr uzunligini bimodal qil:** yo <1s portlash, yo >3.5s ushlash. 1.5–3s "o'rtacha" kadrlardan qoch.
17. **Ikkinchi yarimda kesimni sekinlashtir (~1.5s → ~2.5s), lekin har uzun kadrga kadr ichida harakat qo'y:** marker bilan jonli chizish, doskaga ✗/✓ yopishtirish, **stop-motion bilan ob'ektlarni ko'paytirish** (6.6s lik quti sahnasi).
18. **Abstrakt so'zni ijro et, yozma:** "услуги" → haqiqatan manikyur qil; "бартер" → markerda yoz; "первые деньги" → haqiqiy pulni stolga qo'y. **Kaptsiyada yo'q so'zni rekvizit aytsin.**
19. **Da'voni arxiv bilan hujjatlashtir:** "от хостела до вот такого" — **eski past sifatli selfi** (16s) va yangi kadr (17s) ketma-ket, har biri ~1s. Arxivni sifatli qilib "tozalama" — donadorlik ishonch beradi.
20. **Bo'lim o'tishlarini oq flash bilan bel:** ~0.10s, 12 ta / 71s. Ular ham kesim, ham "yangi bo'lim" signali.
21. **Bir joyda kamerani qimirlatmasdan sub'ektni almashtir** (55.17→55.73: bir xil kreslo, bir xil rakurs, boshqa odam) — bu videodagi eng kuchli reveal, atigi **0.56 soniya** turadi.
22. **CTA'da mukofotni avval, so'rovni keyin ayt.** Kalit so'zni **sariq bilan** ajrat, "в комментарии" ni kichik oq bilan pastiga qo'y. So'rovdan ~4s oldin nimani olishini ayt.
23. **CTA'ni hook'dagi eng g'alati detaldan chiqar** (`в теле девушки` → kalit so'z `АВАТАР`). Hook CTA uchun setup bo'lsin.

## 11. ❌ Ko'chirilmaydigan (bu videoga xos, bir martalik)

1. **"Я стану девушкой на 30 дней" g'oyasi** — bir martalik, shok qiymatiga qurilgan. Har mavzuga ko'chirilmaydi; takrorlansa arzonlashadi.
2. **AI-kartun hook (0–6.5s)** — bu shu videoning "gender-morph" g'oyasiga bog'langan. Boshqa ikki referensda (`DQ19FfMDfer`, `DS7rlXjja9c`) mutlaqo boshqa look. **Har videoda kartun ishlatish korpus uslubi emas.**
3. **AI avatar generatsiyasi (`NANO BANANA PRO`)** — konkret asbob nomi va konkret reality-loyihaga bog'liq.
4. **Shaxsiy arxiv (xostel, 2018 selfilar, katta uy)** — faqat haqiqiy bo'lsa. **To'qib chiqarilmasin.**
5. **Manikyur sahnasi** — "услуги" ni ko'rsatish uchun tanlangan tasodifiy misol; boshqa nishada boshqa xizmat kerak. Ko'chiriladigani — **printsip** (xizmatni ijro etib ko'rsatish), sahnaning o'zi emas.
6. **Konkret raqamlar** (1000 ₽, 15–20 рилсов, ~10 рилсов, 30 дней) — bu kreatorning o'z tajribasidan. Yangi stsenariyda **o'z haqiqiy raqamlaring** bilan almashtiriladi.
7. **CTA'ning o'zi (`Пиши слово «Аватар»`)** — bu yerda **seriya** sotilyapti. Agar reel seriyaga olib bormasa, korpusning asosiy naqshi — **CTA'siz tugatish** (`DQ19FfMDfer` va `DS7rlXjja9c` da CTA yo'q).
