# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        list_adjance = defaultdict(list) # список смежности
        indegree = {}
        for dest,src in prerequisites:
            list_adjance[src].append(dest)
            
            # запись каждого узла в степени
            indegree[dest] = indegree.get(dest,0) + 1
        
        #очередь для списка узлов, имеющих 0 в степени
        zero_indegree_queue = [i for i in range(numCourses) if i not in indegree]
        
        topologic_sort_list = []
        
        # пока в Q есть узлы
        while zero_indegree_queue:
            #возьмемм один узел с 0 степенью
            top = zero_indegree_queue.pop(0)
            topologic_sort_list.append(top)
            
            #понижение степени для всех соседей
            if top in list_adjance:
                for v_neighbor in list_adjance[top]:
                    indegree[v_neighbor] -= 1
                    #добавить соседа в Q если степень стала 0
                    if indegree[v_neighbor] == 0:
                        zero_indegree_queue.append(v_neighbor)
                
        if len(topologic_sort_list) == numCourses:
            return topologic_sort_list
        else:
            return []
