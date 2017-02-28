# coding=utf-8
'''
Created on 20170228

@author: WLX
'''
from __builtin__ import str

if __name__ == '__main__':
    separator = '-----------------------------\r\n'
    
    note = ['This Application is just for',
            'sending the command to QXDM',
            'that can control UE attach', 
            'and detach',]
    function = '*please start Server First!*\r\n'
    print separator,
    for str in note:
        print str
    print separator, function
    
    qxdmType = raw_input("which ")