import command as cm

class CommandFactory():

    # constructor takes in voice object 
    def __init__(self,voiceobj):
        self.command = voiceobj.getcommand()
        self.arg = voiceobj.getarg()
 
    def getcmdobj(self):
        if self.command == "rm":
            return cm.rm(self.command,self.arg) #returns instance of class    
        if self.command == "cd":
            return cm.cd(self.command,self.arg) #returns instance of class    
        if self.command == "cd ..":
            return cm.cdback(self.command,self.arg) #returns instance of class    
        if self.command == "grep":
            return cm.grep(self.command,self.arg)
        else:
            return cm.Command(self.command,self.arg) #returns instance of class  

