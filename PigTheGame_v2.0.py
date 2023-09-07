import random
import sys
import argparse
import time

class Dice:
    def roll(self):
        return random.randint(1, 6)
    


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def addScore(self, roll_points):
        self.score += roll_points

    def __str__(self):
        return f"{self.name} ---- > ({self.score} points)"


class PigTheGame:
    def __init__(self, num_players):
        self.num_players = num_players       
        self.current_player = 0
        self.dice = Dice()
        self.reset_game()
    """def is_game_over(self):
        for player in self.players:
            if player.score >= 10:
                return True
        return False
    
"""
    def reset_game(self):
            self.players = [Player(input(f"Enter Player {i + 1}'s name: ")) for i in range(self.num_players)]
            self.current_player = 0


    def change_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self):
        player = self.players[self.current_player]
        print(f"{player.name}'s turn.")
        point=0
        while (True):
            roll = self.dice.roll()
            if roll == 1:
                    print(f"{player.name} rolled a 1 and lost his turn.")
                    point=0
                    str=player.__str__()
                    print(str)
                    break
                
            else :
                    point+=roll
                    print(f"{player.name} rolled a {roll}")
                    pointstoshow=player.score+point
                    print (f"{player.name} scored {pointstoshow} points")

                    if pointstoshow>=100:
                        break

                     
            ch=input("<------------- Press  'r'  to Roll the dice, 'h' to Hold : --------- : ")
            if ch.lower() == 'h':
                break
            elif ch.lower() == 'r':
                continue
            else : 
                print("\nGame Crashed!")
                sys.exit()
        player.score+=point  

        print(f"{player.name}'s turn is over. {player.name} scored {player.score}.")
        print ("<................................................................................>")
        self.change_player()  

  

    def play(self):
        while all(player.score < 100 for player in self.players):
            self.play_turn()

        winners = [player for player in self.players if player.score >= 100]
        print("\nGame Over!")
        if len(winners) == 1:
            print(f"{winners[0].name} is the winner with {winners[0].score} points!")


if __name__ == "__main__":
    print ("Welcome T0 The PIG GAME")
    print ("<................................................................................>")
    random.seed(0)
    game = PigTheGame(2)
    game.play()

   """ parser = argparse.ArgumentParser()
    parser.add_argument("numPlayers", type=int, help="numberofPlayers")
    args = parser.parse_args()
    if args.numPlayers:
           print ("Welcome T0 The PIG GAME")
           print ("<................................................................................>")
           random.seed(0)
           game = PigTheGame(args.numPlayers)
           game.play()
           while (True):
              print ("<................................................................................>")
              print("Player Another Game with same no of plyers ? Press y to Play, otherwise presss anything to exit ")
              ch = input().lower()
              if ch == 'y':
                game = PigTheGame(args.numPlayers)
                game.play()
              else : 
                  break   
    else:
        print("Exiting the program.")
        sys.exit()"""

  
