# 79.单词搜索（Medium)
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，
# 其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
# 示例:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0 or board is None:
            return False
        m = len(board)
        n = len(board[0])
        if m*n<len(word):
            return False
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def inGrid(x,y):
            return x>=0 and x<m and y>=0 and y<n
        def backtrack(x,y,index,visited):
            if index == len(word)-1:
                return board[x][y] == word[index]
            if board[x][y] == word[index]:
                visited[x][y] = True
                for d in directions:
                    newX = x + d[0]
                    newY = y + d[1]
                    if inGrid(newX,newY) and not visited[newX][newY] and backtrack(newX,newY,index+1,visited):
                        return True
                visited[x][y] = False
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0,visited):
                    return True
        return False


    def exist_1(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0 or board is None:
            return False
        m = len(board)
        n = len(board[0])
        if m*n<len(word):
            return False
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def inGrid(x,y):
            return x>=0 and x<m and y>=0 and y<n
        def backtrack(x,y,index,visited):
            if index == len(word)-1:
                print(board[x][y] == word[index])
                return board[x][y] == word[index]
            if board[x][y] == word[index]:
                visited[x][y] = True
                for d in directions:
                    newX = x + d[0]
                    newY = y + d[1]
                    if inGrid(newX,newY) and not visited[newX][newY]:
                        if backtrack(newX,newY,index+1,visited):
                            return True
                visited[x][y] = False
            return False

        for i in range(m):
            for j in range(n):
                print(i,j,backtrack(i,j,0,visited))
                print(backtrack(i,j,0,visited) == True)
                print(backtrack(i,j,0,visited))
                if backtrack(i,j,0,visited) == True:
                    return True
        return False

if __name__ == '__main__':
    sl = Solution()
    board = [['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']]
    word = "SEE"
    res = sl.exist_1(board,word)
    print(res)
