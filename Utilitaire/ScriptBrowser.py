import Browser


class ScriptBrowser(Browser):
    initial_root = "/root/script/"

    def __init__(self):
        self.super().__init__(self)
        self.current_position = ScriptBrowser.initial_root

    def display_script_in_stack(self):
        # script à exécuter dans l'ordre : ...

    def choose_option(self):
        pass

    def cd_folder(self, folder):
        # os.system(cd folder) ?

    def add_script(self):
        # self.Browser.file_exec.add ...


def set_script_root_position(absolute_path):
        ScriptBrowser.initial_root = absolute_path