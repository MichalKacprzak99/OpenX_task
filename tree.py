from statistics import median, mean
from anytree import Node, PreOrderIter


class NodeMethods:
    """
    This is the class used to analyze the subtree of the node
    
    Attributes:
        node (object of anytree.Node class): Lhe node in tree
        nodes_value (list) : List of values ​​for all nodes in the subtree
    Methods:
        sum: return sum of values in subtree
        average: return average of values in subtree
        median: return median of values in subtree
    """

    def __init__(self, node):
        """
        The constructor for NodeMethods class.
        
        Parameters:
            node (object of anytree.Node class): The node in tree
        """

        self.node = node
        self.nodes_value = []
        for node in PreOrderIter(self.node):
            self.nodes_value.append(node.value)

    def sum(self):
        return sum(self.nodes_value)

    def average(self):
        return mean(self.nodes_value)
    
    def median(self):
        return median(self.nodes_value)


def init_example_tree():
    """
    A function that creates a mapping of the data structure set in a task(tree).
    Return: root of tree
    """

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
    sub_tree = [left_sub_tree, right_sub_tree]
    return Node(name='root', value=5, children=sub_tree)

