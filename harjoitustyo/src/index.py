import pygame
from game_loop import Game

def main():
    pygame.init()
    GAME = Game()
    GAME.start()

if __name__ == '__main__':
    main()