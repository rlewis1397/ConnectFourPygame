"""
Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019

Game piece class

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


class GamePiece:

    _size = (100, 100)

    def __init__(self, screen, location, color=(0, 0, 0)):
        self.location = location
        self.color = color
        self.screen = screen
        self.piece = pygame.draw.circle(self.screen, self.color, self.location, 50)

    def __str__(self):
        return f"{self.location} - {self.color}"

    def __repr__(self):
        return f"{self.location} - {self.color}"

    def __eq__(self, other):
        return self.color == other.color

    def __ne__(self, other):
        return self.color != other
