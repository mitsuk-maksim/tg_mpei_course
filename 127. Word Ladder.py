# https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # у всех слов одинаковая длина
        v_len = len(beginWord)

        #словарь для размещения комбинация слов, которые могут
        #получиться, если менять одну букву за раз
        #ключ - основное слово, значение список комбинаций
        d_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(v_len):
                d_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

        #очередь для поиска в ширину (BFS)
        queue = deque([(beginWord,1)])
        #проверка что не повторяем обработку одного и того же слова
        d_check = {beginWord: True}
        while queue:
            l_current_word, v_level = queue.popleft()
            for i in range(v_len):
                # Промежуточные слова для текущего слова
                intermediate_word = l_current_word[:i] + '*' + l_current_word[i+1:]

                # Дальше все слова, которые имеют одинаковое промежуточное слово
                for word in d_combo_dict[intermediate_word]:
                    # если найдем конечное слово, можем вернуть ответ
                    if word == endWord:
                        return v_level + 1
                    # иначе помещаем его в очередь, помечая что он уже был проверен
                    if word not in d_check:
                        d_check[word] = True
                        queue.append((word,v_level + 1))
                d_combo_dict[intermediate_word] = []
        return 0
