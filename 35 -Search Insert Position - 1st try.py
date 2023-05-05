class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            j = 999
            k = 999
            if target-1 in nums:
                j = nums.index(target-1)
                j_sum = j+1
            if target+1 in nums:
                k = nums.index(target+1)
                k_sub = k-1
            l = min(j,k)
            if l==j:
                return j_sum
            else:
                if k_sub < 0:
                    return 0
                return k_sub
            