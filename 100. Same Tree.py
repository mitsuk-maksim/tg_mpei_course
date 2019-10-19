# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursion method
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        
#iterative method
class Solution:
    def f_check(self,p,q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        return True
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        l_deq = [(p,q)] #создадим дек
        while l_deq:
            p,q = l_deq.pop(0)
            if not self.f_check(p,q):
                return False
            if p:
                l_deq.append((p.left,q.left))
                l_deq.append((p.right,q.right))
        return True
