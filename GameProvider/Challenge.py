from GameProvider.ManualPlayer import ManualPlayer
from GameCommon.IPlayer import IPlayer
from GameCommon.IGame import IGame
from GameCommon import jsondata


data = jsondata.jsonInput()

class ChallangeGame(IGame):
    """All challenge game logic goes here.."""

    def __init__(self,score):
            self.score = score


    def Winner(self, whichPlayer,score):
        """ Prints The Challenge WINNER! """

        if whichPlayer == 0:
            result = self.score[0] - self.score[1]
            print(data['mplayer1'], result)
        else:
            result = self.score[1] - self.score[0]
            print(data['mplayer2'], result)


    def ChallangeGame(self):
        """Plays entire challenge  game."""

        whichPlayer = ManualPlayer.SelectPlayer(self)
        if whichPlayer == 0 or whichPlayer == 1:
            self.playGame(whichPlayer)
        else:
            print(data['invalid'])
            self.ChallangeGame()


    def playGame(self, whichPlayer):
        """keeps playing until reaches 100 points."""

        while True:
            rollHold = ManualPlayer.MyInput(self)
            if rollHold == 'r':
                whichPlayer, cscore = IPlayer.Roll(self, self.score, whichPlayer)

            elif rollHold == 'h':
                whichPlayer, cscore = IPlayer.Hold(self, whichPlayer)
            else:
                print(data['invalid'])
                self.playGame(whichPlayer)
            if (cscore[0] >= 100 or cscore[1] >= 100):
                ChallangeGame.Winner(self, whichPlayer, cscore)
                break

