from anytree import AnyNode, RenderTree
from anytree.exporter import DotExporter

root = AnyNode(value=5, children=[
     AnyNode( value=3, children=[
         AnyNode(value=2),
         AnyNode(value=5),
     ]),
     AnyNode(value =7, children=[
         AnyNode(value=1),
         AnyNode(value=0, children=[
         AnyNode(value=2),
         AnyNode(value=8,children=[
         AnyNode(value=5),
     ]),
     ]),
     ]),
 ])
print(RenderTree(root))
