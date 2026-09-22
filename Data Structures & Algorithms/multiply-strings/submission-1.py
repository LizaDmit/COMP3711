class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0]*(m + n)
        
        for i in range(m - 1, -1, -1):
            mInt = int(num1[i])

            for j in range(n - 1, -1, -1):
                nInt = int(num2[j])

                total = mInt * nInt + res[i + j + 1]
                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        start = 0
        while start < len(res) - 1 and res[start] == 0:
            start += 1

        return "".join(str(d) for d in res[start:])