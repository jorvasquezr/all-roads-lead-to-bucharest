from listClosedNodes import ListClosedNodes
from listOpenNodes import ListOpenNodes
from node import Node

class  A_StarAlgorithm:
  @staticmethod
  def calculateBestRouteFrom(city):
    firstNode=Node(city)
    closedNodes=ListClosedNodes()
    openNodes=ListOpenNodes(firstNode)
    resultList=[]
    resultDistance=0


    if(firstNode.getCityName() != 'Bucharest'):
      openNodes.expandNode(firstNode, closedNodes)
      while(openNodes!=[] and openNodes.getMinNode().getCityName()!='Bucharest'):
        openNodes.expandNode(openNodes.getMinNode(), closedNodes)
      if(openNodes==[]):
        return "Error"

      resultNode=openNodes.getMinNode()
      resultList = [resultNode.getCityName()]
      resultDistance = resultNode.getG()
      PreviousNode=resultNode.getPreviusNode()
      while(PreviousNode!=None):
        resultList =[PreviousNode.getCityName()] +resultList
        PreviousNode = PreviousNode.getPreviusNode()

      return str(round(resultDistance,4))+"\t"+str(resultList)
    return "0\t[Bucharest]"











