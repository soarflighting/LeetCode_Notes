# 88.合并两个有序数组（Easy)
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
class Solution(object):

    # 需要从尾开始遍历，否则在 nums1 上归并得到的值会覆盖还未进行归并比较的值
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index1 = m-1
        index2 = n-1
        indexm = m+n-1
        while index1>=0 and index2>=0:
            if nums1[index1]<nums2[index2]:
                nums1[indexm] = nums2[index2]
                indexm -= 1
                index2 -= 1
            else:
                nums1[indexm] = nums1[index1]
                indexm -= 1
                index1 -= 1
        if index1 <0:
            print(index2)
            nums1[0:indexm+1] = nums2[0:index2+1]
            print(nums2[0:index2])
        if index2 <0:
            print(index1)
            nums1[0:indexm+1] = nums1[0:index1+1]
            print(nums1[0:index1+1])
        return nums1


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,4,7]
    n = 3
    sl = Solution()
    res = sl.merge(nums1,m,nums2,n)
    print(res)

