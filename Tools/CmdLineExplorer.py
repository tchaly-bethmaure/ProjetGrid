#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
import os
from Prompter import Prompter

##
#
class CmdLineExplorer(Prompter, object):
    ## constructor
    def __init__(self, root_folder):
        super(CmdLineExplorer, self).__init__()
        # set paths
        self.initial_path = root_folder
        self.current_path = root_folder
        # set folder infos
        self.folder_information = ""
        self.set_folder_information()

    ## go to the specified folder
    def go_in_folder(self, folder_name):
        if folder_name != "":
            if folder_name == "..":
                self.go_backward()
            else:
                self.go_forward(folder_name)

    ## go the the folder
    def go_forward(self, folder):
        new_path = self.current_path
        if new_path != "/":
            new_path += "/"
        new_path += folder
        if self.is_a_folder(new_path):
            self.current_path = new_path
            self.set_folder_information()

    ## go back to the parent folder
    def go_backward(self):
        tab = str(self.current_path).split("/")
        new_path = ""
        tab.reverse()

        while len(tab) != 1:
            element = tab.pop()
            if element != "":
                new_path += "/" + element
        if new_path != "":
            self.current_path = new_path
        else:
            self.current_path = "/"
        self.set_folder_information()

    ## set directory info
    def set_folder_information(self):
        try:
            self.folder_information = os.listdir(self.current_path)
        except:
            self.print_output_msg("No can't do.")
        finally:
            pass

    ## display directory information
    def display_folder_information(self):
        self.print_msg("# List of files and folders : ")
        self.print_msg("")
        j = 0
        to_print = ""
        for entity in self.folder_information:
            to_print += entity + "  "
            if j == 6:
                j = 0
                to_print += "\n"
            j += 1
        print to_print

    ## check if the specified file is in the current folder
    def is_in_folder(self, file_or_folder):
        if file_or_folder in self.folder_information:
            return True
        else:
            self.print_output_msg(file_or_folder + " is not located in this folder.")
            return False

    ## check if the specified file path is a directory
    def is_a_folder(self, folder_full_path):
        if os.path.isdir(folder_full_path):
            return True
        else:
            self.print_output_msg("Not a folder.")

    ## check if the specified file path is a regular file
    def is_a_file(self, file_full_path):
        if os.path.isfile(file_full_path):
            return True
        else:
            self.print_output_msg("Not a file.")

## test the current class
def test():
    cle = CmdLineExplorer("/home/tchaly/EspaceDeTravail/Git")
    #cle.display_folder_information()
    #cle.go_forward("ProjetGrid")
    #cle.display_folder_information()
    #cle.go_backward()
    #cle.display_folder_information()

    while True:
        cle.go_backward()
        print cle.current_path
        cle.press_a_key_continue()

## launch test
if __name__ == "__main__":
    test()
