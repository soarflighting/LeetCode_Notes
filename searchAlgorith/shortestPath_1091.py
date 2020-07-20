# 1091.二进制矩阵中的最短路径（Medium）
# 在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
# 一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：
# 相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
# C_1 位于 (0, 0)（即，值为 grid[0][0]）
# C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
# 如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
# 返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。
# 示例：
# 输入：[[0,1],[1,0]]
# 输出：2

# 思路分析：
#
# 要找到左上角到右下角的最短路径，最短路径嘛，自然就想到了使用BFS。
# 在二维平面上，八个方向可以进行移动，使用int[][] directions表示八个方向。比如{1,1}就表示右下方向。二维平面常规做法，使用函数boolean inGrid(int x, int y)判断某个点是否在矩形范围内（防止数组越界）。
# 首先将成员变量，表示矩形行列数的row, col初始化。然后如果左上角或者右下角为1，一定无法从左上角到右下角，直接返回-1。
# 然后开始使用队列模拟BFS：
# 我们需要去判断哪些路径已经走过，并且我们还需要知道走到某一个点时的步数，结合题目规定0是通行，1是不可通行，走过的点也不会再走相当于不可通行。所以我们可以用grid[newX][newY] == 0表示没有访问过的可通行的点。
# 按照题意，起点也有长度1，所以设置grid[0][0] = 1;，且 pos.add(new int[]{0,0});。
# 用队列模拟的循环条件!pos.isEmpty() && grid[row - 1][col - 1] == 0，第二个条件不满足时，说明已经有路径到达右下角了，就可以停止搜索。
# 弹出某个点的坐标，通过int preLength = grid[xy[0]][xy[1]];得到到达该点的长度，然后遍历8个方向，试图访问下一个点，满足inGrid(newX, newY) && grid[newX][newY] == 0则可以访问，然后到达下一个点的路径长度就变为grid[newX][newY] = preLength + 1;，然后这个点grid[newX][newY] != 0了，就不会被重复访问。
# 循环结束后，可能是搜索完成但没有到达右下角，此时grid[row - 1][col - 1] == 0；也可能是已经找到到达右下角的路径，按BFS，此时grid[row - 1][col - 1]即为答案。所以最后返回grid[row - 1][col - 1] == 0 ? -1 : grid[row - 1][col - 1];
# 时间复杂度为O(n)O(n)，因为每个元素遍历了一次，n为元素的个数。空间复杂度为O(k)O(k)，k为过程中队列的最大元素个数。

from queue import Queue
class Solution(object):

    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,1],[1,-1],[-1,1]]
        row = len(grid)
        col = len(grid[0])
        def inGrid(x,y):
            return x>=0 and x<row and y>=0 and y<col
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1
        pos = Queue()
        grid[0][0] = 1
        pos.put([0,0])
        while(pos.empty() is not True and grid[row-1][col-1]==0):
            xy = pos.get()
            preLength = grid[xy[0]][xy[1]]
            for i in range(0,8):
                newX = xy[0]+ directions[i][0]
                newY = xy[1]+ directions[i][1]
                if inGrid(newX,newY) and grid[newX][newY] == 0:
                    pos.put([newX,newY])
                    grid[newX][newY] = preLength + 1

        return -1 if grid[row-1][col-1] ==0 else grid[row-1][col-1]


    def shortestPathBinaryMatrix_1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,1],[1,-1],[-1,1]]
        row = len(grid)
        col = len(grid[0])
        def inGrid(x,y):
            return x>=0 and x<row and y>=0 and y<col
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1
        pos = []
        grid[0][0] = 1
        pos.append([0,0])
        while(len(pos)!=0 and grid[row-1][col-1]==0):
            xy = pos[0]
            pos = pos[1:]
            preLength = grid[xy[0]][xy[1]]
            for i in range(0,8):
                newX = xy[0]+ directions[i][0]
                newY = xy[1]+ directions[i][1]
                if inGrid(newX,newY) and grid[newX][newY] == 0:
                    pos.append([newX,newY])
                    grid[newX][newY] = preLength + 1

        return -1 if grid[row-1][col-1] ==0 else grid[row-1][col-1]


if __name__ == '__main__':
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    sl = Solution()
    res = sl.shortestPathBinaryMatrix_1(grid)
    print(res)




