


def stastivcal_calclulation()-> None:
    num = list(map(int, input("enter : ").split()))
    num.sort()
    print( num)
    n = len(num)
    output = 0
    result = 0
    is_repeat = True

    while is_repeat:
        cal_type = input(" what type of calculuation you wana do (mean,median,mode) : ").lower()
        if cal_type == 'mean':
            
            for i in num:
                output +=i
            result = output/n
            print(result)
            
        elif cal_type == 'median':
            if n%2 == 0:
                m_1= num[n//2]
                m_2 = num[n//2+1]
                result = (m_1+m_2)/2
            
            else:
                mid = (n+1)//2
                result = num[mid]
            print(result)
            
        elif cal_type == 'mode':
            result = max(set(num), key=num.count) if num else None
            print(result)
        
        else:
            print("invalid input")
            break

    return

y = stastivcal_calclulation()
print(y)

