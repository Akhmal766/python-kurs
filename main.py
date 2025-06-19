# import avto_info_mod
# import avto_info_mod as aim
# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)
# from avto_info_mod import avto_info as ainf,info_print as iprint #funkiyalar nomini as orqali o'zgartirdik
# avto1 = ainf("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)
import math
import random as r

# son = r.randint(0,55)
# print(son)

#choice ichidan tnalaydi
# ismlar = ["Akmal","Sanjar","Vali"]
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

#shuffle aralashtirib tashlaydi
# x = list(range(11,22))
# print(x)
# r.shuffle(x)
# print(x)

#labda Pythonning o'ziga xos xususiyatlaridan biri, nomsiz vaqtinchalik funksiyalar yaratish imkoniyati. Bunday funksiyalarni yaratishda def operatori o'rniga lambda operatori ishlatilgani uchun ham lambda funskiyalar deb ataladi.
# import math
# uzunlik = lambda pi, r : 2 * pi * r
# print(uzunlik(math.pi,10))
# def daraja(n):
#     return lambda x : x**n
#
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

#map
# son = list(range(1,10))
# ildizlar = list(map(math.sqrt,son))
# print(ildizlar)

# sonlar = list(range(1,10))
# ildizlar = list(map(math.sqrt,sonlar))
# print(ildizlar)
#
# kvadratlar = list(map(lambda x: x * x,sonlar))
# print(kvadratlar)

# a = [3,4,6,8]
# b = [1,2,5,7,9]
#
# a_plus_b = list(map(lambda x,y:x + y ,a,b))
# print(a_plus_b)

#filter() harqanday malumotlarni filterlaydi
#
# import random as r
# sonlar = r.sample(range(100),10)
# print(sonlar)
#
# def juftmi(x):
#     "Sonlarni qabul qilib juf bo'lsa true qaytaradi"
#     return x % 2 == 0
# juft_sonlar = list(filter(lambda x:x % 2 == 0,sonlar))

# class kompyuter:
#     def __init__(self,ram,hdd,gpu,CPU):
#         self.ram = ram
#         self.hdd = hdd
#         self.gpu = gpu
#         self.CPU = CPU
#     def info(self):
#         inf  = f"RAM: {self.ram} HDD: {self.hdd} GPU: {self.gpu} CPU: {self.CPU}"
#         return inf
#
# macbook = kompyuter("16gb","512GB","M1","M1")
# print(macbook.info())


