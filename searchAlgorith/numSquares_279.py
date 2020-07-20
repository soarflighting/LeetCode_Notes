# 279.完全平方数（Medium)
# 给定正整数n,找到若干个完全平方数（比如1,4,9,16，...）使得它们的和等于n。
# 你需要让组成和的完全平方数的个数最少。
# 可以将每个整数看成图中的一个节点，如果两个整数之差为一个平方数，
# 那么这两个整数所在的节点就有一条边。
# 要求解最小的平方数数量，就是求解从节点 n 到节点 0 的最短路径。
# 本题也可以用动态规划求解，在之后动态规划部分中会再次出现。

# 贪心算法 + BFS
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
        level = 0
        queue = {n}
        while len(queue)!=0:
            print(queue)
            level += 1
            next_queue = set()
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        print(remainder)
                        return level
                    elif remainder<square_num:
                        break
                    else:
                        next_queue.add(remainder-square_num)

            queue = next_queue
        return level


if __name__ == '__main__':
    n = 12
    sl = Solution()
    res = sl.numSquares(n)
    print(res)