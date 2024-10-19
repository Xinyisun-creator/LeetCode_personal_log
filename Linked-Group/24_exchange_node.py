# Definition for singly-linked list.

from TestFile import *

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(next=head)
        current = dummy

        while current.next and current.next.next:
            temp = current.next.next
            temp1 = current.next
            temp2 = current.next.next.next
            current.next = temp
            temp.next = temp1
            temp1.next = temp2
            current = current.next.next



        return dummy.next


# 创建测试用例
head = create_linked_list([1,2,3,4,5,6])

solution = Solution()
# 打印原始链表
print("Original linked list:")
print_linked_list(head)

head = solution.swapPairs(head)
# 打印修改后的链表
print("Modified linked list:")
print_linked_list(head)