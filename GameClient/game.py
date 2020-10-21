from GameProvider import ComputerGame,Challenge,Tournament
from GameCommon import jsondata
data = jsondata.jsonInput()

logger = jsondata.setup_logger('game')
class PigGame:
    """Main Pig Game class. """

        def startGame(self):
        """Plays an entire game."""

        try:

            numberofplayers = input(data['numberofplayers'])
            if numberofplayers == "1":
                logger.info('You are playing Computer game')
                compobj = ComputerGame.Computer([0,0])
                compobj.ComputerPlay()
                logger.info('Game is finished')
            elif numberofplayers == '2':
                GameType = input(data['GameType'])
                if GameType == "1":
                    logger.info('You are playing Challenge Game')
                    chobj = Challenge.ChallangeGame([0,0])
                    chobj.ChallangeGame()
                    logger.info('Game is finished')
                elif GameType == "2":
                    logger.info('You are playing Tournament Game')
                    trnobj= Tournament.TournamentGame([0,0])
                    trnobj.Tornament()
                    logger.info('Game is finished')
                else:
                    logger.error('Execution interrutpted due to invalid input ')
                    print(data['invalid'])
                    self.startGame()
            else:
                logger.error('Execution interrutpted due to invalid input ')
                print(data['invalid'])
                self.startGame()

        except:
            return


if __name__ ==  "__main__":

    pigGameobj = PigGame()
    print(data['gameRules'])
    pigGameobj.startGame()
