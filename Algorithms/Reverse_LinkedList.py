# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:  # check whether the list is empty or of 1 element
            return head
        new_head = head
        while head.next != None:
            temp = head.next
            head.next = head.next.next
            temp.next = new_head
            new_head = temp
        return new_head
