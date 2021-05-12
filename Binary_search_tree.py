class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object): #Binary Search Tree
    def __init__(self, root):
        self.root = Node(root)
    def print_tree(self):
        return self.preorder_print(self.root,"")[:-1]
    def insert(self,new_value):
        self.insert_help(self.root,new_value)

    def insert_help(self,start, new_val):
        if new_val > start.value:
            if start.right:
                self.insert_help(start.right,new_val)
            else:
                start.right = Node(new_val)
        elif new_val < start.value:
            if start.left:
                self.insert_help(start.left,new_val)
            else:
                start.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value)+ "-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal



# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)

tree.insert(3)
tree.insert(5)


# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))