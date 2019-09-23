#https://leetcode.com/problems/flipping-an-image/
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            i.reverse()
        new_list=[]
        list_in_list=[]
        for i in A:
            for j in i:
                if j == 1:
                    list_in_list.append(0)
                else:
                    list_in_list.append(1)
            new_list.append(list_in_list.copy())
            list_in_list.clear()
                    
        return(new_list)
