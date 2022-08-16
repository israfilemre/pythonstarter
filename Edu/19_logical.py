
# And operator

x = -15
# sonuc = 10 < x < 20


sonuc = (x > 10) and (x < 20)

# True and True => True
# True and False => False
# False and False => False

karne_notu = 90
devamsizlik = 13

sonuc = (karne_notu >= 50) and (devamsizlik < 10)


# Or operator

# True or True => True
# True or False => True
# False or False => False

sonuc = (x < 10) or (x % 3 == 0)

# Not Operator

sonuc = not(x > 0)

ceza_bilgisi = False

sonuc = (karne_notu >= 85) and (devamsizlik < 10) and (ceza_bilgisi == False)

print(sonuc)
