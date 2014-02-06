#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
import sys
from ClusterShell.NodeSet import NodeSet
from ClusterShell.NodeSet import NodeSetException
from Model.Nodes import Nodes
from Tools.Prompter import Prompter

##
#
class NodeBrowser(Prompter):

    ## constructor
    def __init__(self):
        self.ns = NodeSet()
        self.service = ''
        self.action = ''

    ## launch the prompt menu
    def promptMenu(self):
        try:
            # launch the prompter for node selection
            self.submitNodeList()
        # catch Ctrl + C
        except KeyboardInterrupt :
            print '\n Bye bye !\n'
            sys.exit(1)
    
    ## ask the user to submit the node list
    def submitNodeList(self):
        # info msg
        print '\n# Step 1 of 3 : Please enter nodes name below (using the clustershell syntax <azur1>, <azur[1-2]>) :' 
        # retrieve keyboard input
        try:
            self.ns = NodeSet(self.input_request(''))
            repeat = True
                
            # ask if the user wants to add another node/node group
            while repeat :
                # print added nodes
                for node in self.ns:
                    print 'node : %s' % node
                # user want to add nodes ?
                print '\n### Add nodes ? (yes | no)'
                # retrieve answer
                ans = self.input_request('')
                # check the ans
                if ans == 'Yes' or ans == 'Y' or ans == 'y' or ans == 'yes':
                   print '### Please enter the node/group list below : '
                   # retrieve and append nodes
                   self.ns.add(self.input_request(''))
                # the user don't want to add additionnal nodes
                else:
                   # unset flag
                   repeat = False
                   # check submitted nodes
                   self.ns = self.checkSubmittedNodes(self.ns)

        # invalid submitted node list / syntax error
        except NodeSetException :
            print >> sys.stderr, '\n(!) Error : the submitted node list is not valid\n' % self.ns

    ## retrieve the service to be performed
    def submitService(self):

        # specify the service
        print '\n# Step 2 of 3: Please enter the service to be launched'
        self.service = self.input_request('')
   
    ## retrieve the action to be performed
    def submitAction(self):
        # choose action to be executed
        print '\n# Step 3 of 3 : Please choose the action to perform '
        actionList = ['start','stop','restart','status']
        self.print_choice(actionList)

        # flag for the prompter
        repeat = True        
        # retrieve user's choice
        while repeat :
            # show prompter
            choice = self.input_request('')
            if choice == '1' or choice == 'start':
               self.action = 'start'
               repeat = False
            elif choice == '2' or choice == 'stop':
               self.action = 'stop'
               repeat = False
            elif choice == '3' or choice == 'restart':
               self.action = 'restart'
               repeat = False
            elif choice == '4' or choice == 'status':
               self.action = 'status'
               repeat = False
            else:
               print >> sys.stderr,'Error : invalid choice' 

    ## check and retrieves ok nodes
    def checkSubmittedNodes(self, nodes):
        # create nodeset
        ns = Nodes(nodes)
        # ping nodes
        ns.checkNodes() 
        # return active nodes
        return ns.getActiveNodes()
