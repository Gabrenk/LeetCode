class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_numbers = set()
        for number in nums:
            if number in distinct_numbers:
                return True
            else:
                distinct_numbers.add(number)