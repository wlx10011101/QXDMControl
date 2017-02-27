#!/usr/bin/python
# coding=utf-8
'''
Created on 20170224

@author: WLX
'''
import re
from time import ctime

from Infrastructure.Communication.MessageRule import MESSAGEREX, MESSAGE
from Infrastructure.Communication.NetUdpBase import NetUdpBase
from decimal import threading


class Server(NetUdpBase):

    def __init__(self, host, port):
        super(Server, self).__init__(host, port)
        self._clientDict = {}

    def _recvMessage(self):
        while True:
            print "waiting for recvMessage...."
            data, address = self._socket.recvfrom(1024)
            print "Time:{0}\rnMessage:{1}\rnFrom:{2}\rn".format(ctime(), data, address)
            threading.Thread(target=self.handoverMessage, args=(data, address)).start()

    def handoverMessage(self, message, address):
        reResult = re.findall(MESSAGEREX["ClientRegister"], message)
        if reResult:
            clientDict = {address: reResult[0]}
            self._clientDict.update(clientDict)
            self._sendMessage(MESSAGE["RegisterSucc"].format(clientDict[address]), address)
            print "{0} RegisterSucc\r\n".format(clientDict)
        else:
            reResult = re.findall(MESSAGEREX["ExcuteResult"], message)
            if reResult:
                if self._precheck(address):
                    print "client:{0} {1}\r\n".format(self._clientDict[address], message)
                else:
                    print "unRegister Client {0}\r\n".format(address)
            else:
                self._sendMessage("Invalid Message From {0}\r\n".format(address))

    def _precheck(self, address):
        if address in self._clientDict.keys():
            return True
        else:
            return False

if __name__ == '__main__':
    server = Server('10.9.171.151', 8088)
#     server._recvMessage()
    dict = {('10.9.220.151', 8088): 'client'}
    server._clientDict.update(dict)
    print  server._clientDict
    client1 = {('10.9.220.151', 8088): 'client22'}
    server._clientDict.update(client1)
#     print client1.values()[0] in server._clientDict.values()
    print  server._clientDict
    