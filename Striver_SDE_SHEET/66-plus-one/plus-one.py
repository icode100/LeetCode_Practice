class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N:int = len(digits)
        carry:int = 1

        for i in range(N-1,-1,-1):
            if digits[i]+1<10:
                digits[i]+=carry
                carry = 0
                break
            else:
                newval:int = digits[i]+carry
                digits[i] = newval%10
                carry = newval//10
        
        if carry!=0:
            digits.insert(0,carry)
        
        return digits
        