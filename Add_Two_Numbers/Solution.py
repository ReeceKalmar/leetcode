from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy

        carryOut = False

        n1 = l1
        n2 = l2

        while n1 or n2:
            nsum = 0
            if n1:
                nsum += n1.val
                n1 = n1.next
            if n2:
                nsum += n2.val
                n2 = n2.next

            if carryOut:
                nsum += 1
                carryOut = False

            dummy.val = nsum % 10

            if nsum >= 10:
                carryOut = True

            if not n1 and not n2:
                if carryOut:
                    dummy.next = ListNode(1)
                    return result
                return result

            dummy.next = ListNode()
            dummy = dummy.next

        return result
