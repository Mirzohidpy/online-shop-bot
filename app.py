from aiogram import executor
import logging
from loader import dp, db, loop
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

logging.basicConfig(level=logging.INFO)
async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

    await db.conf()

    await db.create_table_user()

    await db.create_table_category()

    await db.create_table_subcategory()

    await db.create_table_product()

    await db.create_table_order()

    await db.create_table_order_item()
    # data = loop.run_until_complete(db.categories())



    # # category_list = [
    #     ('tvtexno', '📺📷🎥 Televizor, foto-video va audio'),
    #     ('comp', '💻🖨🖥 Noutbuk, printer, kompyuterlar'),
    #     ('phone', '📱⌚️ 🎧︎ Smartfon, telefon, gadjet, aksessuarlar'),
    #     ('homeAppliances', 'Maishiy texnika')
    # ]
    #
    # await db.insert_category(category_list)
    #
    # subcategory_list = [
    #     ('tv', 'Televizorlar', 1), ('audio', 'Audio', 1), ('photo_video', 'Foto, video', 1),
    #     ('noutbook', 'Noutbuk', 2), ('monitor', 'Monitorlar', 2), ('monoblok', 'Monoblok', 2),
    #     ('smartfon', 'Smartfonlar', 3), ('sm_gadjets', 'Gadjetlar va aksessuarlar', 3),
    #     ('washing_machine', 'Kir yuvish mashinalari', 4),
    #     ('air_conditioner', 'Iqlim ta’minlovchi qurilmalar', 4)
    # ]
    #
    # await db.insert_subcategory(subcategory_list)
    #
    # product_list = [('Samsung UE55AU9000UXCE',
    #                  'https://olcha.uz/image/original/products/hSjs8E89Bqk2IqPqWmxIo2Wi80HsGIzKs18SqSHTxkD60GP5endS2x8i1tkY.jpeg',
    #                  'Televizor Samsung UE55AU9000UXCE umumiy ma\'lumotlar\r\nUyqu taymeri: Mavjud\r\nDinamik saxna indeksi: 2800\r\nSmart TV: Bor, Tizen\r\nEkran formati: 16:9\r\nEkranni yangilnish tezligi: 120 Gts\r\nLED yoritilish: Mavjud\r\nTuri: JK-televizor\r\nDiagonal: 54.6"\r\nO\'lchami: 3840x2160\r\nAudio dekoderlari: Dolby Digital\r\nKirishlar: AV, HDMI x3, USB x2, Ethernet (RJ-45), Bluetooth, Wi-Fi 802.11ac, Miracast',
    #                  1, '9064000.00'), ('LG 50NANO796NF NanoCell 50" (2020)',
    #                                     'https://olcha.uz/image/original/products/sxmQmc8eN31sk862QvJjdY8XpywqwbC86xCs1oTk7BYgxhb1GSC8ncpPwPjE.jpeg',
    #                                     'Televizor LG 50NANO796NF NanoCell 50" (2020) umumiy ma\'lumotlar\r\nLocal Dimming: Mavjud\r\nDiagonal: 50"\r\nEkranni yangilanish tezligi: 50 Gts\r\nRazreshenie: 3840x2160\r\nHDR Formati: HDR10\r\nIshlab chiqarilgan yili: 2020\r\nEkran formati: 16:9\r\nSmart TV: Bor, webOS\r\nTuri: JK-televizor, NanoCell\r\nHDR Formati: HDR 10 Pro\r\nDevorga mahkamlash: Mavjud\r\nO’lchami (HD): 4K UHD, HDR\r\nLED yoritilish: Edge LED\r\nUyqu taymeri: Mavjud',
    #                                     1, '7316000.00'), ('Logitech Z607',
    #                                                        'https://olcha.uz/image/original/products/pN11fFhtFGNlgHHgrwtMZVgba24tHLXIyqufeZGKm88kYTFS14ixFThi1z7s.jpeg',
    #                                                        "Logitech Z607 umumiy ma'lumotlar", 2, '2282000.00'), (
    #                     'Fotokamera Nikon D5600 Kit 18-55 Wifi',
    #                     'https://olcha.uz/image/original/products/LSTxuj9polJk0vEkQ9xytliaJ3kr2rwGayUarPK2h7EDNx0CvDxOi4TaP046.jpg',
    #                     'Fotokamera Nikon D5600 Kit 18-55 Wifi haqida tavsif\r\n\r\nIkkiyoqlama tasvirga olish imkoniyati\r\n\r\nSuyuq kristalli fotokamerada jonli va yorqin tasvirlar olish uchun ko‘p karrali optik zum yordamida obyektlarni yaqinlashtirishingiz yetarlidir. Nikon D5500 kamerasi yordamida ikkiyoqlama tasvirga tushirish imkoniyati mavjud, chunki u oynali kamera sanaladi.\r\n\r\n\r\nInternetga ulansa bo‘ladi\r\n\r\nNikon oynali fotokamerasini shtativga mustahkamlab foydalanish qulaylik yaratadi. Masofadan boshqarish imkoni hamda oriyentatsiya datchigi bor. Wifi orqali internetga ulanib fotolarni do‘stlaringiz bilan baham ko‘rishingiz mumkin. Vazni atigi 420 gramm bo‘lib, cho‘ntakka osongina joylashadi. Hamisha va har joyda o‘z vazifasini qoyillatib bajaradi.\r\n\r\n\r\nKuchli batareya va sinovdan o‘tgan sifat\r\n\r\nFotokameraning o‘z Bluetooth tizimi mavjud. Apparat suratga olibgina qolmaydi, balki MOV formatli videoga ham oladi. Ishlash jarayonida qo‘lingizni toliqtirmaydi. Batareyasining sig‘imi katta bo‘lib, 820ta kadrga yetadi. Hayotingizning eng yorqin damlarini Nikon D5500 kamerasi yordamida tarixga muhrlang.',
    #                     3, '7207000.00'), ('Fotokamera Nikon Coolpix B500',
    #                                        'https://olcha.uz/image/original/products/0F7ggLeNmzNgrSBW8FDZAbpr2iIzFrvDpuxqItlEsxyaMM0TzIFSFtsFzLkP.jpg',
    #                                        'Fotokamera Nikon Coolpix B500 haqida tavsif', 3, '3440000.00'), (
    #                     'Monoblok Asus V222FBK-BA009M',
    #                     'https://olcha.uz/image/original/products/gYDdrAriYVDoFwNSnoNqY67HsirlIc5TmIGsS4ZcyNT16NJtbxq0HF7Djg7K.jpeg',
    #                     "Monoblok Asus V222FBK-BA009M haqida tavsif\r\n\r\nMonoblok ASUS Vivo AiO V222FBK - cheklovlarsiz ishlash\r\n\r\n21,5 dyuymli ASUS Vivo AiO V222FBK birma-birligi foydalanuvchi uchun multimediya va mahsuldorlik uchun yangi imkoniyatlarni ochib beradi. Bu kompyuter o'zining zamonaviy uslubi, 2 mm NanoEdge displeyi, murosasiz ishlashi va SonicMaster texnologiyasi tomonidan boshqariladigan bosh refleksli karnaylari bilan ajoyib ovozi bilan sizni xursand qiladi.\r\n\r\nSiz orzu qilishingiz mumkin bo'lgan dizayn\r\n\r\nKompyuter murakkab va murakkab uslubda yaratilgan. All-in-one shaxsiy kompyuterida alyuminiydan yasalgan nafis stend bor, u nafaqat zamonaviy ko'rinishga ega va kompyuteringizni ishonchli ushlab turadi, balki qulay ekran burchagini osongina tanlash va to'g'rilash imkonini beradi.\r\n\r\nNanoEdge displeyi - tasvirga yangicha qarang\r\n\r\nZamonaviy, yuqori sifatli NanoEdge displeyi yordamida siz har bir kadrdan to'liq bahramand bo'lishingiz mumkin. All-in-one 1920 x 1080 pikselli Full HD tasvir formatiga ega, natijada har bir kadr aniq, aniq va boy tasvirlarga ega bo'ladi. Ekran butun tananing 87% ni egallaydi - bu kompyuterning o'yin -kulgilarida yoki filmlarida ishtirok etishning maksimal ta'sirini va unutilmas ijobiy video tajribasini ta'minlaydi.\r\n\r\nHar bir ramka mukammal bo'ladi\r\n\r\nKompyuterdan ish, o'yin yoki video tomosha qilish uchun foydalanayapsizmi, Full HD tasvirlardan zavqlaning. Displey sRGB spektrining 100% ranglari va ranglarini ko'rsatishga qodir - bu real va yuqori kontrastli tasvirlar uchun kalit. Tru2Life Video va Splendid xususiy ikkita texnologiyasidan foydalangan holda, foydalanuvchi monitorni ko'rsatiladigan tarkibga muvofiq bir necha soniya ichida sozlashi mumkin, bu esa unutilmas ko'rish zavqlanishini kafolatlaydi.",
    #                     6, '6115000.00'), ('Noutbuk Dell XPS 15 (9500)',
    #                                        'https://olcha.uz/image/original/products/mlqVoy89MrXcG26bInsZGHAdSeQeNR45BqUE2f9M4evxj8uXhY1S5A4xrr5T.jpeg',
    #                                        'Noutbuk Dell XPS 15 (9500) Core i5-10300H 8GB/512GB SSD 15.6" (N097XPS9500UZ_WH) haqida tavsif\r\nDell XPS 9500 noutbuki ajoyib 15,6 dyuymli displey, kuchli Intel Core i5 10300H (Comet Lake) 2,5 gigagertsli protsessor va MAX-Q dizayndagi yaxshi NVIDIA GeForce® GTX 1650Ti grafik kartasi bilan jihozlangan. XPS 9500 chiroyli dizaynga ega va ko\'pincha noutbukdan dam olish va ish uchun foydalanadigan mijozlar orasida mashhurdir. Dell XPS 9500 noutbuklari ranglarning keng assortimenti, mustahkam shassilari va boy paketlari bilan mashhur.',
    #                                        4, '25059000.00'), ('Acer A315-34-C38Y',
    #                                                            'https://olcha.uz/image/original/products/jNbRXu1Bqcga6yyJkkTTHJ2OTUVculhjLsOQpmGPnfUs8AVhkmoxMnilQbUZ.jpeg',
    #                                                            "Acer A315-34-C38Y umumiy ma'lumotlar\r\n\r\nUmumiy ma’lumot\r\nProtsessor yadrolari soni: 2 yadro\r\nTezkor xotira: 4 GB DDR4\r\nHard disk: 256GB SSD\r\nVeb-kamera: Mavjud\r\nDispley kengligi:1366 x 768\r\nO‘rnatilgan OT: Windows 10\r\nKesh-xotira: 4 MB\r\nProtsessor:Intel Celeron N4020\r\n\r\nAloqa\r\nSimsiz aloqa: Wi-Fi IEEE 802.11ac, Bluetooth\r\nInterfeyslar: USB 2.0 Type A x 2, USB 3.0 Type A, chiqish HDMI, mikrofon/quloqchinlar Combo\r\n\r\nTa’minot\r\nBatareya: 2 Cell\r\nAkkumulyator: 4810 mAh",
    #                                                            4, '3931000.00'), ('Monitor Samsung U32J590UQI',
    #                                                                               'https://olcha.uz/image/original/products/mx4gykkyM8XOoITju6asaqLSnNBqnp6kS5dgmVKAl4J8EeEQTnqTLT5cLUqS.jpeg',
    #                                                                               'Monitor Samsung U32J590UQI umumiy ma\'lumotlar\r\n\r\nEkran o’lchami: 3840x2160\r\nYangilanish chastotasi: 75 Gts\r\nYoritish: LED\r\nDiagonal: 32"\r\nEkran matrisasi turi: VA\r\nMonitor o’lchami: 698.4x392.85 mm\r\n\r\nEkran\r\nKo’rinish kengligi: Garizontal: 178 °, vertikal: 178 °\r\nKontrastligi: 3000:1\r\nJavob qaytarish vaqti: 4 ms\r\nYorqinligi: 270 kd/m2\r\n\r\nUlanish va ta’minot\r\nQuvvat manbai: Tashqi tomon\r\nQuvvat iste’moli: Kutish rejimida: 59 W, uyqu rejimida: 0.3 W',
    #                                                                               5, '4805000.00'), (
    #                     'Smartfon Realme GT Master Edition 5G',
    #                     'https://olcha.uz/image/original/products/9qxEQu1jXsYHpqye8e76WhC9XghSh0g3bEBBwY7BHbvUfLtwcTNVGyqj1D4Q.jpeg',
    #                     'Smartfon Realme GT Master Edition 5G 6/128GB haqida tavsif\r\n\r\nNaoto Fukasava tomonidan ishlab chiqilgan Realme GT Master Edition 2021 iF Design Award mukofotiga sazovor bo‘ldi. iF Design Award yoki qisqacha iF 1953 yilda ta\'sis etilgan va sanoat dizayni uchun "Oskar" hisoblanadi. Yangi QUALCOMM 778G protsessori Kuchli protsessor smartfon imkoniyatlarini maksimal darajada oshirish uchun yaxshi dasturiy komponentlarga muhtoj. Ajoyib o\'yin tajribasi uchun apparat va xususiy GT Master Edition dasturiy ta\'minotining kuchli kombinatsiyasi. 64 megapikselli uch kamerali kamera va 32 megapikselli selfi kamerasi realme GT Master Edition smartfonining kameralari foydalanuvchiga badiiy fotografiyada eng yaxshi foydalanuvchi tajribasi uchun yuqori aniqlik, maksimal tafsilotlar va eng so‘nggi foto rejimlari ro‘yxatini kafolatlaydi. Tez quvvatlash SUPERDART 65W. SuperDart Charge 65W xususiy tez zaryadlash texnologiyasi smartfoningizni tez va xavfsiz zaryadlashni taʼminlaydi. Smartfoningizga tez zaryadlovchi tarmoq zaryadlovchi qurilmasi kiritilgan.',
    #                     8, '3549000.00'), ('Apple Iphone 13 Mini 512 GB Midnight',
    #                                        'https://olcha.uz/image/original/products/UsyqYtIa8OK5FR3JjsXaWcZ8wy0RsVpR9XXixqBYZ7snOBY1a15w2PKEJvNG.jpeg',
    #                                        'Apple Iphone 13 Mini 512 GB Midnight haqida tavsif', 8, '13541000.00'), (
    #                     'Simsiz quloqchinlar Apple Airpods 3',
    #                     'https://olcha.uz/image/original/products/7auI1gNuna59uO9BHlEKrpeE331EagMB8DxHIseJpynkrfcFLU03dlvEked0.jpeg',
    #                     "Simsiz quloqchinlar Apple Airpods 3 umumiy ma'lumotlar", 9, '2675000.00'), (
    #                     'Power Bank Olmio Mimi-20',
    #                     'https://olcha.uz/image/original/products/1Bom9WrPiK4W9bv1zkXlJlo34byw52YUxuaoBRzcZL8VqoFcIM5SKr4Hy5UQ.jpeg',
    #                     "Power Bank Olmio Mimi-20 20000mAh haqida tavsif\r\nOlmio MINI-20 tashqi batareyasi - bu sizning smartfoningiz uchun cho'ntak hajmidagi energiya manbai. Nafaqat telefonlarni, balki planshetlarni, elektron kitoblarni, MP3 pleerlarni va boshqa ko'chma mobil qurilmalarni ham zaryadlash uchun javob beradi.\r\n\r\nJuda katta quvvat banki, quvvati - 20000 mA / soat. Shu bilan birga, akkumulyator juda ixcham, plastik kartadan biroz kattaroq, o'lchamlari - 124 × 68 × 28 mm.\r\n\r\nTez zaryadlanadi, chunki maksimal chiqish oqimi 2,1 A ga etadi.\r\n\r\nIkki USB quyida joylashgan portlar bir vaqtning o'zida bir juft mobil qurilmani quvvatlantirishga imkon beradi.\r\n\r\nOlmio MINI-20 ko'chma akkumulyatoridan foydalanish oson va bir vaqtning o'zida ikkita qurilmani zaryad qilish imkoniyatini beradi. zaryad darajasining past og'irligi va LED ko'rsatkichiga ega. USB-microUSB kabeli bilan sotiladi. Haddan tashqari issiqlik, ortiqcha yuk va qisqa tutashuvlarga qarshi himoya chip bilan jihozlangan. Mahsulot ishlab chiqaruvchining kafolati bilan qoplanadi.",
    #                     9, '218000.00'), ('Muller WDSD814ML',
    #                                       'https://olcha.uz/image/original/products/recp0ixahjUD5G1jbUZzm0Z9JaWFO47SX28ICdBaeGngAVy2mzRWVai6JlBT.jpeg',
    #                                       "Kir yuvish mashinasi Muller WDSD814ML\r\n\r\nKir yuvish mashinasi - to'qimachilik mahsulotlarini (kiyim, ichki kiyim va choyshablar, sumkalar va boshqa narsalar), ba'zan esa poyabzallarni yuvish uchun o'rnatish.",
    #                                       9, '5132000.00'),
    #                 ('Ziffler ZE6-1008S (6kg)',
    #                  'https://olcha.uz/image/original/products/CLorJeQxofVQcp2GbbVtKyxy8lRm33kyvtcPv0cHC562Cjxggdw5lXov9Z2b.jpeg',
    #                  "Kir yuvish mashinasi Ziffler ZE6-1008S (6kg) umumiy ma'lumotlar", 9, '3483000.00'), (
    #                     'Artel Everest 12HE',
    #                     'https://olcha.uz/image/original/products/ehY12N5aEqXMUk2pEsTljvKnywKcubXwClVhQ69HrsyttwuPbq5MaWQ1mUPu.jpeg',
    #                     "Konditsioner Artel Everest 12HE haqida tavsif\r\nArtel Everest 12HE devorga o'rnatiladigan konditsioner\r\n\r\nKonditsioner mamlakatimiz iqlim sharoitiga to‘liq moslashgan. U Turbo ishlash rejimida ishlashi mumkin, agar elektr bilan bog'liq muammolar yuzaga kelsa, u avtomatik ravishda yoqiladi va avval o'rnatilgan rejimni avtomatik ravishda qayta sozlaydi.",
    #                     10, '5143000.00'), ('Polaris PMH 1584',
    #                                         'https://olcha.uz/image/original/products/h72BtNXXOCZ78fqyC3TTKHrqRUxxqHOGfKHUUVKifKjPilOJCspW4PYhexkS.jpeg',
    #                                         "Infraqizil - konvektsion isitgich Polaris PMH 1584 umumiy ma'lumotlar", 10,
    #                                         '1114000.00')]
    #
    # await db.insert_product(product_list)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
