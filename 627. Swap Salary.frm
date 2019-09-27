# https://leetcode.com/problems/swap-salary/
# Write your MySQL query statement below
UPDATE salary
set sex = case sex
when 'f' then 'm'
else 'f'
end;
