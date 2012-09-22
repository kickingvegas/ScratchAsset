#!/usr/bin/env python
#
# Copyright 2012 Yummy Melon Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Charles Y. Choi

import os
import sys
import getopt
import subprocess
import shutil

usageString = '%s -t -c <color> -b <bgcolor> -x -l' % os.path.basename(sys.argv[0])
helpString = """
-t <title>, --title=<title>                title label to render in scratch image
-c <color>, --color=<color>                color of title label (CSS or X11 color name)
-b <bgcolor>, --backgroundcolor=<bgcolor>  background color (CSS or X11 color name)
-x, --execute                              execute to create assets in the directory './scratch' 
-l, --list                                 list file name and dimension of all assets created
-h, --help                                 help
-v, --version                              version

"""

class Asset:
    def __init__(self, atype=None, width=None, height=None, filename=None, retina=True):
        self.atype = atype
        self.width = width
        self.height = height
        self.retina = retina

        if filename is None:

            if self.atype == 'itc':
                filename = '%s_screen_%dx%d.png' % (self.atype, self.width, self.height)
            else:
                filename = 'app_%s_%dx%d.png' % (self.atype, self.width, self.height)
        
        self.filename = filename
            

    def size(self):
        return (self.width, self.height)

    def stringSize(self):
        result = '%dx%d' % self.size()
        return result

class Application:
    def __init__(self):
        self.version = 1.0
        self.options = {}
        self.options['title'] = 'ScratchAsset'
        self.options['color'] = 'black'
        self.options['backgroundcolor'] = '#7CFC00'
        self.options['execute'] = False

        self.assetSpecifications = {}
        self.assetSpecifications['icon114'] = Asset('icon', 114, 114)
        self.assetSpecifications['icon57'] = Asset('icon', 57, 57)
        self.assetSpecifications['icon144'] = Asset('icon', 144, 144)
        self.assetSpecifications['icon72'] = Asset('icon', 72, 72)
        
        self.assetSpecifications['iPhone5LaunchPortrait'] = Asset('launch', 640, 1136, 'Default-568h@2x.png')
        self.assetSpecifications['iPhone4LaunchPortrait'] = Asset('launch', 640, 960, 'Default@2x.png')
        self.assetSpecifications['iPhoneLaunchPortrait'] = Asset('launch', 320, 480, 'Default.png', retina=False)
        self.assetSpecifications['iPad3LaunchPortrait'] = Asset('launch', 1536, 2008, 'Default-Portrait@2x~iPad.png')
        self.assetSpecifications['iPad3LaunchLandscape'] = Asset('launch', 2048, 1496, 'Default-Landscape@2x~iPad.png')
        self.assetSpecifications['iPadLaunchPortrait'] = Asset('launch', 768, 1004, 'Default-Portrait~iPad.png', retina=False)
        self.assetSpecifications['iPadLaunchLandscape'] = Asset('launch', 1024, 748, 'Default-Landscape~iPad.png', retina=False)
                
        self.assetSpecifications['icon58'] = Asset('small_icon', 58, 58)
        self.assetSpecifications['icon29'] = Asset('small_icon', 29, 29)
        self.assetSpecifications['icon100'] = Asset('small_icon', 100, 100)

        self.assetSpecifications['icon1024'] = Asset('icon', 1024, 1024)
        self.assetSpecifications['icon512'] = Asset('icon', 512, 512)
        
        self.assetSpecifications['itc_iPhone4'] = Asset('itc', 640, 960)
        self.assetSpecifications['itc_iPadLandscape'] = Asset('itc', 2048, 1536)
        self.assetSpecifications['itc_iPadPortrait'] = Asset('itc', 1536, 2048)

        self.assetSpecifications['itc_iPhone5Portrait'] = Asset('itc', 640, 1096)
        self.assetSpecifications['itc_iPod5Portrait'] = Asset('itc', 640, 1136)
        
        self.assetSpecifications['itc_iPhone5Landscape'] = Asset('itc', 1136, 600)
        self.assetSpecifications['itc_iPod5Landscape'] = Asset('itc', 1136, 640)


    def list(self):

        tempDict = {}
        
        for key, item in self.assetSpecifications.items():
            tempDict[item.filename] = item


        keyList = tempDict.keys()

        keyList.sort()
        for key in keyList:
            item = tempDict[key]
            sys.stdout.write('%s %s\n' % (key, item.stringSize()))

        
    def run(self, optlist, args):

        for o, i in optlist:
            if o in ('-h', '--help'):
                sys.stderr.write(usageString)
                sys.stderr.write(helpString)
                sys.exit(1)

            elif o in ('-v', '--version'):
                sys.stdout.write('%s\n' % str(self.version))
                sys.exit(0)

            elif o in ('-t', '--title'):
                self.options['title'] = i

            elif o in ('-c', '--color'):
                self.options['color'] = i
                
            elif o in ('-b', '--background'):
                self.options['backgroundcolor'] = i


            elif o in ('-x', '--execute'):
                self.options['execute'] = True

            elif o in ('-l', '--l'):
                self.list()
                sys.exit(0)
                
                
                
        if len(args) < 1:
            pass


        self.createAssets()

    def createAssets(self):

        if self.options['execute']:
            if not os.path.exists('scratch'):
                os.mkdir('scratch')

        for key, item in self.assetSpecifications.items():
            cmdList = []

            cmdList.append('convert')
            cmdList.append('-size')
            cmdList.append(item.stringSize())
            cmdList.append('xc:%s' % self.options['backgroundcolor'])
            cmdList.append('temp.png')

            #print ' '.join(cmdList)
            if self.options['execute']:
                sys.stdout.write('Generating %s\n' % item.filename)
                subprocess.call(cmdList)
            else:
                sys.stdout.write('%s\n' % ' '.join(cmdList))

            cmdList2 = []

            cmdList2.append('convert')

            if item.width > 300:
                pointSize = 20
            else:
                pointSize = 8
                
            cmdList2.append('-pointsize')
            cmdList2.append('%d' % pointSize)

            cmdList2.append('-fill')
            cmdList2.append('%s' % self.options['color'])

            if item.width > 144:
                x = item.width / 2
                y = item.height / 2
            else:
                x = 0
                y = 10
                
            draw = 'text %d,%d "%s"' % (x, y, self.options['title'])
            cmdList2.append('-draw')
            cmdList2.append('%s' % draw)

            cmdList2.append('temp.png')
            cmdList2.append(item.filename)

            #print ' '.join(cmdList2)
            if self.options['execute']:
                subprocess.call(cmdList2)
            
                if os.path.exists('scratch/%s' % item.filename):
                    os.unlink('scratch/%s' % item.filename)

                shutil.move(item.filename, 'scratch')
            
                os.unlink('temp.png')

            else:
                sys.stdout.write('%s\n' % ' '.join(cmdList2))

         
if __name__ == '__main__':

    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'hvt:c:b:xl',
                                      ('help'
                                       , 'title='
                                       , 'color='
                                       , 'backgroundcolor='
                                       , 'execute'
                                       , 'list'
                                       , 'version'))
                                       
    except getopt.error, msg:
        sys.stderr.write('ERROR: %s\n' % msg[0])
        sys.stderr.write('%s\n' % usageString)
        sys.exit(1)

    app = Application()
    app.run(optlist, args)

