# Scratch Asset

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

<table>
<tr><td>Default-568h@2x.png</td><td>640x1136</td></tr>
<tr><td>Default-Landscape@2x~iPad.png</td><td>2048x1496</td></tr>
<tr><td>Default-Landscape~iPad.png</td><td>1024x748</td></tr>
<tr><td>Default-Portrait@2x~iPad.png</td><td>1536x2008</td></tr>
<tr><td>Default-Portrait~iPad.png</td><td>768x1004</td></tr>
<tr><td>Default.png</td><td>320x480</td></tr>
<tr><td>Default@2x.png</td><td>640x960</td></tr>
<tr><td>app_icon_1024x1024.png</td><td>1024x1024</td></tr>
<tr><td>app_icon_114x114.png</td><td>114x114</td></tr>
<tr><td>app_icon_144x144.png</td><td>144x144</td></tr>
<tr><td>app_icon_512x512.png</td><td>512x512</td></tr>
<tr><td>app_icon_57x57.png</td><td>57x57</td></tr>
<tr><td>app_icon_72x72.png</td><td>72x72</td></tr>
<tr><td>app_small_icon_100x100.png</td><td>100x100</td></tr>
<tr><td>app_small_icon_29x29.png</td><td>29x29</td></tr>
<tr><td>app_small_icon_58x58.png</td><td>58x58</td></tr>
<tr><td>itc_screen_1136x600.png</td><td>1136x600</td></tr>
<tr><td>itc_screen_1136x640.png</td><td>1136x640</td></tr>
<tr><td>itc_screen_1536x2048.png</td><td>1536x2048</td></tr>
<tr><td>itc_screen_2048x1536.png</td><td>2048x1536</td></tr>
<tr><td>itc_screen_640x1096.png</td><td>640x1096</td></tr>
<tr><td>itc_screen_640x1136.png</td><td>640x1136</td></tr>
<tr><td>itc_screen_640x960.png</td><td>640x960</td></tr>
</table>


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








