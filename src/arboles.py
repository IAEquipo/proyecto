from anytree import Node, RenderTree

udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

print(udo)

raiz = Node("Hola")
padre = raiz
padre = Node("Mundo", parent = padre)
