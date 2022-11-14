# s="Python Programming"
# p=s.upper()
# print(p)

# for a in s:
#     if a in ['a','e','i','o','u','A','E','I','O','U']:
#         print(a,end=' ')
# print()
# i=input("enter to remove ")
# p=s.replace(i,' ')
# print(p)

# l=['a','e','i','o','u','A','E','I','O','U']
# print(l[5:])
# l[4:]="u"
# print(l)

a=[]
n=int(input(""))
for i in range(1,n+1):
    # b=int(input("Enter "))
    a.append(i)
even=[]
odd=[]
for j in a:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print(even)
print(odd)
l=even.extend(odd)
if a==l:
    print(True)
else:
    print(False)