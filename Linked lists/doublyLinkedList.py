class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1
        return self

    def printList(self):
        array = []
        current = self.head
        while current:
            array.append(current.value)
            current = current.next
        return array

    def insert(self, index, value):
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            i = 0
            current = self.head
            while True:
                if i == index-1:
                    newNode = Node(value)
                    nextNode = current.next
                    current.next = newNode
                    newNode.prev = current
                    newNode.next = nextNode
                    nextNode.prev = newNode
                    self.length +=1
                    break
                else:
                    i += 1
                    current = current.next

        return self.printList()

    def remove(self, index):
        if not self.length:
            print('the list is empty')
            return []

        if index >= self.length:
            print('Invalid index')
            return []

        if index == 0: #remove head
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
            self.length -=1

        elif index == self.length - 1:  #remove tail
            beforeLast = self.getNodeAtIndex(self.length - 2)
            last = beforeLast.next
            beforeLast.next = None
            self.tail = beforeLast
            del last
            self.length -=1

        else:
            toDelete = self.getNodeAtIndex(index)
            previousNode = toDelete.prev
            nextNode = toDelete.next
            toDelete.next = None
            toDelete.prev = None
            previousNode.next = nextNode
            nextNode.prev = previousNode
            del toDelete
            self.length -= 1

        return self.printList()


    def getNodeAtIndex(self,index):
        i = 0
        current = self.head

        while i != index:
            current = current.next
            i += 1
        return current



if __name__ == '__main__':

    myLinkedlist = DoublyLinkedList(10)
    myLinkedlist.append(15)
    myLinkedlist.append(115)
    myLinkedlist.prepend(41)
    myLinkedlist.insert(2,45)
    myLinkedlist.insert(0,147)
    myLinkedlist.insert(50, 89)
    print(myLinkedlist.printList())
    myLinkedlist.remove(0)
    print(myLinkedlist.printList())
    print(myLinkedlist.head.prev)
