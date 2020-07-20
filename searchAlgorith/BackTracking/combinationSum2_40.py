# 40.组合总和（Medium)
# 题目描述：
# 给定一个数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 回溯算法 + 剪枝操作
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(candidates,target,path,s,res,start):
            if s >= target:
                if s == target:
                    res.append(path[:])
                return
            for i in range(start,len(candidates)):
                # 剪枝处
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                s += candidates[i]
                backtrack(candidates,target,path,s,res,i+1)
                s -= candidates[i]
                path.pop()
        candidates.sort()
        res = []
        if len(candidates) == 0:
            return res
        backtrack(candidates,target,[],0,res,0)
        return res

if __name__ == '__main__':
    candidates = [2,5,2,1,2]
    target = 5
    sl = Solution()
    res = sl.combinationSum2(candidates,target)
    print(res)