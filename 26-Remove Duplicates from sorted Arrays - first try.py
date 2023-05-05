class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        create a list or dic where all unique numbers are stored.
        check if actual number in unique numbers if not add it, else remove it
        from current list
        """
        unique_numbers =[]
        for i in range(len(nums)):
            if nums[i] not in unique_numbers:
                unique_numbers.append(nums[i])
        j = []
        for  i in range((len(nums) - len(unique_numbers))):
            j.append('_')
        final_list = unique_numbers + j
            
        return len(unique_numbers)
