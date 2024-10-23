

class ListNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(next = head)
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next


class MyLinkedList(object):
    def __init__(self):
        self.dummy_head = ListNode()
        self.list_size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index > self.list_size:
            return -1
        else:
            current = self.dummy_head
            for i in range(index):
                current = current.next
            return current.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        new_node.next = self.dummy_head.next
        self.dummy.next = new_node
        self.list_size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.dummy_head
        for i in range(self.list_size):
            current = current.next
        current.next = ListNode(val)


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.list_size:
            return -1
        else:
            current = self.dummy_head
            for i in range(index):
                current = current.next
            if current.next.next:
                current.next = ListNode(val,next = current.next.next)
            else:
                current.next = ListNode(val)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index > self.list_size:
            return -1
        else:
            current = self.dummy_head
            for i in range(index-1):
                current = current.next
            if current.next.next:
                current.next = current.next.next
            else:
                current.next = None
        self.list_size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
        
class MyLinkedList(object):
    def __init__(self):
        self.dummy_head = ListNode()
        self.list_size = 0
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.list_size:
            return -1

        current = self.dummy_head.next
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = ListNode(val,self.dummy_head.next)
        self.list_size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.list_size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.list_size:
            return -1

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val,current.next)
        self.list_size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.list_size:
            return -1

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.list_size -= 1
