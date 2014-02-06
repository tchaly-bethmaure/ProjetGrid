#! /usr/bin/python

# imports
from ClusterShell.NodeSet import NodeSet
from ClusterShell.Task import task_self
from Tools.Prompter import Prompter

## class for executing commands
#
class JobExecutor(Prompter):

    ## constructor
    def __init__(self):
        # task launcher
        self.task = task_self()

    ## execute a service
    def executeService(self, ns, service, action):
        # set command
        command = 'service ' + service + ' ' + action

        # print info message
        if action == 'start':
            print '\n== Launching \'%s\' on [%s] ==' % (service, ns)
        elif action == 'stop':
            print '\n== Stopping \'%s\' on [%s] ==' % (service, ns)
        elif action == 'restart':
            print '\n== Restarting \'%s\' on [%s] ==' % (service, ns)
        elif action == 'status':
            print '\n== Get status of \'%s\' on [%s] ==' % (service, ns)
        else:
            print 'Error : <action> must be start | stop | restart | status'
            exit(1)

        # run command
        self.task.run(command, nodes=ns)

        # handling output
        for output, nodes in self.task.iter_buffers():
            # agregate and print output
            print '%s : %s' % (nodes, output)
        # print blank line
        print ''

    ## execute the stack of jobs
    def executeScripts(self, stack, nodes):
        for job in stack:
            self.task.run(job.tool + " " + job.path, nodes=nodes)

            # handling output
            for output, nodes in self.task.iter_buffers():
                # agregate and print output
                print '%s : %s' % (nodes, output)
