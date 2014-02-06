#! /usr/bin/python

# imports
import os
import sys
from Model.Nodes import Nodes
from Model.ConfFileManager import ConfFileManager
from Tools.ScriptBrowser import ScriptBrowser
from Tools.NodeBrowser import NodeBrowser
from Tools.Prompter import Prompter
from Tools.JobExecutor import JobExecutor

##
#
class IHM(Prompter):

    ## constructor
    def __init__(self):
        # the task executor
        self.exe = JobExecutor()

    ## a GUI for static mode execution
    def staticMode(self, nodes, service, action):
        # check and retrieve active nodes
        ns = Nodes(nodes)
        ns.checkNodes()
        ns_ok = ns.getActiveNodes()

        # execute the specified service
        self.exe.executeService(ns_ok, service, action)

    ## a GUI for conf file processing and execution
    def fileConfigMode(self, fileName):
        # instantiate the conf file manager
        s = ConfFileManager(None, None, None)
        try:
            # launch it
            s.executeFromFile(fileName)
        # catch Ctrl + C
        except KeyboardInterrupt :
            print '\n Bye bye !\n'
            sys.exit(1)

    ## a GUI for nodes and service browsing and execution
    def interactiveMode(self):
        # clear screen
        os.system('clear')
        print '\n== Welcome to Clustershell ! =='

        # browse node
        nbp = NodeBrowser()
        nbp.promptMenu()

        # browse service and action
        nbp.submitService()
        nbp.submitAction()
        
        # retrieve active nodes and execute
        self.exe.executeService(nbp.ns, nbp.service, nbp.action) 

    ## a GUI for scripts browsing and execution
    def fullInteractiveMode(self):
        # clear screen
        os.system('clear')
        print '\n== Welcome to Clustershell ! =='

        # browse nodes
        nbp = NodeBrowser()
        nbp.promptMenu()
       
        try:
            # browse script
            sbp = ScriptBrowser(self.prompt_question("Script root folder ?"))
            sbp.prompt_menu()
        # catch Ctrl + C
        except KeyboardInterrupt :
            print '\n Bye bye !\n'
            sys.exit(1)

        # execute the script to the specified nodes
        self.exe.executeScripts(sbp.file_exec, nbp.ns)

    ## display error msg if invalid arguments
    def displayErrorMsg(self):
  
        print >> sys.stderr,'\n== Error : invalid arguments =='
        print >> sys.stderr,'=> Right syntax for static mode           : python Launcher.py -s <nodeset> <service> <action>'
        print >> sys.stderr,'=> Right syntax for conf file mode        : python Launcher.py -f <filename>'
        print >> sys.stderr,'=> Right syntax for interactive mode      : python Launcher.py -i'
        print >> sys.stderr,'=> Right syntax for full interactive mode : python Launcher.py -fi'
        exit(1)

