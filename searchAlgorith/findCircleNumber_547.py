# 547.朋友圈（Medium)
# 班上有 N 名学生。其中有些人是朋友，有些则不是。
# 他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，
# 那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
# 如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
# 你必须输出所有学生中的已知的朋友圈总数。
# 示例 1:
# 输入:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 注意：
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n =  len(M)
        circelNum = 0
        visited = [0]*n
        def dfs(visited,i):
            for j in range(0,n):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(visited,j)
        for i in range(0,n):
            if visited[i] == 0:
                dfs(visited,i)
                circelNum+=1
        return circelNum


    def findCircleNum_1(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if M == None or len(M) == 0:
            return 0
        stack = []
        n = len(M)
        circelNum = 0
        visited = [0]*n
        for i in range(0,n):
            if visited[i] == 0:
                for j in range(0,n):
                    if M[i][j] == 1 and visited[j] == 0:
                        visited[j] = 1
                        stack.append(j)
                        while len(stack) != 0:
                            x = stack.pop()
                            for k in range(0,n):
                                if M[x][k] == 1 and visited[k] == 0:
                                    visited[k] = 1
                                    stack.append(k)
                        circelNum+=1
        return circelNum

if __name__ == '__main__':
    M = [[1,0,0,1],
         [0,1,1,0],
         [0,1,1,1],
         [1,0,1,1]]
    sl = Solution()
    res = sl.findCircleNum_1(M)
    print(res)
