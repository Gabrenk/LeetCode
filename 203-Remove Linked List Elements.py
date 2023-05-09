# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], rval: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        previous = dummy
        current = head

        while current:
            next = current.next

            if current.val == rval:
                previous.next = next
            else:
                previous = current
            current = next

        return dummy.next