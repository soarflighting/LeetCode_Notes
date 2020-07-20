# 451.根据字符出现频率排序（Medium)
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
# 示例 1:
# 输入:"tree"
# 输出:"eert"
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        n_f = {}
        f_n = {}
        for w in s:
            if w not in n_f:
                n_f[w] = 1
            else:
                n_f[w] += 1
        for n,f in n_f.items():
            if f not in f_n:
                f_n[f] = [n]
            else:
                f_n[f].append(n)
        attr = []
        for x in range(len(s),0,-1):
            if x in f_n:
                for i in f_n[x]:
                    attr.append(i*x)
        print(attr)
        return "".join(attr)

if __name__ == '__main__':
    s = "cccaaabb"
    sl = Solution()
    res = sl.frequencySort(s)
    print(res)