# 39.组合求和（Medium)
# 问题描述：
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 回溯算法 + 剪枝
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(candidates,target,path,res,start,s):
            if s >= target:
                if s == target:
                    res.append(path[:])
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                s += candidates[i]
                # i 为剪枝点
                backtrack(candidates,target,path,res,i,s)
                s -= candidates[i]
                path.pop()
        res = []
        if candidates is None or len(candidates) == 0:
            return [[]]
        s = 0
        backtrack(candidates,target,[],res,0,s)
        return res


if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 0
    sl = Solution()
    res = sl.combinationSum(candidates,target)
    print(res)

