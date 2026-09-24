class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = nums[0]
        for i in range(len(nums)):
            if nums[i] == cand:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                cand = nums[i + 1]
        
        return cand
        