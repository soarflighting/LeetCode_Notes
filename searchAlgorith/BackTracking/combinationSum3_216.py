# 216.组合求和III（Medium)
# 问题描述：
# 找出所有相加之和为 n 的 k 个数的组合。
# 组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
# 所有数字都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(k,n,path,start,end,res,s):
            if len(path) == k and s == n:
                res.append(path[:])
                return
            if s > n or len(path)> k:
                return
            for i in range(start,end):
                path.append(i)
                s += i
                backtrack(k,n,path,i+1,end,res,s)
                s -= i
                path.pop()
        res = []
        backtrack(k,n,[],1,10,res,0)
        return res

if __name__ == '__main__':
    k = 0
    n = 1
    sl = Solution()
    res = sl.combinationSum3(k,n)
    print(res)
