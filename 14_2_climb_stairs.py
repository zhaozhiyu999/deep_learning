#给定一个共有n阶的楼梯，你每步可以上1阶或者2阶，但不能连续两轮跳1阶，请问有多少种方案可以爬到楼顶？带约束的爬楼梯
def climbing_stairs_constraint_dp(n: int) -> int:
    """带约束爬楼梯：动态规划"""
    if n == 1 or n == 2:
        return 1
    
    dp = [[0]*3 for _ in range(n+1)]
    #初始小值,d[i][j],第i阶，上一个状态是走了j阶
    dp[1][2],dp[1][1] = 0, 1
    dp[2][1],dp[2][2] = 0, 1

    for i in range(3, n+1):
        dp[i][1] = dp[i-1][2]
        dp[i][2] = dp[i-2][1]+dp[i-2][2]

    return dp[n][1]+dp[n][2]

if __name__ == "__main__":
    n = 9
    res = climbing_stairs_constraint_dp(n)
    print(f"total{n} stairs, have {res}solutions")
