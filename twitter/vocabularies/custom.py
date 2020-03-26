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
        for key in languages:
            print(languages[key])
            for char in languages[key]:
                if self.__pattern.get(char) is None:
                    self.__pattern[char] = 1

    def accepts(self, item) -> bool:
        if self.__pattern[item] is 1:
            return True
        else:
            return False

    def __len__(self) -> int:
        return len(self.__pattern)

    def __str__(self):
        return '0'
