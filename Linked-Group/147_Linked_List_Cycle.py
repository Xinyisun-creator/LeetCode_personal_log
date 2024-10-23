class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head
        fast = head
        index = 0

        if not head:
            return None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            index  += 1
            if slow == fast:
                print("Detect a cycle in Listnode")
                slow = head
                while slow.next:
                    if fast == slow:
                        return fast
                    slow = slow.next
                    fast = fast.next

        return None