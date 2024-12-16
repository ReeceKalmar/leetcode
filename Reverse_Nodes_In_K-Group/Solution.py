from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        right = head
        reveresed = []
        counter = 1
        while right:
            reveresed.append(right.val)
            if counter == k:
                while counter > 0:
                    left.val = reveresed.pop()
                    left = left.next
                    counter -= 1
            right = right.next
            counter += 1
        return head
