
list1 = [1,3,5,14,3]
thistuple = (1,2,"altı",False,2)
thistuple2 = (1,4,"beş",True,2)

print(type(list1))
print(type(thistuple))

print(list1[1])
print(thistuple[2])

print(len(list1))
print(len(thistuple))

list1[0] = 5


list1.append(45)

print(list1)

# thistuple[2] = "beş" # you can't change the tuple.

# thistuple.append(23) # you can't append to the tuple.

print(list1.count(3))
print(thistuple.count(2))

print(thistuple + thistuple2)

# We use "[]" for lists.
# We use "()" for tuples. it is not necessary but recommended.

list2 = tuple([6,8,3,12])

print(type(list2))

print(list2)


