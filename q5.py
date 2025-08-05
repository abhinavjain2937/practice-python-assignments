def calculation():

    num = int(input("enter the number till you wana add: "))
    sum_2 = 0
    sum_1 = 2
    for i in range(1, num+1):

        sum_2+=sum_1
        sum_1 += 2 * 10**i
        i+=1
    return sum_2

output = calculation()
print(output)

