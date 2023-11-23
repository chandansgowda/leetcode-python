class Solution:
    def countDigits(self, num: int) -> int:
        str_num, count = str(num), 0
        for digit in str_num:
            if num % int(digit) == 0:
                count += 1
        return count
        
