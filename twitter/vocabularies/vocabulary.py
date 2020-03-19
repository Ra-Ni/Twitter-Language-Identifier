from abc import ABC, abstractmethod
from re import sub


class Vocabulary(ABC):

    def __init__(self, window_size=1):
        self.window_size = window_size

    @property
    def window_size(self):
        return self._window_size

    @window_size.setter
    def window_size(self, new_window):
        if new_window > 0:
            self._window_size = new_window
        else:
            raise ValueError

    def filter(self, post):
        iterator = iter(post)
        buffer = []

        for __ in range(1, self._window_size):
            try:
                next_item = next(iterator)
            except StopIteration:
                return
            buffer.append(next_item)

        for item in iterator:
            buffer.append(item)
            new_item = ''.join(buffer)
            if self.accepts(new_item):
                yield new_item
            del buffer[0]

    def pre_process(self, item):
        return sub('[\r\n]+', '', item)

    def load(self, target):

        with open(target, 'r') as reader:

            for line in reader:
                new_line = self.pre_process(line)

                if new_line:
                    post_id, user, language, post = tuple(new_line.split('\t'))
                    yield post_id, user, language, self.filter(post)

    @abstractmethod
    def accepts(self, item):
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __str__(self):
        pass
