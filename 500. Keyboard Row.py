# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "QWERTYUIOPqwertyuiop"
        second = "ASDFGHJKLasdfghjkl"
        third = "ZXCVBNMzxcvbnm"
        result=[]
        for i in words:
            flag = True
            if i[0] in first:
                for j in range(len(i)):
                    if i[j] not in first:
                        flag = False
                        break
                        
            if i[0] in second:
                for j in range(len(i)):
                    if i[j] not in second:
                        flag = False
                        break
                        
            if i[0] in third:
                for j in range(len(i)):
                    if i[j] not in third:
                        flag = False
                        break
                
            if flag:
                result.append(i)
        return(result)
                
                        
                        
                      
            
