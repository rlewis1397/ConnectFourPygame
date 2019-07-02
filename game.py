"""
Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019

Game class, runs 'main'

Author: Rachel Lewis
Class: CSI-260-02
Assignment: Final
Due Date: April 28, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import pygame
import board
from red_player import RedPlayer
from blue_player import BluePlayer
from screen import Screen


class Game:

    @classmethod
    def connect_four(cls):
        pygame.init()
        pygame.font.init()
        screen = Screen()
        screen.screen.fill(screen.background_color)
        game_board = board.Board(screen)
        game_board.populate_board()
        red_player = RedPlayer()
        blue_player = BluePlayer()
        pygame.display.flip()
        counter = 0

        while not screen.close_request:
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN and not game_board.win_state:
                    column = game_board.evaluate_click(pygame.mouse.get_pos())
                    if column == -1:
                        pass
                    if counter % 2 == 0 and column > -1:
                        game_board.assign_piece(column, red_player)
                        pygame.display.update()
                        game_board.evaluate_board(red_player)
                        counter += 1
                    elif counter % 2 == 1 and column > -1:
                        game_board.assign_piece(column, blue_player)
                        pygame.display.update()
                        game_board.evaluate_board(blue_player)
                        counter += 1
                if event.type is pygame.QUIT:
                    screen.close_requested = True
                    pygame.display.quit()


if __name__ == '__main__':
    Game.connect_four()
