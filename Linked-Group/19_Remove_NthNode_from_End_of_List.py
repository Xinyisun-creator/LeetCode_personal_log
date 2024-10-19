from TestFile import *

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

                

# 创建测试用例
head = create_linked_list([1,2,3,4,5,6])

solution = Solution()
# 打印原始链表
print("Original linked list:")
print_linked_list(head)

head = solution.removeNthFromEnd(head,n=2)
# 打印修改后的链表
print("Modified linked list:")
print_linked_list(head)