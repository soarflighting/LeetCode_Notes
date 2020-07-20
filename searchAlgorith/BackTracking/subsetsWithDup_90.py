# 90.子集II（Medium)
# 问题描述：
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
# 输入: [1,2,2]
# 输出:
# [[2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []]
# 回溯 + 剪枝
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums,path,start,res):
            res.append(path[:])
            for i in range(start,len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums,path,i+1,res)
                path.pop()
        res = []
        if len(nums) == 0:
            return [[]]
        # 之所以在回溯之前，需要先对nums排序，排序后nums里相同的元素必定相邻，
        # 然后在遍历解空间树的时候，要做一个去重的操作，当遇到重复出现，
        # 也就是和前面相邻元素相同的时候，直接跳过该节点，不让它向下递归
        nums.sort()
        backtrack(nums,[],0,res)
        return res

if __name__ == '__main__':
    nums = [4,4,4,1,4]
    sl = Solution()
    res = sl.subsetsWithDup(nums)
    print(res)
