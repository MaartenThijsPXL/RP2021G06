# Handles user input and displaying chessboard.

import pygame as p

from Chess import ChessEngine

SCREEN_WIDTH = 1062
SCREEN_HEIGHT = 562
BOARD_WIDTH = BOARD_HEIGHT = 512
DIMENSION = 8
SQ_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

# Initialize a global dictionary of images. This will be called once in the main.

def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # NOTE: We can access an image by saying 'IMAGES["wP"]'

# Main driver for our code. This will handle user input and updating the graphics.

def main():
    p.init()
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color(102, 102, 51))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

# Responsible for all the graphics within a current game state.

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

# Draw the squares on the board.

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("dark gray")]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            color = colors[((i + j) % 2)]
            p.draw.rect(screen, color, p.Rect(j * SQ_SIZE + 150, i * SQ_SIZE + 25, SQ_SIZE, SQ_SIZE))

# Draw the pieces on the board.

def drawPieces(screen, board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = board[i][j]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(j * SQ_SIZE + 150, i * SQ_SIZE + 25, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()
