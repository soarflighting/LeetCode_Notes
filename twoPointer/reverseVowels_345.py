# 345.翻转字符串中的元音字母 （Easy)
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 示例 1:
# 输入: "hello"
# 输出: "holle"
# 示例 2:
# 输入: "leetcode"
# 输出: "leotcede"
# 元音字母不包含字母"y"。
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yy = ['a','e','i','o','u','A','E','I','O','U']
        n = len(s)
        i = 0
        j = n-1
        while i<j:
            if s[i] in yy and s[j] in yy:
                if s[i] != s[j]:
                    temp = s[j]
                    trailer = s[j+1:] if j+1<n else ""
                    s = s[0:j]+s[i]+trailer
                    s = s[0:i]+temp+s[i+1:]
                i += 1
                j -= 1
            elif s[i] in yy :
                j -= 1
            else:
                i += 1
        return s

    def reverseVowels_2(self, s):
        x={'a','e','i','o','u','A','E','I','O','U'}
        res=[]
        j=len(s)-1
        for i,k in enumerate(s):
            if k in x:
                while s[j] not in x:
                    j-=1
                res.append(s[j])
                j-=1
                print(res)
            else:
                res.append(k)
                print(res)
        return ''.join(res)


if __name__ == '__main__':
    sl = Solution()
    c = "leetcode"
    res = sl.reverseVowels_2(c)
    print(res)

