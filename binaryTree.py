# Class that represents a Node
class Node:

    # Constructor method that creates the node root
    def __init__(self, data: int):
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
    def __init__(self, node = None):
        self.root = node

    def getRoot(self):
        return self.root

    # Function that recursively prints the whole tree (Preorder)
    def preOrderTransverse(self, pointer):

        # Verifies if the tree is empty
        if self.root == None:
            return 'The tree is empty!'

        # Verifies if there's a son
        if pointer:
            # Prints the data of the pointer (also called root) node
            print(pointer.getData())

            # Prints the data of the left son
            self.preOrderTransverse(pointer.getLeftSon())

            # Prints the data of the right son
            self.preOrderTransverse(pointer.getRightSon())

    # Function that searches for a given node in the tree
    def search(self, pointer:Node, node: Node):
        # Base case, to stop the recursive function
        if pointer.getData() == None or node.getData() == pointer.getData():
            return pointer

        # Verifies if the value to be found is lower than the pointer, then if it is, call the left son
        if node.getData() < pointer.getData():
            return self.search(pointer.getLeftSon(), node)

        # If not, call the right son instead
        else:
            return self.search(pointer.getRightSon(), node)

    # Returns the more to the left node of the tree
    def minimum(self, pointer = None):
        # Verifies if a starting point was given to start the search
        if pointer == None:
            # If there's not a given point, the search will begin with the root
            pointer = self.getRoot()

        # Will repeat until the node more to the left is found
        while pointer.getLeftSon() != None:
            # If it's not found yet, go to the left son
            pointer = pointer.getLeftSon()
        return pointer

    # Returns the more to the right node of the tree
    def maximum(self, pointer = None):
        # Verifies if a starting point was given to start the search
        if pointer == None:
            # If there's not a given point, the search will begin with the root
            pointer = self.getRoot()

        # Will repeat until the node more to the right is found
        while pointer.getRightSon() != None:
            # If it's not found yet, go to the right son
            pointer = pointer.getRightSon()
        return pointer

    # Returns the node with the lowest value but bigger than the value of the given node
    def successor(self, node: Node):

        # Verifies is there is a right sub-tree (because the successor is the minimum of that sub-tree)
        if node.getRightSon() != None:
            return self.minimum(node.getRightSon())
        
        pointer = node.getFather()

        # Search for the first ancestral whose left son is also a father of the given node
        while pointer != None and node == pointer.getRightSon():
            # Swapping the values of the variable
            node, pointer = pointer, pointer.getFather()
        
        # Return the successor
        return pointer

     # Returns the node with the biggest value but lower than the value of the given node
    def predecessor(self, node: Node):

        # Verifies is there is a left sub-tree (because the successor is the maximum of that sub-tree)
        if node.getLeftSon() != None:
            return self.maximum(node.getLeftSon())
        
        pointer = node.getFather()

        # Search for the first ancestral whose right son is also a father of the given node
        while pointer != None and node == pointer.getLeftSon():
            # Swapping the values of the variable
            node, pointer = pointer, pointer.getFather()
        
        # Return the successor
        return pointer
    
    # Function that inserts a new node into the binary tree  
    def insert(self, node: Node):
        # Starting point of iteration
        pointer = self.getRoot()
        temp = None

        # Verifies whether the value is lower or bigger than the pointer to insert
        while pointer != None:
            # Store the value of the current node
            temp = pointer
            # Verifies where to place the new node (left or right sub-tree)
            if node.getData() < pointer.getData():
                pointer = pointer.getLeftSon()
            else: 
                pointer = pointer.getRightSon()

        # Temp becomes the given node father
        node.father = temp

        # Verifies if the tree is empty, if it is, then the given value becomes the root
        if temp == None:
            self.root = node

        # Verifies if the given node is lower than the current node
        elif node.getData() < temp.getData():
            temp.leftSon = node
        # The given node is bigger than the current node
        else:
            temp.rightSon = node

# Main program
tree = BinaryTree()

tree.insert(Node(25))
tree.insert(Node(20))
tree.insert(Node(36))
tree.insert(Node(10))
tree.insert(Node(22))
tree.insert(Node(5))
tree.insert(Node(12))
node1 =  Node(30)
tree.insert(node1)
tree.insert(Node(40))
tree.insert(Node(28))
tree.insert(Node(38))
tree.insert(Node(48))
