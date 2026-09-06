class Solution:
    def findPeakElementHelper(self, nums: List[int], l, r) -> int:
        if l >= r: return l
        m = (l + r)//2

        if nums[m] < nums[m + 1]:
            return self.findPeakElementHelper(nums, m + 1, r)
        else: return self.findPeakElementHelper(nums, l, m)

    def findPeakElement(self, nums: List[int]) -> int:
        return self.findPeakElementHelper(nums, 0, len(nums) - 1)