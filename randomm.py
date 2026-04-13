import random
a=random.randint(1,50)
l=int(input("Enter length of password: "))
b=""
for i in range(l):
    b+=random.choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*QWERTYUIOPASDFGHJKLZXCVBNM")
print(a)
print(b)
