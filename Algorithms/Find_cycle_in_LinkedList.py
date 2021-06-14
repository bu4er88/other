# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
    # Solution 1 --> O(n)
        # bag = set()
        # while head:
        #      if head in bag:
        #          return True
        #      bag.add(head)
        #      head = head.next

    # Solution 2 --> O(1)
        if head is None:
            return False
        i = head
        j = head.next
        while i != j:
            if j is None or j.next is None:
                return False
            i = i.next
            j = j.next.next
        return True
