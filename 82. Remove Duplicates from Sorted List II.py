# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        lst = lst_cur = ListNode(0)
        cur = head
        prev = None

        while cur:
            if prev!=None and prev == cur.val:
                lst_cur.next = None
            else:
                if lst_cur.next:
                    lst_cur = lst_cur.next
                lst_cur.next = cur
            prev = cur.val
            cur = cur.next
        return lst.next
