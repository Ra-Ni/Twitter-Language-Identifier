import string

from vocabularies import Vocabulary

"""
Basque:
Ññ

Catalan:
ÇçàÀèÈéÉíÍïÏòÒóÓúÚüÜ

Galician:
ÑñáÁéÉïÏíÍóÓüÜ

Spanish:
ÁÉÍÓÚÜÑáéíóúüñ¿¡

Portuguese:
áÁâÂãÃàÀçÇéÉêÊíÍóÓôÔõÕúÚ
"""


class CustomVocabulary(Vocabulary):

    def __init__(self, window_size=1):
        super().__init__(window_size)
        languages = list('ôÔÉÍéüÇÑÒèáàÁÕõÚúÜñã¿íÃòÊÈóêçâ¡ÓïÏÀÂ')
        self.__pattern = dict.fromkeys(list(string.ascii_letters) + list(languages), None)

    def accepts(self, item) -> bool:
        return all(sub_item in self.__pattern for sub_item in item)

    def __len__(self) -> int:
        return len(self.__pattern)

    def __str__(self):
        return '5'
