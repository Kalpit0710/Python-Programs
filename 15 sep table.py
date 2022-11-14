'''n=int(input("Enter the number: "))
for i in range (1,1001):
    print(n,"*",i,"=",n*i)'''

n=int(input("Enter the number: "))
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print(" ")