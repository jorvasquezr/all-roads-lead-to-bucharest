from node import Node
class ListOpenNodes:

  # F(n) = g(n) + h'(n)
  def __init__(self,node):
    self.__opennodes=[node]


  def addNode(self,node):
    try:
      eqnode = self.__opennodes[self.__opennodes.index(node)]
      if (eqnode > node):
        self.__opennodes.remove(eqnode)
        self.__opennodes.append(node)
    except:
      self.__opennodes.append(node)

  def expandNode(self,node,closedNodes):
    self.__opennodes.remove(node)
    closedNodes.closeNode(node)
    l = node.getConnections()
    for n in l:
      if(not closedNodes.exists(n)):
        self.addNode(Node(n,node))

  def getMinNode(self):
    return min(self.__opennodes)
  def getL(self):
    return self.__opennodes








