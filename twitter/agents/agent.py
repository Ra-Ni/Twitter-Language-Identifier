from abc import abstractmethod, ABC

class Agent(ABC):

    def __init__(self, target_path):
        self.target_path = target_path

    @property
    def target_path(self):
        return self._target_path

    @target_path.setter
    def target_path(self, new_target):
        self._target_path = new_target

    @abstractmethod
    def run(self, database, vocabulary):
        pass
