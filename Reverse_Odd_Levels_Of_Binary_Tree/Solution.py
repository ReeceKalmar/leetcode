from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(stack, level):
            if level & 1:
                left = 0
                right = len(stack) - 1
                while left < right:
                    nleft = stack[left]
                    nright = stack[right]
                    tmp = nleft.val
                    nleft.val = nright.val
                    nright.val = tmp
                    left += 1
                    right -= 1

            if not stack[0].left:
                return

            tmp_stack = []
            for n in stack:
                tmp_stack.append(n.left)
                tmp_stack.append(n.right)
            reverse(tmp_stack, level + 1)

        reverse([root], 0)
        return root
