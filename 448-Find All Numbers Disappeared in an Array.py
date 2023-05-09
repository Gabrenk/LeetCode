class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing_numbers = []
        a = set(nums)
        for i in range(1, len(nums)+1):
            if i not in a:
                missing_numbers.append(i)
        return missing_numbers
