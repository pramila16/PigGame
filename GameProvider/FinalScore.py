from GameCommon.IScore import IScore
from GameCommon import jsondata
data= jsondata.jsonInput()

class Finalscore(IScore):
    """A Class for calculating final score."""

    def FinalScore(self, score):

        finalScore = score
        print(data['finalScore'],"Player1 ", finalScore[0],"Player2",finalScore[1])
        return finalScore


