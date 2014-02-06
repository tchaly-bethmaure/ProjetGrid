#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
import sys
from ClusterShell.NodeSet import NodeSet
from ClusterShell.Task import task_self
from ClusterShell.NodeSet import NodeSetException

##
#
class Nodes:

    ## initialize the object
    def __init__(self, nodeset):
        # the node set
        self.ns = nodeset
        # active nodes
        self.ns_ok = NodeSet()
        # inactive or inexisting nodes
        self.ns_ko = NodeSet()
    
    ## add the specified node
    def add(self, node):
        self.ns |= NodeSet.fromlist(node)

    ## delete the specified node
    def delete(self, node):
        self.ns -= NodeSet.fromlist(node)

    ## check if the submitted nodes are active
    def checkNodes(self):
        try:
           # print command info
           print '\n== Checking active nodes =='
           # launch ping on the specified nodes
           task_self().run('echo OK', nodes=self.ns)
           # retrieve and check return code
           for retcode, nodes in task_self().iter_retcodes():
               if retcode in (0, 1, 2):
                   # add nodes to OK set
                   self.ns_ok |= NodeSet.fromlist(nodes)
                   print '%s : OK' % nodes
               else:
                   # add nodes to KO set
                   self.ns_ko |= NodeSet.fromlist(nodes)
                   print '%s : KO' % nodes
        # syntax error
        except NodeSetException:
            print >> sys.stderr, '(!) Error : the submitted nodeset [%s] is not valid' % self.ns

    ## get all submitted nodes (include invalid)
    def getAllNodes(self):
        return self.ns

    ## retrieve the active nodes    
    def getActiveNodes(self):
        return self.ns_ok

## check and retrieve active nodes
def filter_disfunctional_nodes(ns):
    n = Nodes(ns)
    n.checkNodes()
    return n.getActiveNodes()

