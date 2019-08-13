from GameCommon.IScore import IScore
from GameCommon import jsondata
data= jsondata.jsonInput()
logger = jsondata.setup_logger('Score')

class Score(IScore):
    """A class for score calculation and player switch."""

    def __init__(self,score):
        self.score =score


    def ChangePlayer(whichPlayer):
        """Swiches player on hold or dice 1 condition."""

        whichPlayer = 1 - int(whichPlayer)
        print(data['turn'] + str(whichPlayer+1))
        return whichPlayer


    def CalculateScore(self,cscore,dice,whichPlayer):
        """Calculates score for human as well as computer player."""

        if dice == 1:
            if whichPlayer == 0:
                cscore[0] = 0
            else:
                cscore[1] = 0

            whichPlayer = Score.ChangePlayer(whichPlayer)
            logger.info('Player switched')
            return whichPlayer,cscore
        else:
            if whichPlayer == 0:
                cscore[0] = self.score[0] + dice
            else:
                cscore[1] = self.score[1] + dice

            return whichPlayer,cscore
