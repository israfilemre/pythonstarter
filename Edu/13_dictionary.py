
# # 34 => İstanbul
# # 35 => İzmir

# sehirler = ["İstanbul","İzmir"]
# plakalar = [34,35]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(sehirler.index("İstanbul"))

# print(plakalar[sehirler.index("İstanbul")])
# print(plakalar[sehirler.index("İzmir")])


# # key - value (key to value).

# plakalar = {"İzmir": 35,"İstanbul": 34}

# print(plakalar["İzmir"])
# print(plakalar["İstanbul"])

# plakalar["Eskişehir"] = 26
# plakalar["Bursa"] = 16
# print(plakalar)

urunler = {
    100: {
        "urunAdi": "Monitör",
        "urunAciklamasi": "16 inç",
        "garantiSuresi": 3,
        "fiyati": [800,944]
    },
    101: {
        "urunAdi": "SSD",
        "urunAciklamasi": "256 GB",
        "garantiSuresi": 2,
        "fiyati": [1500,1770]
    }
}

# sonuc = urunler

# print(urunler)
# print(type(urunler))

# sonuc = urunler[100]["fiyati"]

# print(sonuc)

tutar = urunler[100]["fiyati"][1] + urunler[101]["fiyati"][1]


print(tutar)
