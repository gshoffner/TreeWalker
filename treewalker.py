class Node:
    def __init__(self, value, left_node = None, right_node = None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
    def __str__(self):
        return "value = %s, left_node = (%s), right_node = (%s)" % (self.value, self.left_node, self.right_node)

    def is_leaf(self):
        return (self.left_node is None and self.right_node is None)

    def has_two_children(self):
        return (self.left_node and self.right_node)

    def has_only_one_child(self):
        return not (self.is_leaf() or self.has_two_children())

    def parent_is_greater_than_children(self):
        return (self.value >= self.left_node.value) and (self.value >= self.right_node.value)

    def children_are_equal(self):
        return (self.left_node.value == self.right_node.value)

    def left_child_is_greater(self):
        return (self.left_node.value > self.right_node.value)

def walk_maximum_path(node):
    if node.is_leaf():
        print node.value
        return
    elif node.has_only_one_child():
        print "ERROR, node has only one child, must have zero or two"
        return
    else:
        if node.parent_is_greater_than_children():
            print node.value
            return
        else:
            if node.children_are_equal():
                print node.value
                print node.left_node.value
                return
            else:
                print node.value
                if node.left_child_is_greater():
                    walk_maximum_path(node.left_node)
                else:
                    walk_maximum_path(node.right_node)
    
if __name__ == "__main__":
    leaf_a = Node(10)
    leaf_b = Node(10)
    leaf_c = Node(6)
    leaf_d = Node(1)

    left_child = Node(6, leaf_a, leaf_b)
    right_child = Node(3, leaf_c, leaf_d)

    root = Node(5, left_child, right_child)

    walk_maximum_path(root)

    """
    print root 
    print "testing '.is_leaf()'..."
    print root.is_leaf() == False
    print left_child.is_leaf() == True
    print right_child.is_leaf() == True
    print [(node.has_only_one_child() == False) for node in [root, left_child, right_child]]
    """
