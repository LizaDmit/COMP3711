class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for j in range(1, len(nums)):
            key = nums[j]
            i = j - 1

            while i >= 0 and key < nums[i]:
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = key

        return nums
            

