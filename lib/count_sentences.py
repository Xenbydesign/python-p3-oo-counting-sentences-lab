#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, strVal):
        if type(strVal) == str:
            self._value = strVal
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        value = self.value
        for punctuation in ["!", "?"]:
            value = value.replace(punctuation, ".")
        sentences = [sen for sen in value.split(".") if sen]
        return len(sentences)
