# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        next_sum = temp

        while next_sum:
            sum = 0
            while next_sum.val != 0:
                sum += next_sum.val
                next_sum = next_sum.next
            
            temp.val = sum

            next_sum = next_sum.next
            temp.next = next_sum
            temp = temp.next
        return head.next

# Recursive approach

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        if not head:
            return head
        
        temp = head
        sum = 0

        while temp.val != 0:
            sum += temp.val
            temp = temp.next

        head.val = sum
        head.next = self.mergeNodes(temp)

        return head
