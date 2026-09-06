class Solution:
    def leftmostPos(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l == r:
            return l
        m = (l + r)//2
        if nums[m] < target:
            return self.leftmostPos(nums, target, m + 1, r)
        else:
            return self.leftmostPos(nums, target, l, m)
    def rightmostPos(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l == r:
            return l
        m = (l + r)//2
        if nums[m] <= target:
            return self.rightmostPos(nums, target, m + 1, r)
        else:
            return self.rightmostPos(nums, target, l, m)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        leftPos = self.leftmostPos(nums, target, l, r)
        if leftPos == len(nums) or nums[leftPos] != target:
            return [-1, -1]
        rightPos = self.rightmostPos(nums, target, l, r) - 1

        return [leftPos, rightPos]
