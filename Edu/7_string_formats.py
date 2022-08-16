
name = "İsrafil Emre"
surname = "Arslan"
age = 36

print("My name is {} {}.".format(name,surname))
print("My name is {} {}. I am {}.".format(name,surname,age))
print("My name is {s} {n}. I am {a}.".format(n=name,s=surname,a=age))
print("My name is {1} {0}. I am {2}. {2}".format(name,surname,age))


number = 5 / 3
print("The result is {n:1.3}.".format(n=number))
print("The result is {n:1.1}.".format(n=number))
print("The result is {n:1.6}.".format(n=number))
# print("The result is {n:1.}.".format(n=number))   That does not work.
# print("The result is {n:1}.".format(n=number)) The result continues with the decimal points.
# print("The result is {n:1.0}.".format(n=number)) The result is the same with the code including n:1.1


print(f"My name is {surname} {name}. I am {age}.") # That command line is described as "f-string method".




