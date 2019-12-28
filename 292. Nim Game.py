# https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        '''
        так получается, что мы проигрываем всегда, когда кол-во камней = 4
        пысы: вспоминаем егэ по инфе
        '''
        return n%4 != 0
        
