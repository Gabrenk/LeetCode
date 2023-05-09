class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(len(n) - 1):
            current = one
            one = current + two
            two = current
    
        return one
        