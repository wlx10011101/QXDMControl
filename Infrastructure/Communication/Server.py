# coding=utf-8
'''
Created on 20170224

@author: WLX
'''
from Infrastructure.Communication.NetUdpBase import NetUdpBase


class Server(NetUdpBase):

    def __init__(self, host, port):
        super(self, Server).__init__(host, port)

    def _recvMessage(self):
        pass

    def _sendMessage(self, message, host, port):
        pass
