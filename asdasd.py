# def avto_info(kompaniya:str,model,rangi,karobka,yili,narhi = None):
#     "Avtomobil ma'lumotlari"
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rangi": rangi,
#         "karobka":karobka,
#         "yili":yili,
#         "narh" : narhi
#     }
#     return avto
#
# avto1 = avto_info("GM","Malibu","Qora","mexanik","2015")
# avto2 = avto_info("GM","Nexia","Qora","mexanik","2015",5_000_000)
# avtolar = [avto1,avto2]
# print(avtolar[0]['model'])
# print("Onalyn bozorda bor mashinalar")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto1["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rangi']} {avto['model']}.Narh: {narh}")
#
# # def oraliq(min,max,qadam = ''):
# #     "Rangeni qo'lbola ver"
# #     sonlar = []
# #     while min < max:
# #         if qadam:
# #             sonlar.append(min)
# #             min +=qadam
# #         else:
# #                 sonlar.append(min)
# #                 min +=1
# #     return sonlar
# # print(oraliq(0,10))
# print("Yangi avtolar shaklantiramiza")
# yangi_avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ")
#     kompaniya =input("Kompaniyasi ")
#     model = input("Modeli ")
#     rangi = input("Rangi")
#     karobka = input("Karobka")
#     yili = input("Yili")
#     narh =input("narhi")
#     avtolar.append(avto_info(kompaniya,model,rangi,karobka,yili,narh))
#     javob = input("Yangi avtomabil qo'shasizmi (yes or no) ?")
#     if javob == "no":
#         break
# print("Hamma avtolar")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:narh = "noma'lum"
#       print(f"{avto['rangi']} {avto['model']}.Narh: {narh}")
# def baholash(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"{ism.title()}")
#         baholar[ism] = baho
#     return baholar
#
# talabalar =['ali','vali']
# baholar = baholash(talabalar[:])
# print(baholar)
# def summa(*sonlar):
#     "Bu funksiya sonlarni yig'indisini qaytaradi"
#     yigindi = 0
#     for son in sonlar:
#         yigindi +=son
#     return yigindi
#

# def avyo_info(kompaniya,model,**malumotlar):
#     "Ma'lumotlarni olib lug'at ko'rinishida qaytaradi"
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# avto1 = avyo_info("GM","Malibu",rang='qora',yili=2025)
# print(avto1)

