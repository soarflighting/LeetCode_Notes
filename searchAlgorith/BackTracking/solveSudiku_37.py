# 37.解数独（Hard)
# 问题描述：
# 编写一个程序，通过已填充的空格来解决数独问题。
# 一个数独的解法需遵循如下规则：
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。
# Note:
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 行中已用过的数
        rsused = [[False for _ in range(9)] for _ in range(9)]
        # 列中已用过的数
        csused = [[False for _ in range(9)] for _ in range(9)]
        # 3x3方阵中用过的数
        cubesused = [[False for _ in range(9)] for _ in range(9)]

        # 计算属于那个方阵
        def cubeNum(i,j):
            r = i//3
            c = j//3
            return r*3+c

        # 回溯 + 剪枝
        def backtrack(board,rsused,csused,cubesused,row,col):
            # 边界校验，如果已经填充，返回True,表示结束
            if col == len(board):
                col = 0
                row += 1
                if row == len(board[0]):
                    return True
            # 是空的话则表示填充
            if board[row][col] == ".":
                #尝试填充1-9的数字
                for num in range(0,9):
                    # 若num符合未使用条件，则使用num
                    canUsed = rsused[row][num] or csused[col][num] or cubesused[cubeNum(row,col)][num]
                    if  not canUsed:
                        rsused[row][num] = True
                        csused[col][num] = True
                        cubesused[cubeNum(row,col)][num] = True

                        board[row][col] = str(num+1)
                        # 若当前填充条件可以满足数独，则直接返回
                        if backtrack(board,rsused,csused,cubesused,row,col+1):
                            return True
                        # 如果当前填充不能满足数独，则将本次循环的num取出，尝试下一个num
                        board[row][col] = '.'
                        rsused[row][num] = False
                        csused[col][num] = False
                        cubesused[cubeNum(row,col)][num] = False
            else:
                return backtrack(board,rsused,csused,cubesused,row,col+1)
            return False


        # 初始化
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    num = int(board[r][c])
                    if 1 <= num and num <=9 :
                        rsused[r][num-1] = True
                        csused[c][num-1] = True
                        cubesused[cubeNum(r,c)][num-1] = True

        backtrack(board,rsused,csused,cubesused,0,0)
        return board


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
    sl = Solution()
    res = sl.solveSudoku(board)
    print(res)


