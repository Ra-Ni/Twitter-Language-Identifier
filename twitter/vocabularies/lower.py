from re import compile

from vocabularies import Vocabulary


class LowerVocabulary(Vocabulary):

    def __init__(self, window_size=1):
        super().__init__(window_size)
        self._pattern = compile('.*[^a-zA-Z].*')

    def filter(self, post):
        return super().filter(post.lower())

    def accepts(self, item) -> bool:
        return not self._pattern.match(item)

    def __len__(self) -> int:
        return 26

    def __str__(self):
        return '0'
