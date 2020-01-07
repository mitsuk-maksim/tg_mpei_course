# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''   ошибка времени
       for char in s:
            if s.count(char) == 1:
                return s.find(char)
        return -1
        '''
        # воспользуеся словарем из collections
        count = Counter(s)
        for char in s:
            if count[char] == 1:
                return s.find(char)
        return -1
        
