# 75.颜色分类（Medium)
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，
# 原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 注意:不能使用代码库中的排序函数来解决这道题。
# 示例:
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？

# 荷兰三色旗问题解
# # 对于所有 idx < p0 : nums[idx < p0] = 0
# # curr是当前考虑元素的下标
# p0 = curr = 0
# # 对于所有 idx > p2 : nums[idx > p2] = 2
# p2 = len(nums) - 1


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        start = 0
        end = len(nums)-1
        current = 0
        while current <= end:
            if nums[current] == 0:
                # swap(nums,current,start)
                nums[current],nums[start] = nums[start],nums[current]
                current += 1
                start += 1
            elif nums[current]==2:
                # swap(nums,current,end)
                nums[current],nums[end] = nums[end],nums[current]
                end -= 1
            else:
                current += 1
        return nums

if __name__ == '__main__':
    nums = [0, 1, 2, 0, 2, 1,1, 0, 2, 1, 2, 0, 2, 0, 1, 2, 1, 0]
    sl = Solution()
    res = sl.sortColors(nums)
    print(res)
