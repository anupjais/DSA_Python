class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)

    def push(self, data):
        self.s.insert(0,data)
        # self.s.append(data)

    def peek(self):
        # if self.s.length() == 0:
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        else:
            return self.s[0]

    def pop(self):
        # if self.s.length() == 0:
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.s.pop(0)
            # return self.s.pop()

    def is_empty(self):
        return len(self.s) == 0

stk = Stack()

stk.push(10)
stk.push(20)
stk.push(30)
stk.push(70)

while not stk.is_empty():
    print(stk.pop())

# print(stk.peek())
# stk.peek()
