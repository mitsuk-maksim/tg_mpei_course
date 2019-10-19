# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        v_middle = len(nums) // 2
        l_node = TreeNode(nums[v_middle]) #делаем вершину центральным элементом
        l_node.left = self.sortedArrayToBST(nums[:v_middle])
        l_node.right = self.sortedArrayToBST(nums[v_middle+1:])
       # print(l_node)
        return l_node















def stringToIntegerList(input):
    return json.loads(input)

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().sortedArrayToBST(nums)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
