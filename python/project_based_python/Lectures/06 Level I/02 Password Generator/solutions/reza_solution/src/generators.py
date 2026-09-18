import string
import random
import nltk
# nltk.download('words')
from nltk.corpus import words

class PasswordGenerator:
    def __init__(self):
        self.numbers = [str(i) for i in range(10)]
        self.lower_case = [l for l in string.ascii_lowercase]
        self.upper_case = [L for L in string.ascii_uppercase]
        self.symbols = '''! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ ] ^ _ { | }  ~ `'''.split(' ')

    def generate(self,):
        pass


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, num_chars: int=10, use_numbers: bool=True, use_symbols: bool=True):
        super().__init__()
        self.num_chars = num_chars
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols
        self.possible_letter = self.get_possible_letter()

    def get_possible_letter(self):
        letter_list = self.lower_case + self.upper_case
        if self.use_numbers:
            letter_list.extend(self.numbers)
        if self.use_symbols:
            letter_list.extend(self.symbols)
        return letter_list
    
    def generate(self):
        password = "".join([random.choice(self.possible_letter) for _ in range(self.num_chars)])
        return password

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, words_len:int=4, seperator:str='Hyphen', 
                    capitalize:bool=False, full_words:bool=True):
        super().__init__()
        self.words_len = words_len
        self.seperator = self.get_separator(seperator)
        self.capitalize = capitalize
        self.full_words = full_words
        self.english_words = words.words()

    def get_separator(self, sep_name):
        if sep_name == "Hyphen":
            return "-"
        elif sep_name == "Semicolon":
            return ";"
        elif sep_name == "Colon":
            return ":"
        else:
            raise(ValueError)

    def get_random_word(self):
        random_word = random.choice(self.english_words)
        if self.full_words:
            return random_word
        else:
            return random_word[:len(random_word)//2+1]
        
    def generate(self):
        return self.seperator.join([self.get_random_word() for _ in range(self.words_len)])


class PINPasswordGenerator(PasswordGenerator):
    def __init__(self, len_num=8):
        super().__init__()
        self.len_num = len_num

    def generate(self):
        return "".join([random.choice(self.numbers) for _ in range(self.len_num)])
    
        

if __name__ == "__main__":
    pg = PINPasswordGenerator()
    print(pg.generate())
    