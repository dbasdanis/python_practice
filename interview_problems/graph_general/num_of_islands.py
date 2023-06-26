from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        stack = []

        def is_valid(row,col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1':
                return True
            else:
                return False 
            
        def dfs(row, col):
            stack.append((row,col))

            while stack:
                curr_row, curr_col = stack.pop()

                if not is_valid(curr_row, curr_col):
                    continue

                grid[curr_row][curr_col] = '0' # mark the current land as visited

                stack.append((curr_row + 1, curr_col))  # check down
                stack.append((curr_row - 1, curr_col))  # check up
                stack.append((curr_row, curr_col + 1))  # check right
                stack.append((curr_row, curr_col - 1))  # check left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)

        return count