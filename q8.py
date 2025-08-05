# factorial  number calculation

def factirial_calculation():
    num = int(input("enter : "))
    j = 1
    for i in range(1,num+1):
        j*=i
    return j


out = factirial_calculation()
print(out)