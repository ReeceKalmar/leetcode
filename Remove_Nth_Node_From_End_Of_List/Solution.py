from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        def traverse(node, i):
            if not node.next:
                return i - n
            index = traverse(node.next, i + 1)
            if i != index:
                return index
            else:
                node.next = node.next.next
                return index

        check = traverse(head, 0)
        if check == -1:
            head = head.next
        return head
