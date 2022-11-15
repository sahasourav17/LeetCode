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

# Approach -2 (Concise)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        slow,fast,vis= head,head,head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                while vis != slow:
                    slow = slow.next
                    vis = vis.next
                return slow
        return None
