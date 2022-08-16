
isim = "İsrafil Emre Arslan"

for harf in isim:
    if (harf == "E") or (harf == "e"):
        break
    print(harf)


# i = 0

# while (i < 10):
#     i += 1
#     if (i ==5):
#         continue
#     print(i)
# print("Döngü bitti!")


# # The summation of the odd numbers between 0 and 101

# i = 0
# toplam = 0

# while (i < 100):
#     i += 1
#     if (i % 2 == 0):
#         continue
#     toplam += i
# print(f"Genel Toplam: {toplam}")


# The summation of the even numbers between 0 and 101

i = 0
toplam = 0

while (i < 100):
    i += 1
    if (i % 2 == 1):
        continue
    toplam += i
print(f"Genel Toplam: {toplam}")
