# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = left = right = ListNode(0, head)
        for i in range(n+1):
            right = right.next
        while right != None:
            print(left)
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
        