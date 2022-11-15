class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            if there is 0 or 1 node and no cycle
        '''
        if head is None or head.next is None:
            return None

        slow = head.next
        fast = head.next.next

        '''
            two nodes but no cycle
            as fast pointer reaches at the end
        '''
        if fast is None:
            return None

        while slow != fast:
            if fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next

            else:
                return None

        '''
            If cycle found then we will go one position at 
            a time for both pointer
        '''
        fast = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast