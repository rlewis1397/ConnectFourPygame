"""
Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019

Board class, does bulk of work.
Populates board
Evaluates board

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

import game_piece
import pygame
from locations import piece_locations


class Board:

    def __init__(self, surface):
        self.width = 8
        self.height = 6
        self.surface = surface
        self.screen = surface.screen
        self.pieces = [[], [], [], [], [], []]
        self.win_state = False
        self.columns_full = [False, False, False, False, False, False, False, False]
        self.title_font = pygame.font.SysFont("ComicSans", 60)  # Font doesn't show as comic sans

    def populate_board(self):
        for x in range(self.height):
            for y in range(self.width):
                new_piece = game_piece.GamePiece(self.screen, piece_locations[x][y])
                self.pieces[x].append({(x, y): ['BLACK', new_piece]})

    def evaluate_board(self, player):
        if self.vertical_check() or self.horizontal_check() or self.diagonal_check():
            self.win(player)

    def assign_piece(self, column, player):
        for x in range(self.height - 1, -1, -1):
            if self.pieces[x][column].get((x, column))[0] == 'BLACK':
                entry = self.pieces[x][column].get((x, column))
                piece = entry[1]
                location = piece.location
                assigned_piece = game_piece.GamePiece(self.screen, location, player.color)
                if assigned_piece.location[1] == 100:
                    self.columns_full[column] = True
                entry[0] = player.text_color
                entry[1] = assigned_piece
                pygame.display.update()
                return

    def evaluate_click(self, mouse_position):
        column = 0
        if mouse_position[0] in range(0, 150):
            column = 0
        elif mouse_position[0] in range(150, 300):
            column = 1
        elif mouse_position[0] in range(300, 450):
            column = 2
        elif mouse_position[0] in range(450, 600):
            column = 3
        elif mouse_position[0] in range(600, 750):
            column = 4
        elif mouse_position[0] in range(750, 900):
            column = 5
        elif mouse_position[0] in range(900, 1050):
            column = 6
        elif mouse_position[0] in range(1050, 1200):
            column = 7
        if self.columns_full[column]:
            column = -1
            return column
        return column

    def horizontal_check(self):
        for x in range(self.height):
            entry = self.pieces[x]
            piece_colors = []
            for piece, y in zip(entry, range(8)):
                p = entry[y].get((x, y))[0]
                piece_colors.append(p)
            if self.eval_chain(piece_colors):
                return True
        return False

    def vertical_check(self):
        for x in range(self.width):
            eval_array = []
            for y in range(self.height):
                entry = self.pieces[y][x].get((y, x))[0]
                eval_array.append(entry)
            if self.eval_chain(eval_array):
                return True
        return False

    def diagonal_check(self):
        for x in range(3):
            for y in range(5):
                block = [self.pieces[x][y:y+4][0:4], self.pieces[x+1][y:y+4][0:4],
                         self.pieces[x+2][y:y+4][0:4], self.pieces[x+3][y:y+4][0:4]]
                if self.eval_block(block):
                    return True

    def win(self, player):
        print(f"Congratulations {player.text_color}, you won!")
        text = self.title_font.render(player.win_text, True, player.color)
        self.win_state = True
        self.screen.blit(text, (10, 0))
        pygame.display.update()

    @staticmethod
    def eval_chain(array):
        for x in range(len(array)-3):
            if array[x] == array[x+1] == array[x+2] == array[x+3] != 'BLACK':
                return True
        return False

    @staticmethod
    def eval_block(array):
        left_diagonal = []
        right_diagonal = []

        for x in range(4):
            left_diagonal.append(list(array[x][-(x+1)].values())[0][1])
            right_diagonal.append(list(array[x][x].values())[0][1])
        if left_diagonal[0] == left_diagonal[1] == left_diagonal[2] == left_diagonal[3] != (0, 0, 0):
            return True
        if right_diagonal[0] == right_diagonal[1] == right_diagonal[2] == right_diagonal[3] != (0, 0, 0):
            return True
        return False
