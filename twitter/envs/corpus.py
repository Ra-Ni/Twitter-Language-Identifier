from math import log

from itertools import tee


class Corpus:
    __global_count = 0.0

    def __init__(self, size=0, smoothing_value=0, label=None):
        self.size = size
        self.smoothing_value = smoothing_value
        self.label = label

        self.frequencies = {}

        self.local_count = float(size * smoothing_value)
        Corpus.__global_count += self.local_count
        self.local_score = None

    def items(self):
        return self.frequencies.items()

    def keys(self):
        return self.frequencies.keys()

    def update(self, item):
        self.frequencies[item] = self.frequencies.get(item, 0) + 1
        self.local_count += 1
        Corpus.__global_count += 1

    def update_all(self, iterator):
        for item in iterator:
            self.frequencies[item] = self.frequencies.get(item, 0) + 1
            self.local_count += 1
            Corpus.__global_count += 1

    def individual_score(self, item):
        return log((self.smoothing_value + self.frequencies.get(item, 0)) / self.local_count, 10)

    def score(self, iterator):
        if not self.local_score:
            self.local_score = log(self.local_count / Corpus.__global_count, 10)

        results = self.local_score
        for item in iterator:
            results += log((self.smoothing_value + self.frequencies.get(item, 0)) / self.local_count, 10)

        return results

    def __iter__(self):
        for key, frequency in self.frequencies.items():
            yield key, frequency, (frequency + self.smoothing_value) / self.local_count

    def __hash__(self):
        return hash(self.frequencies)

    def __len__(self):
        return int(self.local_count)


class CorpusController:

    def __init__(self, size, smoothing_value, *languages):
        super().__init__()
        self.languages = languages
        self.smoothing_value = smoothing_value
        self.size = size
        self.corpora = {}
        for language in languages:
            self.corpora[language] = Corpus(self.size, self.smoothing_value, label=language)

    def train(self, iterator, language):
        self.corpora[language].update_all(iterator)

    def classify(self, iterator):
        copies = iter(tee(iterator, len(self.corpora)))
        probabilities = [(corpus.score(next(copies)), label) for label, corpus in self.corpora.items()]
        score, predicted_label = max(probabilities)
        return score, predicted_label

    def save(self, target):
        with open(target, 'w') as writer:
            for corpus in self.corpora.values():
                writer.write(f'{corpus.label}')
                items = list(iter(corpus))
                items.sort(key=lambda x: x[2], reverse=True)
                for item in items:
                    writer.write(f'\r\n\t{item[0]}\t{item[1]}\t{item[2]}')
                writer.write('\r\n\r\n')
