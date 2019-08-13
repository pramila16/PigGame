from abc import ABC, abstractmethod

class IScore(ABC):
    """A base class for score calculation."""

    @abstractmethod
    def CalculateScore(self):
        """Returns the calculated score on every roll."""
        pass

    @abstractmethod
    def FinalScore(self):
        """Return the final score on hold or dice 1. """
        pass
