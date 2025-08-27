num = [56,3,1,4,9,9,12,7]
num.sort()
m = int(input("enter: "))
n = len(num)
dic = {}
count = []


j = 0


while m < n:
    l1 = list(num[j:m])
    diff = max(l1)-min(l1)
    count.append(diff)
    dic[str(l1)] = diff
    print(l1)
    m+=1
    j+=1

print(f" the minimum differance is {min(count)}")
print(dic)

    