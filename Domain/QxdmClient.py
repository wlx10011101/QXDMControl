# coding=utf-8
'''
Created on Feb 27, 2017

@author: wlx
'''
import Queue
import psutil
import re
import threading

from Domain.QxdmCmd import UE
from Infrastructure.Application.QxdmApp import QXDM
from Infrastructure.Communication.Client import Client
from Infrastructure.Communication.MessageRule import MESSAGEREX, MESSAGE,\
    CLIENT_PORT, SERVER_PORT


class QxdmClient(object):
    '''
    classdocs
    '''
    def __init__(self):
        self._dataQueue = Queue.Queue
        self._addrQueue = Queue.Queue
        while(not self._initQxdm()):pass
        while(not self._initClient()):pass

    def _initClient(self):
        host = '127.0.0.1'
        name = raw_input("please input client name: ")
        serverHost = raw_input("please input server IP: ")
        self._client = Client(host, CLIENT_PORT, name)
        if self._client.registerClient(serverHost):
            threading.Thread(target=self._client._recvMessage, args=(self._dataQueue, self._addrQueue)).start()
            threading.Thread(target=self.handoverMessage).start()
            return True
        else:
            return False

    def _initQxdm(self):
        qxdmPath = raw_input("please input the absolutepath of QXDM.exe: \n")
        qxdmPath = self._pathFormat(qxdmPath)
        for process in psutil.process_iter():
            if process.name().upper() == "QXDM.EXE":
                if qxdmPath == self._pathFormat(process.cmdline()[0]):
                    qxdmPid = process.pid
                    self._qxdm = QXDM(qxdmPath, qxdmPid)
                    return self._qxdm._connectApp()
        else:
            self._qxdm = QXDM(qxdmPath)
            return self._qxdm._startApp()

    def handoverMessage(self):
        while True:
            if not self._dataQueue.empty():
                message = self._dataQueue.get()
                address = self._addrQueue.get()
                reResult = re.findall(MESSAGEREX['QxdmCmd'], message)
                
                if re.findall(MESSAGEREX['ClientRegisterAgain'], message):
                    self._client._sendMessage(MESSAGE["ClientRegister"].format(self._client._name), (address, SERVER_PORT))
                elif message == MESSAGE["RegisterSucc"].format(self._name):
                    pass
                elif reResult:
                    self._qxdm.sendCommand(UE[reResult[0].upper()])
                    self._client._sendMessage(MESSAGE["ExcuteResult"].format("Success"), (address, SERVER_PORT))
                else: 
                    self._client._sendMessage(MESSAGE["ExcuteResult"].format("Fail"), (address, SERVER_PORT))

                

    def _pathFormat(self, path):
        return '\\\\'.join(path.split('\\'))

if __name__ == "__main__":
#     host = raw_input("please input client IP: ")
#     port = 8088
#     name = raw_input("please input client name: ")
#     serverHost = raw_input("please input server IP: ")
#     serverPort = 8088
#     print host, port, name, serverHost, serverPort
    qxdmPath = "C:\Program Files\Qualcomm\QxdmApp\Bin\QxdmApp.exe"
    print '\\\\'.join(qxdmPath.split('\\'))