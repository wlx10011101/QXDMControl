# coding=utf-8
'''
Created on Feb 27, 2017

@author: wlx
'''
import re

import psutil

from Domain.QxdmCmd import UE
from Infrastructure.Application.QXDM import QXDM
from Infrastructure.Communication import Client
from Infrastructure.Communication.MessageRule import MESSAGEREX, MESSAGE


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
        self._client = Client(host, port, name)
        if self._client.registerClient(serverHost, serverPort):
            self._client._recvMessage()

    def _initQxdm(self):
        qxdmPath = raw_input("please input the absolutepath of QXDM.exe: ")
        for process in psutil.process_iter():
            if process.name().upper() == "QXDM.EXE":
                if qxdmPath in process.cmdline():
                    qxdmPid = process.pid
                    self._qxdm = QXDM(qxdmPath, qxdmPid)
                    self._qxdm._connectApp()
        else:
            self._qxdm = QXDM(qxdmPath)
            self._qxdm._startApp()

    def handoverMessage(self):
        while not self._client._dataQueue.empty():
            message = self._client._dataQueue.get()
            address = self._client._addrQueue.get()
            reResult = re.findall(MESSAGEREX['QxdmCmd'], message)
            if reResult:
                self._qxdm.sendCommand(UE[reResult[0].upeer()])
                self._client._sendMessage(MESSAGE["ExcuteResult"].format("Success"))
            else:
                self._client._sendMessage(MESSAGE["ExcuteResult"].format("Falure"))

if __name__ == "__main__":
    host = raw_input("please input client IP: ")
    port = 8088
    name = raw_input("please input client name: ")
    serverHost = raw_input("please input server IP: ")
    serverPort = 8088
    print host, port, name, serverHost, serverPort
