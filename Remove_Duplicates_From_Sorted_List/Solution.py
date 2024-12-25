from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        latest = head.val
        node = head

        while node and node.next:
            temp = node.next
            if temp.val == latest:
                node.next = node.next.next
                continue
            
            else:
                latest = temp.val
            node = node.next
        return head
