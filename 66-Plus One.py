class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            digits.reverse()
            carry = 1
            for i in range(len(digits)):
                digits[i] += carry
                if digits[i] == 10:
                    digits[i] = 0
                else:
                    carry = 0
                if digits[i] is digits[-1] and carry==1:
                    digits.append(1)
            digits.reverse()
        
        return digits
    