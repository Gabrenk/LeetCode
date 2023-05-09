class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[0:m] + nums2[0:n]
        for i in range(len(nums3)):
            nums1[i] = nums3[i]
        nums1.sort()

#    def merge(self, nums1, m, nums2, n):
#      for j in range(n):
#          nums1[m+j] = nums2[j]
#      nums1.sort()