from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node = head
        while node and node.next:
            temp = node.next.val
            node.next.val = node.val
            node.val = temp
            node = node.next.next
        return head
