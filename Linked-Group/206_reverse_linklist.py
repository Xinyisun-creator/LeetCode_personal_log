from TestFile import *

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev

# 创建测试用例
head = create_linked_list([1,2,3,4,5])

solution = Solution()
# 打印原始链表
print("Original linked list:")
print_linked_list(head)

head = solution.reverseList(head)
# 打印修改后的链表
print("Modified linked list:")
print_linked_list(head)