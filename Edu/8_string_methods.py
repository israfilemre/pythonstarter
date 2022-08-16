
yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.upper()
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.lower()
print(sonuc)

yazi = "hi! my name is israfil emre arslan. i live in maslak, istanbul."

sonuc = yazi.title()
print(sonuc)

yazi = "hi! my name is İsrafil Emre Arslan. i live in Maslak, İstanbul."

sonuc = yazi.capitalize() # It just capitalizes the first letter of the string not each of the sentences' firs letters in the string.
print(sonuc)

yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.isspace()
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.islower()
print(sonuc)


yazi = "hi! my name is israfil emre arslan. i live in maslak, istanbul."

sonuc = yazi.islower()
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.isupper()
print(sonuc)


yazi = "      Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul.           "

sonuc = yazi.strip() # Deletes the spaces from the beginning and the ending of the string.
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.split()
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.split(".")
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.split(" ")
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = "_".join(yazi)
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul.  "

sonuc = "-".join(yazi) # That command does not work in the beginning of the string but it works at the end of the string.
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = " ".join(yazi)
print(sonuc)


yazi = " Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.index(" ")
print(sonuc)


# yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

# sonuc = yazi.index("israfil") -Watch out for the upper and lower letters!
# print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.index("İsrafil")
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.index(" ")
print(sonuc)


# yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

# sonuc = yazi.index() -That does not work.
# print(sonuc)


# yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

# sonuc = yazi.index( ) -That does not work.
# print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.startswith("H")
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.startswith("h")
print(sonuc)


yazi = " Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.startswith(" ")
print(sonuc)


yazi = " Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.startswith("")
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.endswith(".")
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.endswith("l")
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.replace("Maslak", "Sarıyer")
print(sonuc)


yazi = "Hi! My name is İsrafil Emre Arslan. I live in Maslak, İstanbul."

sonuc = yazi.replace("ı", "i").replace("ş", "s") # Replaces some letters.
print(sonuc)



# Visit "https://www.w3schools.com/python/python_ref_string.asp" to train string methods deeply!
 