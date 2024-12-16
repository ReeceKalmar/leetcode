# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        node = ListNode()
        head = node

        while list1 or list2:
            node.next = ListNode()
            node = node.next
            if list1 and list2:
                left = list1.val
                right = list2.val
                if left < right:
                    node.val = left
                    list1 = list1.next
                else:
                    node.val = right
                    list2 = list2.next
            elif not list1:
                node.val = list2.val
                list2 = list2.next
            else:
                node.val = list1.val
                list1 = list1.next

        return head.next
