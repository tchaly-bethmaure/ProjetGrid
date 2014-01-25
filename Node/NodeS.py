from ClusterShell.NodeSet import NodeSet
from ClusterShell.Task import task_self


class NodeS:
    def __init__(self, initial_nodes):
        self.set = str(initial_nodes)

    def add_nodeset(self, nodes):
        self.set_of_nodeset |= NodeSet.fromlist(nodes)

    def delete_nodeset(self, nodes):
        self.set_of_nodeset -= NodeSet.fromlist(nodes)

    def ping_nodes(self):
        task_self().run("/bin/echo OK", nodes=self.set)
        nodes_ok = NodeSet()
        nodes_nok = NodeSet()

        for retcode, nodes in task_self().iter_retcodes():
            if retcode in (0, 1, 2):
                nodes_ok |= NodeSet.fromlist(nodes)
                for node in nodes:
                    self.displayMSG(node, "OK")
            else:
                nodes_nok |= NodeSet.fromlist(nodes)
                for node in nodes:
                    self.displayMSG(node, retcode)


    def displayMSG(self, thing1, thing2):
        print(str(thing1) + " : " + str(thing2))

# Pour tester cette classe : méthode test()
def test():
    n = NodeS("127.0.0.1")
    n.ping_nodes()

if __name__ == "__main__":
    test()