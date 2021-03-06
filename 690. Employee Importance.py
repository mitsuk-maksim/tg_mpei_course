# https://leetcode.com/problems/employee-importance/

"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        m_id = {emp.id: emp for emp in employees}
        #print(m_id)
        def search(ind):
            employees = m_id[ind]
            return (employees.importance + sum(search(ind) for ind in employees.subordinates))
        return search(id)
