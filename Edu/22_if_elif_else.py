
# a = 10
# b = 10

# if (a > b):
#     print("a, b'den büyüktür.")
# elif (a == b):
#     print("a, b'ye eşittir.")
# else:
#     print("b, a'dan büyüktür.")


karne_notu = float((input("Karne notunuzu giriniz: ")))

if (karne_notu >= 0) and (karne_notu < 50):
    print("Sınıf tekrarı almanız gerekmektedir.")
elif (karne_notu >= 50) and (karne_notu < 70):
    print("Bir sonraki sınıfa geçmeye hak kazandınız!")
elif (karne_notu >= 70) and (karne_notu < 85):
    print("Teşekkür Belgesi almaya hak kazandınız!")
elif (karne_notu >= 85) and (karne_notu <= 100):
    print("Takdir belgesi almaya hak kazandınız!")
else:
    print("Karne notunuzu tekrar giriniz!")
