# 680.验证回文字符串（Easy)
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 示例 1:
# 输入: "aba"
# 输出: True
# 注意:字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
class Solution(object):

    def isPalindrome(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s,left,right-1)or self.isPalindrome(s,left+1,right)
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    sl = Solution()
    s = "cdabbac"
    res = sl.validPalindrome(s)
    print(res)
