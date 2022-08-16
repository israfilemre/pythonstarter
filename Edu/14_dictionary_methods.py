
arabaAudi = {
    "marka" : "Audi",
    "model" : "A6",
    "yil" : 2021
}


# # reaching the values

# sonuc = arabaAudi["marka"] # key to value
# sonuc = arabaAudi.get("marka")


# print(sonuc)


# # examination of operations

# sonuc = "marka" in arabaAudi
# print(sonuc)

# sonuc = "marka2" in arabaAudi
# print(sonuc)

# sonuc = len(arabaAudi)
# print(sonuc)


# # addition operations

# arabaAudi["renk"] = "beyaz"
# print(arabaAudi)


# # deleting operations

# arabaAudi.pop("yil")
# print(arabaAudi)

# arabaAudi.popitem()
# print(arabaAudi)

# del arabaAudi["marka"]
# print(arabaAudi)

# del arabaAudi
# print(arabaAudi)

# arabaAudi.clear()
# print(arabaAudi)


# # duplicating the objects

# araba = arabaAudi.copy()
# print(araba)

# araba["marka"] = "Mercedes"

# print(araba)
# print(arabaAudi)


# # updating the values

# arabaAudi.update({
#     "marka" : "BMW",
#     "model" : "X2",
#     "yil" : 2019
# })

# print(arabaAudi)

# arabaAudi.update({
#     "marka" : "BMW",
#     "model" : "X2",
#     "yil" : 2019
# })

# arabaBMW = arabaAudi.copy()

# print(arabaBMW)

