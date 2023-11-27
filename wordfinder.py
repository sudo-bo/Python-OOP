"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    
    def __init__(self, file_path):
        self.words = open(f"{file_path}", "r")
        self.words_list = self.create_list(self.words)
        self.words.close()

    def create_list(self, words):
        new_list = [word.strip() for word in words]
        print(f"{len(new_list)} words read")
        return new_list
    
    def random(self):
        return choice(self.words_list)
        
class SpecialWordFinder(WordFinder):

    def __init__(self, file_path):
        super().__init__(file_path)

    def create_list(self, words):
        new_list = []
        for word in words:
            if not word.isspace():
                new_list.append(word.strip())
            if word.startswith("# "):
                new_list.append(word.strip()[2:])
        print(f"{len(new_list)} words read for special finder")
        return new_list