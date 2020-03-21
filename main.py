class Tree :
    def __init__(self, value, left_children=None, right_children=None):
        self.value = value
        self.left_children = left_children
        self.right_children = right_children
  
#create a left subtree(bottom up)
left_sub_tree = Tree(3, Tree(2), Tree(value=5))

#create a right subtree(bottom up)
rst1b = Tree(8, Tree(value=5) ) 
rsr1 = Tree(0, Tree(value=2), rst1b)
right_sub_tree = Tree(7, Tree(value=1), rsr1)
root = Tree(5 ,left_sub_tree, right_sub_tree)

class Tree_methods:
    def __init__(self,tree):
        self.list_of_nodes = []
        self.tree = tree
        self.preorderIterative()

    def sum(self):
        return sum(self.list_of_nodes)
    def average(self):
        return sum(self.list_of_nodes)/len(self.list_of_nodes)
    def mediana(self):
        if self.lenght%2 == 1:
            return self.list_of_nodes[int(self.lenght/2)]
        else: return ( self.list_of_nodes[int(self.lenght/2) -1] + self.list_of_nodes[int(self.lenght/2) + 1] ) / 2

    def preorderIterative(self): 
        curr = self.tree
        tmp = []
        self.list_of_nodes
        while (len(tmp) or curr != None): 
            while (curr != None): 
                self.list_of_nodes.append(curr.value)
                if (curr.right_children != None): 
                    tmp.append(curr.right_children)
                curr = curr.left_children
            if (len(tmp) > 0): 
                curr = tmp[-1] 
                tmp.pop()
        self.list_of_nodes.sort()
        self.lenght = len(self.list_of_nodes)

test = Tree_methods(root)
print(test.list_of_nodes)
print(test.average())
print(test.sum())
print(test.mediana())

assert test.sum() == 38, "Should be 6"
