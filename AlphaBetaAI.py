import chess
import math

class AlphaBetaAI():
    def __init__(self, depth):
        self.max_depth = depth
        self.player = False

    def choose_move(self, board):
        self.player = board.turn
        moves = self.AlphaBeta(board, 0)
        print("Alpha Beta moves are ", moves)
        return moves

    def AlphaBeta(self, board, depth):
        v, move = self.max_val(board, depth, -math.inf, math.inf)
        return move

    def evaluation(self, board):
        if board.is_checkmate() and board.outcome().winner == self.player:
            return math.inf

        vals = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 0}
        total = 0

        for square_name in chess.SQUARE_NAMES:
            piece = board.piece_at(chess.parse_square(square_name))
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

    def max_val(self, board, depth, alpha, beta):
        if self.cutoff_test(board, depth):
            if board.is_game_over() and board.outcome().winner == self.player:
                print("Minimax won")
            return self.evaluation(board), None
        v = -math.inf
        children = list(board.legal_moves)
        move = None

        for child in children:
            board.push(child)
            nextv, nextmoves = self.min_val(board, depth + 1, alpha, beta)
            if nextv > v:
                v = nextv
                move = child
                alpha = max(alpha,v)
            board.pop()
            if v >= beta:
                return v, move
        return v, move

    def min_val(self, board, depth, alpha, beta):
        if self.cutoff_test(board, depth):
            if board.is_game_over() and board.outcome().winner == self.player:
                print("Minimax won")
            return self.evaluation(board), None
        val = math.inf
        children = list(board.legal_moves)
        move = None
        for child in children:
            board.push(child)
            next_val, next_moves = self.max_val(board, depth + 1, alpha, beta)
            if next_val < val:
                val = next_val
                move = child
            board.pop()
            if val <= alpha:
                return val,move

        return val,move