from vocabularies import Vocabulary


class AlphaVocabulary(Vocabulary):

    def accepts(self, item) -> bool:
        return all(character.isalpha() for character in item)

    def __len__(self) -> int:
        return 116766

    def __str__(self):
        return '2'
