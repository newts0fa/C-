def func(n):
    if n < 0 or n > 20:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(func(n))

