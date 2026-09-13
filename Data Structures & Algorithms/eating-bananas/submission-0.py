from math import ceil
class Solution:

    def feasible(self, piles: List[int], h: int, k: int) -> bool:
        sum = 0

        for i in range(len(piles)):
            sum += ceil(piles[i]/k)

        return sum <= h


    def minEatingSpeedHelper(self, piles: List[int], h: int, minK: int, maxK: int) -> int:
        if minK == maxK:
            return minK

        k = (minK + maxK)//2

        if self.feasible(piles, h, k):
            return self.minEatingSpeedHelper(piles, h, minK, k)
        else:
            return self.minEatingSpeedHelper(piles, h, k + 1, maxK)

        


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.minEatingSpeedHelper(piles, h, 1, max(piles))