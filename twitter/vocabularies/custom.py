from re import compile
import string

from vocabularies import Vocabulary


class CustomVocabulary(Vocabulary):

    def __init__(self, window_size=1):
        super().__init__(window_size)
        languages = {
            "basque" : list('Ññ'),
            "catalan" : list('ÇçàÀèÈéÉíÍïÏòÒóÓúÚüÜ'),
            "galician" : list('ÑñáÁéÉïÏíÍóÓüÜ'),
            "spanish" : list('ÁÉÍÓÚÜÑáéíóúüñ¿¡'),
            "portuguese" : list('áÁâÂãÃàÀçÇéÉêÊíÍóÓôÔõÕúÚ'),
        }

        self.__pattern = dict.fromkeys(list(string.ascii_letters), 1)
        for values_list in languages.values():
            for item in values_list:
                self.__pattern.setdefault(item, 1)

    def accepts(self, item) -> bool:
        return item in self.__pattern

    def __len__(self) -> int:
        return len(self.__pattern)

    def __str__(self):
        return '0'
