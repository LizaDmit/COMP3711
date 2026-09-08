class Solution:
    def sortArrayHelper(self, nums: List[int], l: int, r: int) -> List[int]:
        if l >= r: return

        m = (l + r)//2

        self.sortArrayHelper(nums, l, m)
        self.sortArrayHelper(nums, m + 1, r)

        lArr = nums[l:m + 1]
        rArr = nums[m + 1:r + 1]
        lInd = 0
        rInd = 0

        for k in range(l, r + 1):
            if lInd < len(lArr) and (rInd >= len(rArr) or lArr[lInd] <= rArr[rInd]):
                nums[k] = lArr[lInd]
                lInd += 1
            else:
                nums[k] = rArr[rInd]
                rInd += 1
        return nums


    def sortArray(self, nums: List[int]) -> List[int]:
        self.sortArrayHelper(nums, 0, len(nums) - 1)

        return nums