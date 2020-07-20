# 215.数组中的第K个最大元素（Medium）
# 在未排序的数组中找到第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 示例 1:
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

import heapq
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        res = nums[n-k]
        return res

    ### 创建一个小顶堆，队中维持k个元素
    def findKthLargest_1(self, nums, k):
         return heapq.nlargest(k, nums)[-1]

    ### 快速排序
    def findKthLargest_2(self, nums, k):

        def partition(left,right,pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index],nums[right] = nums[right],nums[pivot_index]
            store_index = left
            for i in range(left,right):
                if nums[i]<pivot:
                    nums[store_index],nums[i] =  nums[i],nums[store_index]
                    store_index += 1
            nums[right],nums[store_index] = nums[store_index],nums[right]
            return store_index

        def select(left,right,k_smallest):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left,right)
            pivot_index = partition(left,right,pivot_index)

            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left,pivot_index-1,k_smallest)
            else:
                return select(pivot_index+1,right,k_smallest)

        return select(0,len(nums)-1,len(nums)-k)


if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    target = 4
    sl = Solution()
    res = sl.findKthLargest_2(nums,target)
    print(res)