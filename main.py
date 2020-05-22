# starting
from GameInfo import GameInfo
from Player import Player


Game = GameInfo()
players = list("")
for i in range(1, Game.getNPLayer()+1):
  players.append(Player(i))

while Game.getGuessCombination() != Game.getCombination():
  for i in range(0, Game.getNPLayer()):
    player = players[i]
    proposition = player.guess()
    Game.setGuessCombination(proposition)
    for i in range(0, len(proposition)):
      combination = Game.getCombination()
      if proposition[i] == combination[i]:
        Game.setCombinationClue(i)
    print( "Game indice", Game.getCombinationClue())
    print( "\n\n\n" )
    if Game.getGuessCombination() == Game.getCombination():
      Game.setWinnerId(player.getId())
    
print("Congratualtion, you found the code in ", Game.getWinnerId())
#add the number of iteration


  







