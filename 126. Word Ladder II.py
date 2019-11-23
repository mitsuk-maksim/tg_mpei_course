# https://leetcode.com/problems/word-ladder-ii/

from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        s_word_set = set(wordList)
        d_layer = {}
        d_layer[beginWord] = [[beginWord]] #храним текущее слово и все последовательности, как добрались до него

        while d_layer:
            d_new_layer = defaultdict(list)  #возвращает [] для недостающих ключей
            for word in d_layer:
                if word == endWord:
                    return d_layer[word] # возращаем все найденные последовательности
                for i in range(len(word)): #меняем каждую букву и смотрим есть ли она в словаре
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in s_word_set:
                            # добавление нового элемента ко всем последовательности и формирование нового слоя элемента
                            d_new_layer[new_word] += [j + [new_word] for j in d_layer[word]]
            s_word_set -= set(d_new_layer.keys()) # удаление из словаря, чтобы исключить списки
            d_layer = d_new_layer #переход на новый "уровень"
            
        return []
