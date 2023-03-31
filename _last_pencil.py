#!/bin/python3

from random import choice
import string


class Game:
    WORDS = "python,java,swift,javascript".split(",")
    tot_won = 0
    tot_lost = 0

    def __init__(self):
        self.attempts_left = 8
        print(f"H A N G M A N # {self.attempts_left} attempts")
        self.WORD = choice(self.WORDS)
        # self.WORD= 'python' # DDD
        self.word_found = False

    def ask_input(self):
        i = input("Input a letter: ")
        if len(i) != 1:
            print("Please, input a single letter.")
            return None
        if not i in string.ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
            return None

        return i

    def check_word(self, input_letters):
        if self.get_masked_word(input_letters) == self.WORD:
            self.word_found = True

    def get_masked_word(self, input_letters) -> str:
        res = [j if j in input_letters else "-" for (i, j) in enumerate(self.WORD)]
        return "".join(res)

    def is_still_on(self):
        return self.attempts_left > 0 and not self.word_found

    def get_curr_attempts(self):
        return f"# {self.attempts_left} attempts"

    def res_not_improvements(self, input_letters, input_letter):
        if input_letter in input_letters:
            return True
        return False

    def res_letter_not_in_word(self, input_letter):
        if input_letter not in self.WORD:
            self.attempts_left -= 1
            return True
        return False


if __name__ == "__main__":
    while True:
        game = Game()
        main_input = input(
            'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
        )
        if main_input == "exit":
            break
        if main_input == "results":
            print(
                f"""\
You won: {Game.tot_won} times.
You lost: {Game.tot_lost} times.
            """
            )
            continue
        if main_input == "play":
            input_letters = set()
            while game.is_still_on():
                print("\n" + game.get_masked_word(input_letters))
                input_letter = game.ask_input()
                if input_letter is None:
                    continue

                if game.res_not_improvements(input_letters, input_letter):
                    print("You've already guessed this letter.")
                if game.res_letter_not_in_word(input_letter):
                    print("That letter doesn't appear in the word. ", end="")
                    print(game.get_curr_attempts())
                input_letters.add(input_letter)
                game.check_word(input_letters)
                if not game.is_still_on():
                    break

            if game.word_found:
                Game.tot_won += 1
                print(
                    f"""
You guessed the word {game.WORD}!
You survived!"""
                )
            else:
                Game.tot_lost += 1
                print("\nYou lost!")
