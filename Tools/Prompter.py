#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
import os

##
#
class Prompter:

    ## constructor
    def __init__(self):
        pass

    ## list available choices
    def prompt_choice(self, question, iterable):
        self.print_question(question)
        self.print_choice(iterable)
        return self.input_request("choose an option (1, 2, 3, ...) ?")

    ## ask a question
    def prompt_question(self, sentence):
        self.print_msg("")
        self.print_question(sentence)
        return self.input_request(" type here : ")

    ## ask the user to press a key to continue
    def press_a_key_continue(self):
        self.input_request("Press a key to continue...")

    ## retrieve the user's choice
    def print_option_choosen(self, rep, liste):
        try:
            self.print_output_msg("You've choosen : " + str(liste[int(rep)]))
        except:
            self.print_output_msg(str(rep) + " is not in the list.")

    ## print the user's choice
    def print_choice(self, iterable):
        i = 1
        for option in iterable:
            self.print_option(i, option)
            i += 1

    ## print option
    def print_option(self, number, msg):
        self.print_msg(str(number) + ") " + msg)

    ## print question
    def print_question(self, msg):
        self.print_msg("? : " + str(msg))

    ## print output msg
    def print_output_msg(self, msg):
        self.print_msg("")
        self.print_msg("[Output] : " + msg)
        return msg

    ## print the specified message
    def print_msg(self, msg):
        print(msg)

    ## prompter
    def input_request(self, msg):
        some_text = raw_input("-> " + str(msg))
        return some_text

    ## clear the screen
    def clear_screen(self):
        os.system("clear")


## test
def test():
    p = Prompter()

    # the question
    p.print_output_msg(p.prompt_question("Is python a good language ?"))

    # available choices
    list = ["SUPAman doh", "Make me feel cool", "Back to the old scripting fashion time..."]
    index = p.print_output_msg(p.prompt_choice("What's developping in Python makes you feel like ?", list))
    p.print_option_choosen(index, list)

## launch test
if __name__ == "__main__":
    test()
