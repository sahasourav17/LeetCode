class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Initializing two pointer, basically floyd tortoise hare approach.
            slow pointer will move one position at a time and
            fast pointer will move two at a time.
        '''
        slow = head
        fast = head

        '''
            Iterating till the fast pointer
            reaches at the end.
        '''
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        '''
            returning the slow pointer as it will
            always in the middle position.
        '''
        return slow