

class UniqueFinder:
    def __init__(self, nums):
        self.nums = nums

    def findSingles(self):
        xor = 0
        for num in self.nums:
            xor ^= num

        diff = xor & -xor
        a = b = 0
        for num in self.nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        return [a, b]

nums = [1, 2, 1, 3, 2, 5]
finder = UniqueFinder(nums)
result = finder.findSingles()
print("Unique elements:", result)
