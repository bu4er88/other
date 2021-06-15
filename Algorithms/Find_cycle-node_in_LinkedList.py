'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Solution 1 --> O(n) memory and O(n) speed
        # seen = set()
        # i = head
        # j = head.next
        # while i != j:
        #     if j in None or j.next in None:
        #         return
        #     if i == j:
        #         return j
        #     seen.add(head)
        #     count += 1
        #     head = head.next

        # Solution 2 --> O(1) memory and O(n) speed
        i = headA
        j = headB
        while i != j:
            if i is None:
                i = headB
            else:
                i = i.next
            if j is None:
                j = headA
            else:
                j = j.next
        return i
