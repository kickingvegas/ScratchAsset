#!/usr/bin/env python
# Copyright 2012 Yummy Melon Software
# Author: Charles Y. Choi

import os
import sys
import getopt
import subprocess
import shutil


usageString = '%s ...' % os.path.basename(sys.argv[0])
helpString = """
-h, --help                help
-v, --version             version

"""

class Application:
    def __init__(self):
        self.version = 1.0
        self.options = {}
        
        
    def run(self, optlist, args):
        sys.stdout.write('hello, world...\n')

        for o, i in optlist:
            if o in ('-h', '--help'):
                sys.stderr.write(usageString)
                sys.stderr.write(helpString)
                sys.exit(1)

            elif o in ('-v', '--version'):
                sys.stdout.write('%s\n' % str(self.version))
                sys.exit(0)
                
        if len(args) < 1:
            pass

        cmdList = ['ls', '-al']
        subprocess.call(cmdList)


         
if __name__ == '__main__':

    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'hv',
                                      ('help',
                                       'version'))
    except getopt.error, msg:
        sys.stderr.write(msg + '\n')
        sys.stderr.write(usageString)
        sys.exit(1)

    
    app = Application()
    app.run(optlist, args)

    
