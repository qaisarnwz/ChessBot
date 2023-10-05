# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IDSMiniMaxAI import IDSMiniMaxAI

import sys

player1 = RandomAI()
player2 = MinimaxAI(1)
player3 = HumanPlayer()
player4 = IDSMiniMaxAI(2)
player5 = AlphaBetaAI(2)
game = ChessGame(player1, player4)

while not game.is_game_over():
    print(game)
    game.make_move()

print(game.result())
