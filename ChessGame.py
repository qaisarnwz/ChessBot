import chess


class ChessGame:
    def __init__(self, player1, player2):
        self.board = chess.Board()
        self.players = [player1, player2]

    def make_move(self):

        player = self.players[1 - int(self.board.turn)]
        move = player.choose_move(self.board)

        self.board.push(move)

    def is_game_over(self):
        return self.board.is_game_over()

    def result(self):
        return self.board.outcome()

    def __str__(self):

        setup_str = "\n----------------\na b c d e f g h\n"
        board_str =  str(self.board) + setup_str

        if self.board.turn:
            move_str = "White's turn"
        else:
            move_str = "Black's turn"

        return board_str + "\n" + move_str + "\n"
