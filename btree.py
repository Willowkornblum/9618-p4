class node:
    def __init__ (self,data):
        self.data = data 
        self.left = None
        self.right = None

# root = node('+')
# root.left = node('A')
# root.right = node('B')

def inorder (rootnode):
    if (rootnode != None):
        inorder(rootnode.left)
        print(rootnode.data)
        inorder(rootnode.right)

def preorder(rootnode):
    if(rootnode != None):
        print(rootnode.data)
        preorder(rootnode.left)
        preorder(rootnode.right)

def postorder(rootnode): 
    if(rootnode != None):
        postorder(rootnode.left)
        postorder(rootnode.right)
        print(rootnode.data)

def search (rootnode,num):
    if (rootnode != None):
        if (rootnode.data == num):
            return "these are the root node and its children" , rootnode.data , rootnode.left.data, rootnode.right.data
        elif (rootnode.data > num ):
            return search(rootnode.left,num)
        elif (rootnode.data < num):
            return search(rootnode.right,num)
    else:
        return False 

def insert (rootnode,num):
    if (rootnode != None):
        if (num < rootnode.data):
            rootnode.left =  insert(rootnode.left,num)
        elif (num> rootnode.data):
            rootnode.right = insert(rootnode.right,num)
        return rootnode
    else:
        return node(num)


# inorder(root)
# preorder(root)
# postorder(root)
root = node(10)
root.left = node(5)
root.right = node(15)
root.left.left = node(2)
root.right.right= node(20)
#print (search(root,5))
print (insert(root,7))
inorder(root)
