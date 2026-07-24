# Teardown: `DS7rlXjja9c.mp4`

## 1. Meta
| | |
|---|---|
| Davomiylik | **80.53s** |
| O'lcham | 1080×1920 · 9:16 · 30fps |
| Kesimlar (@0.25) | **30** · o'rtacha **2.35s** |
| Arxetip | **Story → Framework (3 qoida)** · mavsumiy (Yangi yil) |
| Ovoz | VO + sokin fon |
| Kostyum | **Ayoz bobo kostyumi** — mavsumiy marker, bo'lim belgisi sifatida ham ishlaydi |

## 2. So'zma-so'z transkript
```
 0.00– 3.68  8 лет назад, в новогоднюю ночь, я выложил пост с 10 целями на год.
 3.74– 7.32  Я думал, что выйду на миллион в месяц, побываю в трех странах и куплю себе Мерс.
 7.36– 9.78  Но из всего списка целей я сделал только ничего.
10.06–13.08  Тогда я понял, что если у тебя большие мечты и ты хочешь получить все сразу,
13.54–15.08  ты ни хрена не получишь.
15.16–18.72  Из-за количества целей я не знал, за что браться и не доводил дела до конца.
18.92–22.02  Казалось, что я делаю много, но жизнь не менялась.
22.08–24.78  Поэтому я решил отстать от себя и у меня появилось три правила.
24.88–26.20  Первое. Держи фокус.
26.20–33.60  Я убрал все лишнее и вместо десятков целей на год я начал ставить одну цель и уделять ей все внимание.
33.86–35.42  Второе правило. Упрощай.
35.50–40.78  Например, завести блог и набрать 10 тысяч подписчиков слишком большая цель и непонятно с чего начать.
40.84–44.98  Лучше потратить час в начале года, чтобы разбить ее на маленькие шаги и идти по ним друг за другом.
45.04–46.92  И третье правило. Создай рутину.
46.98–49.34  Не жди, что ты выполнишь цель за один рывок.
49.46–53.06  Создай образ жизни, который автоматически приведет тебя к цели.
53.06–57.08  Если ты держишь фокус на том, чтобы похудеть на 10 кг к лету, ты не похудеешь.
57.08–61.54  А если ты создашь привычку всегда тренироваться 3 раза в неделю и правильно питаться,
61.54–63.54  у тебя неизбежно будет классная форма[?].
63.54–65.40  По этим правилам я живу последние 7 лет.
65.40–68.48  И по итогу вместо миллиона в месяц я делаю в 10 раз больше,
68.48–71.88  а вместо Мерседеса купил себе Феррари и подарил Ламбу жене.
71.88–74.32  Мы переоцениваем то, что мы можем сделать в течение года,
74.32–79.16  но недооцениваем то, к чему может привести правильный образ жизни в течение нескольких лет.
79.16–80.38  С Новым Годом!
```

## 3. Hook teardown (0–4s)
| Vaqt | Ekranda | Aytilgan | Ekran matni |
|---|---|---|---|
| 0.0s | Ayoz bobo kostyumida, archa oldida | "8 лет назад…" | **8 ЛЕТ** (sariq, katta) |
| 1.0s | Sama | "…в новогоднюю ночь…" | В НОВОГОДНЮЮ (oq) |
| 2.0s | Bosma post varag'ini ko'taradi | "…я выложил пост…" | Я ВЫЛОЖИЛ / **ПОСТ** (sariq) |
| 3.0s | Varaqni kameraga tutadi (10 maqsad ro'yxati o'qiladi) | "…с 10-ю целями на год." | С 10-Ю ЦЕЛЯМИ / **НА ГОД** (sariq) |

- **Pattern interrupt:** kostyum (Ayoz bobo) + katta sariq raqam "8 ЛЕТ"
- **Birinchi jumla:** 11 so'z
- **Ochilgan loop:** *o'sha 10 maqsaddan nimasi bajarildi?*
- **Isbot darhol:** 4-6s da **haqiqiy eski postning skrinshoti** ko'rsatiladi va marker bilan belgilanadi — hikoya birinchi 5 soniyada hujjatlashtiriladi

## 4. Struktura
```
 0.0– 3.7s  HOOK          "8 yil oldin 10 ta maqsadli post"
 3.7– 7.3s  VA'DA-DETAL   "mln/oy, 3 davlat, Mers"        ← bu 3 ta detal oxirida qaytadi
 7.4– 9.8s  DEFLATSIYA    "я сделал только ничего"        ← hazil, kutilmagan pasayish
10.1–22.0s  DIAGNOZ       nega bajarilmadi (fokus yo'q)
22.1–24.8s  VA'DA         "у меня появилось три правила"
24.9–33.6s  QOIDA 1       Держи фокус
33.9–44.9s  QOIDA 2       Упрощай
45.0–63.5s  QOIDA 3       Создай рутину
63.5–71.9s  ISBOT+CALLBACK "вместо миллиона — в 10 раз больше, вместо Мерседеса — Феррари"
71.9–79.2s  UNIVERSAL     "Мы переоцениваем год, недооцениваем несколько лет"
79.2–80.4s  YAKUN         "С Новым Годом!"  ← CTA YO'Q
```

> ### 🔑 Loop yopilishi — callback mexanikasi
> Hook'da **aniq 3 ta detal** aytiladi: *миллион в месяц · три страны · Мерс*.
> 68-soniyada **aynan o'sha detallar javob oladi**: *"вместо миллиона — в 10 раз больше, вместо Мерседеса — Феррари"*.
> Ya'ni: **hook'da aytilgan konkret narsalar finalda birma-bir yopiladi.** Bu tomoshabinni oxirigacha ushlaydigan eng aniq qurilma.

