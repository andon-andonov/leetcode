# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = odd_tail = head
        even_head = even_tail = head.next if head is not None else None
        while even_tail is not None and even_tail.next is not None:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
            even_tail.next = odd_tail.next
            even_tail = even_tail.next
            odd_tail.next = even_head
        return odd_head
