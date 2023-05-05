class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        input_number = x
        new_number = 0
        while x > 0:
            new_number = new_number * 10 + x%10
            x = x//10

        return new_number == input_number