from math import inf
#给定一个m*n的二维网格 grid ，网格中的每个单元格包含一个非负整数，表示该单元格的代价。机器人以左上角单元格为起始点，每次只能向下或者向右移动一步，直至到达右下角单元格。请返回从左上角到右下角的最小路径和。
#1.暴力搜索
def min_path_sum_dfs(grid: list[list[int]], i: int, j: int) -> int:
    """最小路径和：暴力搜索"""
    #要为递归做准备，不仅考虑最后回到00，更要考虑对比时候是有负边界情况，这种情况给无穷大，在min操作时候自然被过滤掉
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return inf
    
    up = min_path_sum_dfs(grid, i-1, j)
    left = min_path_sum_dfs(grid, i, j-1)

    return min(up,left) + grid[i][j]

#2.记忆化搜索
def min_path_sum_dfs_mem(
    grid: list[list[int]], mem: list[list[int]], i: int, j: int
) -> int:
    """最小路径和：记忆化搜索"""
    # 若为左上角单元格，则终止搜索
    if i == 0 and j == 0:
        return grid[0][0]
    # 若行列索引越界，则返回 +∞ 代价
    if i < 0 or j < 0:
        return inf
    # 若已有记录，则直接返回
    if mem[i][j] != -1:
        return mem[i][j]
    # 左边和上边单元格的最小路径代价
    up = min_path_sum_dfs_mem(grid, mem, i - 1, j)
    left = min_path_sum_dfs_mem(grid, mem, i, j - 1)
    # 记录并返回左上角到 (i, j) 的最小路径代价
    mem[i][j] = min(left, up) + grid[i][j]
    return mem[i][j]

#3.动态规划
def min_path_sum_dp(grid: list[list[int]]) -> int:
    """最小路径和：动态规划"""
    n, m = len(grid), len(grid[0])
    # 初始化 dp 表
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    # 状态转移：首行
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    # 状态转移：首列
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    # 状态转移：其余行和列
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
    return dp[n - 1][m - 1]



"""Driver Code"""
if __name__ == "__main__":
    grid = [[1, 3, 1, 5], [2, 4, 2, 2], [5, 3, 2, 1], [4, 3, 5, 2]]
    n, m = len(grid), len(grid[0])
    #1.暴力搜索    
    res1 = min_path_sum_dfs(grid, n - 1, m - 1)
    print(f"从左上角到右下角的做小路径和为 {res1}")

    #2.记忆化搜索
    mem = [[-1] * m for _ in range(n)]
    res2 = min_path_sum_dfs_mem(grid, mem, n - 1, m - 1)
    print(f"从左上角到右下角的做小路径和为 {res2}")
    #3.动态规划
    res3 = min_path_sum_dp(grid)
    print(f"从左上角到右下角的做小路径和为 {res3}")
