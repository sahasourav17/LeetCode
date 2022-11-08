'''
    Iterative Approach
    Time Complexity: O(N)
    Space Complexity: O(1)
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return

        prevNode = None
        curNode = head
        nextNode = None

        while curNode != None:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode

            if nextNode != None:
                nextNode = nextNode.next;
        return prevNode
