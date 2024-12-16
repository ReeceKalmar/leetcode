# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode()
        head = dummy
        empty = False
        while not empty:
            m = None
            z = None
            empty = True
            for i in range(len(lists)):
                node = lists[i]

                if not node:
                    continue

                empty = False

                if m == None:
                    m = node.val
                    z = i
                    continue
                if m > node.val:
                    m = node.val
                    z = i

            if not empty:
                lists[z] = lists[z].next
                dummy.next = ListNode(m)
                dummy = dummy.next
        return head.next
