from requests import head


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
            

    def insertAtBeg(self,data):
        if self.head == None:
            self.head = Node(data)
            return
        
        new_node = Node(data)
        # self.head.prev = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insertAtPos(self, data, val):
        new_node = Node(data)
        temp = self.head

        while temp:
            if temp.data == val:
                new_node.next = temp.next
                
                if temp.next:
                    temp.next.prev = new_node
                
                temp.next = new_node
                new_node.prev = temp
                return
            
            temp = temp.next

    def deleteByVal(self, val):
        temp = self.head
        if temp == None:
            print("Dear, deletion not possible")
            return
        
        if temp.data == val:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
            
        while temp:
            if temp.data == val:
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return

            temp = temp.next

        print("Value not found")

    def reverse(self):
        temp = self.head
        rev = None

        while temp:
            rev = temp
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev

        if rev:
            self.head = rev

    def printList(self):
        if self.head == None:
            print("Empty List")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" <--> " if temp.next else " ")
            temp = temp.next

        print()


dl1 = DoublyLL()
dl1.insertAtEnd(50)
dl1.insertAtEnd(60)
dl1.insertAtBeg(10)

dl1.insertAtPos(100, 10)
dl1.insertAtPos(400, 50)
dl1.insertAtPos(700, 60)
dl1.insertAtPos(800, 600)

# dl1.printList()
# dl1.deleteByVal(10)
# dl1.printList()
# dl1.deleteByVal(50)
# dl1.printList()
# dl1.deleteByVal(700)
dl1.printList()
dl1.reverse()
dl1.printList()