"""
It's up to you how you implement it . You don't have to actually visualise the drawing of the man hanging . 
Start simple, with everything running cell by cell group code which works together 
to perform a single task into a single function when you have a simple working mvp, 
try and put your code into a Hangman class It is expected you use OOP extra points for using unpacking using magic methods.
"""

import random

list_of_words = ["pocket", "cattle", "scarf", "overwrought", "lucky", "strap",
                 "damaged", "undress", "bounce", "trucks", "detect", "receipt", "discussion"]


class Hangman:

    def __init__(self, word):
        self.word = word

    def pick_a_word():
        word = random.choice(list_of_words)
        return word

    def ch_to_list(self):
        for i in range(len(self.word)):
            return list(self.word)

    def mask(self, list):
        mask_word_list = []
        word_list = Hangman.ch_to_list(word)
        for i in range(len(word_list)):
            if word_list[i] in list:
                mask_word_list += word_list[i]
            else:
                mask_word_list.append('*')
        return mask_word_list

    def jointer(list):
        return ''.join(list)

    def char_checker(self, ch):
        if ch in self.word:
            return True

    def attempt_counter(count):
        count -= 1
        if count == 0:
            print('Game Over')
        else:
            return count


print('Let\'s get started!\n Ya ready to be hanged?...here\'s Your word:')
list_successes = []
word_pick = Hangman.pick_a_word()                          # random word picked

word = Hangman(word_pick)  # instance of the class


# print the inicial mask
print(Hangman.jointer(Hangman.mask(word, list_successes)))
attemps = 6
# print(word_pick)


while attemps > 0:
    if '*' in Hangman.jointer(Hangman.mask(word, list_successes)):
        ch = input('Pick a character: ')
        if Hangman.char_checker(word, ch):
            list_successes.append(ch)
            print(Hangman.jointer(Hangman.mask(word, list_successes)))
        else:
            attemps -= 1
            print('Be carefull.You have got:', attemps, ' left.')
    else:
        print('                                                                Congratulations! You are save!')
        break
if attemps == 0:
    print('                                                                        You\'ve been hanged!!!')
    print('The word, anyway was: ', word_pick)
