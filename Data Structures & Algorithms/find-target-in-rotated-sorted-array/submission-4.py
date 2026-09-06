class Solution:
    def searchHelper(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l >= r: return l # if there is no ratiation and it shrunks toa single position
        m = (l + r)//2

        if nums[m] > nums[m + 1]: return m # the pea is found
        elif nums[m] >= nums[l]: return self.searchHelper(nums, target, m + 1, r) # still in the first sorted half
        else: return self.searchHelper(nums, target, l, m - 1) # peak is somewhere in between / m was alr ruled out on the first comparison

    def BinarySearch(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l > r: return -1 #DO NOT FORGET
        m = (l + r)//2

        if nums[m] == target: return m
        elif nums[m] > target: return self.BinarySearch(nums, target, l, m - 1)
        else: return self.BinarySearch(nums, target, m + 1, r)

    def search(self, nums: List[int], target: int) -> int:
        k = self.searchHelper(nums, target, 0, len(nums) - 1)
       
        if target >= nums[0]:
            return self.BinarySearch(nums, target, 0, k) # search the first half (before k)
        else:
            return self.BinarySearch(nums, target, k + 1, len(nums) - 1) # search the second half (after k)

    
    







