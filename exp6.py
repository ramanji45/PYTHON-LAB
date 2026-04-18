import random
a=random.randrange(91,10)
b=int(input("Guess ano between 1 to 10 untill you bget it right:"))
while b!=a:
    b=int(input("Guess ano between 1 to 10 untill you bget it right:"))
else:
    print("Well Guess:",a)
