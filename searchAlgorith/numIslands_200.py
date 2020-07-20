# 200.岛屿数量（Medium)
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围
# 示例 1:
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) == 0:
            return 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        stack = []
        row = len(grid)
        col = len(grid[0])
        islandnum = 0
        def inGrid(x,y):
            return x>=0 and x<row and y>=0 and y<col
        for i in range(0,row):
            for j in range(0,col):
                if grid[i][j] == "1":
                    stack.append([i,j])
                    grid[i][j]="0"
                    while len(stack)!=0:
                        xy = stack.pop()
                        for d in directions:
                            newX = xy[0]+d[0]
                            newY = xy[1]+d[1]
                            if  inGrid(newX,newY) and grid[newX][newY] == "1":
                                stack.append([newX,newY])
                                grid[newX][newY] = "0"
                    islandnum+=1
        return islandnum


if __name__ == '__main__':
    sl = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    res = sl.numIslands(grid)
    print(res)
