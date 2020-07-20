# 46.全排列（Medium)
# 给定一个没有重复的数字的序列，返回所有可能的全排列
# 示例:
# 输入: [1,2,3]
# 输出:
# [ [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]]
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


if __name__ == '__main__':
    nums = [1,2,3]
    sl = Solution()
    res = sl.permute(nums)
    print(res)
