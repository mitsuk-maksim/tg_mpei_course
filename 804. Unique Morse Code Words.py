#https://leetcode.com/problems/unique-morse-code-words/
class Solution:
    def translate_to_morze(self,st:str) -> str:
        morze = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        dictionary = dict(zip(lower_case,morze))
        result=""
        for i in st:
            result+=dictionary[i]
        return result

    

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = [""]*len(words)
        i=0
        for q in words:
            res[i]=self.translate_to_morze(q)
            i+=1
        return (len(set(res)))
