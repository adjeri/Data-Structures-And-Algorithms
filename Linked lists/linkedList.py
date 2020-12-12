class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
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
                    newNode.next = nextNode
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
            previousNode = self.getNodeAtIndex(index - 1)
            toDelete = previousNode.next
            nextNode = toDelete.next
            toDelete.next = None
            previousNode.next = nextNode
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

    def reverse(self):
        nextNode = None
        previousNode = None
        current = self.head

        while current:
            nextNode = current.next
            current.next = previousNode
            previousNode = current
            current = nextNode

        self.head = previousNode

        return self.printList()



if __name__ == '__main__':

    myLinkedlist = LinkedList(10)
    myLinkedlist.append(15)
    myLinkedlist.append(115)
    myLinkedlist.prepend(41)
    myLinkedlist.insert(2,225)
    myLinkedlist.insert(2,45)
    myLinkedlist.insert(0,147)
    myLinkedlist.insert(50, 89)
    print(myLinkedlist.printList())
    myLinkedlist.remove(14)
    myLinkedlist.reverse()
    print(myLinkedlist.printList())
