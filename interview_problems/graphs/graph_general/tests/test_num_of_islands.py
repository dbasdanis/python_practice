import unittest
from num_of_islands import Solution

class TestNumOfIslands(unittest.TestCase):
    def test_numIslands(self):
        solution = Solution()
        # Test case 1: Empty grid
        grid = [[]]
        assert solution.numIslands(grid) == 0

        # Test case 2: Grid with no islands
        grid = [
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0']
        ]
        assert solution.numIslands(grid) == 0

        # Test case 3: Grid with one island
        grid = [
            ['1', '1', '1', '1'],
            ['0', '1', '0', '1'],
            ['1', '1', '1', '1'],
            ['0', '0', '0', '0']
        ]
        assert solution.numIslands(grid) == 1

        # Test case 4: Grid with multiple islands
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        assert solution.numIslands(grid) == 3