# 695.岛屿的最大面积（Medium)
# 给定一个包含了一些 0 和 1 的非空数组grid.
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，
# 这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
# 你可以假设 grid 的四个边缘都被 0（代表水）包围着。
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
# 示例 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or len(grid) == 0:
            return 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        stack = []
        row = len(grid)
        col = len(grid[0])
        maxArea = 0
        # def inGrid(x,y):
        #     return x>=0 and x<row and y>=0 and y<col
        def dfs(gird,i,j):
            if i<0 or i>=row or j <0 or j>=col or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            for d in directions:
                area += dfs(grid,i+d[0],j+d[1])
            return area
        for i in range(0,row):
            for j in range(0,col):
                maxArea = max(maxArea,dfs(grid,i,j))
        return maxArea

    def maxAreaOfIsland_1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or len(grid) == 0:
            return 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        stack = []
        row = len(grid)
        col = len(grid[0])
        maxArea = 0
        area = 0
        def inGrid(x,y):
            return x>=0 and x<row and y>=0 and y<col
        for i in range(0,row):
            for j in range(0,col):
                if grid[i][j] == 1:
                    stack.append([i,j])
                    grid[i][j]=0
                    area = 1
                    while len(stack)!=0:
                        xy = stack.pop()
                        for d in directions:
                            newX = xy[0]+d[0]
                            newY = xy[1]+d[1]
                            if  inGrid(newX,newY) and grid[newX][newY] == 1:
                                stack.append([newX,newY])
                                area += 1
                                grid[newX][newY] = 0
                    maxArea = max(maxArea,area)
        return maxArea


if __name__ == '__main__':
    # grid = [[1]]

    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    sl = Solution()
    res = sl.maxAreaOfIsland_1(grid)
    print(res)

