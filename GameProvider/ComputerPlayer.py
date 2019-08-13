import random
from GameCommon.IPlayer import IPlayer
from GameCommon import jsondata
data= jsondata.jsonInput()

class ComputerPlayer(IPlayer):
    """A class for computer player."""

    def SelectPlayer(self):
        """selects player randomly."""

        player = random.randint(0, 1)
        return player


    def MyInput(self,whichPlayer):
        """Returns random outcome if computer player, asks for input if human player."""

        if whichPlayer == 0:
            outcome = random.randint(0,1000)
            if outcome%2 == 0:
                print("computer roll: ")
                return 'r'
            else:
                print("computer hold: ")
                return 'h'
        else:
            rollHold = input(data['rollHold']).lower()
            return rollHold

