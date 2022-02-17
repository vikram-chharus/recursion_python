
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
nodes = []
def create_tree( level=0, node=None, alpha=97):
    if level == 0:
        return None 
    node = Node(chr(alpha))
    nodes.append(node.data)
    print("Level : ", level, " Adding Node : ", node.data)
    print("--",node.data,"-Left--")
    node.left = create_tree( level-1, node,  alpha+1)
    print("--",node.data, "-right--")
    node.right = create_tree( level-1, node,  alpha+2)
    return node

node = create_tree(4)
print(nodes)
