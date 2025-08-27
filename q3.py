
int_arr = [1, 5, 7, -1]
num = 6 #int( input("enter: "))

k = []
j = len(int_arr) - 1
count = 0

for idx,  i in enumerate(int_arr):
    compliment = num - i
    if compliment in int_arr:
        l1 = []
        if ([compliment,i]) not in k:
            l1.append(i)
            l1.append(compliment)
            k.append(l1)
            count+=1

print(k)
print(count)
