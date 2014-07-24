#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
from Model.Script import Script
from Tools.Prompter import Prompter
from Tools.CmdLineExplorer import CmdLineExplorer
from Tools.JobExecutor import JobExecutor

##
#
class ScriptBrowser(Prompter, object):
    ## available choices for menu
    choix_menu = {
        1: "Add a script to queue",
        2: "Delete a script from queue",
        3: "Next step"
    }
    ## available choices for folder mode selection
    choix_folder_mode = {
        1: "Add a script located in this folder",
        2: "Parent folder",
        3: "Go in a specific folder",
        4: "Previous menu"
    }
    ## available choices for file removing
    choix_deletion_mode = {
        1: "Delete file from stack",
        2: "Previous menu"
    }

    question = "Choose an action among those : "

    ## constructor
    def __init__(self, init_root):
        super(ScriptBrowser, self).__init__()
        self.file_exec = []
        self.initial_root = init_root

    ## display script stack
    def display_stack(self):
        self.print_msg("######## Current script stack : ")
        string_to_print = "[ "
        i = 0
        while i < len(self.file_exec):
            script_object = self.file_exec[i]
            if i != 0:
                string_to_print += ", " + str(script_object)
            else:

                string_to_print += str(script_object)
            i += 1
        string_to_print += " ]"
        self.print_msg(string_to_print)

    ## launch the prompt menu
    def prompt_menu(self):
        choix_utilisateur = "-1"

        while choix_utilisateur != "3":
            self.clear_screen()
            self.display_stack()
            self.print_msg("") # saut de ligne
            choix_utilisateur = self.prompt_choice(ScriptBrowser.question, ScriptBrowser.choix_menu.itervalues())
            self.print_option_choosen(choix_utilisateur, ScriptBrowser.choix_menu)

            self.press_a_key_continue()

            # Mode : menu d'exploration de dossier et ajout de script dans la file.
            if choix_utilisateur == "1":
                self.prompt_folder_mode()
            # Mode : menu de suppression de fichier.
            if choix_utilisateur == "2":
                self.prompt_stack_deletion_mode()

    ## launch the prompter for folder selection
    def prompt_folder_mode(self):
        choix_utilisateur = "-1"
        file_explorer = CmdLineExplorer(self.initial_root)

        while choix_utilisateur != "4":
            self.clear_screen()
            self.display_stack()
            self.print_msg("\n######## Current folder : " + file_explorer.current_path)
            file_explorer.display_folder_information()
            self.print_msg("")
            choix_utilisateur = self.prompt_choice(ScriptBrowser.question, ScriptBrowser.choix_folder_mode.itervalues())
            self.print_option_choosen(choix_utilisateur, ScriptBrowser.choix_folder_mode)

            # add a script
            if choix_utilisateur == "1":
                file = self.prompt_question("Which file to stack ?")
                if file_explorer.is_in_folder(file) and file_explorer.is_a_file(file_explorer.current_path + "/" + file):
                    tool = self.prompt_question("With which tool do you want to execute this tool ?")
                    self.add_script_in_stack(file, tool, file_explorer.current_path + "/" + file)

            # go to a specific folder
            if choix_utilisateur == "3":
                folder = self.prompt_question("In which folder would you like to go into ?")
                if file_explorer.is_in_folder(folder) and file_explorer.is_a_folder(file_explorer.current_path + "/" + folder):
                    file_explorer.go_forward(folder)

            self.press_a_key_continue()

            # go back to the parent folder
            if choix_utilisateur == "2" or choix_utilisateur == "cd ..":
                file_explorer.go_backward()

    ## launch the prompter for removing file from stack
    def prompt_stack_deletion_mode(self):
        choix_utilisateur = "-1"

        while choix_utilisateur != "2":
            self.clear_screen()
            self.display_stack()
            self.print_msg("")
            choix_utilisateur = self.prompt_choice(ScriptBrowser.question, ScriptBrowser.choix_deletion_mode.itervalues())
            self.print_option_choosen(choix_utilisateur, ScriptBrowser.choix_deletion_mode)

            # the user want to remove a file
            if choix_utilisateur == "1":
                file = self.prompt_question("Which file to delete from stack ?")
                file_deleted = False
                for script in self.file_exec:
                    if script.intitule == file:
                        self.delete_scrit_from_stack(script)
                        file_deleted = True
                if not file_deleted:
                    self.print_output_msg("File hasn't been found.")
                self.press_a_key_continue()
        self.prompt_menu()

    ## add the specified script into the stack
    def add_script_in_stack(self, file_name, tool, file_full_path):
        s = Script(file_name, tool, file_full_path)
        self.file_exec.append(s)
        self.print_output_msg("Script has been added.")

    ## delete the specified script from the stack
    def delete_scrit_from_stack(self, element_object):
        self.file_exec.remove(element_object)
        self.print_output_msg("Script has been deleted.")

## test
def test():
    sbp = ScriptBrowser()
    # Options selection
    sbp.prompt_menu()
    #for script in sbp.file_exec:
    #    print script.intitule
    exe = JobExecutor()
    exe.executeScripts(sbp.file_exec, "node0")

## launch test
if __name__ == "__main__":
    test()
