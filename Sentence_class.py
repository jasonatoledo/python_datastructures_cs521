   
    In this problem, I had to build a class called "Sentence" that would take
a sentence as a parameter (defualt is empty string) and remove all of the
punctuations then convert it to a list object. I then had to create several
methods as requested and use a if __name__ block & assert to test one of the
methods. This was really fun and a great way to get more familar with classes!

"""
import random
import string

class Sentence(object):
    """this class takes a string (in English) as an input and converts it to a
    list. it has several methods to manipulate the original string value."""
    __PUNC = string.punctuation  # create mangled static punctuation object
    
    def __init__(self, sentence=""):
        """initialize the class and remove punctations, convert the sentence
        object into list. the sentence is set as a private attribute."""
        self.__sentence = sentence
        for i in self.__sentence:
            if i in Sentence.__PUNC:
                self.__sentence = self.__sentence.replace(i,"")
        self.__sentence = self.__sentence.split()
    
    def get_all_words(self):
        """a method that will get all words from the string and return them
        as a list."""
        return self.__sentence
    
    def get_word(self, index):
        """this method takes an index as its parameter and returns the word at 
        the index provided. if the index is out of bounds, the method will 
        return an empty string."""
        if len(self.__sentence) > index and 0-len(self.__sentence) < index:
            return str(self.__sentence[index])
        else:
            return ""
    
    def set_word(self, index, new_word):
        """this method accepts an index as the first value and for the second
        value, a new word (string) that will replace the word at the index
        provided for the instance."""
        # set new_word object as a string value
        new_word = str(new_word)
        if len(self.__sentence) > index and 0-len(self.__sentence) < index:
            self.sentence =  self.__sentence[index] = new_word

    def scramble(self):
        """this method takes the sentence as a list and scrambles it. calling
        this method does not change the sentence attribute for the instance"""
        return random.sample(self.__sentence,len(self.__sentence))
    
    def __str__(self):
        """built in method used for printing"""
        return " ".join(self.__sentence)
    
    def __repr__(self):
        """a built in method to return the sentence as a single string with a
        period at the end by simply typing the object's name""" 
        return "".join(self.__str__()) + "."
    
# run if __name__ block with unit test using assert
if __name__ == "__main__":
    sentence = "HELLO WORLD PART TWO BECAUSE I CAN'T GO ON IF YOU CAN'T MAKE\
 PYTHON KEEP THE PARTY GOING NON-STOP!"
    my_inst = Sentence(sentence)
    # validate set_word method through assert test
    assert my_inst.set_word(3, "THREE") != my_inst
    print("-"*10,"Sentence unit test successful on set_word method","-"*10)
    # print the three outputs per requirements
    print("\nOriginal sentence:",sentence)
    print("\nSentence scrambled:",*my_inst.scramble())
    print("\nFinal version of the sentence:", my_inst)
