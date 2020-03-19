import string


class Reader:
    def __init__(self, file, v, n):
        self.file = file
        self.v = v
        self.n = n

        if self.v == 0:
            self.vocabulary = dict.fromkeys(list(string.ascii_lowercase), 1)
        elif self.v == 1:
            self.vocabulary = dict.fromkeys(list(string.ascii_letters), 1)

        with open(file, 'r', encoding='UTF8') as f:
            self.content = f.readlines()
        f.close()

        # In case to read it top to bottom
        # self.content.reverse()

    def has_next(self):
        return False if self.content == [] else True

    def next(self):
        if self.has_next() is False:
            return None

        # Grab one line and split it onto list
        line = self.content.pop()
        line = line.split()
        line.reverse()

        # Segregate id, username and language
        id = line.pop()
        user = line.pop()
        language = line.pop()

        '''
        # Remove any terms starting with #, @ or http
        for element in line:
            if element.startswith("#") or element.startswith("@") or element.startswith("http"):
                line.remove(element)
        '''

        if self.v == 0 or self.v == 1:
            if self.v == 0:
                for element in line:
                    element.lower()

            # Replace any character not within vocabulary as space, potentially splitting word and add it back into list
            new_line = []
            for index in range(len(line)):
                characters = list(line[index])
                for character in characters:
                    if self.vocabulary.get(character) is None:
                        line[index] = line[index].replace(character, " ")
                new_line += line[index].split()

        else:
            # Replace any character not within vocabulary as space, potentially splitting word and add it back into list
            # See example in section 1.2.2
            new_line = []
            for index in range(len(line)):
                if line[index].isalpha():
                    characters = list(line[index])
                    for character in characters:
                        if character.isalpha():
                            line[index] = line[index].replace(character, " ")
                new_line += line[index].split()

        grams = []
        for term in new_line:
            index = 0;
            while index + self.n <= len(term):
                grams.append(term[index:index+self.n])
                index += 1

        return id, grams


sample = Reader("training-tweets.txt", 1, 3)
while sample.has_next():
    print(sample.next())




