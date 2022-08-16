yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul.".split()

print(yazi)
print(yazi[0])
print(yazi[3])
print(yazi[3][0])

sayilar = [1,2,3,4,5,6]
sonuc = sayilar
print(sonuc)
print(sonuc[0])

sonuc = sayilar[0]
print(sonuc)

sonuc = sayilar
print(sonuc[3])



isimler = ["Mert", "Ceyda", "Kerem", "Aslı"]
print(isimler[0])
print(type(isimler))
sonuc = isimler[1]
print(sonuc)
print(type(sonuc))
print(type(sonuc[0]))
print(type(isimler[2]))


listeOmer = ["Ömer Can",20]
listeEmre = ["İsrafil Emre",19]

print(listeOmer[0])
print(listeEmre[1])
sonuc = listeOmer[1]
print(sonuc)


ogrenciler = [["İsrafil Emre", 19],["Ömer Can", 20]]
print(ogrenciler)
print(ogrenciler[1])
print(ogrenciler[0][1])

ogrenciler = [listeEmre,listeOmer]
print(ogrenciler)
print(ogrenciler[1])
print(ogrenciler[1][0])
