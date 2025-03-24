import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ").lower()
            answer2 = input("player2: ").lower()

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0
        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def calculate_vowels(self, word: str):
        vowels = "aeiouyåöäö"
        number_of_vowels = 0
        for c in word:
            if c in vowels:
                number_of_vowels += 1
        return vowels
    
    def round_winner(self, player1_word, player2_word):
        if self.calculate_vowels(player1_word) > self.calculate_vowels(player2_word):
            return 1
        elif self.calculate_vowels(player2_word) > self.calculate_vowels(player1_word):
            return 2
        else:
            return 0
        
class RockPaperScissorsLizardSpock(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        rules = {
            "scissors": ["paper", "lizard"],
            "paper": ["rock", "spock"],
            "rock": ["lizard", "scissors"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }

        if player1_word not in rules and player2_word not in rules:
            return 0  # It's a tie

        if player1_word not in rules:
            return 2  # Player 1 loses

        if player2_word not in rules:
            return 1  # Player 2 loses

        if player2_word in rules[player1_word]:
            return 1  # Player 1 wins
        elif player1_word in rules[player2_word]:
            return 2  # Player 2 wins
        else:
            return 0  # It's a tie



if __name__ == "__main__":
    p = WordGame(3)
    p.play()
    p2 = LongestWord(3)
    p2.play()
    p3 = RockPaperScissorsLizardSpock(3)
    p3.play()
