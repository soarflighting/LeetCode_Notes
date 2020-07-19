# 633. 平方数之和 (Easy)
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a的平方 + b的平方 = c。
# 示例1:
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
# 输入: 3
# 输出: False

# 本题的关键是右指针的初始化，实现剪枝，从而降低时间复杂度。设右指针为 x，
# 左指针固定为 0，
# 为了使 02 + x2 的值尽可能接近 target，我们可以将 x 取为 sqrt(target)。
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        b = int(math.sqrt(c))
        while a<=b:
            s = a**2+b**2
            if s == c:
                return True
            elif s<c:
                a += 1
            else:
                b -= 1
        return False

if __name__ == '__main__':
    c = 2
    sl = Solution()
    res = sl.judgeSquareSum(c)
    print(res)


