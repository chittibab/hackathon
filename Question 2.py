class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def preorder():
    print("preorder:")
    print(root.data)
    print(root.left.data)
    print(root.left.left.data)
    print(root.left.right.data)
    print(root.left.right.left.data)
    print(root.right.data)
    print(root.right.left.data)
    print(root.right.left.right.data)
    print(root.right.right.data)
def postorder():
    print("postorder:")
    print(root.left.left.data)
    print(root.left.right.left.data)
    print(root.left.right.data)
    print(root.left.data)
    print(root.right.left.right.data)
    print(root.right.left.data)
    print(root.right.right.data)
    print(root.right.data )
    print(root.data)
        
def inorder():
    print("inorder:")
    print(root.left.left.data)
    print(root.left.data)
    print(root.left.right.left.data)
    print(root.left.right.data)
    print(root.data)
    print(root.right.left.data)
    print(root.right.left.right.data)
    print(root.right.data)
    print(root.right.right.data)
root = Tree()
root.data = "A"
root.left = Tree()
root.left.data = "B"
root.right = Tree()
root.right.data = "C"
root.left.left=Tree()
root.left.left.data="D"
root.left.right=Tree()
root.left.right.data="E"
root.right.left=Tree()
root.right.left.data="F"
root.right.right=Tree()
root.right.right.data="G"
root.left.right.left=Tree()
root.left.right.left.data="M"
root.right.left.right=Tree()
root.right.left.right.data="N"

preorder()
postorder()
inorder()
