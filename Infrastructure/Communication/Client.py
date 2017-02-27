# coding=utf-8
'''
Created on 20170224

@author: WLX
'''
from time import ctime

from Infrastructure.Communication.NetUdpBase import NetUdpBase
from Infrastructure.Communication.MessageRule import MESSAGE


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
        
    def registerClient(self, serverHost, serverPort):
        serverAddr = (serverHost, serverPort)
        self._sendMessage(MESSAGE["ClientRegister"].format(self._name), serverAddr)
        print "send message ", MESSAGE["ClientRegister"].format(self._name)
        while True:
            data, addr = self._socket.recvfrom(1024)
            print "waiting for message ---"
            print data, addr
            if addr == serverAddr and data == MESSAGE["RegisterSucc"].format(self._name):
                print ">>>>\r\nTime:{0}\r\nClient:{1}\r\nRegister Success\r\n<<<<\r\n".format(ctime(), self._name)
                self._serverAddr = serverAddr
                return True
            else:
                print ">>>>\r\nTime:{0}\r\nClient:{1}\r\nRegister Failure:{2\r\n<<<<\r\n".format(ctime(), self._name, data)
                return False
 
    def _recvMessage(self):
        while True:
            data, addr = self._socket.recvfrom(1024)
            if self.precheck(addr):
                print "Time:{0}\rMessage:{1}\r".format(ctime(), data)
                self.handoverMessage(data)
#             handover the message
if __name__ == "__main__":
    client1 = Client('10.9.171.165', 8088, 'clent1')
    client1.registerClient('10.9.171.151', 8088)
    