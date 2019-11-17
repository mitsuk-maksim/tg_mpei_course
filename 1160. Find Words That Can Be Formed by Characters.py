# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        for v_word in words:
            flag = True
            l_chars = [_ for _ in chars]
            for v_char in v_word:
                if v_char in l_chars:
                    l_chars.remove(v_char)
                 #   print(l_chars)
                else:
                    flag = False
                    break
            if flag:
                counter += len(v_word)
        return counter
