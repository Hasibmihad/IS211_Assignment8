import random
import sys
import time
import argparse

class Dice:
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, roll_points):
        self.score += roll_points

    def __str__(self):
        return f"{self.name} ----> ({self.score} points)"

class ComputerPlayer(Player):
    def make_decision(self):
        time.sleep(0.5)
        if self.score < 25 or self.score < (100 - self.score):
            return 'h'
        else:
            return 'r'

class HumanPlayer(Player):
    def make_decision(self):
            while (True):
                ch = input("<------------- Press 'r' to Roll the dice, 'h' to Hold : --------- : ")
                if ch.lower() == 'h' or ch.lower() == 'r':
                    return ch.lower()
                else:
                    print("Invalid input. Please enter 'r' or 'h'.")

class PlayerFactory:
    @staticmethod
    def create_player(player_type):
        if player_type == 'human':
            name='HUMAN'
            return HumanPlayer(name)
        elif player_type == 'computer':
            name='COMPUTER'
            return ComputerPlayer(name)
        else:
            raise ValueError(f"Invalid player type: {player_type}")     

class TimedGameProxy:
    def __init__(self, player_list, timed):
        self.players = player_list       
        self.current_player = 0
        self.dice = Dice()
        self.timed = timed
        self.start_time = time.time()
        self.timeflag=False

    def change_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.timed:
            self.timeflag=True
            print("One minute has elapsed. Game over!")
            return 

        player = self.players[self.current_player]
        print(f"{player.name}'s turn.")
        print("<..................................>")
        point = 0 

        while True:
            roll = self.dice.roll()
            if roll == 1:
                print(f"{player.name} rolled a 1 ............. and ........lost his turn.")
                point = 0
                print(player)
                break
            else:
                point += roll
                print(f"{player.name} rolled a {roll}")
                points_to_show = player.score + point
                print(f"{player.name} scored {points_to_show} points")

                if points_to_show >= 100:
                    break

            decision = player.make_decision()
            if decision == 'h':
                break
            elif decision == 'r':
                continue

        player.add_score(point)

        print(f"{player.name}'s turn is over. {player.name} scored {player.score}.")
        print("<................................................................................>")
        self.change_player()  

    def play(self):
        while (all(player.score < 100 for player in self.players)) and self.timeflag==False:
            self.play_turn()
        if (self.timeflag==True):
            dict2= {}
            dict2[self.players[0].name]=self.players[0].score
            dict2[self.players[1].name]=self.players[1].score
            dict(sorted(dict2.items(), key=lambda item: item[1]))
            second_pair = list(dict2.items())[1]
            second_key, second_value = second_pair
            print(f"{second_key} is the winner with {second_value} points!")



        winners = [player for player in self.players if player.score >= 100]
        if len(winners) == 1:
            print(f"{winners[0].name} is the winner with {winners[0].score} points!")




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("player1", type=str, choices=["human", "computer"], default="human", help="Type of Player 1")
    parser.add_argument("player2", type=str, choices=["human", "computer"], default="human", help="Type of Player 2")
    parser.add_argument("timed", type=int,default=60, help="TIMER")
    args = parser.parse_args()

    print("Welcome To The PIG GAME")
    print("<................................................................................>")
    random.seed(0)
        
    player1_type = args.player1
    player2_type = args.player2

    player1 = PlayerFactory.create_player(player1_type)
    player2 = PlayerFactory.create_player(player2_type)

    game = TimedGameProxy([player1, player2], args.timed)
    game.play()
