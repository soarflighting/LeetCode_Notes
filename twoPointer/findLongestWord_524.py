# 524.通过删除字母匹配到字典里的最长单词（Medium）
# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，
# 该字符串可以通过删除给定字符串的某些字符来得到。
# 如果答案不止一个，返回长度最长且字典顺序最小的字符串。
# 如果答案不存在，则返回空字符串。
# 示例 1:
# 输入:s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 输出: "apple"
class Solution(object):
    # 通过删除字符串 s 中的一个字符能得到字符串 t，可以认为 t 是 s 的子序列，
    # 我们可以使用双指针来判断一个字符串是否为另一个字符串的子序列。
    def isSubstr(self,s,word):
        n1 = len(s)
        n2 = len(word)
        i=0
        j=0
        while i<n1 and j<n2:
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == n2

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ### 先按长度排序，在按字典序排序
        d.sort(key=lambda x: (-len(x), x))
        isSubstr = False
        longestword = ""
        for word in d:
            l1 = len(longestword)
            l2 = len(word)
            isSubstr = self.isSubstr(s,word)
            if isSubstr and l1<l2:
                longestword = word
            else:
                continue
        return longestword



if __name__ == '__main__':
    s = "abpcplea"
    d = ["ale","apple","monkey","plea"]
    sl = Solution()
    res = sl.findLongestWord(s,d)
    print(res)



