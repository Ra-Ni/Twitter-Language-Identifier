from math import log10

from itertools import tee


class Corpus:
    __global_count = 0.0

    def __init__(self, size, smoothing_value, label):
        self.size = size
        self.smoothing_value = smoothing_value
        self.label = label

        self.frequencies = {}
        self.total_frequencies = float(size * smoothing_value)
        self.local_count = 0.0

    def items(self):
        return self.frequencies.items()

    def keys(self):
        return self.frequencies.keys()

    def update(self, iterator):

        for item in iterator:
            self.frequencies[item] = self.frequencies.get(item, self.smoothing_value) + 1
            self.total_frequencies += 1

        self.local_count += 1
        Corpus.__global_count += 1

    def score(self, iterator):
        results = log10(self.local_count / Corpus.__global_count)
        for item in iterator:
            results += log10(self.frequencies.get(item, self.smoothing_value) / self.total_frequencies)
        return results

    def __iter__(self):
        for key, frequency in self.frequencies.items():
            yield key, frequency, (frequency + self.smoothing_value) / self.total_frequencies

    def __hash__(self):
        return hash(self.frequencies)

    def __len__(self):
        return int(self.total_frequencies)


class CorpusController:

    def __init__(self, size, smoothing_value, *languages):
        super().__init__()
        self.languages = languages
        self.smoothing_value = smoothing_value
        self.size = size
        self.corpora = {}
        for language in languages:
            self.corpora[language] = Corpus(self.size, self.smoothing_value, language)

    def train(self, iterator, language):
        self.corpora[language].update(iterator)

    def classify(self, iterator):
        copies = iter(tee(iterator, len(self.corpora)))
        probabilities = [(corpus.score(next(copies)), label) for label, corpus in self.corpora.items()]
        return max(probabilities)

    def save(self, target):
        with open(target, 'w') as writer:
            for corpus in self.corpora.values():
                writer.write(f'{corpus.label}')
                items = list(iter(corpus))
                items.sort(key=lambda x: x[2], reverse=True)
                for item in items:
                    writer.write(f'\r\n\t{item[0]}\t{item[1]}\t{item[2]}')
                writer.write('\r\n\r\n')
