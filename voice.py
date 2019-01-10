class Voice:
    
    cmdDict = {'copy' : 'cp',
            'cp' : 'cp',
            'move' : 'mv',
            'rename' : 'mv',
            'make directory' : 'mkdir',
            'list' : 'ls',
            'ls' : 'ls',
            'remove' : 'rm',
            'change directory' : 'cd',
            'cd' : 'cd',
            'search' : 'grep',
            'ssh' : 'ssh',
            'python' : 'python',
            'bash' : 'bash',
            'run' : 'bash',
            'go back' : 'cd ..',
            'print directory' : 'pwd',
            'pwd' : 'pwd',
            'open' : 'open',
            'say' : 'say',
            'touch' : 'touch'} #Dictionary of commands
    subsDict = {'user' : '-u',
            'all' : '-a',
            'recursively' : '-r',
            'underscore' : '_',
            'star' : '*',
            'asterisk' : '*'} #Dictionary of word substitutions
    toRem = {'to', 'the', 'a', 'from', 'for'} #Set of words to remove

    # Reads in string
    def __init__(self, command):
        self.cmdStr = self.removeExtra(command.split())
        self.argInd = 0

    # Returns command as string
    def getcommand(self):
        try:
            cmd = self.cmdDict[self.cmdStr[0]]
            self.argInd = 1
            return cmd
        except KeyError:
            try:
                cmd = self.cmdDict[self.cmdStr[0]+' '+self.cmdStr[1]]
                self.argInd = 2
                return cmd
            except (KeyError, IndexError) as e:
                raise ValueError
    
    # Returns arguments as list
    def getarg(self):
        if self.argInd == 0:
            self.getcommand()
        if len(self.cmdStr) == self.argInd:
            return []
        args = self.cmdStr[self.argInd:]
        arg2 = self.substitute(args)
        arg3 = self.remSpace(arg2)
        return arg3

    # Removes superfluous words
    def removeExtra(self, argList):
        return [arg for arg in argList if arg not in self.toRem]

    # Substitutes for words
    def substitute(self, argList):
        for i in range(len(argList)):
            try:
                argList[i]=self.subsDict[argList[i]]
            except:
                pass
        return argList

    # Remove space after periods, before numbers, and before and after underscore
    def remSpace(self, argList):
        i = 0
        while i < len(argList):
            if argList[i][-1] == '.' and i+1 < len(argList):
                # Combine with next
                argList[i:i+2] = [''.join(argList[i:i+2])]
            elif self.checkNum(argList[i][0]) and i > 0:
                # Combine with previous
                argList[i-1:i+1] = [''.join(argList[i-1:i+1])]
            elif argList[i] == '_' and i > 0 and i+1 < len(argList):
                # Combine with next and previous
                argList[i-1:i+2] = [''.join(argList[i-1:i+2])]
            elif argList[i] == '_' and i > 0:
                # Combine with previous
                argList[i-1:i+1] = [''.join(argList[i-1:i+1])]
            elif argList[i] == '_':
                # Combine with next
                argList[i:i+2] = [''.join(argList[i:i+2])]
            else:
                i += 1
        return argList

    # Check if string is number
    def checkNum(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False
