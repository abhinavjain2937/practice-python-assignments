num = list(map(int ,input("enter a number: ").split()))

output = []

for n in num:
    if n > 500:
        break
    if n % 5 == 0:
        output.append(n)
    if n > 150:
        continue

print(f"hte output is : {output}")