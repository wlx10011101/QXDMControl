# coding=utf-8
'''
Created on 20170224

@author: WLX
'''
import socket


class NetUdpBase(object):

    def __init__(self, host, port):
        '''
        Constructor
        '''
        self._host = host
        self._port = port
        self._address = (self._host, self._port)
        self._socket_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def _recvMessage(self):
        raise "NotImpletementERROR"

    def _sendMessage(self, message, address):
        self._socket_send.sendto(message, address)
