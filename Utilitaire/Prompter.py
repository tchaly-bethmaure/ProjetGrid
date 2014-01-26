#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Prompter:
    def __init__(self):
        pass

    # demande a l'utilisateur de choisir parmis les choix dans iterable
    def prompt_choice(self, question, iterable):
        clear_screen()
        self.print_question(question)
        self.print_choice(iterable)
        return input_request("choose an option (1, 2, 3, ...) ?")

    # pose a l'utilisateur une question et lui demande d'y repondre
    def prompt_question(self, sentence):
        self.print_msg("")
        self.print_question(sentence)
        return input_request(" type here : ")

    # suite au choix, output le choix de l'utilisateur
    def print_option_choosen(self, rep, liste):
        try:
            self.print_output_msg("Réponse choisie : " + str(liste[int(rep) - 1]))
        except:
            self.print_output_msg("La réponse " + str(rep) + " n'est pas dans la liste des choix.")

    def print_choice(self, iterable):
        i = 1
        for option in iterable:
            self.print_option(i, option)
            i += 1

    def print_option(self, number, msg):
        self.print_msg(str(number) + ") " + msg)

    def print_question(self, msg):
        self.print_msg("? : " + str(msg))

    def print_output_msg(self, msg):
        self.print_msg("[Output] : " + msg)
        return msg

    def print_msg(self, msg):
        print(msg)

def clear_screen():
    os.system("clear")

def input_request(msg):
    some_text = raw_input("-> " + str(msg))
    return some_text


# Pour tester cette classe : methode test()
def test():
    p = Prompter()

    # Une question simple
    p.print_output_msg(p.prompt_question("Is python a good language ?"))

    # un choix
    list = ["SUPAman doh", "Make me feel cool", "Back to the old scripting fashion time..."]
    index = p.print_output_msg(p.prompt_choice("What's developping in Python makes you feel like ?", list))
    p.print_option_choosen(index, list)

if __name__ == "__main__":
    test()