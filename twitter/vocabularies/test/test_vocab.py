import unittest

import vocabularies


class MyTestCase(unittest.TestCase):
    def test_something(self):
        vocabulary = vocabularies.make(2, 2)
        generator = vocabulary.load('../../../OriginalDataSet/training-tweets.txt')
        for id, user, lang, gen in generator:
            print(id, user, lang, end='\t')
            for item in gen:
                print(item, end='\t')
            print()

if __name__ == '__main__':
    unittest.main()
