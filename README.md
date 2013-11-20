# Scratch Asset 2.0

A utility to generate scratch image assets for an iOS project and its corresponding iTunes Connect app submission. 

## Requirements

Python, ImageMagick tools


## Installation

To install edit the `INSTALL` path to your preference in the `Makefile` and run the following command:

        $ make install

## Quick Start

        $ scratchasset -x -t 'My App Name' -c blue -b orange
	
## Help

        $ scratchasset -h

# Assets Created

When the utility is executed, the following files are generated in the directory `scratch` that is placed in the current directory.

## iOS 7 Assets

The following assets are generated to support the specification listed in:

<https://developer.apple.com/library/ios/documentation/userexperience/conceptual/mobilehig/IconMatrix.html#//apple_ref/doc/uid/TP40006556-CH27-SW1>

<https://developer.apple.com/library/ios/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/8_AddingNewApps/AddingNewApps.html#//apple_ref/doc/uid/TP40011225-CH13-SW42>

| Image Name               | Resolution |
| :--                      |        :-- |
| app_icon_1024x1024.png   |  1024x1024 |
| app_icon_120x120.png     |    120x120 |
| app_icon_152x152.png     |    152x152 |
| app_launch_1024x768.png  |   1024x768 |
| app_launch_1536x2048.png |  1536x2048 |
| app_launch_2048x1536.png |  2048x1536 |
| app_launch_640x1136.png  |   640x1136 |
| app_launch_640x960.png   |    640x960 |
| app_launch_768x1024.png  |   768x1024 |
| app_settings_58x58.png   |      58x58 |
| app_spotlight_40x40.png  |      40x40 |
| app_spotlight_80x80.png  |      80x80 |
| itc_screen_1024x748.png  |   1024x748 |
| itc_screen_1136x600.png  |   1136x600 |
| itc_screen_1536x2008.png |  1536x2008 |
| itc_screen_2048x1496.png |  2048x1496 |
| itc_screen_640x1096.png  |   640x1096 |
| itc_screen_640x920.png   |    640x920 |
| itc_screen_768x1004.png  |   768x1004 |
| itc_screen_960x600.png   |    960x600 |


## iOS 6 Assets

| Image Name                    | Resolution |
| :--                           |        :-- |
| Default-568h@2x.png           |   640x1136 |
| Default-Landscape@2x~iPad.png |  2048x1496 |
| Default-Landscape~iPad.png    |   1024x748 |
| Default-Portrait@2x~iPad.png  |  1536x2008 |
| Default-Portrait~iPad.png     |   768x1004 |
| Default.png                   |    320x480 |
| Default@2x.png                |    640x960 |
| app_icon_1024x1024.png        |  1024x1024 |
| app_icon_114x114.png          |    114x114 |
| app_icon_144x144.png          |    144x144 |
| app_icon_512x512.png          |    512x512 |
| app_icon_57x57.png            |      57x57 |
| app_icon_72x72.png            |      72x72 |
| app_small_icon_100x100.png    |    100x100 |
| app_small_icon_29x29.png      |      29x29 |
| app_small_icon_58x58.png      |      58x58 |
| itc_screen_1136x600.png       |   1136x600 |
| itc_screen_1136x640.png       |   1136x640 |
| itc_screen_1536x2048.png      |  1536x2048 |
| itc_screen_2048x1536.png      |  2048x1536 |
| itc_screen_640x1096.png       |   640x1096 |
| itc_screen_640x1136.png       |   640x1136 |
| itc_screen_640x960.png        |    640x960 |

## License

Copyright 2012 Yummy Melon Software LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author: Charles Y. Choi <charles.choi@yummymelon.com>








