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


class Server(NetUdpBase):

    def __init__(self, host, port):
        super(self, Server).__init__(host, port)
        self._clientAddrList = []

    def _recvMessage(self):
        while True:
            print "waiting for recvMessage"
            data, address = self._socket.recvfrom(1024)
            print "Time:{0}\rMessage:{1}\rFrom:{2}\r".format(ctime(), data, address)
            self.handoverMessage(data, address)
#             handover the message

#     def _sendMessage(self, message, host, port):
#         pass
    
    def handoverMessage(self, message, address):
        client = re.findall(MESSAGEREX["ClientRegister"], message)
        if client:
            clientDict = {'name': client[0], 'addr': address}
            self._clientAddrList.append(clientDict)
            self._sendMessage(MESSAGE["RegisterSucc"].format(clientDict['name']), address)
        

if __name__ == '__main__':
    server = Server('10.9.171.151', 8088)
    server._recvMessage()
