# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# head = [2,1,5]
#                      round 1        round 2       round 3
#answer_array              [0]         [0, 0]      [0, 0, 0]
#stack                   [(2,0)]    [(2,0), (1,1)]     

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        l_answer_array = []
        l_stack = []
        v_index = 0
        
        while head:
            l_answer_array.append(0)
            current_value = head.val
            
            while l_stack and l_stack[-1][0] < current_value:
                last_value = l_stack.pop()  
              #  print(last_value) #здесь у нас хранятся (элемент,индекс)
                l_answer_array[last_value[1]] = current_value
                
            l_stack.append((current_value, v_index))
            v_index += 1
            head = head.next
        return l_answer_array


def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            head = stringToListNode(line);
            
            ret = Solution().nextLargerNodes(head)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
