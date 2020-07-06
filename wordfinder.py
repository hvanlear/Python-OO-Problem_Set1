"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, path):

        self.path = path
        print(f"{sum(1 for line in open(self.path))} words read")

    def __repr__(self):
        return f"this reads lines of a files and also will print random"

    def random_word(self):
        print(random.choice(list(open(self.path))))


class SpecialWordFinder(WordFinder):
    def parse(self, path):
        return [w.strip() for w in self.path if w.strip() and not w.startswith('#')]
