import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE, PURPLE, GREY
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.moves_since_last_capture = 0 # Counter for moves since last capture
        self.last_piece_count = self.board.red_left + self.board.white_left 

    def winner(self):
        if self.moves_since_last_capture >= 30: 
            return GREY
        return self.board.winner()

    def get_board(self):
        return self.board

    def ai_move(self, board):
        current_piece_count = board.red_left + board.white_left
        if current_piece_count < self.last_piece_count:
            self.moves_since_last_capture = 0 # Reset counter if AI captured a piece
            self.last_piece_count = current_piece_count # Update piece count
        
        self.board = board
        self.change_turn()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
                self.moves_since_last_capture = 0 # Reset counter if a piece is skipped (captured)
                # Update piece count after capture
                self.last_piece_count = self.board.red_left + self.board.white_left 
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.moves_since_last_capture += 1 
        
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = PURPLE
        else:
            self.turn = RED