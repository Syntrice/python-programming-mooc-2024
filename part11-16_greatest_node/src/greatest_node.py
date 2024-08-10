# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        
def greatest_node(root: Node):
    
    # assume this value is greatest
    greatest = root.value
    
    # process left child
    if root.left_child is not None:
        left_greatest = greatest_node(root.left_child)
        if left_greatest > greatest:
            greatest = left_greatest
    
    # process right child
    if root.right_child is not None:
        right_greatest = greatest_node(root.right_child)
        if right_greatest > greatest:
            greatest = right_greatest
        
    return greatest
        
      
def find_node(root: Node, value):
    if root is None:
        return False

    if value == root.value:
        return True

    if value > root.value:
        return find_node(root.right_child, value)

    return find_node(root.left_child, value)
        
if __name__ == "__main__":
    
    tree = Node(7)
    tree.left_child = Node(3)
    tree.right_child = Node(11)
    
    tree.left_child.left_child = Node(2)
    tree.left_child.right_child = Node(5)
    tree.left_child.right_child.left_child = Node(4)
    
    tree.right_child = Node(11)
    tree.right_child.right_child = Node(14)
    tree.right_child.right_child.left_child = Node(9)
    tree.right_child.right_child.right_child = Node(16)
    
    print(find_node(tree, 9))
    