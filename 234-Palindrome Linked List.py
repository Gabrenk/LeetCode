# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            middle = slow.next
            fast = fast.next.next
        
        previous = None
        while slow:
            next = slow.next
            slow.next = previous
            previous = slow
            slow = next

        left, right = head, previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True