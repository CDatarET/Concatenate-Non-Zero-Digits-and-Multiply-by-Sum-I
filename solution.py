class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n <= 0:
            return 0

        prod = []
        s = 0
        for c in str(n):
            if c != '0':
                prod.append(c)
                s += int(c)
        
        return int("".join(prod)) * s
