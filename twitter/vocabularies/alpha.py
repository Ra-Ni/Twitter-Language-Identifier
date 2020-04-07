from vocabularies import Vocabulary


class AlphaVocabulary(Vocabulary):

    def accepts(self, item: str) -> bool:
        return item.isalpha()

    def __len__(self) -> int:
        # why did we do this? because our machines have different locale settings.
        # the hard way...
        count = 0
        for codepoint in range(17 * 2 ** 16):
            ch = chr(codepoint)
            if ch.isalpha():
                count += 1
        return count

    def __str__(self):
        return '2'
