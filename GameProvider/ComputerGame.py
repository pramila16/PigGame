from GameProvider.ComputerPlayer import ComputerPlayer
from GameCommon.IPlayer import IPlayer
from GameCommon.IGame import IGame
from GameCommon import jsondata
data= jsondata.jsonInput()

class Computer(IGame):
    """All computer game logic goes here.."""

    def __init__(self,score):
            self.score = score


    def Winner(self, whichPlayer, score):
        """Prints Computer Game WINNER!"""

        if whichPlayer == 0:
            result = self.score[0] - self.score[1]
            print(data['mplayer1'], result)

        else:
            result = self.score[1] - self.score[0]
            print(data['mplayer2'], result)


    def ComputerPlay(self):
        """Plays entire computer game."""

        whichPlayer = ComputerPlayer.SelectPlayer(self)
        if whichPlayer == 0 or whichPlayer == 1:
            self.playGame(whichPlayer)
        else:
            print(data['invalid'])
            self.ComputerPlay()


    def playGame(self,whichPlayer):
        """keeps playing until reach 100 points."""

        while True:
            rollHold = ComputerPlayer.MyInput(self, whichPlayer)
            if rollHold == 'r':
                whichPlayer, cscore = IPlayer.Roll(self, self.score, whichPlayer)
            elif rollHold == 'h':
                whichPlayer, cscore = IPlayer.Hold(self, whichPlayer)
            else:
                print(data['invalid'])
                self.playGame(whichPlayer)
            if (cscore[0] >= 100 or cscore[1] >= 100):
                Computer.Winner(self, whichPlayer, cscore)
                break


