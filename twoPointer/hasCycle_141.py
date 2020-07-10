# 141.环形链表（Easy)
# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，
# 我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 使用双指针，一个指针每次移动一个节点，
    # 一个指针每次移动两个节点，如果存在环，那么这两个指针一定会相遇。
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        l1 = head
        l2 = head.next
        while l1!=None and l2!=None and l2.next != None:
            if l1==l2:
                return True
            l1 = l1.next
            l2 = l2.next.next
        return False


