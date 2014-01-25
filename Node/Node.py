import os


class Node():
    def __init__(self, name, ipv4, ipv6, macadress):
        self.name = name
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.mac = macadress

    def is_awake(self):
        reponse = os.system("ping -c 1 " + str(self.ipv4) + " > temp")
        os.system("rm temp")
        if reponse == 0:
            return True
        else:
            return False

    def ping(self):
        if self.is_awake():
            print(self.name + " : OK")
        else:
            print(self.name + " : KO")

# Pour tester cette classe : methode test()
def test():
    n = Node("tchaly","127.0.0.1","lol","lol")
    n.ping()

if __name__ == "__main__":
    test()