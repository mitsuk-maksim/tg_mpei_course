# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        m_indexes = [i for i,char in enumerate(S) if char == C]
        m_result = []

        for i in range(len(S)):
            minimum = len(S)
            for indx in m_indexes:
                difference = abs(indx - i)
                if difference < minimum:
                    minimum = difference
            m_result.append(minimum)
        return m_result
