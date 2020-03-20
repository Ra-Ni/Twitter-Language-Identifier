from re import sub

from vocabularies import Vocabulary


class NoFilterVocabulary(Vocabulary):

    def filter(self, post):
        post = sub('([@#][^ ]*)|((https?:)[^ ]*)', '', post)
        return super().filter(post)

    def accepts(self, item):
        return True

    def __len__(self) -> int:
        return 16 * 2 ** 17

    def __str__(self):
        return '4'
