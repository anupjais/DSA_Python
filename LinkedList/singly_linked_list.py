class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = temp

    def insertAtBeg(self, data):
        self.head = Node(data, self.head)
        # temp = Node(data)
        # temp.next = self.head
        # self.head = temp
        # return
    

    def insertAfterValue(self, data, value):
        curr = self.head
        while curr:
            if curr.data == value:
                curr.next = Node(data, curr.next)
                return True
            curr = curr.next
        return False
        # if self.head is None:
        #     return "Empty List"
    
        # temp = Node(data)
        # t1 = self.head

        # while t1:
        #     if t1.data == value:
        #         temp.next = t1.next
        #         t1.next = temp
        #         return

        #     t1 = t1.next

        # return f"{value} not found"
        

    def deleteByValue(self, data):
        if self.head is None:
            return "Empty List"

        # Case 1: deleting head
        if self.head.data == data:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == data:
                prev.next = curr.next
                curr.next = None
                return
            prev = curr
            curr = curr.next

        return "Data not found"
        
    
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev
    
    def printList(self):
        if self.head is None:
            print("Empty List")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

l1 = SinglyLinkedList(None)
l1.insertAtEnd(10)
l1.insertAtEnd(20)
l1.insertAtEnd(30)
l1.insertAtEnd(40)
l1.insertAtEnd(50)
l1.insertAtBeg(500)
l1.insertAfterValue(7, 40)
l1.insertAfterValue(9, 10)
l1.insertAfterValue(19, 500)
# l1.deleteByValue(500)
# l1.deleteByValue(10)
# l1.deleteByValue(50)
# l1.deleteByValue(20)
# l1.deleteByValue(30)
# l1.deleteByValue(40)
# l1.deleteByValue(100)

l1.printList()
l1.reverse()
l1.printList()
l1.reverseLinkedList(500)
l1.printList()
