# 257.二叉树的所有路径（Easy)
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        values = []
        def isLeaf(node):
            return node.left == None and node.right == None
        def buildPath(values):
            s = []
            for i in range(len(values)):
                s.append(str(values[i]))
                if i!= len(values)-1:
                    s.append("->")
            return "".join(s)
        def backtrack(node,values,paths):
            if node is None:
                return
            values.append(node.val)
            if isLeaf(node):
                paths.append(buildPath(values))
            else:
                backtrack(node.left,values,paths)
                backtrack(node.right,values,paths)
            values.pop()
        if root is None:
            return paths
        backtrack(root,values,paths)
        return paths



if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    root = node1
    node1.left = node2
    node1.right = node3
    node2.right = node4
    sl = Solution()
    res = sl.binaryTreePaths(root)
    print(res)


