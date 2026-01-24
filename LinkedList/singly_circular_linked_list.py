class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def insertAtbeg(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def deleteByValue(self, val):
        if self.head is None:
            print("Dear, deletion not possible")
            return
        
        curr = self.head
        prev = None

        if curr.next == self.head and curr.data == val:
            self.head = None
            return
        
        if curr.data == val:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            self.head = curr.next
            temp.next = self.head
            return

        prev = curr
        curr = curr.next
        while curr != self.head:
            if curr.data == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return

        prev = None
        curr = self.head

        while True:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            if curr == self.head:
                break

        self.head.next = prev
        self.head = prev

    def display(self):
        if self.head is None:
            print("Empty List")
            return
        
        temp = self.head
        while True:
            if temp.next == self.head:
                print(temp.data, end="")
            else:
                print(temp.data, end=" -> ")

            temp = temp.next

            if temp == self.head:
                break

        print()
        # print("\nBack to Head")


scl = SinglyCircularLinkedList()

scl.insertAtEnd(40)
scl.insertAtEnd(30)
scl.insertAtEnd(10)

scl.insertAtbeg(5)

scl.display()
# scl.deleteByValue(40)
# scl.deleteByValue(30)
# scl.deleteByValue(10)
# scl.deleteByValue(5)
scl.reverse()
scl.display()