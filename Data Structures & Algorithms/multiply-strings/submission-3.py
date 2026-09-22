class Solution:
    def add(self, x: str, y: str) -> str:
        i, j = len(x) - 1, len(y) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            d1 = ord(x[i]) - ord('0') if i >= 0 else 0
            d2 = ord(y[j]) - ord('0') if j >= 0 else 0
            total = d1 + d2 + carry
            res.append(str(total % 10))     # digit for this column
            carry = total // 10             # carry to next column
            i -= 1
            j -= 1
        return "".join(reversed(res))


    def sub(self, x: str, y: str) -> str:
        # assumes x >= y (always true in Karatsuba)
        i, j = len(x) - 1, len(y) - 1
        borrow = 0
        res = []
        while i >= 0:
            d1 = ord(x[i]) - ord('0') - borrow
            d2 = ord(y[j]) - ord('0') if j >= 0 else 0
            if d1 < d2:
                d1 += 10                    # borrow from next column
                borrow = 1
            else:
                borrow = 0
            res.append(str(d1 - d2))
            i -= 1
            j -= 1
        out = "".join(reversed(res)).lstrip('0')
        return out if out else "0"

    def normalize(self, num1: str, num2: str) -> tuple[str, str]:
        n1, n2 = len(num1), len(num2)

        if n1 < n2:
            num1 = "0" * (n2 - n1) + num1
        elif n2 < n1:
            num2 = "0" * (n1 - n2) + num2

        return num1, num2

    def multiply(self, num1: str, num2: str) -> str:

        num1, num2 = self.normalize(num1, num2)
        
        n = len(num1)
        if n == 1:
            return str(int(num1[0])*int(num2[0]))

        
        m = n//2

        M1 = self.multiply(num1[:m], num2[:m])
        M2 = self.multiply(num1[m:], num2[m:])

        m1 = self.add(num1[:m], num1[m:])
        m2 = self.add(num2[m:], num2[:m])

        M3 = self.multiply(m1, m2)

        middle = self.sub(M3, self.add(M1, M2))

        res = self.add(self.add(M1 + 2 * (n - m) * "0", middle + (n - m) * "0"), M2)

        start = 0
        while start < len(res) - 1 and res[start] == "0":
            start += 1

        return res[start:]