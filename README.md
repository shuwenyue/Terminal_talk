
-------------
Description
-------------

This python package allows users to access command line tools using 
voice control.  Users can voice commands using natural language to 
manage files, maneuver around directories, and run scripts. A complete 
list of speech commands is listed below, along with their corresponding 
terminal commands. Furthermore, extending this program to include 
additional commands is straightforward to carry out. Enjoy!

Created by Shuwen Yue and Jeffrey Young for HackPrinceton2018

------------------------
Requirements
------------------------
SpeechRecognition
portaudio
pyaudio
os
subprocess

------------------------
Run using command line
------------------------
To run, type
python main.py

To exit, say
exit, quit, stop

------------------------
Possible voice commands
------------------------
terminal command - voice command
cp - copy, cp
mv - move, rename
mkdir - make directory
ls - list, ls
rm - remove
cd - change directory, cd
cd .. - go back
grep - search
python - python
bash - bash, run
pwd - print directory, pdw
open - open
say - say

------------------------
Possible flags
------------------------
flag - voice command
-u - user
-a - all
-r - recursively

------------------------
Ignored words
------------------------
to
the
a
from
for

------------------------
Extending commands
------------------------
A simple command with any number of arguments can be easily added by 
matching it with a corresponding voice command (up to two words) in the
dictionary in voice.py. More complex commands can be added by 
extenending the Command class in command.py.
