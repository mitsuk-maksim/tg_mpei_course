# https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        set_to_delete = set(to_delete)
        result = []

        def helper(root, is_root):
            if not root:
                return None
            check_root_deleted = root.val in set_to_delete
            if is_root and not check_root_deleted:
                result.append(root)
            root.left = helper(root.left,check_root_deleted)
            root.right = helper(root.right,check_root_deleted)
            if check_root_deleted:
                return None
            else:
                return root
        helper(root,True)
        return result
