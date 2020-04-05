from vocabularies import Vocabulary


class AlphaVocabulary(Vocabulary):

    def accepts(self, item: str) -> bool:
        return item.isalpha()

    def __len__(self) -> int:
        return 125643

    def __str__(self):
        return '2'
