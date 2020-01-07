# https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Write your MySQL query statement below
SELECT
    empl_1.Name as 'Employee'
   FROM
        Employee AS empl_1,
        Employee AS empl_2
          WHERE
             empl_1.ManagerId = empl_2.Id AND empl_1.Salary > empl_2.Salary;
