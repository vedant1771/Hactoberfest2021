class Stack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Pop operation can't performed on empty stack")
    def traverse(self):
        if not self.stack:
            print("Stack is Empty")
        while self.stack:
            print(self.pop())
    
        
        
stack = Stack()
arr = [22,3,45,6,1,7,8]
stack.push(22)
stack.push(3)
stack.push(45)
stack.push(6)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
# print(stack.stack)
# stack.traverse()
# stack.pop()
# stack.traverse()



