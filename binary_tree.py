from random import randint


class Node:
    def __init__(self, data, left=None, right= None):
        self.data = data,
        self.left= left
        self.right= right
    

def in_order(Node):
    if Node is None:
        return
    if Node.left:
        in_order(Node.left)
    print(Node.data, end='')
    if Node.right:
        in_order(Node.right)
    
def pre_order(Node):
    if Node is None:
        return
    print(Node.data, end='')
    if Node.left:
        pre_order(Node.left)
    if Node.right:
        pre_order(Node.right)

def post_order(Node):
    if Node is None:
        return
    if Node.left:
        post_order(Node.left)
    if Node.right:
        post_order(Node.right)
    print(Node.data, end='')



item1 = Node("A",Node("B",Node("C"),Node("D")), Node("E", Node("F", Node("G"),Node("H")),Node("I", None, Node("J"))))

# in_order(item1)
# print("")
# pre_order(item1)
# print("")
# post_order(item1)