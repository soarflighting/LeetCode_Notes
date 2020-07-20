# 77.组合（Medium)
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 示例:
# 输入: n = 4, k = 2
# 输出:
# [ [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(ans,path,s):
            print(path)
            print(s)
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(s,n+1):
                path.append(i)
                backtrack(ans,path,i+1)
                path.pop()
        if n == 0:
            return ans
        backtrack(ans,[],1)
        return ans

    def combine_1(self, n, k):
        nums = list(range(1,k+1))+[n+1]
        output = []
        j = 0
        while j<k:
            output.append(nums[:k])
            j = 0
            while j<k and nums[j+1] == nums[j]+1:
                print(nums,j)
                nums[j] = j+1
                print(nums)
                j += 1
            nums[j] += 1
            print(nums)
        return output

if __name__ == '__main__':
    n = 4
    k = 2
    sl = Solution()
    res = sl.combine_1(n,k)
    print(res)

