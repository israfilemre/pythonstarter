
sayilar = []

liste = [3,8,5,12,40]

# for i in range(10):
#     sayilar.append(i)
# print(sayilar)

# for i in liste:
#     i **= 2
#     sayilar.append(i)
# print(sayilar)


# # [expression for item in list]

sayilar = [i for i in range(10)]
sayilar = [i*2 for i in range(10)]
sayilar = [i/2 for i in range(10)]
sayilar = [i**2 for i in range(10)]

sayilar = [i*2 for i in liste]

print(sayilar)

sonuc = [str(sayi) for sayi in liste] # put every numbers of "liste" into the "sayi" and then convert the new list called "sayi" into strings.

isim = "İsrafil Emre"
isimler = ["Ayça","Emre","Kübra","Refika"]

sonuc = [a.upper() for a in isim]
sonuc = [i.lower() for i in isimler]
sonuc = [b.upper() for b in isimler]

print(sonuc)
