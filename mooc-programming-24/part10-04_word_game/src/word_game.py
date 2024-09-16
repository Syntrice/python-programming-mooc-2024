# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

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


class MostVowels(LongestWord):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def __get_vowels(self, word: str):
        word = word.lower()
        return [ch for ch in word if ch in "aeiou"]

    def round_winner(self, player1_word: str, player2_word: str):
        return super().round_winner(
            self.__get_vowels(player1_word), self.__get_vowels(player2_word)
        )


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        
        player1_word, player2_word = player1_word.lower(), player2_word.lower()

        wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        
        player1_valid = True if player1_word in wins.keys() else False
        player2_valid = True if player2_word in wins.keys() else False
        
        if player1_valid and player2_valid:
            if player1_word == player2_word:
                winner = 0
            elif wins[player1_word] == player2_word:
                winner = 1
            else:
                winner = 2
        elif player1_valid > player2_valid:
            winner = 1
        elif player2_valid > player1_valid:
            winner = 2
        else:
            winner = 0
            
        return winner
            
        

if __name__ == "__main__":

    p = RockPaperScissors(4)
    p.play()
