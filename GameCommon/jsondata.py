import json
import logging


def jsonInput():
    """Reads 'input.txt',returns a dictionary. """

    try:
        file = '..//GameCommon//Input.txt'
        with open(file) as f:
            input = json.load(f)
        return{'player': input['player'],'rollHold':input['rollHold'],'invalid': input['invalid'],"numberofplayers": input["numberofplayers"],"GameType": input["GameType"],"finalScore": input["finalScore"],"tResult": input["tResult"],"tplayer1": input["tplayer1"],"tplayer2": input["tplayer2"],"mplayer1": input["mplayer1"],"mplayer2": input["mplayer2"],"turn": input["turn"],"scoreCard": input["scoreCard"],"gameRules":input['gameRules']}
    except IOError:
        print("Error: File does not appear to exist.")


formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name='mylogFile', log_file='logFile.log', level=logging.INFO):
    """Returns a log """

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
