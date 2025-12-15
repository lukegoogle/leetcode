class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        if s[0] == '+':
            i += 1
        elif s[0] == '-':
            sign = -1
            i += 1
            
        result = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            if sign == 1:
                if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                    return INT_MAX
            else:
                if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 8):
                    return INT_MIN
                    
            result = result * 10 + digit
            i += 1
            
        return result * sign