# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # straightforward solution

        while head and head.val == val:
            head = head.next
        i = head
        while i != None and i.next != None:
            if i.next.val == val:
                i.next = i.next.next
            else:
                i = i.next
        return head

        # # solution with addition of the 0-th node

        # extended = ListNode(next=head)
        # i = extended
        # while i != None and i.next != None:
        #     if i.next.val == val:
        #         i.next = i.next.next
        #     else:
        #         i = i.next
        # return extended.next
