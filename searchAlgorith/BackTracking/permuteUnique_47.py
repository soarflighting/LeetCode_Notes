# 47.全排列（Medium)
# 给定一个包含重复的序列，返回所有不重复的全排列
# 示例:
# 输入: [1,1,2]
# 输出:
# [[1,1,2],
#   [1,2,1],
#   [2,1,1]]

# 第一种方法：回溯得到所有的排列数组，然后在结果中去重操作
# 第二种算法：先对nums 数组进行排序，然后利用剪枝方法对重复操作的地方进行剪枝
# 1、在图中 ② 处，搜索的数也和上一次一样，但是上一次的 1 还在使用中；
# 2、在图中 ① 处，搜索的数也和上一次一样，但是上一次的 1 刚刚被撤销，
# 正是因为刚被撤销，下面的搜索中还会使用到，因此会产生重复，
# 剪掉的就应该是这样的分支。

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums,path,visited,res):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    ## 剪枝操作
                    if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(nums,path,visited,res)
                    path.pop()
                    visited[i] = False
        n = len(nums)
        res = []
        if n == 0:
            return [[]]
        nums.sort()
        visited = [False for _ in range(n)]
        backtrack(nums,[],visited,res)
        return res


if __name__ == '__main__':
    nums = [3,3,0,3]
    sl = Solution()
    res = sl.permuteUnique(nums)
    print(res)

