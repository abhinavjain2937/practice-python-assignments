inp =list(map (int, input('enter : ').split()))
j = ''
n  = ''
for i in (inp):
    if i < 0 :
        j+=" " + str(i)
    else:
        n+=" " + str(i)



print(f" the outputn is : " , j+n)