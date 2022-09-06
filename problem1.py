'''
98. Validate Binary Search Tree

TIME COMPLEXITY: O(h) height of tree
SPACE COMPLEXITY: O(h)
APPROACH: recursive function with pointers
LEETCODE: yes
DIFFICULTY: 
    * Python global variables are hard to use compared to java.
    * Coding without global variables was challenging.
    * Anyways, I found solution after watching the class.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        prev = -1 * (2 ** 31) - 1
        def traverse(root, prev, res):
            
            # prev, res = prev, res 
            if root == None:
                return prev, res
            if res:
                prev, res = traverse(root.left, prev, res)
            if root.val <= prev:
                res = False
            prev = root.val
            
            if res:
                prev, res = traverse(root.right, prev, res)
            return prev, res
        
        prev, res = traverse(root, prev, res)
        return res
        
