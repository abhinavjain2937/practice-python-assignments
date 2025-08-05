num = '1234' #input("enter : ")
a = []
b = ''

for i in num:
    a.append(i)
n = len(a)
print(n)
for j in range (len(a)):
    print(j)
    b += a[n-j-1]
    print(b)





