# coding=utf-8
'''
Created on Feb 27, 2017

@author: wlx
'''
import logging
import threading
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
            logging.info("Control client {0} ue attach".format(self._server._clientDict[address]))
            self._server._sendMessage(MESSAGE['UeAttach'], address)

    def ueDetach(self):
        for address in self._server._clientDict.keys():
            logging.info("Control client {0} ue detach".format(self._server._clientDict[address]))
            self._server._sendMessage(MESSAGE['UeDetach'], address)
