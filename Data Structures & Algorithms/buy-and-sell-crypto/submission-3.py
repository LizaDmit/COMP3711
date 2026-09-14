class Solution:
    def maxProfitHelper(self, prices: List[int], l: int, r: int) -> int:
        if l == r: return 0

        m = (l + r)//2
        M1 = self.maxProfitHelper(prices, l, m)
        M2 = self.maxProfitHelper(prices, m + 1, r)

        return max(M1, M2, max(prices[m + 1:r + 1]) - min(prices[l:m + 1]))


    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitHelper(prices, 0, len(prices) - 1)