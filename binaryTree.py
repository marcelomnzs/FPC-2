# Class that represents a Node
class Node:

    # Constructor method that creates the node root
    def __init__(self, data):
        self.data = data
        self.leftSon = None
        self.rightSon = None
        self.father = None

    # Returns the data inside the node
    def getData(self):
        return self.data

    # Returns the son that is in the left side of the node that calls the function
    def getLeftSon(self):
        return self.leftSon

    # Returns the son that is in the right side of the node that calls the function
    def getRightSon(self):
        return self.rightSon

    # Returns the father of the node that calls the function
    def getFather(self):
        return self.father

    # Verifies if the passed node is the left son of a node
    def isLeftSon(self):
        nodeFather = self.getFather()

        # The current node is the root node
        if nodeFather == None:
            return False

        # Verifies if the node in the left side is equal to self
        if nodeFather.getLeftSon() == self:
            return True

        # If neither of the cases are true, return false
        return False

     # Verifies if the passed node is the right son of a node
    def isRightSon(self):
        nodeFather = self.getFather()

        # Verifies if the current node is the root node
        if nodeFather == None:
            return False

        # Verifies if the node in the right side is equal to self
        if nodeFather.getRightSon() == self:
            return True

        # If neither of the cases are true, return false
        return False

    # Returns the brother of the specfied node
    def getBrother(self):
        nodeFather = self.getFather()

        # Verifies if the current node is the root node
        if nodeFather == None:
            return False

        # If the given node is the left son, then return his brother on the right side
        if self.isLeftSon():
            return nodeFather.getRightSon()

        # If he's not the son, return his brother on the left side
        return nodeFather.getLeftSon()

# Class that represents a binary tree
class BinaryTree:

    # Creates a binary tree (by default, a binary tree is created empty)
    def __init__(self, node: Node):
        self.root = node

    # Function that recursively prints the whole tree (Preorder)
    def preOrderTransverse(self, pointer: Node):

        # Verifies if the tree is empty
        if self.root == None:
            return 'The tree is empty!'

        # Verifies if there's a son
        if pointer:
            # Prints the data of the pointer (also called root) node
            print(pointer.getData(), end=' ')

            # Prints the data of the left son
            self.preOrderTransverse(pointer.getLeftSon())

            # Prints the data of the right son
            self.preOrderTransverse(pointer.getRightSon())

    # Function that inserts a new node into the binary tree
    def insert(self, rootPoint: Node, node: Node):
        # Verifies if the tree is empty
        if self.root == None:
            self.root = node

        # Verifies if the value to be inserted is bigger than the current node
        elif rootPoint.getData() < node.getData():
            # Verifies if there's a son on the right side, if not, node becomes the son
            if rootPoint.getRightSon() == None:
                rootPoint.rightSon = node
            else:
                self.insert(rootPoint.getRightSon(), node)

        # Verifies if the value to be inserted is smaller than the current node
        elif rootPoint.getData() > node.getData():
            # Verifies if there's a son on the left side, if not, node becomes the son
            if rootPoint.getLeftSon() == None:
                rootPoint.leftSon = node
            else:
                self.insert(rootPoint.getLeftSon(), node)

        # The values are equal, then the repeated value goes to a list 
        else:
            # The program stops and return the value that is repeated
            if node.getData() not in repeatedNumbers:
                repeatedNumbers.append(node.getData())

    # Function that detects repeated numbers on a unordered numeric list
    def verifyRepeatedNumber(self, list):
        # Iterates through a list of nodes
        for i in list:
            self.insert(self.root, i)

# Main program

repeatedNumbers = []
node1 = Node(40)
# Creates a binary tree and puts 'node1' as it's root node
tree = BinaryTree(node1)

# Creating nodes
node1 = Node(40)
node2 = Node(10)
node3 = Node(60)
node4 = Node(80)
node5 = Node(40)
node6 = Node(120)
node7 = Node(70)
node8 = Node(40)
node9 = Node(90)
node10 = Node(10)
node11 = Node(70)
node12 = Node(90)
node13 = Node(80)

nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13]
tree.verifyRepeatedNumber(nodes)
print(repeatedNumbers)