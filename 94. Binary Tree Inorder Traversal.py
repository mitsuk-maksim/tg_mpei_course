# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#recursion method
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
# iterative method
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        l_list = root
        l_stack = []
        l_res = []
        while l_list or l_stack:
            while l_list:
                l_stack.append(l_list)
                l_list = l_list.left
            v_node = l_stack.pop()
            l_res.append(v_node.val)
            l_list = v_node.right
        return l_res
