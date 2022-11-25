# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
            initially previous node points to None
        '''
        temp,prev = head,None

        while temp != None:

            '''
                Case 1: If the first node value is equal to val
                Case 2: If any middle node value == val
                Case 3: Keep moving until no node val is equal to val
            '''
            if temp.val == val and prev == None:
                temp = temp.next
                head = temp

            elif temp.val == val:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return head
