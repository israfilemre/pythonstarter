
iller = ["Balıkesir","İstanbul","Erzurum","İzmir"]

sonuc = iller
sonuc = iller[0]
sonuc = iller[0:3]
sonuc = iller[0:]
sonuc = iller[-3:]
sonuc = iller[-3:-1]
sonuc = iller[:3]
sonuc = iller

# print(sonuc)
# print(iller[0])

# sonuc = len(iller)
# print(sonuc)

# del iller[0]
# print(iller)
# del iller[0:2]
# print(iller)

# iller[1] = "Balıkesir"
# iller[-1] = "Ankara"
# print(iller)

sonuc = iller + ["Adana","Tekirdağ","Aksaray"]
del iller[0] # "iller" variable had been changed before this line got written. So the variable "sonuc" remains the same after this line.


print(sonuc)
print(iller)

