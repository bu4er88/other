class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList():

    def __init__(self):
        """"
        Initialize your data structure here.
        """
        self.head = None

    def __str__(self):
        out = ''
        if self.head is None:
            return f'[]'
        lst = ''
        node = self.head
        while node:
            lst += str(node.val) + ' -> '
            node = node.next
        return lst

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1
        """
        if self.head is None or index >= len(self):
             return -1
        count = 0
        node = self.head
        while node:
            if index == count:
                return node.val
            node = node.next
            count += 1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        """Append a node of value val to the last element of the linked list."""
        if self.head is None:
            self.head = Node(val)   # next=None
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)       # next=None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > len(self):
            raise IndexError('Index is not valid!')
        if index == 0 or self.head is None:
            self.addAtHead(val)     # next=None
        if index == len(self):
            self.addAtTail(val)     # next=None
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                new_node = Node(val, node.next)
                node.next = new_node
                break
            node = node.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > len(self):
            raise IndexError('Index is not valid!')
        if index == 0:
            self.head = self.head.next
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                node.next = node.next.next
                break
            count += 1
            node = node.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

myLinkedList = MyLinkedList()
#print(myLinkedList, len(myLinkedList))
myLinkedList.addAtHead('head')
# # print(myLinkedList, len(myLinkedList))
myLinkedList.addAtHead('second_head')
# # print(myLinkedList, len(myLinkedList))
myLinkedList.addAtHead('third head')
# # print(myLinkedList, len(myLinkedList))
myLinkedList.addAtTail('tail')
print(myLinkedList, len(myLinkedList))
# print('llist:', myLinkedList)
myLinkedList.addAtIndex(2, "New 2nd node")  # linked list becomes 1->2->3
print(myLinkedList, len(myLinkedList))
# print(myLinkedList.get(0))              # return 2
myLinkedList.deleteAtIndex(0)        # now the linked list is 1->3
print(myLinkedList, len(myLinkedList))
# print(myLinkedList.get(1))                  # return 3
# print('llist:', myLinkedList)
# print('Length:', len(myLinkedList))
print(myLinkedList.get(1))
myLinkedList.addAtTail('second_tail')
print(myLinkedList, myLinkedList.get(4))

