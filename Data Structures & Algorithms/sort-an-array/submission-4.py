import random
class Solution:
    def swap(self, nums: List[int], ind1: int, ind2: int) -> List[int]:
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp

        return nums

    def partition(self, nums: List[int], l: int, r: int) -> int:
        key = nums[r]
        i = l - 1
        for j in range(l, r):
            if key >= nums[j]:
                i += 1
                nums = self.swap(nums, i, j)
        
        self.swap(nums, i + 1, r) 

        return i + 1 

    def sortArrayHelper(self, nums: List[int], l: int, r: int) -> List[int]:
        if l >= r:
            return
        key = random.randint(l, r)
        self.swap(nums, key, r)

        m = self.partition(nums, l, r)
        self.sortArrayHelper(nums, l, m - 1)
        self.sortArrayHelper(nums, m + 1, r)

        return nums

        
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums
        return self.sortArrayHelper(nums, 0, len(nums) - 1)
        