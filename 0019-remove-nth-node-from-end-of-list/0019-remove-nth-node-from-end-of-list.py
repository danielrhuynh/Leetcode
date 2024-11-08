# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def countNodes(head):
            count = 0
            curr = head
            while curr is not None:
                count += 1
                curr = curr.next
            return count
        
        dummy = head
        nNodes = countNodes(dummy)
        if nNodes == 1:
            return None
        nFromHead = nNodes - n
        dummy = head
        if nFromHead == 0:
            return head.next
        else:
            for i in range(nFromHead-1):
                dummy = dummy.next
            if dummy.next:
                dummy.next = dummy.next.next
            else:
                dummy.next = None
        return head
        