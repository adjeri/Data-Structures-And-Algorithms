import json

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        root = self.root
        newNode = Node(value)
        if root is None:
            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if value < current.value:
                    # left
                    if not current.left:
                        current.left = newNode
                        return self

                    current = current.left
                else:
                    # right
                    if not current.right:
                        current.right = newNode
                        return self
                    current = current.right


    def lookup(self, value):
        if self.root is None:
            return False
        current = self.root
        while current:
            # print(current.value)
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            elif current.value == value:
                return current
        return False

    def remove(self, value):
        if self.root is None:
            return False
        parent = None
        current = self.root
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            elif current.value == value:
                if current.right is None:
                    if parent is None:
                        self.root = current.left
                    else:
                        if current.value < parent.value:
                            parent.left = current.left
                        elif current.value > parent.value:
                            parent.right = current.left
                elif current.right.left is None:
                    if parent is None:
                        self.root = current.left
                    else:
                        current.right.left = current.left
                        if current.value < parent.value:
                            parent.left = current.right
                        elif current.value > parent.value:
                            parent.right = current.right
                else:
                    leftMost = current.right.left
                    leftMostParent = current.right
                    while leftMost.left is not None:
                        leftMostParent = leftMost
                        leftMost = leftMost.left

                    leftMostParent.left = leftMost.right
                    leftMost.left = current.left
                    leftMost.right = current.right

                    if parent is None:
                        self.root = leftMost
                    else:
                        if current.value < parent.value:
                            parent.left = leftMost
                        else:
                            if current.value > parent.value:
                                parent.right = leftMost
        return True

    def breadthFirstSearch(self):
        current = self.root
        array = []
        queue = []
        queue.append(current)

        while len(queue):
            current = queue.pop(0)
            print(current.value)
            array.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return list

    def breadthFirstSearchR(self,queue,array):
        if not len(queue):
            return array
        current = queue.pop(0)
        array.append(current.value)
        if current.left:
                queue.append(current.left)
        if current.right:
            queue.append(current.right)

        return self.breadthFirstSearchR(queue, array)

    def DFSInOrder(self):
        return traverseInOrder(self.root, [])

    def DFSPreOrder(self):
        return traversePreOrder(self.root, [])

    def DFSPostOrder(self):
        return traversePostOrder(self.root, [])

def traverseInOrder(node, array):
    if node.left:
        traverseInOrder(node.left, array)
    array.append(node.value)
    if node.right:
        traverseInOrder(node.right, array)
    return array

def traversePreOrder(node, array):
    array.append(node.value)
    if node.left:
        traverseInOrder(node.left, array)
    if node.right:
        traverseInOrder(node.right, array)
    return array

def traversePostOrder(node, array):
    if node.left:
        traversePostOrder(node.left, array)
    if node.right:
        traversePostOrder(node.right, array)
    array.append(node.value)
    return array



def traverse(node):
    tree = node
    tree.left = None if node.left is None else traverse(node.left)
    tree.right = None if node.right is None else traverse(node.right)
    return tree


#        9
#   4         20
# 1   6     15   170




if __name__ == '__main__':

    binaryTree = BinarySearchTree()
    binaryTree.insert(9)
    binaryTree.insert(4)
    binaryTree.insert(20)
    binaryTree.insert(1)
    binaryTree.insert(6)
    binaryTree.insert(15)
    binaryTree.insert(170)
    binaryTree.lookup(6)
    # print(binaryTree.remove(170))
    # array = binaryTree.breadthFirstSearchR([binaryTree.root], [])
    array = binaryTree.DFSInOrder()
    print(array)
    array = binaryTree.DFSPreOrder()
    print(array)
    array = binaryTree.DFSPreOrder()
    print(array)

    # y = json.dumps(traverse(binaryTree.root))

    # print(y)

