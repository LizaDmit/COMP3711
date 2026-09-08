class Solution:
    def maxSubArrayHelper(self, nums: List[int], l: int, r: int) -> int:
        if l == r: return nums[l]

        m = (l + r)//2
        lBest = self.maxSubArrayHelper(nums, l, m)
        rBest = self.maxSubArrayHelper(nums, m + 1, r)

        lSum, rSum = 0, 0
        lBestExt, rBestExt = float('-inf'), float('-inf')

        for i in range(m, l - 1, -1):
            lSum += nums[i]
            lBestExt = max(lBestExt, lSum)
        for i in range(m + 1, r + 1):
            rSum += nums[i]
            rBestExt = max(rBestExt, rSum)

        return max(lBest, rBest, lBestExt + rBestExt)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
        
