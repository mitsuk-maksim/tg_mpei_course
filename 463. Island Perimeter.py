# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        square = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    square += 1
                    if i > 0 and grid[i-1][j] == 1:
                        count += 1
                    if j > 0 and grid[i][j-1] == 1:
                        count += 1
        return square*4-2*count
