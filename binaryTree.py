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
    def __init__(self):
        self.root = None

    # Function that recursively prints the whole tree (Preorder)
    def preOrderTransverse(self, pointer):

        # Verifies if the tree is empty
        if self.root == None:
            return 'The tree is empty!'

        # Prints the data of the pointer (also called root) node
        print(pointer.getData())

        # Prints the data of the left son
        self.preOrderTransverse(pointer.getLeftSon())

        # Prints the data of the right son
        self.preOrderTransverse(pointer.getRightSon())




# Main program
unorderedList = [14,15,4,9,15]

node1 = Node(5)

# binaryTree = BinaryTree()
# binaryTree.insert(node1)
