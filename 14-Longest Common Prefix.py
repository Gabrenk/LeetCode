class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        the longest common prefix should be the longest among ALL the words,
        that said, if we arrenge them in alphabetical order and check the first
        and the last word and they do not match we can end the search right away
        Else will check how long does the prefix is.
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ''
        strs_sorted = sorted(strs)
        for i in range(len(strs_sorted)):
            if strs_sorted[0][i] != strs_sorted[-1][i]:
                return common_prefix
            common_prefix += strs_sorted[0][i]

        return common_prefix 
