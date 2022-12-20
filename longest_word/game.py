# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
import requests

BASE = 'https://wagon-dictionary.herokuapp.com/'

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase, k=9)


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        # if  word == '':
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        response = requests.get(BASE + word).json()
        print(response)
        if response['found'] != True:
            return False
        return True
