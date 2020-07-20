# 93.复原IP地址（Meidum）
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        segments = []
        output = []
        def valid(segment):
            return int(segment) <= 255 if segment[0]!='0'else len(segment) == 1

        def update_output(curr_pos):
            segment = s[curr_pos+1:n]
            if valid(segment):
                segments.append(segment)
                output.append(".".join(segments))
                segments.pop()
        def backward(prev_pos = -1,dots=3):
            for curr_pos in range(prev_pos+1,min(n-1,prev_pos+4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                print(segment)
                if valid(segment):
                    segments.append(segment)
                    if dots-1 == 0:
                        update_output(curr_pos)
                    else:
                        backward(curr_pos,dots-1)
                    segments.pop()

        backward()
        return output

if __name__ == '__main__':
    s = "25525511135"
    sl = Solution()
    res = sl.restoreIpAddresses(s)
    print(res)

