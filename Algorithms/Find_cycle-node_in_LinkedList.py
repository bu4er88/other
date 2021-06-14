# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        # Solution 1 --> O(n)
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

        # Solution 2 --> O(1)
        i = head
        j = head
        while j != None and j.next != None:
            i = i.next
            j = j.next.next
            if i == j:
                i = head
                while i != j:
                    i = i.next
                    j = j.next
                return i
        return None
