import random
a=int(input("Enter lower range: "))
b=int(input("Enter upper range: "))
i=random.randint(a,b+1)
print("The number is",i)

def odd():
    if (i % 2) == 0:
        print("The number",i,"is even")
    else:
        print("The number",i,"is odd")
odd()
def neg():
    if i==0:
        print("The number is zero")
    elif i<0:
        print("The number",i,"is negative")
    else:
        print("The number",i,"is positive")
neg()
def prime():
    if i > 1:
        for a in range(2, i):
            if (i % a) == 0:
                print(i, "is NOT a prime number")
                break
        else:
            print(i, "is a PRIME number")
    elif i == 0 or 1:
        print(i, "is neither a prime NOR composite number")
    else:
        print(i, "is a COMPOSITE number")
prime()