class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        
        prev_sequence = self.countAndSay(n - 1)
        result = []
        i = 0
        
        while i < len(prev_sequence):
            count = 1
            j = i + 1
            while j < len(prev_sequence) and prev_sequence[j] == prev_sequence[i]:
                count += 1
                j += 1
            result.append(str(count) + prev_sequence[i])
            i = j
            
        return "".join(result)
