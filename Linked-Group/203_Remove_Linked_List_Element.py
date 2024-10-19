class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(lst):
    dummy = ListNode(0)
    ptr = dummy
    for number in lst:
        ptr.next = ListNode(number)
        ptr = ptr.next
    return dummy.next

def print_linked_list(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next


# 创建测试用例
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
val = 6

solution = Solution()
# 打印原始链表
print("Original linked list:")
print_linked_list(head)
# 移除值为6的节点
head = solution.removeElements(head, val)
# 打印修改后的链表
print("Modified linked list:")
print_linked_list(head)