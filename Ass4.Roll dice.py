import random
print("wellcome to Dice Roll Game")

n=random.randint(1,6)
print(n)

if n<6:
        print("try again")
while n==6:
    print("well down")
    print(n)
    n=random.randint(1,6)
    if n<6:
        exit
