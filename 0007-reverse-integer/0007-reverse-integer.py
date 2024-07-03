class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)     
        is_minus = False
        if str_num[0] == "-":
            str_num = str_num[1:]
            is_minus = True
        
        reversed_num = str_num[::-1]
        reversed_num = int(reversed_num)
        
        if is_minus:
            reversed_num = -reversed_num
        
        # 32비트 정수 범위 확인
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num