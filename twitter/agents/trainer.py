from agents import Agent


class Trainer(Agent):

    def __init__(self, target_path):
        super().__init__(target_path)

    def run(self, database, vocabulary):
        contents = vocabulary.load(self._target_path)

        for content in contents:
            database.train(content[3], content[2])
