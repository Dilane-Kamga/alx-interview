#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5])))
print("Winner: {}".format(isWinner(5, [0, 0, 0, 0, 0])))
