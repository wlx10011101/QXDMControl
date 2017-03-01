#!/usr/bin/python
# coding=utf-8
'''
Created on 20170224

@author: WLX
'''
import logging
import re
import threading

from Infrastructure.Communication.MessageRule import MESSAGEREX, MESSAGE, \
    CLIENT_PORT, SERVER_PORT, ALL_IP_OF_HOST
from Infrastructure.Communication.NetUdpBase import NetUdpBase


logging.basicConfig(level=logging.DEBUG)


class Server(NetUdpBase):

    def __init__(self, host, port):
        super(Server, self).__init__(host, port)
        self._clientDict = {}
        self._socket_recv.bind((ALL_IP_OF_HOST, SERVER_PORT))
        self._socket_send.bind((ALL_IP_OF_HOST, CLIENT_PORT))
    def _recvMessage(self):
        while True:
            logging.info("waiting for recvMessage---")
            data, address = self._socket_recv.recvfrom(1024)
            logging.info("Message:{0} From:{1}".format(data, address[0]))
            threading.Thread(target=self.handoverMessage, args=(data, address[0])).start()

    def handoverMessage(self, message, hostIP):
        reResult = re.findall(MESSAGEREX["ClientRegister"], message)
        clientAddr = (hostIP, CLIENT_PORT)
        if reResult:
            clientDict = {clientAddr: reResult[0]}
            if clientAddr not in self._clientDict.keys():
                self._recordTxt(hostIP)
            self._clientDict.update(clientDict)
            self._sendMessage(MESSAGE["RegisterSucc"].format(clientDict[(hostIP, CLIENT_PORT)]), clientAddr)
            logging.info("{0} RegisterSucc".format(clientDict))
        else:
            reResult = re.findall(MESSAGEREX["ExcuteResult"], message)
            if reResult:
                if self._precheck(hostIP):
                    logging.info("client:{0} {1}".format(self._clientDict[(hostIP, CLIENT_PORT)], message))
                else:
                    logging.info("unRegister Client {0}".format(hostIP))
            else:
                self._sendMessage("Invalid Message From {0}".format(hostIP))

    def _precheck(self, host):
        if (host, CLIENT_PORT) in self._clientDict.keys():
            return True
        else:
            return False
        
    def _recordTxt(self, host):
        fileObject = open('client.txt','a')
        fileObject.write(host+'\r\n')
        fileObject.close()

if __name__ == '__main__':
#     server = Server('10.9.171.151', 8088)
# #     server._recvMessage()
# #     dict = {('10.9.220.151', 8088): 'client'}
#     server._clientDict.update(dict)
#     print  server._clientDict
    address = ('10.9.220.151', 8088)
    print address[0]
    address1 = '10.9.222.111'
    client1 = {('10.9.220.151', 8088): 'client22'}
#     server._clientDict.update(client1)
# #     print client1.values()[0] in server._clientDict.values()
#     print  server._clientDict
    fileObject = open('client.txt','a')
    fileObject.writelines(address[0]+'\r\n')
    fileObject.write(address1+'\r\n')
    fileObject.close()
    fileObject = open('client.txt','a')
    fileObject.write(address1+'\r\n')
    fileObject.close()
    