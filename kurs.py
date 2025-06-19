# for i in range(1,100):
#     if i % 2 == 0:
#         print(i)
# juftlar = []
# toqlar = []
# tcount = 0
# jcount = 0
# for i in range(10):
#
#     a = int(input(f"{i + 1} - Sonni kiriting: "))
#     if a % 2 == 0:
#         juftlar.append(a)
#         jcount +=1
#     else:
#         toqlar.append(a)
#         tcount +=1
# print(f"Juftlari: {juftlar} soni {jcount}, Toqlari: {toqlar} soni {tcount}")
# uchga = []
# beshga = []
# ucount = 0
# bcount = 0
# for i in range(1,1000):
#     if i % 3 == 0:
#         uchga.append(i)
#         ucount += 1
#     elif i % 5 == 0:
#         beshga.append(i)
#         bcount += 1
# print(f"Uchga karrali sonlar: {uchga} soni {ucount}"
# f"\nBeshga karrali sonlar {beshga} soni {bcount} ")
#
# natija = True
# while natija:
#     parol = 'Akmalbek888'
#     kiritish = input("Parolni kiriting: ")
#     if parol.lower() != kiritish.lower():
#         print(f"Siz kiritgan parol = [{kiritish}] - noto'g'ri")
#     else:
#         print(f"Siz kirtgan parol - [{kiritish}] - to'g'ri")
#         natija = False

# kirtish = input("Matnni kiriting: ")
# sana = 0
# for i in kirtish:
#
#     if i.lower() == 'u' or i.lower() == 'a' or i.lower() == "o'" or i.lower() == 'o' or i.lower()== 'e' or i.lower() == 'i':
#         sana +=1
#
# print(sana)

# for i in range(1,21):
#     s = pow(i,2)
#     print(s)
# for i in range(1, 101):
#     if i % 7 == 0:
#         continue
#     print(i)
# son = 1
#
# while True:
#     javob = input(f"{son} → Davom etish uchun Enter, to‘xtatish uchun 'stop' deb yozing: ")
#     if javob.lower() == 'stop':
#         break
#     son += 1

# son = [4, 7, 1, 9, 3]
# max1 = son[0]
# min1 = son[0]
# for i in son:
#
#     if i > max1:
#         max1 = i
#     if i < min1 :
#         min1 = i
# print(max1,min1)

# sonlar = input("Sonlarnio kirting: ")
# osish = []
# max = 0
# for i in sonlar:
#     if i.isdigit():
#         osish.append(int(i))
# osish.sort()
# print(osish)
### split() matlardan iborat list hosil qiladi
# a = input("soz")
# part = a.split()
# print(part,len(part))

# kiritish = input("To'liq FIO ni kiriting: ")
# parts = kiritish.strip().split() # uchta elementdan iborat list hosil qilinidi split() orqali va strip() bo'shliq ni olib tashladi
# print(parts)
# if len(parts) == 3:
#     familiya = parts[0].title()
#     space = ""
#     for i in range(1,3):
#         space += parts[i][0].upper() + '.'
# print(f"{familiya} {space}")

# def tub_sonlar(min,max):
#     sonlar = []
#     for n in range(min,max + 1):
#         javob  = True
#         if n == 1:
#             javob = False
#         elif n == 2:
#             javob = True
#         else:
#             for x in range(2,n):
#                 if n % x == 0:
#                     javob = False
#         if javob:
#             sonlar.append(n)
#
#     return sonlar
# print(tub_sonlar(1,100))

# matn = "Salom123dunyo45"
# sanash = 0
# son = ''
# for i in matn:
#     if i.isdigit():
#         son += i
#     else:
#         if son:
#             sanash += int(son)
#             son =''
# if son:
#     sanash +=int(son)
#
# print(sanash)

# soz = 'Akmal Atabayev Anvarovich'
# parts = soz.strip().split()
# print(len(parts))

# son = [4, 2, 4, 6, 4, 2, 3]
# sanash = 0
# for i in son:
#     if son.count(i) > 1:
#         print(i)
