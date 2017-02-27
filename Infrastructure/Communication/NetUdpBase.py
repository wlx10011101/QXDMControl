# coding=utf-8
'''
Created on 20170224

@author: WLX
'''
import socket
ALL_IP_OF_HOST = '0.0.0.0'


class NetUdpBase(object):

    def __init__(self, host, port):
        '''
        Constructor
        '''
        self._host = host
        self._port = port
        self._address = (self._host, self._port)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(ALL_IP_OF_HOST, self._port)

    def _recvMessage(self):
        raise "NotImpletementERROR"

    def _sendMessage(self, message, address):
        self._socket.sendto(message, address)
