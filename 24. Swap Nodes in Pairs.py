# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        list_first = head.next
        list_second = head
        list_second.next = self.swapPairs(list_first.next)
        list_first.next = list_second
        return list_first
