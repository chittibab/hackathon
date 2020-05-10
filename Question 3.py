#Generic Tree Traversal 
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
        
# create nodes
n = Node(5)
p = Node(6)
q = Node(7)
r = Node(9)
m = Node(11)
s = Node(12)
l = Node(14)
t = Node(15)
n.add_child(p)
n.add_child(q)
n.add_child(r)
p.add_child(m)
p.add_child(s)
q.add_child(l)
r.add_child(t)

for c in n.children:
    print (c.data)
for c in p.children:
    Print (c.data)
for c in q.children:
    Print (c.data)
for c in r.children:
    Print (c.data)
