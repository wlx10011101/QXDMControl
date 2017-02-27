'''
Created on Feb 27, 2017

@author: wlx
'''
import psutil

from Infrastructure.Application.QXDM import QXDM
from Infrastructure.Communication import Client


class QxdmClient(object):
    '''
    classdocs
    '''
    def __init__(self):
        self._initQxdm()
        self._initClient()
        
    def _initClient(self):
        host = raw_input("please input client IP: ")
        port = 8088
        name = raw_input("please input client name: ")
        serverHost = raw_input("please input server IP: ")
        serverPort = 8088
        client = Client(host, port, name)
        if client.registerClient(serverHost, serverPort):
            client._recvMessage()
    
    def _initQxdm(self):
        qxdmPath = raw_input("please input the absolutepath of QXDM.exe: ")
        for process in psutil.process_iter():
            if process.name().upper() == "QXDM.EXE":
                if name in process.cmdline():
                    qxdmPid = process.pid
                    qxdm = QXDM(qxdmPath, qxdmPid)
                    qxdm._connectApp()
        else:
            qxdm = QXDM(qxdmPath)
            qxdm._startApp()
                    

if __name__ == "__main__":
    host = raw_input("please input client IP: ")
    port = 8088
    name = raw_input("please input client name: ")
    serverHost = raw_input("please input server IP: ")
    serverPort = 8088
    print host, port, name, serverHost, serverPort
    