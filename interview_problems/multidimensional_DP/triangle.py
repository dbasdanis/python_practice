from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle.copy()  # Create a copy of the triangle
        
        for i in range(n-2, -1, -1):  # Iterate from the second last row to the first row
            for j in range(i+1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]