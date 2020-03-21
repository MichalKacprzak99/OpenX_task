from anytree import Node, RenderTree, PreOrderIter

class Tree_methods:
    def __init__(self, tree):
        self.tree = tree
        self.list_of_nodes_val = []
        for node in PreOrderIter(self.tree):
            self.list_of_nodes_val.append(node.value)
        self.list_of_nodes_val.sort()
    def sum(self):
        return sum(self.list_of_nodes_val)
    def average(self):
        return sum(self.list_of_nodes_val)/len(self.list_of_nodes_val)
    def mediana(self):
        self.lenght = len(self.list_of_nodes_val)
        if self.lenght%2 == 1:
            return self.list_of_nodes_val[int(self.lenght/2)]
        else: return ( self.list_of_nodes_val[int(self.lenght/2) -1] + self.list_of_nodes_val[int(self.lenght/2) + 1] ) / 2 
              
def init_example_tree():
    left_sub_tree = Node(name='lst', value=3, children=[
         Node(name='lst1', value=2),
         Node(name='lst2', value=5),
     ])
    right_sub_tree = Node(name='rst', value =7, children=[
         Node(name='rst1', value=1),
         Node(name='rst2', value=0, children=[
         Node(name='rst2a', value=2),
         Node(name='rst2b', value=8,children=[
         Node(name='rst2bb', value=5),
     ]),
     ]),
     ])
    return Node(name='root', value=5, children=[left_sub_tree, right_sub_tree])
