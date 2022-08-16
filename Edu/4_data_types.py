# int
# float
# str
# bool

age = 20
weight = 53.5
name = 'Ayça'
isStudent = True
isMarried = True

print(type(age))
print(type(weight))
print(type(isStudent))
print(type(name))
print(type(isMarried))


# int to float

result = float(age) # that order do not change the variable of 'age'. 
print(result)
print(age)

age = float(age) # that order change the int variable called 'age' into a float.
print(age)


# float to int

result= int(weight) # deletes the decimal part.
print(result)

# bool to str

result = str(isStudent)
print(result)
print(type(result))

# bool to int

result = int(isStudent)
print(result)
print(type(result))



