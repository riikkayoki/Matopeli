import pygame
from services.game import Game


def main():
    pygame.init()
    GAME = Game()
    GAME.run()

if __name__ == '__main__':
    main()
