class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length += 1
        return self

    def pop(self):
        if not self.top:
            return None

        if self.top == self.bottom:
            self.bottom = None

        top = self.top
        nextTop = top.next
        self.top = nextTop
        del top
        self.length -= 1
        return self


if __name__ == '__main__':

    stack = Stack()
    stack.push('google')
    stack.push('udemy')
    stack.push('youtube')
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)
