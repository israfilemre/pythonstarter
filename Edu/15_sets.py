# lists # changing and sorting the values.
# tuples # can't be changed. works faster because of not having updates.
# dictionaries # stores as keys and values.

# # # sets # can't be indexed, changed or sorted. more stable than tuples. works more faster.

# # defining the set

markalar = {"Audi","Mercedes","BMW","Honda"}
markalar2 = {"Renault","Toyota","Mazda"}

# sonuc = markalar[0] # 'set' object is not subscriptable.
# print(sonuc)


# # examination
 
sonuc = "BMW" in markalar
print(sonuc)

markalar.add("Opel")
print(markalar)

markalar.update(["Toyota","Skoda"])
print(markalar)

# print(len(markalar))

# markalar.remove("Opel")
# print(markalar)

# sonuc = markalar.pop()
# print(sonuc)
# print(markalar)

# markalar.clear()
# print(markalar)

# sonuc = markalar.union(markalar2)
# print(sonuc)

