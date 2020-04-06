import vocabularies
from agents import Evaluator, Trainer
from envs import CorpusController

if __name__ == '__main__':
    vocabulary_type = 5
    ngram_size = 2
    smoothing_value = 1e-64

    vocabulary = vocabularies.make(vocabulary_type, ngram_size)
    twitter_database = CorpusController(len(vocabulary), ngram_size, smoothing_value, 'eu', 'ca', 'gl', 'es', 'en', 'pt')
    trainer = Trainer('../OriginalDataSet/training-tweets.txt')
    evaluator = Evaluator('../OriginalDataSet/test-tweets-given.txt')
    trainer.run(twitter_database, vocabulary)
    evaluator.run(twitter_database, vocabulary)
