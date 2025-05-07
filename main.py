import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, PURPLE, WHITE, BLACK, GREEN
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def display_message(win, message):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 80)
    text = font.render(message, 1, GREEN)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    game_over_message = None

    while run:
        clock.tick(FPS)

        if game_over_message:
            display_message(WIN, game_over_message)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
            continue

        if game.turn == PURPLE:
            value, new_board = minimax(game.get_board(), 3, PURPLE, game)
            if new_board:
                game.ai_move(new_board)
            else:
                if not game.winner():
                    print("AI has no moves.")

        winner = game.winner()
        if winner is not None:
            if winner == RED:
                game_over_message = "Red Wins!"
            elif winner == PURPLE:
                game_over_message = "Purple Wins!"
            elif winner == WHITE:
                game_over_message = "White Wins!"
            else:
                game_over_message = "Draw!"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over_message:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        if not game_over_message:
            game.update()
        else:
            display_message(WIN, game_over_message)

    pygame.quit()

main()