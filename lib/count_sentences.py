class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print('The value must be a string.')
        else:
            self._value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        delimiters = ['.', '?', '!']
        count = 0
        sentences = self.value.split()
        for sentence in sentences:
            if sentence[-1] in delimiters:
                count += 1
        return count