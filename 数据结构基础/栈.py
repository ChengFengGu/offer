class Stack:
    def __init__(self):
        self.stack = []
    def push(self,e):
        self.stack.append(e)
    def pop(self):
        self.stack.pop()
    def get