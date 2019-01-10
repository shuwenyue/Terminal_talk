import subprocess
import os
import speech_recognition as sr

class Command:

    # constructor takes in voice object 
    def __init__(self,command,arg):
        self.command = command
        self.arg = arg

    # run function takes in command and arguments, runs process, returns exit status
    def run(self):
        print (self.command + ' ' + ' '.join(self.arg))
        exit = subprocess.run([self.command]+self.arg)
        return exit.returncode


class rm(Command):

    def run(self):
        r = sr.Recognizer()
        mic = sr.Microphone()
        print (self.command + ' ' + ' '.join(self.arg))
        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                print('Are you sure you want to remove', self.command + ' ' + ' '.join(self.arg),'?')
                audio = r.listen(source)
            try:
                cmdString = r.recognize_google(audio).lower()
                print(cmdString)
                if cmdString == 'yes':
                    print(self.command + ' ' + ' '.join(self.arg), 'removed')
                    exit = subprocess.run([self.command]+self.arg)
                    returncode = exit.returncode
                    break
                if cmdString == 'no':
                    print(self.command + ' ' + ' '.join(self.arg), 'NOT removed')
                    returncode = 0
                    break
            except:
                print('Could not understand, try again')

        return returncode

class cd(Command):
    def run(self):
        print (self.command + ' ' + ' '.join(self.arg))
        if len(self.arg) == 1:
            try:
                os.chdir(self.arg[0])
            except FileNotFoundError:
                raise ValueError
        elif len(self.arg) == 0:
            os.chdir(os.path.expanduser("~/"))
        else:
            raise ValueError
        return 0

class cdback(cd):
    def __init__(self,command,arg):
        if arg != []:
            raise ValueError
        self.command = "cd"
        self.arg = [".."]


class grep(Command):
    def __init__(self,command,arg):
        if len(arg) != 2:
            raise ValueError
        self.command = command
        self.arg = arg



