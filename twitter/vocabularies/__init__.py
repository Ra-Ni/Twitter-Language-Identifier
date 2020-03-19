from .vocabulary import *
from .alpha import *
from .lower import *
from .lower_upper import *
from .printable import *

__registry = {
    0: LowerVocabulary,
    1: LowerUpperVocabulary,
    2: AlphaVocabulary,
    3: PrintableVocabulary
}


def make(vocabulary_type, window_size):
    if vocabulary_type in __registry:
        return __registry[vocabulary_type](window_size)
