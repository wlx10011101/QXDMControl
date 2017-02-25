# coding=utf-8
'''
Created on 20170224

@author: WLX
'''
from Infrastructure.Communication.NetUdpBase import NetUdpBase


class Client(NetUdpBase):
    '''
    Client for communication
    '''

    def __init__(self, host, port, name):
        '''
        Constructor
        '''
        super(self, Client).__init__(host, port)
        self._name = name

    def _recvMessage(self):
        pass

    def _sendMessage(self, message, host, port):
        pass
