# coding=utf-8
'''
Created on 20170224

@author: wlx
'''


class AppBase(object):
    '''
    classdocs
    '''

    def __init__(self, appPath, appProcess=None, appHandle=None):
        '''
        Constructor
        '''
        self._appPath = appPath
        self._appProcess = appProcess
        self._appHandle = appHandle

    def _startApp(self):
        raise "_startApp NotImpleteMentERROR"

    def _connectApp(self):
        raise "_connectApp NotImpleteMentERROR"
