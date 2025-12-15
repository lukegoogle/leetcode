class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        pos = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                d1 = int(num1[i])
                d2 = int(num2[j])
                
                mult = d1 * d2
                
                p1 = i + j
                p2 = i + j + 1
                
                s = mult + pos[p2]
                
                pos[p1] += s // 10
                pos[p2] = s % 10
        
        result = []
        for digit in pos:
            if not (len(result) == 0 and digit == 0):
                result.append(str(digit))
        
        return "".join(result)