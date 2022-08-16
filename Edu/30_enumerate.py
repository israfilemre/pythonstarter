
languages = ["Python","JavaScript","Flutter"]

# index = 0

# for i in languages:
#     print(f"{index+1}-{languages[index]}")
#     index += 1


# # enumerate method

object = enumerate(languages)

print(type(object))
print(list(object))


for i in enumerate(languages):
    print(i)


for index,value in enumerate(languages):
    print(f"{index+1}-{value}")


for index,value in enumerate(languages,10):
    print(f"{index}-{value}")

