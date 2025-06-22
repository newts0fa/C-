def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def backtrack(row, board):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1  # Откат

    solutions = []
    backtrack(0, [-1] * n)

    result = []
    for sol in solutions:
        solution_str = []
        for col in sol:
            solution_str.append('.' * col + 'Q' + '.' * (n - col - 1))
        result.append(solution_str)
    return result
