def snakesAndLadders(board):
    n = len(board)
    visited = set()

    def dfs(square):
        if square == n ** 2:
            return 0
        if square in visited:
            return float('inf')

        visited.add(square)
        min_moves = float('inf')

        for next_square in range(square + 1, min(square + 6, n ** 2) + 1):
            row, col = getRowCol(next_square)
            if board[row][col] != -1:
                next_square = board[row][col]

            min_moves = min(min_moves, dfs(next_square))

        visited.remove(square)
        return min_moves + 1

    def getRowCol(square):
        row = (n - 1) - (square - 1) // n
        if row % 2 == (n % 2):
            col = (square - 1) % n
        else:
            col = (n - 1) - (square - 1) % n
        return row, col

    min_moves = dfs(1)
    return min_moves if min_moves != float('inf') else -1
