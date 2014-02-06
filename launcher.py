#! /usr/bin/python

import sys
from View.IHM import IHM

if __name__ == '__main__':

    # instantiate the GUI
    view = IHM()

    # check params and launch the appropriate mode
    if len(sys.argv) == 5 and (sys.argv[1] == '-s' or sys.argv[1] == '--static'):
        # launch static mode
        view.staticMode(sys.argv[2], sys.argv[3], sys.argv[4])

    elif len(sys.argv) == 3 and sys.argv[1] == '-f':
        # launch conf mode
        view.fileConfigMode(sys.argv[2])

    elif len(sys.argv) == 2 and sys.argv[1] == '-i':
        # launch interactive mode
        view.interactiveMode()

    elif len(sys.argv) == 2 and sys.argv[1] == '-fi':
        # launch full interactive mode
        view.fullInteractiveMode()

    else:
        view.displayErrorMsg()
