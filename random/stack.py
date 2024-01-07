class Stack:
    def __init__(self):
        self.stack = []
        print(self.stack)
    
    def push(self, value):
        self.stack.append(value)
        return "Value added to stack"
    
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False
    
    def __str__(self):
        if self.isEmpty() == False:
            values = self.stack.reverse()
            values = [str(x) for x in self.stack]
            return "\n".join(values)
        else:
            return "The stack is empty"
    
    def pop(self):
        if self.isEmpty():
            return "empty stack"
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "empty stack"
        else:
            return self.stack[-1]

    def delete(self):
        self.stack = None
        return "stack deleted"
    
    

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.delete())