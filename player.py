from enum import Enum


class Player(Enum):
    """
    Initialize enum definitions for the team colors
    """
    BLACK = 0
    WHITE = 1

    def next(self):
        """
        Get the next enum defined, in this case alternating between the black and white teams.
        :return: The next team in the enum
        """
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        return members[index]

