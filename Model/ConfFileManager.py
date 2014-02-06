#! /usr/bin/python

# imports
import sys
from Model.Nodes import Nodes
from Tools.JobExecutor import JobExecutor
from ClusterShell.NodeSet import NodeSet
from ClusterShell.Task import task_self

##
#
class ConfFileManager:

    ## constructor (noeuds, service et action)
    def __init__(self, ns, service, action):
        # check params
        if(ns is not None and service is not None and action is not None):
            self.ns = NodeSet(ns)       
            self.service = service  
            self.action = action  # <start|stop|restart|status>
        else:
            self.ns = None
            self.service = ''
            self.action = ''
        # the service executor 
        self.executor = JobExecutor()

    ## parse the file and execute it
    def executeFromFile(self,nom_fichier):
	fichier = open(nom_fichier,'r')
        line = ''
	for ligne in fichier.readlines():
            # remove blanks
	    line = ligne.replace(' ','')
            # check if not empty => prevent parsing error
            if str(line) > 0 and line[0] != '\n' and line[0] != '#':
                # parse line 
		self.executeFromLine(line)
        # close the file
	fichier.close()

    ## parse the line and execute it
    def executeFromLine(self,line):
        # the error message to be printed
	error_len_3 = 'Error : configuration file usage is <set of services>::<set of nodes>::<action>[-> <set of services>::<set of nodes>::<action>]\n'
        # the node set
        self.ns = None
	commande = ''
	# ignore comment or empty lines
        if line == '' or line[0] == '#':
           pass
        else:
            # retrieve each block   
            for bloc_dependance in line.split('->'):
                # retrieve each item
                split = bloc_dependance.split('::')

                # parse error
                if len(split) != 3:
                   print '%s' % error_len_3
                   exit(1)
                # retrieve services, nodes and action
                services = split[0]
                nodes = split[1]
                self.action = split[2].replace('\n','')

                print '***************************************'
                print '* Handling \'%s\' *' % bloc_dependance
                print '***************************************'
                # check nodes
                nodeList = Nodes(nodes)
                nodeList.checkNodes()
                # update node list
                self.ns = nodeList.getActiveNodes()
            
                # execute each service for the specified nodes
                for service in services.split(','):
                    self.service = service
                    self.executor.executeService(self.ns, self.service, self.action)

