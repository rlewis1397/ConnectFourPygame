"""
Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019

Blue player

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

from player import Player


class BluePlayer(Player):

    BLU = (0, 0, 255)

    def __init__(self):
        self.color = BluePlayer.BLU
        self.text_color = 'BLUE'
        self.win_text = 'Congratulations BLUE you WIN!'
