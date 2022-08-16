
# for item in liste:
#     if (condition):
#         expression


#  [expression for item in liste if condition]

sayilar = [1,3,7,12,22,34]
sonuc = []

for sayi in sayilar:
    if (sayi % 2 == 0):
        sonuc.append(sayi)


sonuc = [sayi for sayi in sayilar if sayi % 2 == 0]
# sonuc = [sayi for sayi in sayilar if sayi % 2 == 1 else "Çift Sayı"] ! it does not work !
sonuc = [sayi if sayi % 2 == 1 else "Çift Sayı" for sayi in sayilar] 

print(sonuc)
