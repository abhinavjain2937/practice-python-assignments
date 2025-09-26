# class SparseVector:
#     def __init__(self, nums):
#         self.data = {i: num for i, num in enumerate(nums) if num != 0}

#     def dotProduct(self, vec):
#         result = 0
#         for i in self.data:
#             if i in vec.data:
#                 result += self.data[i] * vec.data[i]
#         return result

# nums1 = [1, 0, 0, 2, 3]
# nums2 = [0, 3, 0, 4, 0]
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# print("Dot Product:", v1.dotProduct(v2))













































class SparseVector:
    def __init__(self,num) -> None:
        self.data = {i:n for i,n in enumerate (num) if n != 0}
    def dot_multiplication(self,vec):
        result = 0 
        for i in self.data:
            if i in vec.data:
                result += self.data[i]* vec.data[i]
               
        return result

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
vec1 = SparseVector(nums1)
vec2 = SparseVector(nums2)

print(f'the dot product of the expression is :{vec1.dot_multiplication(vec2)}')


        