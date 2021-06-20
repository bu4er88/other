# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        extended = ListNode(0)   # adding a new head node in the beginning of the LinkedList
        extended.next = head  # connect new head to the initial head of the LList
        i = j = extended
        for _ in range(n):
            j = j.next
        while j.next != None:
            j = j.next
            i = i.next
        i.next = i.next.next  # skip N-th node
        return extended.next  # return the extended LinkedList without unnecessary 0-th node
