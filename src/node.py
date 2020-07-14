from city import City
from distance import Distance


class Node:

  # F(n) = g(n) + h'(n)
  def __init__(self, city: City, previusnode=None):
    self.__previusnode = previusnode
    self.__g = 0
    self.__hprime = 0
    self.__f = 0
    self.__city=city

    if(previusnode != None):
      self.data = self.__city.get_data(self.__previusnode.getCity())
      self.__calculateG()
      self.__calculateHprime()
      self.__calculateF()
      #print(previusnode.getCityName(),self.__g,self.__hprime,self.__f)
  def __eq__(self, other):
    try:
      return self.getCityName == other.getCityName
    except:
      return False

  def __lt__(self, other):
    return self.getF() < other.getF()
  def __gt__(self, other):
    return self.getF() > other.getF()





  def __calculateG(self):

    actualG= (1/4)*self.__getID() + (1/4)*self.__getIEC() +(1/2)*self.__getIP() 
    #(2*self.data[0]*( 1 +  self.__getIEC() + self.__getIP()*4))/6
    self.__g= actualG+ self.__previusnode.getG()

  def __getID(self):
    return (self.data[0]-71)/(211-71) #Distance

  def __getIP(self):
    return (self.data[2] - 1) / (5 - 1)  # Distance

  def __getIEC(self):
    return 1 - ((self.data[1] - 1) / (10 - 1))  # Distance

    self.data[1] #Status
    self.data[2] #Danger




  def __calculateHprime(self):
    minV = min(list(Distance.get_distancesValues()))
    maxV = max(list(Distance.get_distancesValues()))
    self.__hprime=(Distance.get_distance(self.getCityName())-minV)/(maxV-minV)

  def __calculateF(self):
    self.__f=self.__g+self.__hprime

  def isFirstNode(self):
    return self.__previusnode==None


  def getG(self):
    return self.__g

  def getPreviusNode(self):
    return self.__previusnode

  def getF(self):
    return self.__f

  def getCityName(self):
    return self.__city.get_name()

  def getCity(self):
    return self.__city

  def getConnections(self):
    return list(self.__city.get_connections())


