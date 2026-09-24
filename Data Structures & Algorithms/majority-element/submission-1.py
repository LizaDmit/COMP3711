import random
class Solution:
    def majorityElement(self, A: List[int]) -> int:
        n = len(A)
        while True:
            candidate = random.choice(A)
            count = sum(1 for x in A if x == candidate)
            if count > n // 2:
                return candidate
        