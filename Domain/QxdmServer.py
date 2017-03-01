# coding=utf-8
'''
Created on Feb 27, 2017

@author: wlx
'''
import logging
logging.basicConfig(level=logging.DEBUG)
import threading

from Infrastructure.Communication.MessageRule import MESSAGE, SERVER_PORT,\
    CLIENT_PORT
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
        host = '127.0.0.1'
        logging.info('starting Server---')
        self._server = Server(host, SERVER_PORT)
        threading.Thread(target=self._server._recvMessage).start()
        self.initClientDict()
        
    def initClientDict(self):
        try:
            fileObject = open('..\/Service\/client.txt', 'r')
            fileLines = fileObject.readlines()
            fileObject.close()
            fileObject = open('..\/Service\/client.txt', 'w+')
            fileObject.truncate()
            fileObject.close()
            for fileLine in fileLines:
                if file:
                    address = (fileLine[:-2], CLIENT_PORT)
                    self._server._sendMessage(MESSAGE['ClientRegisterAgain'], address)
                    logging.info("{0} to {1}".format(MESSAGE['ClientRegisterAgain'],address))
        except Exception:
            logging.info('No record for Client')
            

    def ueAttach(self):
        for address in self._server._clientDict.keys():
            logging.info("Control client {0} ue attach".format(self._server._clientDict[address]))
            self._server._sendMessage(MESSAGE['UeAttach'], address)

    def ueDetach(self):
        for address in self._server._clientDict.keys():
            logging.info("Control client {0} ue detach".format(self._server._clientDict[address]))
            self._server._sendMessage(MESSAGE['UeDetach'], address)
