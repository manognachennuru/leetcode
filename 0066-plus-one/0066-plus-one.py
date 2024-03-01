class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #first reverse the array
        digits.reverse()

        #now initialise carry
        carry = 0

        digits[0] += 1
        if digits[0] <= 9:
            #no carry
            digits.reverse()
            return digits

        for i in range(0, len(digits)):
            digits[i] += carry
            if digits[i] > 9:
                carry = digits[i] // 10
                digits[i] %= 10
            else:
                #no more carry
                digits.reverse()
                return digits
        
        #say for example, we still have carry after the whole loop
        #append carry
        digits.append(carry)
        digits.reverse()
        return digits