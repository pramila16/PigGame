from GameCommon.IPlayer import IPlayer
from GameCommon import jsondata
data= jsondata.jsonInput()

class ManualPlayer(IPlayer):
    """A class for user input. """

    def SelectPlayer(self):
        """Asks human player to select player1 or player2. """

        player = input(data['player'])
        if player == "1":
            return 0
        elif player == "2":
            return 1
        else:
            return 'invalid'

    def MyInput(self):
        """Asks human player to roll or hold the dice."""

        rollHold = input(data['rollHold']).lower()
        return rollHold


