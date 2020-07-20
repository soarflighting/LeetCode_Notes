# 131.分割回文字符串（Medium)
# 问题描述
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
# 示例:
# 输入: "aab"
# 输出:
# [["aa","b"],
#   ["a","a","b"]]
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def backtrack(s,res,path):
            if len(s) == 0:
                res.append(path[:])
                return
            for i in range(len(s)):
                temps = s[0:i+1]
                if temps == temps[::-1]:
                    path.append(temps)
                    backtrack(s[i+1:],res,path)
                    path.pop()

        res = []
        if len(s) == 0:
            return res
        backtrack(s,res,[])
        return res

if __name__ == '__main__':
   s = "aab"
   sl = Solution()
   res = sl.partition(s)
   print(res)