
## class for handling scripts
#
class Script(object):

    ## constructor
    def __init__(self, nom_script, tool_script, chemin_fichier):
        super(Script,self).__init__()
        # script name
        self.intitule = nom_script
        # tool
        self.tool = tool_script
        # script path
        self.path = chemin_fichier
    
    ## get script name
    def __str__(self):
        return self.intitule

    ## get script path
    def get_file_with_path(self):
        return self.path
