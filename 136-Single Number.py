class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        by XOR two numbers if they are equal, then will return 0( for False)
        """
        value = 0
        for num in nums:
            value ^= num
        
        return value