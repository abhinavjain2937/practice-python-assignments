
def req (num):
    x= []
    n = len(num)
    for i in range(n):
        for j in range(i+1):
            for k in range(j+1):
                if i!= j and j!=k and i!=k and num[i]+num[j]+num[k] == 0:
                    l1 = []
                    if num[i] and num[j] and num[k] not in x:

                        l1.append(num[i])
                        l1.append(num[j])
                        l1.append(num[k])
                        x.append(l1)
    return x





number = [-1,0,1,2,-1,-4]

output = req(number)
print(output)


