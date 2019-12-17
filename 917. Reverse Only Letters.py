# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        mas = [i for i in S]
        mas_alpha = [i for i in S if i.isalpha()]
        mas_char = ['']*len(mas)
        result = []
        for i,ch in enumerate(mas):
            if not ch.isalpha():
                mas_char[i] = ch
            else:
                mas_char[i] = 'T'
        
        mas_alpha.reverse()
        print(mas_alpha)
        print(mas_char)
        j = 0
        for ch in mas_char:
            if ch == 'T':
                result.append(mas_alpha[j])
                j += 1
            else:
                result.append(ch)
        return ''.join(map(str,result))
