

def multiplication (num:list):
    '''Given an integer array nums, return an array answer such that answer[i] is equal to theproduct of all the elements of nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.'''
    mul = {0:1}
    ans = []
    for i in num:
        if i == 0:
            mul[1] = 0
            continue
        else:
            mul[0] = mul[0]*i
    for i in num:
        if i == 0:
            req = mul[0]
            ans.append(req)
        else:
            req = mul[1]//i
            ans.append(req)

    return ans

    



number1= [1,2,3,4]
number2 = [-1,1,0,-3,3]


output = multiplication(number2)
print(output)
  