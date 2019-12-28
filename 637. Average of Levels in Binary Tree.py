# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # используем DFS чтобы отслеживать на какой глубине находимся. Два элемента
        # сумма узлов и кол-во узлов
        information = []
        def f_dfs(t_node, v_depth = 0):
            if t_node:
                if len(information) <= v_depth:
                    information.append([0,0])
                information[v_depth][0] += t_node.val
                information[v_depth][1] += 1
                f_dfs(t_node.left, v_depth + 1)
                f_dfs(t_node.right, v_depth + 1)
        f_dfs(root)
        return [sm/float(num) for sm, num in information]
