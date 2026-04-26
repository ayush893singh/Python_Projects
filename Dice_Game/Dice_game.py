import random

class DiceGame:
    def __init__(self):
        self.players = []

    def setup_players(self):
        print("\n===== DICE GAME =====")
        p1 = input("Enter Player 1 name: ")
        p2 = input("Enter Player 2 name: ")

        self.players = [p1, p2]
        print(f"\nMatch: {p1} vs {p2}")

    def roll_dice(self):
        return random.randint(1, 6)

    def player_turn(self, player_name):
        total = 0
        print(f"\n{player_name}'s TURN (4 rolls)")

        for i in range(1, 5): 
            input(f"Press Enter for roll {i}...")
            roll = self.roll_dice()
            print(f"Roll {i}: {roll}")
            total += roll

        print(f"\n***Total score of {player_name}: {total}***")
        return total

    def play(self):
        if len(self.players) < 2:
            print("Please add players first")
            return

        print("\n===== GAME START =====")

        p1_score = self.player_turn(self.players[0])
        p2_score = self.player_turn(self.players[1])

        print("\n===== FINAL RESULT =====")
        print(f"{self.players[0]}: {p1_score}")
        print(f"{self.players[1]}: {p2_score}")

        if p1_score > p2_score:
            print(f"\nWinner: {self.players[0]}")
        elif p2_score > p1_score:
            print(f"\n---Winner: {self.players[1]}---")
        else:
            print("\nMatch Draw")
game = DiceGame()
game.setup_players()
game.play()