## 5. Jumla tuzilishi
- **Jumlalar:** 25
- **So'z sanog'i:** `[11,14,10,15,5,15,9,12,3,20,3,16,17,4,8,9,15,15,6,8,11,10,9,14,3]`
- **O'rtacha:** 10.5 · **mediana:** 10
- **Eng uzun:** 20 · **eng qisqa:** 3

### ⭐ Bo'lim sarlavhalari — 3–4 so'z, buyruq fe'l
> "Первое. **Держи фокус**." (3)
> "Второе правило. **Упрощай**." (3)
> "И третье правило. **Создай рутину**." (4)

`DQ19FfMDfer`dagi "Во-первых, веди блог" (3) bilan bir xil. **Qoida: har bo'lim sarlavhasi = tartib raqami + 1–2 so'zli buyruq.**

### ⭐ Deflatsiya hazili
> "Но из всего списка целей я сделал **только ничего**."

Grammatik jihatdan "noto'g'ri", lekin aynan shuning uchun kuladi. Setup → kutilmagan pasayish. 10-soniyada joylashgan — hook'dan keyingi birinchi ushlash nuqtasi.

### ⭐ "Agar… u holda" juftligi (qoida 3)
> "**Если** ты держишь фокус на том, чтобы похудеть… ты **не** похудеешь.
> **А если** ты создашь привычку… у тебя **неизбежно** будет…"

Salbiy shart → ijobiy shart. Ketma-ket, bir xil qurilishda. **Qarama-qarshi juftlik** — korpusda takrorlanadi.

### Murojaat almashishi (tasdiqlandi)
- Hikoya (0–22s): **я**
- Qoidalar (22–63s): **ты** + buyruq (`Держи`, `Упрощай`, `Создай`, `Не жди`)
- Isbot (63–72s): **я** ga qaytadi
- Universal (72–79s): **мы** ← *"Мы переоцениваем… недооцениваем"*

⭐ **Uch bosqichli shaxs harakati: я → ты → мы.** Yakundagi "мы" gapni umuminsoniy qiladi va o'qituvchi ohangini yumshatadi.

## 6. Montaj barmoq izi
- **Kesim:** har 2.35s
- **Vizual metafora jismonan quriladi:** doskadagi stikerlar — avval **tartibsiz ko'p** (16–18s), keyin qo'l bilan **olib tashlanadi** va **bitta** stiker qoladi (32s). Ya'ni "fokus" tushunchasi gapirilmaydi — **ko'rsatiladi**.
- **Isbot skrinshotlari:** haqiqiy eski Instagram posti (4–6s), telefon ekrani (39s)
- **Lokatsiya almashishi bo'limni bildiradi:** archa oldi (hikoya) ↔ oq doska (qoidalar) ↔ stol/noutbuk (muammo)
- **Kostyum:** Ayoz bobo → oq futbolka → Ayoz bobo. Kostyum o'zgarishi = bo'lim chegarasi.

### Ekran matni (korpus tizimi tasdiqlandi)
- Past-markaz, ikki qavat: kichik oq lowercase + **KATTA SARIQ UPPERCASE**
- 1–4 so'z/kartochka, ~1–1.5s
- **Progressiv yig'ilish:** `ПОЛУЧИТЬ` → `ПОЛУЧИТЬ ВСЕ СРАЗУ`; `И НЕ ДОВОДИЛ` → `И НЕ ДОВОДИЛ ДЕЛА ДО КОНЦА`
- **Qisqartma printsipi:** ovozda *"я начал ставить одну цель и уделять ей все внимание"* → ekranda faqat **ОДНУ ЦЕЛЬ / И УДЕЛЯТЬ ЕЙ ВСЕ ВНИМАНИЕ**

## 7. Yakun
- **Universal aforizm:** "Мы переоцениваем то, что можем сделать в течение года, но недооцениваем… в течение нескольких лет"
- **Mavsumiy sign-off:** "С Новым Годом!"
- ⛔ **CTA yo'q.** Obuna/saqlash/komment so'ralmaydi.

## 8. ✅ Ko'chiriladigan qoidalar
1. **Hook'da 2–3 ta konkret detal ayt** va finalda **aynan o'sha detallarni yop** (callback loop).
2. **Hook'dan keyin 10-soniyada deflatsiya hazili qo'y** — "…я сделал только ничего" tipida.
3. **Bo'lim sarlavhasi = raqam + 1–2 so'zli buyruq** ("Первое. Держи фокус.").
4. **Shaxsni bosqichma-bosqich almashtir: я → ты → мы.** Yakun "мы"da.
5. **Qarama-qarshi shart juftligini ishlat:** "Если… не получишь. А если… неизбежно…"
6. **Abstrakt tushunchani jismoniy metafora bilan ko'rsat** (stikerlarni olib tashlash = fokus). Aytma — ko'rsat.
7. **Da'voni birinchi 5 soniyada hujjatlashtir** (eski post skrinshoti, arxiv).
8. **CTA'siz tugat** — universal aforizm bilan.
9. **Kostyum/lokatsiya almashishi bo'lim chegarasini bildiradi.**

## 9. ❌ Ko'chirilmaydigan
1. Ayoz bobo kostyumi va "С Новым Годом" — faqat mavsumiy kontentda.
2. Feррari/Lambo raqamlari — shaxsiy va haqiqiy; to'qib bo'lmaydi.
3. "ни хрена" — qo'pol leksika; brend ovoziga qarab moslashtiriladi.
