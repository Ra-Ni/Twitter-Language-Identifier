from re import compile

from vocabularies import Vocabulary


class LowerUpperVocabulary(Vocabulary):

    def __init__(self, window_size=1):
        super().__init__(window_size)
        self._pattern = compile('.*[^a-zA-Z].*')

    def accepts(self, item) -> bool:
        return not self._pattern.match(item)

    def __len__(self) -> int:
        return 52

    def __str__(self):
        return '1'
