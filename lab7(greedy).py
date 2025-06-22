def max_flowers(grid, n, m):
    dp = [[0] * m for _ in range(n)]
    dp[n-1][0] = int(grid[n-1][0])

    for i in range(n-1, -1, -1):
        for j in range(m):
            if i == n-1 and j == 0:
                continue
            from_bottom = dp[i+1][j] if i+1 < n else 0
            from_left = dp[i][j-1] if j-1 >= 0 else 0
            dp[i][j] = int(grid[i][j]) + max(from_bottom, from_left)

    return dp[0][m-1]
