num =int(input("enter your numbeer : "))


def count_num_char(x):
    if x == 0:
        return 1
    count = 0
    while x != 0:
        x = x // 10
        count += 1
    return count

output = count_num_char(num)

print(output)