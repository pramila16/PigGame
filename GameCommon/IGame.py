from abc import ABC, abstractmethod

class IGame(ABC):
    """A base class for game interface"""

    @abstractmethod
    def Winner(self,whichplayer,dice,score):
        """Displays the winner"""
        pass

