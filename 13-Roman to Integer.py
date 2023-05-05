class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romandic ={
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        sum = 0
        for i in range(len(s) -1):
            if romandic[s[i]] < romandic[s[i+1]]:
                sum -= romandic[s[i]]
            else:
                sum += romandic[s[i]]
        return sum+romandic[s[-1]]