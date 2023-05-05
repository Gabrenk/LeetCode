class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #Since any number, except 9, plus one is always equal to 
        # a single digit number, check it
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        #If the last number is 9 we'll begin a loop that will add the
        #carry to the last digit,then the to the last -1 and so forth. 
        #Remembering that the carry will be zeroed if digits[i]+carry =10
        #And then, if our carry remains equal to 1, create a new house for it
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
