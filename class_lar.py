# """ Tashqaridan kirib kelgan classlarni ko'rish dir"""
# """Atributlarni o'zgartirish uchun methodn (set) bilan ko'rish uchun esa (get) bilan yozish kerak"""
# # class Talaba:
#
# #     def __init__(self, ism, familiya, tyil):
# #         """Talaba klassining asosiy atributlarini belgilaydi."""
# #         self.name = ism
# #         self.surename = familiya
# #         self.year = tyil
# #
# #     def lastname(self):
# #         """Talabaning familiyasini qaytaradi."""
# #         return self.surename
# #
# #     def talaba_yoshi(self, yil):
# #         """Berilgan yilga nisbatan talabani yoshini hisoblaydi."""
# #         return yil - self.year
# #
# #     def get_name(self):
# #         """Talabaning ismini qaytaradi."""
# #         return self.name
# #
# #     def tanishtir(self):
# #         """Talabani tanishtiradi (ism, familiya, tug‘ilgan yil)."""
# #         return f"Mening ismim {self.name}, familiyam: {self.surename}, tug'ilgan yilim: {self.year}"
# #
# # talaba1 = Talaba("Akmal","Atabayev",2000)
# # print(talaba1.get_name())
# # print(talaba1.talaba_yoshi(2025))
# # print(talaba1.lastname())
# # print(talaba1.tanishtir())
#
# class Talaba:
#     def __init__(self, ism, familiya, tyil):
#         """Talaba klassining asosiy atributlarini belgilaydi."""
#         self.name = ism
#         self.surename = familiya
#         self.year = tyil
#         self.bosqich = 1
#
#
#     def set_bosqich(self,yangi_bosqich):
#             """Talabaning kursini o'zgartiruvchi method"""
#             self.bosqich = yangi_bosqich
#
#     def update_bosqich(self):
#         """Bosqichni yangilash"""
#         self.bosqich += 1
#
#     def get_info(self):
#         return f"Ismi {self.name} Familiya {self.surename} Tug'ilgan yili:{self.year} Kurs: {self.bosqich}"
#
#     def talaba_yoshi(self, yil):
#             """Berilgan yilga nisbatan talabani yoshini hisoblaydi."""
#             return yil - self.year
#
# talaba1 = Talaba("Akmal","Atabayev",2004)
# # talaba1.set_bosqich(3)
# # talaba1.update_bosqich()
# # print(talaba1.get_info())
#
# class Fan:
#
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
#
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni +=1
#
#     def get_fan(self):
#         """ Fan nomi """
#         return self.nomi
#
#     def get_students(self):
#         """ Fanga yozilgan talabalar haqida ma'lumotlar """
#         return [ talaba.get_info() for talaba in self.talabalar ]
# # print(dir(Talaba))
# matem = Fan("Oliy matematika")
# matem.add_student(talaba1)
# print(matem.talabalar)

class Avto:

    def __init__(self,model,rang,karobka,narh,):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.kilometr = 0

    def get_info(self):
       """Hususiyatlari """
       return f"Model: {self.model} Rangi: {self.rang} karobka: {self.karobka} narhi: {self.narh} Kilometri: {self.kilometr}"

    def set_kilometr(self,yangi_kilometr):
        """KIlometrini  qo'lda kiritadi"""
        self.kilometr = yangi_kilometr


avto1 = Avto("Malibu","qora","Mexanik",30000)
avto1.set_kilometr(30000)
print(avto1.get_info())

class Avtosalon:
    def __init__(self,salon_nomi,manzili,sotuvdagi_avtomobillar):
        """Class atributlari yani hususiyatlari"""
        self.salon_nomi = salon_nomi
        self.manzili =manzili
        self.sotuvdagi_avtolar = sotuvdagi_avtomobillar
        self.avtomobillar_soni  = 0
        self.avtomobillar = []

    def add_avtomobiler(self,mashina):
        """Yangi mashina qo'shish"""
        self.avtomobillar.append(mashina)
        self.avtomobillar_soni += 1

    def get_info_avto(self):
        """Salondagi mashinalarning ma'lumotalrini qaytaradi"""
        return [avto.get_info() for avto in self.avtomobillar]

Avtosalon1 =Avtosalon("GM","Toshkent","kobalt")
avto2 = Avto("Nexia 2","oq","mexanika",6000)

Avtosalon1.add_avtomobiler(avto1)
Avtosalon1.add_avtomobiler(avto2)
print(Avtosalon1.get_info_avto())

