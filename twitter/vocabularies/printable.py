from vocabularies import Vocabulary


class PrintableVocabulary(Vocabulary):

    def accepts(self, item) -> bool:
        return item.isprintable()

    def __len__(self) -> int:
        return 137750

    def __str__(self):
        return '3'
