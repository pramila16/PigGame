from abc import ABC, abstractmethod
from GameProvider.Score import Score
from GameProvider.FinalScore import Finalscore
import sys
import random
from GameCommon import jsondata

data = jsondata.jsonInput()
logger = jsondata.setup_logger('IPlayer')

class IPlayer(ABC):
    """ A base class for player interface. """

    def DiceThrow(self):
        """ Returns the random rolled dice. """

        dice = random.randint(1,6)
        return dice


    def invalid(self):
        """ Exit the game. """

        print(data['invalid'])
        logger.error("input is invalid")
        sys.exit()


    def Roll(self,score,whichplayer):
        """Retruns the score of a player on dice roll."""

        dice = IPlayer.DiceThrow(self)
        print("dice: ", dice)
        whichPlayer,cscore = Score.CalculateScore(self,score,dice,whichplayer)
        logger.info("dice is rolled")
        print(data['scoreCard'],"Player1 ", cscore[0], "player2 ",cscore[1])
        return whichPlayer,cscore


    def Hold(self,whichPlayer):
        """Turn passes to the other player and freeze the score. """

        newscore = Finalscore.FinalScore(self,self.score)
        whichPlayer = Score.ChangePlayer(whichPlayer)
        logger.info('dice is held')
        return whichPlayer,newscore


    @abstractmethod
    def SelectPlayer(self):
        """User input to select a player"""
        pass


    @abstractmethod
    def MyInput(self):
        """Takes input from user either roll or hold"""
        pass
