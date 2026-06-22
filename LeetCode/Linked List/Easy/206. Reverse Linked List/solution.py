# Complexity:
# Time: O(n): We traverse the list once, where n is the number of nodes.
# Space: O(1): We are using a constant amount of extra space.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        return prev
