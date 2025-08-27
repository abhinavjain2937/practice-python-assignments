def roman_to_number(string):
    rv ={
        'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
    }

    result = 0
      

    for  i in range(len(string)-1):
        if rv[string[i]] < rv[string[i+1]]:
            j = rv[string[i+1]] - rv[string[i]]
            result+=j
        
        elif rv[string[i]] >= rv[string[i+1]]:
            result += rv[string[i]]
        elif rv[string[i+1]] == None:
            result+=rv[string[i+1]]
            

    return result


string = input("enter: ").upper().split()
out = roman_to_number(string)
print(out)
print(string)