# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        nodeDict = {}
        while head:
            nodeDict[count] = head
            head = head.next
            count += 1
        return nodeDict[count//2]
            
            