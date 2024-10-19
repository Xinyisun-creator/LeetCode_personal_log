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
