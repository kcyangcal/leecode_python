# https://oj.leetcode.com/problems/binary-tree-postorder-traversal/

# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        rl = list()
        if root is None:
            return rl
        stack = list()
        cur = root
        while not not cur or not not stack:
            while not not cur:
                stack.append(cur)
                rl.insert(0,cur.val)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return rl
