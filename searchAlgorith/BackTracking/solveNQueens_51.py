# 51.N皇后问题（Hard)
# 问题描述：
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 示例:
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 提示：在 n*n 的矩阵中摆放 n 个皇后，并且每个皇后不能在同一行，同一列，同一对角线上
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        csUsed = [False for _ in range(n)]
        # 左斜i = row+col
        leftUsed = [False for _ in range(2*n-1)]
        # 右斜i= n-1-(row-col)
        rightUsed = [False for _ in range(2*n-1)]

        queens = [["." for _ in range(n)] for _ in range(n)]
        def backtrack(res,queens,csUsed,leftUsed,rightUsed,row):
            if row == n:
                q = []
                for queen in queens:
                    q.append("".join(queen[:]))
                res.append(q)
                return
            for col in range(n):
                leftidx = row + col
                rightidx = n - 1 - (row - col)
                canUsed = csUsed[col] or leftUsed[leftidx] or rightUsed[rightidx]
                if not canUsed:
                    queens[row][col] = "Q"
                    csUsed[col] = True
                    leftUsed[leftidx] = True
                    rightUsed[rightidx] = True
                    backtrack(res,queens,csUsed,leftUsed,rightUsed,row+1)
                    queens[row][col] = "."
                    csUsed[col] = False
                    leftUsed[leftidx] = False
                    rightUsed[rightidx] = False

        res = []
        backtrack(res,queens,csUsed,leftUsed,rightUsed,0)
        return res




if __name__ == '__main__':
    n = 8
    sl = Solution()
    res = sl.solveNQueens(n)
    print(res)