# Floyd tortoise and hare method
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
		slow and fast pointer will start from same position at the beginning.
		But slow pointer will move one position at each iteration while fast pointer moves two position.
		So, eventually fast pointer (hare) will catch up the slow pointer (tortoise) if there any cycle exists.
		'''
        slowPointer,fastPointer = head,head
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if fastPointer==slowPointer:
                return True
        return False
# time complexity O(N)