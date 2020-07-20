# 417.太平洋大西洋的水流问题（Medium)
# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。
# “太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
# 规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
# 请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
# 提示：
# 输出坐标的顺序不重要
# m 和 n 都小于150
# 给定下面的 5x5 矩阵:
#   太平洋 ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * 大西洋
# 返回:
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix is None or len(matrix) == 0:
            return matrix
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        m = len(matrix)
        n = len(matrix[0])
        def inGrid(x,y):
            return x>=0 and x<m and y>=0 and y<n
        def dfs(x,y,visited):
            visited[x][y] = True
            for d in directions:
                newX = x+d[0]
                newY = y+d[1]
                if inGrid(newX,newY) and matrix[x][y] <= matrix[newX][newY] and not visited[newX][newY]:
                    dfs(newX,newY,visited)
        ans = []
        # 到达太平洋
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        # 表示能流到大西洋的点
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(0,n):
            dfs(0,i,p_visited)
            dfs(m-1,i,a_visited)
        for i in range(0,m):
            dfs(i,0,p_visited)
            dfs(i,n-1,a_visited)
        for i in range(0,m):
            for j in range(0,n):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i,j])
        return ans

    def pacificAtlantic_1(self, matrix):
        if not matrix or not matrix[0]: return []
        # 流向太平洋的位置
        res1 = set()
        # 流向大西洋的位置
        res2 = set()
        row = len(matrix)
        col = len(matrix[0])

        # 从边界遍历
        def dfs(i, j, cur, res):
            res.add((i, j))
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[i][j] <= matrix[tmp_i][tmp_j] and (tmp_i, tmp_j) not in res:
                    dfs(tmp_i, tmp_j, matrix[i][j], res)
        # 太平洋
        for i in range(row):
            dfs(i, 0, 0, res1)
        # 太平洋
        for j in range(col):
            dfs(0, j, 0, res1)
        # 大西洋
        for i in range(row):
            dfs(i, col - 1, 0, res2)
        # 大西洋
        for j in range(col):
            dfs(row - 1, j, 0, res2)

        return res1 & res2


if __name__ == '__main__':
    matrix = [[1,2,2,3,5],
              [3,2,3,4,4],
              [2,4,5,3,1],
              [6,7,1,4,5],
              [5,1,1,2,4]]
    sl = Solution()
    res = sl.pacificAtlantic(matrix)
    print(res)
