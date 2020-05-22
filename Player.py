class Player:

  # Attributs
  id = 0
  name = ""
  lastGuess = list("")
  nPlay = 0

  # Constructor
  def __init__(self, _id):
    self.name = input("Choose your name \n")
    self.id = _id

  # Methods
  def guess(self):
    print("Please ", self.name, "enter a combination")
    self.setNPlay()
    self.lastGuess =  list(input())
    return self.lastGuess

  # setter
  def setNPlay(self):
    self.nPlay = self.nPlay+1;

  # getter
  def getNPlayer(self):
    return self.nPlay

  def getId(self):
    return self.id

