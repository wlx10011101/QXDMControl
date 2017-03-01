# coding=utf-8
'''
Created on 20170224

@author: WLX
'''
import logging
logging.basicConfig(level=logging.DEBUG)
import Queue

from Infrastructure.Communication.MessageRule import MESSAGE
from Infrastructure.Communication.NetUdpBase import NetUdpBase


class Client(NetUdpBase):
    '''
    Client for communication
    '''

    def __init__(self, host, port, name):
        '''
        Constructor
        '''
        super(Client, self).__init__(host, port)
        self._name = name
        self._serverAddr = None
        self._dataQueue = Queue.Queue()
        self._addrQueue = Queue.Queue()

    def registerClient(self, serverHost, serverPort):
        serverAddr = (serverHost, serverPort)
        self._sendMessage(MESSAGE["ClientRegister"].format(self._name), serverAddr)
        logging.info("send message {0}".format(MESSAGE["ClientRegister"].format(self._name)))
        while True:
            data, addr = self._socket.recvfrom(1024)
            logging.info("waiting for message ---")
            print data, addr
            if addr == serverAddr and data == MESSAGE["RegisterSucc"].format(self._name):
                logging.info("Client:{0} Register Success".format(self._name))
                self._serverAddr = serverAddr
                return True
            else:
                logging.info("Client:{0} Register Failure:{1}".format(self._name, data))
                return False

    def _recvMessage(self):
        while True:
            data, addr = self._socket.recvfrom(1024)
            if self._precheck(addr):
                logging.info("Message:{0}".format(data))
                self._dataQueue.put(data)
                self._addrQueue.put(addr)

    def _precheck(self, address):
        if address == self._serverAddr:
            return True
        else:
            return False

if __name__ == "__main__":
    client1 = Client('10.9.171.151', 8088, 'clent1')
    print "register"
    client1.registerClient('10.9.171.165', 8088)
