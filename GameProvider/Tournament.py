from GameProvider.ManualPlayer import ManualPlayer
from GameCommon.IPlayer import IPlayer
from GameCommon import jsondata

data= jsondata.jsonInput()

class TournamentGame:
    """All Tournament game logic goes here.."""

    def __init__(self,score):
            self.score = score


    def Winner(self, whichPlayer, tResult, score, gameCount):
        """ Prints The Tournament WINNER!"""

        if whichPlayer == 0:
            tResult[0] = tResult[0] + score[0]
        else:
            tResult[1] = tResult[1] + score[1]
        print(data['tResult'],"player1 ", tResult[0],"player2 ",tResult[1])
        if gameCount == 3:
            if tResult[0] > tResult[1]:
                print(data['mplayer1'],tResult[0] - tResult[1])
            else:
                print(data['mplayer2'],tResult[1] - tResult[0])
        return whichPlayer, score, gameCount, tResult


    def Tornament(self):
        """Plays entire Tournament."""

        tResult =[0,0]
        gameCount = 0
        whichPlayer = ManualPlayer.SelectPlayer(self)
        if whichPlayer == 0 or  whichPlayer == 1:
            self.playGame(tResult,gameCount,whichPlayer)
        else:
            print('Invalid input')
            self.Tornament()



    def playGame(self,tResult,gameCount,whichPlayer):
        """keeps playing until reaches 100 points."""

        while (gameCount < 3):
            while True:
                rollHold = ManualPlayer.MyInput(self)
                if rollHold == 'r':
                    whichPlayer,cscore= IPlayer.Roll(self,self.score,whichPlayer)
                elif rollHold == 'h':
                    whichPlayer,cscore = IPlayer.Hold(self,whichPlayer)
                else:
                    print(data['invalid'])
                    self.playGame(tResult,gameCount,whichPlayer)
                if(cscore[0] >= 100 or cscore[1] >= 100):
                    gameCount = gameCount + 1
                    whichPlayer, cscore, gameCount, tResult = TournamentGame.Winner(self,whichPlayer,tResult,cscore,gameCount)
                    cscore[0] = 0
                    cscore[1] = 0
                    break