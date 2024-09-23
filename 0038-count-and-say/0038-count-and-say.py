class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev_result = "1"
        
        for _ in range(2, n+1):
            current_result = ""
            count = 1
            
            for j in range(1, len(prev_result)):
                if prev_result[j] == prev_result[j-1]:
                    count += 1
                else:
                    current_result += str(count) + prev_result[j-1]
                    count = 1
            
            current_result += str(count) + prev_result[-1]
            prev_result = current_result
            
        return prev_result