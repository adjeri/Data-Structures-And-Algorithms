class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            holdingPointer = self.last
            self.last = newNode
            holdingPointer.next = newNode
        self.length += 1
        return self

    def dequeue(self):
        if not self.first:
            return None

        if self.first == self.last:
            self.last = None

        first = self.first
        nextFirst = first.next
        self.first = nextFirst
        del first
        self.length -= 1
        return self


if __name__ == '__main__':

    queue = Queue()
    queue.enqueue('google')
    queue.enqueue('udemy')
    queue.enqueue('youtube')
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print(queue)
