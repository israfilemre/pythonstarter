print (7000 + (7000*0.18))
print (8000 + (8000*0.18))

urun1 = 7000
urun2 = 8500
urun3 = 10000
kdv = 0.18

print(urun1+urun1*kdv)
print(urun2+urun2*kdv)
print(urun3+urun3*kdv)

urun1= float(input("İlk ürünün satış fiyatını giriniz = "))
urun2= float(input("İkinci ürünün satış fiyatını giriniz = "))
urun3= float(input("Üçüncü ürünün satış fiyatını giriniz = "))
kdv= float(input("KDV oranını giriniz = "))

# it also could be an integer.

satis1= urun1+urun1*kdv
satis2= urun2+urun2*kdv  
satis3= urun3+urun3*kdv

print("Birinci ürünün liste fiyatı=",satis1) 
print("İkinci ürünün liste fiyatı=",satis2)
print("Üçüncü ürünün liste fiyatı=",satis3)
#  Check out the last three lines.




# Değişkenler sayıyla başlayamaz, boşluk ve simge içeremez.
# Değişkenlerde Türkçe karakter kullanmamaya özen göstermeliyiz.
# Değişkenler büyük ve küçük harflere duyarlıdır.

a, b, c = 10, 20, 30

print(a)

print(b,c,a)

print(type(c))

name = "Ayça"
print(type(name))
print(name)

isStudent = True
print(type(isStudent))

a, b, name, isStudent = 10, 40, "Ayça", False
print(a, b, isStudent, name)


