# 127.单词接龙（Medium）    最短单词路径
# 给定两个单词（beginWord 和 endWord) 和一个字典
# 找到从beginWord 到 endWord 的最短转换序列的长度
# 转换需遵循如下规则：
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
# 示例 1:
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 输出: 5
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。

from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)
        queue = [(beginWord,1)]
        visited = {beginWord:True}
        while len(queue)!=0:
            current_word,level = queue.pop(0)
            for i in range(L):
                intermediate_word = current_word[:i]+"*"+current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited[word]=True
                        queue.append((word,level+1))
                all_combo_dict[intermediate_word]=[]
        return 0




if __name__ == '__main__':
    sl = Solution()
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ["hot","dot","dog","lot","log","cog"]
    res = sl.ladderLength(beginWord,endWord,wordList)
    print(res)


