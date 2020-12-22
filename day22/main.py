import itertools
import functools
import re
import math

from copy import deepcopy

INPUT_FILE = 'input.txt'

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result

def get_players(lines):
    player1 = []
    player2 = []
    i = 0
    while i < len(lines):
        player = player1 if lines[i] == 'Player 1:' else player2
        i += 1
        l = lines[i]
        while l:
            player.append(int(l))
            i += 1
            if i >= len(lines):
                break
            l = lines[i]
        i += 1
    return player1, player2

def main1():
    lines = read_file(INPUT_FILE)
    player1, player2 = get_players(lines)
    max_cards = len(player1) * 2
    while len(player1) and len(player2):
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        p = player1 if card1 > card2 else player2
        p.append(max(card1, card2))
        p.append(min(card1, card2))
    p = player1 or player2
    print(sum(x * (max_cards - i) for i, x in enumerate(p)))

def main2():
    lines = read_file(INPUT_FILE)
    
if __name__ == "__main__":
    main1()
    main2()
