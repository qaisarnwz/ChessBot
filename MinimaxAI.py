import chess
import math


class MinimaxAI():
    def __init__(self, depth):
        self.max_depth = depth
        self.player = False

    def choose_move(self, board):
        self.player = board.turn
        moves = self.minimax(board, 0)
        print("Minimax moves are ", moves)
        return moves

    def minimax(self, board, depth):
        v, move = self.max_val(board, depth)
        return move

    def evaluation(self, board):
        if board.is_checkmate() and board.outcome().winner == self.player:
            return math.inf

        vals = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 0}
        total = 0
        for square in chess.SQUARE_NAMES:
            piece = board.piece_at(chess.parse_square(square))
            if piece:
                name = piece.symbol().lower()
                color = piece.color
                val = vals[name]
                if color == self.player:
                    total += val
                else:
                    total -= val

        return total

    def cutoff_test(self, board, depth):
        if depth > self.max_depth or board.is_game_over():
            return True
        return False

    def max_val(self, board, depth):
        if self.cutoff_test(board, depth):
            if board.is_game_over() and board.outcome().winner == self.player:
                print("Minimax won")
            return self.evaluation(board), None
        v = -math.inf
        moves_list = list(board.legal_moves)
        final_move = None

        for move in moves_list:
            board.push(move)
            next_v, next_moves = self.min_val(board, depth + 1)
            if next_v > v:
                v = next_v
                final_move = move
            board.pop()
        return v, final_move

    def min_val(self, board, depth):
        if self.cutoff_test(board, depth):
            if board.is_game_over() and board.outcome().winner == self.player:
                print("Minimax won")
            return self.evaluation(board), None

        val = math.inf
        moves_list = list(board.legal_moves)
        final_move = None
        for move in moves_list:
            board.push(move)
            next_val, next_moves = self.max_val(board, depth + 1)
            if next_val < val:
                val = next_val
                final_move = move
            board.pop()
        return val, final_move
