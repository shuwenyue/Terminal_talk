import unittest
from voice import Voice
from command import Command
from commandfactory import CommandFactory
import subprocess

class TestVoice(unittest.TestCase):
    def test_remove(self):
        v = Voice('test')
        result = v.removeExtra('this is a test from me'.split())
        assert('this is test me'.split() == result)

    def test_substitue(self):
        v = Voice('test')
        result = v.substitute('test substitution user all these'.split())
        assert('test substitution -u -a these'.split() == result)

    def test_space(self):
        v = Voice('test')
        result = v.remSpace('test 4space removal. here with _ too.'.split())
        assert('test4space removal.here with_too.'.split() == result)
        result2 = v.remSpace('5 at begin _'.split())
        assert('5 at begin_'.split() == result2)
        result3 = v.remSpace('remove at. end'.split())
        assert('remove at.end'.split() == result3)

class commandtest(unittest.TestCase):

    def commandobj(self):
        V = Voice("rm")
        factoryobj = CommandFactory(V)
        commandobj = factoryobj.getcmdobj()
        assert(commandobj.command == "rm")

    def test_init(self):
        V = Voice("copy file")
        factoryobj = CommandFactory(V)
        commandobj = factoryobj.getcmdobj()
        assert(commandobj.command == "cp")
        assert(commandobj.arg == ["file"])
    
    def test_copy(self):
        V = Voice("copy test.py test1.py")
        factoryobj = CommandFactory(V)
        commandobj = factoryobj.getcmdobj()
        runstatus = commandobj.run()
        assert(runstatus == 0)

    def test_ls(self):
        V = Voice("list")
        factoryobj = CommandFactory(V)
        commandobj = factoryobj.getcmdobj()
        runstatus = commandobj.run()
        assert(runstatus == 0)

    '''
    def test_rm(self):
        V = Voice("remove 93t84up34w98u43")
        factoryobj = CommandFactory(V)
        commandobj = factoryobj.getcmdobj()
        runstatus = commandobj.run()
        assert(runstatus == 1)
     '''

    def test_goback(self):
        V = Voice("go back")
        factoryobj = CommandFactory(V)
        commandobj = factoryobj.getcmdobj()
        runstatus = commandobj.run()
        assert(runstatus == 0)

if __name__ == '__main__':
    unittest.main()
