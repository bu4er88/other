# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        i = head
        j = even_start = head.next
        while True:
            if i.next is None or j.next is None:
                i.next = even_start
                return head
            i.next = i.next.next
            j.next = j.next.next
            i = i.next
            j = j.next
