class GameInfo:
  import random

  # Attributs
  nPlayer = 1
  combination = list("0000")
  guessCombination = list("")
  combinationClue = list("0000")
  winnerId = 0
  

  # Methods
  # Constructors
  def __init__(self):
    print("******Masterming game lunched******")
    self.combination = list(str(self.random.randint(1, 9999)))
    self.setNPlayer( int(input("Select number of player \n") ))  
    
    

  #set Methods
  def setGuessCombination(self, guessCombination):
    self.guessCombination = guessCombination

  def setCombinationClue(self, combinationIdx):
    self.combinationClue[combinationIdx] = 1

  def setNPlayer(self, _nPlayer):
    self.nPlayer = _nPlayer

  def setWinnerId(self, _id):
    self.winnerId = _id

  #get Methods
  def getGuessCombination(self):
    return self.guessCombination

  def getCombinationClue(self):
    return self.combinationClue

  def getCombination(self):
    return self.combination

  def getNPLayer(self):
    return self.nPlayer

  def getWinnerId(self):
    return self.winnerId







