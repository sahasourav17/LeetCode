# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        return l == l[::-1]

# another efficient solution
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # no element
        if head == None:
            return True

        # only one element
        elif head != None and head.next == None:
            return True
        else:
            slow,fast,l = head,head,[]
            while fast and fast.next:
                l.append(slow.val)
                slow = slow.next
                fast = fast.next.next
            if fast:
                slow = slow.next

            # palindrome check
            while slow:
                if slow.val != l.pop():
                    return False
                else:
                    slow = slow.next
            return True
