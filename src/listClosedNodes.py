class ListClosedNodes:

  # F(n) = g(n) + h'(n)
  def __init__(self):
    self.__closedNodes = []

  def exists(self, node):
    return node in self.__closedNodes

  def closeNode(self,node):
    self.__closedNodes.append(node)

