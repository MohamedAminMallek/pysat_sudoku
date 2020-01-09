import pygame, sys
from pygame.locals import *
import numpy as np
import pickle

# Number of frames per second
FPS = 10


# Sets size of grid
WINDOWMULTIPLIER = 5  # Modify this number to change size of grid
WINDOWSIZE = 81
WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3)  # size of a 3x3 square
CELLSIZE = int(SQUARESIZE / 3)  # Size of a cell
NUMBERSIZE = CELLSIZE / 3  # Position of unsolved number

# Set up the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGRAY = (200, 200, 200)


def drawGrid():
    ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (0, y), (WINDOWWIDTH, y))

    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, SQUARESIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (WINDOWWIDTH, y))

    return None


def initiateCells():
    currentGrid = {}
    with open("solmat.txt", "rb") as fp:  # Unpickling
        matrix = pickle.load(fp)
    print(matrix)
    for xCoord in range(0, 9):
        for yCoord in range(0, 9):
            fullCell = [matrix[xCoord, yCoord]]
            if fullCell[0] != 0:
                currentGrid[xCoord, yCoord] = list(fullCell)  # Copies List
        else:
            currentGrid[xCoord, yCoord] = list([' '])

    return currentGrid


# Takes the remaining numbers and displays them in the cells.
def displayCells(currentGrid):
    # Create offset factors to display numbers in right location in cells.
    xFactor = 0
    yFactor = 0
    for item in currentGrid:  # item is x,y co-ordinate from 0 -8
        #print(currentGrid)
        cellData = currentGrid[item]  # isolates the numbers still available for that cell
        print(item)
        populateCells(cellData[0], (item[0] * 45),(item[1] * 45))
    return None


# writes cellData at given x, y co-ordinates
def populateCells(cellData, x, y):
    cellSurf = BASICFONT.render('%s' % (cellData), True, BLACK)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (y+10,x+5)
    DISPLAYSURF.blit(cellSurf, cellRect)


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Sudoku Solver')

    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 40
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    DISPLAYSURF.fill(WHITE)

    currentGrid = initiateCells()
    displayCells(currentGrid)

    drawGrid()

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()