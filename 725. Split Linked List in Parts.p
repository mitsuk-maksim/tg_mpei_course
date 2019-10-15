# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root:
            return [root]*k

        l_list = root
        v_count = 0
        while l_list:
            v_count += 1
            l_list = l_list.next

        v_len_div = v_count // k
        v_len_mode = v_count % k

        l_result_list = []
        l_list = root
        for i in range(k):
            v_count = v_len_div
            if v_len_mode:
                v_count += 1
                v_len_mode -= 1

            if l_list:
                for j in range(v_count-1):
                    l_list = l_list.next
                v_pointer = l_list.next
                l_list.next = None
                l_result_list.append(root)
                root = v_pointer
                l_list = v_pointer
            else:
                l_result_list.append(root)
        return l_result_list