# def summa(*sonlar):
#     "Istalgan sonlarni qabul qiladi va qaytaradi"
#     kopaytma = 1
#     for i in sonlar:
#         kopaytma *= i
#     return kopaytma
# print(summa(2,3,4,5))
# def student_info(ism,familiya,**malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familiya'] = familiya
#     return malumotlar
# print(student_info("Akmal","Atabayev",guruhi='212'))
#
# def about_your(ism:str,familiya:str,t_yil:int,yoshi:int,yashash_manzili:str,tel_raqam:int= None,el_manzili =None):
#     "O'zingiz haqingizdagi ma'lumotlarni olib qaytaradi"
#     haqida = {
#         'ism' :ism,
#         "familiya":familiya,
#         "t_yil":t_yil,
#         "yoshi":yoshi,
#         "yashash_manzili":yashash_manzili,
#         "tel_raqam":tel_raqam,
#         "el_manzili":el_manzili
#
#     }
#     return haqida
# human1 = about_your("Akmal","Atabayev",2004,21,"Qoraqalpo'iston")
# human2 = about_your("Akmal","Atabayev",2004,21,"Qoraqalpo'iston",931607665,"avadvadfv")
# humans = [human1,human2]
# for odam in humans:
#     if odam["tel_raqam"]:
#         raqam = odam['tel_raqam']
#     elif odam['el_manzili']:
#         el_manzili = odam['el_manzili']
#     else:
#         raqam = 'Noma\'lum'
#         el_manzili = 'Noma\'lum'
#     print(f"{odam['ism'].title()} {odam['familiya'].title()} {odam['tel_raqam']}")
# print("\nYangi mijoz qo'shamiza")
# yangi_mijoz = []
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     t_yili = input("Tug'ilgan yili: ")
#     yoshi = input("Yoshi: ")
#     tel_raqami = input("Telefon raqami: " )
#     yashash_manzili = input("Yashash manzili: ")
#     el_manzili = input("Elekron manzili: ")
#     yangi_mijoz.append(about_your(ism,familiya,t_yili,yoshi,tel_raqami,yashash_manzili,el_manzili))
#     javob = input("Yana odamm qo'shasizmi (Y/n)?")
#     if javob == "n":
#         break
# print(yangi_mijoz)
# def kata(a,b,c):
#     "Uchta sonni eng kattasini qaytaradi"
#     return max(a,b,c)
# d = int(input("1 - son: "))
# e = int(input("2 - son: "))
# r = int(input("3 - son: "))
# print(kata(d,e,r))
#
# def hajmi(radius):
#     "Radiusini qabul qilib qolgan qiymatlarni qaytaradi"
#     diametri = 2 * radius
#     yuzi = 3.14 * pow(radius,2)
#     perimetri = 3.14 * 2 * radius
#     aylana = {
#         "radiusi":radius,
#         "diametri" :diametri,
#         'yuzi':yuzi,
#         "perimetri":perimetri,
#     }
#     return aylana
# r = int(input("Aylana radiusini kiriting: "))
# print(hajmi(r))

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if (n == 1):
#             tub = False
#         elif (n == 2):
#             tub = True
#         else:
#             for x in range(2, n):
#                 if (n % x == 0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#
#     return tub_sonlar
#
#
# print(tub_sonlar_top(1, 20))
# def fib(n):
#     "Funksiya fibonachi sonlarini chiqaradi"
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#
#     return sonlar
#
# print(fib(8))

# def yili(ismi:str,yoshi:int):
#     "Foydalanuvchi tomonidan kiritilgan qiymatlarni olib tug'ilgan yilini qaytaradi"
#
#     yili1 = {
#         'ismi':ismi,
#         'yoshi': yoshi,
#         "age" : 2025 - yoshi
#     }
#     return yili1
# odamlar = []
# for i in range(1):
#     ismi = input("Ismingizni kiriting: ")
#     yoshi = int(input("yoshinizni kiriting: "))
#     odamlar.append(yili(ismi,yoshi))
#
# for o in odamlar:
#     print(f"{o['ismi'].title()} yoshi: {o['yoshi']} yili: {o['age']}")

# def kub_and_kvadrat(n):
#     "Foydalanuvchi tomonida kiritilgan sonni kub va kvadratini hisoblaydi"
#     return f"Kvadrati: {pow(n,2)} Kubi: {pow(n,3)}"
# a = int(input(" Sonni kiriting: "))
# print(kub_and_kvadrat(a))

# def couple_or_odd(n):
#     "Foydalanuvchi tomonidan kiritilgan sonlarni juft yoki toq ekanini tekshiradi"
#     if n % 2 == 1:
#         return f"Toq son"
#     else:
#         return f"Juft son"
#
# a = int(input("Sonni kiriting:"))
#
# print(couple_or_odd(a))
# def standar(a ,y = 2):
#     return a,y
# a = int(input("son"))
# y = int(input("son"))
# print(standar(a,y))

# print(f"Bozordan olinadigan narsalar")
# def bozorlik(*malumotlar):
#     "Mahsulotlarni qabul qilib ro'yhatni qaytardi"
#     bozorlik = []
#     narhlangan_mahsulotlar = {}
#     choice1 = True
#     while choice1:
#         bozorlik.append(malumotlar)
#         nomi_bozor = bozorlik.pop()
#         narh = int(input(f"{nomi_bozor} ni bahosi"))
#         print(f"{nomi_bozor} baholandi")
#         narhlangan_mahsulotlar[nomi_bozor] = narh
#         javob = input("Yana qo'shasizmi (y/n)? ")
#         if javob == 'n':
#            choice1 = False
#
#     return narhlangan_mahsulotlar
# nomi = input("Bozorlikni kiriting ?")
# print(bozorlik(nomi))