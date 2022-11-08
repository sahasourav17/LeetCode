# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
            creates a dummy node for handling edge cases
        '''
        dummy = ListNode()
        tail = dummy

        '''
            while no linked list is not null
        '''
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        '''
            if one of the list null
        '''
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        '''
            returning dummy.next because we've added
            an dummy node before our actual node.
        '''
        return dummy.next

'''
    Time Complexity: O(N)
    Space Complexity: O(1)
'''
