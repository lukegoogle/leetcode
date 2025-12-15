class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        reversed_x = 0
        
        while x != 0:
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            
            x = (x - digit) // 10
            
            if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and digit > 7):
                return 0
            
            if reversed_x < INT_MIN // 10 or (reversed_x == INT_MIN // 10 and digit < -8):
                return 0
            
            reversed_x = reversed_x * 10 + digit
            
        return reversed_x