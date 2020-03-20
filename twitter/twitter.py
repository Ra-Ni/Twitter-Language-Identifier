import vocabularies
from agents import Evaluator, Trainer
from envs import CorpusController

if __name__ == '__main__':
    vocabulary_type = 4
    ngram_size = 1
    smoothing_value = 0.00000000001

    vocabulary = vocabularies.make(vocabulary_type, ngram_size)
    twitter_database = CorpusController(len(vocabulary), smoothing_value, 'eu', 'ca', 'gl', 'es', 'en', 'pt')
    trainer = Trainer('../OriginalDataSet/training-tweets.txt')
    evaluator = Evaluator('../OriginalDataSet/test-tweets-given.txt')
    trainer.run(twitter_database, vocabulary)
    evaluator.run(twitter_database, vocabulary)
    twitter_database.save('../OriginalDataSet/db.txt')

