import random
n=int(input("n=:"))
x=[]
#while True:
#for i in range(n):
while len(x)<n:
    r=random.randint(0,n)
    if r not in x:
       x.append(r)
print(x)