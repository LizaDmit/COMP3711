class Solution:
    def KadaneMax(self, nums: List[int]) -> int:
        V, Vmax = 0, nums[0]

        for i in range(0, len(nums)):
            V = max(V + nums[i], nums[i])
            Vmax = max(V, Vmax)

        return Vmax

    def KadaneMin(self, nums: List[int]) -> int:
        V, Vmin = 0, nums[0]

        for i in range(0, len(nums)):
            V = min(V + nums[i], nums[i])
            Vmin = min(V, Vmin)

        return Vmin

    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        allNeg = True
        for i in range(len(nums)):
            if nums[i] >= 0: allNeg = False
        if allNeg: return max(nums)

        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

        return max(sum - self.KadaneMin(nums), self.KadaneMax(nums))