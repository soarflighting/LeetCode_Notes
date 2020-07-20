# 78.子集（Medium)
# 题目描述：
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集，[1, 2] 和 [2, 1] 这种子集算重复
# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [[3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []]
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums,path,start,res):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(nums,path,i+1,res)
                path.pop()
        res = []
        if len(nums) == 0:
            return [[]]
        backtrack(nums,[],0,res)
        return res

if __name__ == '__main__':
    nums = [1,2,3]
    sl = Solution()
    res = sl.subsets(nums)
    print(res)

