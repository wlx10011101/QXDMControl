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
#             self.handoverMessage(data, address)
#             handover the message

#     def _sendMessage(self, message, host, port):
#         pass
    
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
                print "client:{0} {1}".format(self._clientDict[address], message)
            else:
                self._sendMessage("Invaild Message", address)
        

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
    