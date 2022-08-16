
#  # Application - 1

# sayi = int(input("Sayı giriniz: "))

# if (sayi > 0):
#     if (sayi % 2 == 1):
#         print("Girilen sayı, pozitif tek sayıdır.")
#     else:
#         print("Girilen sayı, pozitif çift sayıdır.")
# elif (sayi == 0):
#     print("0 rakamı işaret ve teklik, çiftlik bakımından değerlendirilemez.")
# else:
#     print("Girilen sayı negatiftir.")


# # Application - 2

# x = float(input("x : "))
# y = float(input("y : "))
# z = float(input("z : "))

# if (x>y) and (x>z):
#     print("x en büyük sayıdır.")
# elif (y>x) and (y>z):
#     print("y en büyük sayıdır.")
# elif (z>x) and (z>y):
#     print("z en büyük sayıdır.")


# # Application - 3

isim = input("İsim : ")
yas = int(input("Yaş : "))
egitim = input("Eğitim : ")

if (yas >= 18):
    if (egitim == "Lise" or egitim == "Üniversite"):
        print("Ehliyet alabilirsiniz.")
    else:
        print(f'Sayın {isim}, ehliyet alamazsınız çünkü eğitim durumunuz yetersizdir.')
else:
    print(f'Sayın {isim}, ehliyet alamazsınız çünkü yaşınız tutmuyor.')
