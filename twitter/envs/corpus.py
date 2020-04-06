from math import log10

from itertools import tee


class Corpus:
    __global_corpus_frequency = 0.0

    def __init__(self, size, depth, smoothing_value, label):
        self.depth = depth
        self.size = size
        self.smoothing_value = smoothing_value
        self.label = label

        self.frequencies = {}
        self.total_frequencies = float(size * smoothing_value)
        self.local_corpus_frequency = 0.0

    def items(self):
        return self.frequencies.items()

    def keys(self):
        return self.frequencies.keys()

    def values(self):
        return self.frequencies.values()

    def update(self, iterator):

        for item in iterator:
            target = self.frequencies

            for character in item:
                new_target = target.setdefault(character, [0, {}])
                new_target[0] += 1
                target = new_target[1]

        self.local_corpus_frequency += 1
        Corpus.__global_corpus_frequency += 1

    def score(self, iterator):
        results = log10(self.local_corpus_frequency / Corpus.__global_corpus_frequency)

        for item in iterator:
            previous_target, target = None, self.frequencies

            for character in item:
                new_target = target.get(character, [0, {}])
                previous_target, target = target, new_target[1]

            numerator = previous_target.get(item[-1], [0, {}])[0] + self.smoothing_value
            denominator = sum([value for value, __ in previous_target.values()]) + self.smoothing_value * self.size
            try:
                results += log10(numerator / denominator)
            except (ZeroDivisionError, ValueError):
                results += log10(1e-64)

        return results

    def __hash__(self):
        return hash(self.label)


class CorpusController:

    def __init__(self, size, depth, smoothing_value, *labels):
        self.languages = labels
        self.smoothing_value = smoothing_value
        self.size = size
        self.depth = depth
        self.corpora = {}
        for label in labels:
            self.corpora[label] = Corpus(self.size, self.depth, self.smoothing_value, label)

    def train(self, iterator, label):
        self.corpora[label].update(iterator)

    def classify(self, iterator):
        copies = iter(tee(iterator, len(self.corpora)))
        probabilities = [(corpus.score(next(copies)), label) for label, corpus in self.corpora.items()]
        return max(probabilities)
