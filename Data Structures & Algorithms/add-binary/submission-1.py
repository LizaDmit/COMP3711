class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summ = 0
        carry = 0

        na, nb = len(a), len(b)

        if na > nb:
            b = "0"*(na - nb) + b
        elif nb > na:
            a = "0"*(nb - na) + a

        res = ""

        for i in range(len(a) - 1, -1, -1):
            summ = (int(a[i]) + int(b[i]) + carry)%2
            carry = (int(a[i]) + int(b[i]) + carry)//2

            res += str(summ)

        res += str(carry)

        res = res[::-1]
        start = 0
        while start < len(res) - 1 and res[start] == "0":
            start += 1

        return res[start::]

