# 130.被围绕的区域（Medium)
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 示例:
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
# X X X X
# X X X X
# X X X X
# X O X X
# 解释:
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
# 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
# 如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return board
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        row = len(board)
        col = len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=row or j>=col or board[i][j] == "X" or board[i][j] =="#":
                return
            board[i][j] = "#"
            for d in directions:
                dfs(i+d[0],j+d[1])

        for i in range(0,row):
            for j in range(0,col):
                isEdge = i==0 or j==0 or i == row-1 or j == col-1
                if isEdge and board[i][j] == "O":
                    dfs(i,j)
        for i in range(0,row):
            for j in range(0,col):
                if board[i][j] =="O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
        return board


if __name__ == '__main__':
    sl = Solution()
    # board = [['X','X','X','X'],
    #          ['X','O','O','X'],
    #          ['X','X','O','X'],
    #          ['X','O','X','X']]
    board = []
    res = sl.solve(board)
    print(res)




