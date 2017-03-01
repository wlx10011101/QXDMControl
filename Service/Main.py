# coding=utf-8
'''
Created on 20170228

@author: WLX
'''
from Domain.QxdmClient import QxdmClient
from Domain.QxdmServer import QxdmServer


class MainService(object):
    
    def __init__(self):
        self.separator = '-----------------------------\r\n'
    
    
    def _printNote(self):
        notes = ['This Application is just for',
                'sending the command to QXDM',
                'that can control UE attach', 
                'and detach',]
        function = '*please start Server First!*\r\n'
        print self.separator,
        for note in notes:
            print note
        print self.separator, function
    
    def _initApp(self):
        print "1.start Client"
        print "2.start Server"
        qxdmType = raw_input("which one?: ")
        if qxdmType == "1":
            self._clientService = QxdmClient()
        elif qxdmType == "2":
            self._ServerService = QxdmServer()
            self._controlUe()
        else:
            print "Invalid Input"
    
    def _controlUe(self):
        notes = ["Now plese make sure ue connected QXDM",
                 "then you can send command to UE"]
        ueControlNotes = ["1.UE attach;2.UE detach"]
        print self.separator
        for note in notes:
            print note
            
        print ueControlNotes
        while True:
            action = raw_input("your action: ")
            if action == "1":
                self._ServerService.ueAttach()
            elif action == "2":
                self._ServerService.ueDetach()
            else:
                print "Invalid Input"

def main():
    service = MainService()
    service._printNote()
    service._initApp()
if __name__ == '__main__':
    main()
