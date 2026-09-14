class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        V, V1, V2 = 1, 1, 1
        Vmax, Vmin = nums[0], nums[0]

        for i in range(len(nums)):
            V1temp, V2temp = V1, V2
            V1 = min(nums[i]*V1temp, nums[i]*V2temp, nums[i])
            V2 = max(nums[i]*V1temp, nums[i]*V2temp, nums[i])

            if V1 < Vmin: Vmin = V1
            if V2 > Vmax: Vmax = V2
            

        return Vmax