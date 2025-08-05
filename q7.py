num = list(map(int ,input("enter a number: ").split()))
a =[]
for n in range (len(num)):
    if n % 2 ==0 :
        continue
    else:
        number = num[n]
        a.append(number)

print(a)



