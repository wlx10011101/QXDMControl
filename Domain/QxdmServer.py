# coding=utf-8
'''
Created on Feb 27, 2017

@author: wlx
'''
from decimal import threading
from time import ctime

from Infrastructure.Communication.MessageRule import MESSAGE
from Infrastructure.Communication.Server import Server


class QxdmServer(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._initServer()

    def _initServer(self):
        host = raw_input("please input server IP: ")
        port = 8088
        self._server = Server(host, port)
        threading.Thread(target=self._server._recvMessage).start()

    def ueAttach(self):
        for address in self._server._clientDict.keys():
            print "Time:{0}\r\nControl client {1} ue attach\r\n".format(ctime(), self._server._clientDict[address])
            self._server._sendMessage(MESSAGE['UeAttach'], address)

    def ueDettach(self):
        for address in self._server._clientDict.keys():
            print "Time:{0}\r\nControl client {1} ue dettach\r\n".format(ctime(), self._server._clientDict[address])
            self._server._sendMessage(MESSAGE['UeDettach'], address)