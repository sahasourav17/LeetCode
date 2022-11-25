# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        '''
            My idea to solve this problem:
             1. Find the length of the linked list
             2. Calculate ListLength - n to find the element
                to be removed from the beginning of the list
             3. Remove the desire element
        '''

        '''
            Calculating Linked list length
            lenList: the list length
        '''
        temp,lenList = head,0
        while temp:
            lenList += 1
            temp = temp.next

        '''
            Case 1:
                if the length of the list One
                then after removal there will be no element
                So, We return None

            Case 2:
                if n is equal to the listLen.
                it means that we've to remove the first element from the
                beginning of the list.
                So, we just return head.next
        '''
        if lenList == 1:
            head = None
            return head
        if lenList == n:
            return head.next


        '''
            Removing k th element
            from the beginning
        '''
        k = lenList-n

        newHead = head
        for i in range(1,k):
            newHead = newHead.next

        if newHead.next.next:
            newHead.next = newHead.next.next
        else:
            newHead.next = None

        return head