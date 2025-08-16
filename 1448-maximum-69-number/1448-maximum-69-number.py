class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = [int(d) for d in str(num)]  
        for i in range(len(digits)):
            if digits[i] == 6: 
                digits[i] = 9
                break
        
        return int(''.join(map(str, digits)))
