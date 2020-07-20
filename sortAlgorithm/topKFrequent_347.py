# 347.前K个高频元素（Medium）
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
class Solution(object):
    ### 桶排序
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n_f = {}
        f_n = {}
        for i in nums:
            if i not in n_f:
                n_f[i] = 1
            else:
                n_f[i] += 1

        print(n_f)
        for n,f in n_f.items():
            if f not in f_n:
                f_n[f] = [n]
            else:
                f_n[f].append(n)
        print(f_n)
        arr = []
        for x in range(len(nums),0,-1):
            if x in f_n:
                for i in f_n[x]:
                    arr.append(i)
        print(arr)
        return arr[:k]

if __name__ == '__main__':
    nums = [1,1,1,2,2,3,3]
    k = 2
    sl = Solution()
    res = sl.topKFrequent(nums,k)
    print(res)


