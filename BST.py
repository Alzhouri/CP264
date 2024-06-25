class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
# Create an empty BST
root = None


def insert_node(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert_node(root.left, key)
    elif key > root.key:
        root.right = insert_node(root.right, key)
    return root

def search_node(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search_node(root.left, key)
    return search_node(root.right, key)



# Insert nodes into the BST
root = insert_node(root, 6)
root = insert_node(root, 4)
root = insert_node(root, 8)
root = insert_node(root, 2)
root = insert_node(root, 5)
root = insert_node(root, 7)

# Search for a node in the BST
key_to_find = 7
result = search_node(root, key_to_find)
if result:
    print(f"Node with key {key_to_find} found in the BST.")
else:
    print(f"Node with key {key_to_find} not found in the BST.")
        
        