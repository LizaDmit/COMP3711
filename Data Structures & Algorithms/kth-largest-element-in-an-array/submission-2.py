import random
class Solution:
    def swap(self, nums: List[int], n1: int, n2: int) -> List[int]:
        temp = nums[n1]
        nums[n1] = nums[n2]
        nums[n2] = temp

        return nums

    def partition(self, nums: List[int], l: int, r: int) -> int:
        pivot = nums[r]
        i = l - 1

        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                self.swap(nums, i, j)

        self.swap(nums, i + 1, r)

        return i + 1

    def findKthLargestHelper(self, nums: List[int], k: int, l: int, r: int) -> int:
        pivot = random.randint(l, r)
        self.swap(nums, pivot, r)

        m = self.partition(nums, l, r)

        if m == k: return nums[m]

        if m > k:
            return self.findKthLargestHelper(nums, k, l, m - 1)
        else:
            return self.findKthLargestHelper(nums, k, m + 1, r)



    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargestHelper(nums, len(nums) - k, 0, len(nums) - 1)

        