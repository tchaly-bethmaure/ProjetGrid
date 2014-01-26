import Prompter


class ScriptBrowsePrompter(Prompter):
    def __init__(self):
        self.super().__init__(self)

    def prompt_option(self):
    # charger un script dans la stack, supprimer un script de la stack,
    # aller dans un dossier, revenir au dossier parent, etape suivante (node to execute on)

