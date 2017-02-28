# coding=utf-8
'''
Created on 20170228

@author: WLX
'''
from Domain.QxdmClient import QxdmClient
from Domain.QxdmServer import QxdmServer


separator = '-----------------------------\r\n'


def _initNote():
    notes = ['This Application is just for',
            'sending the command to QXDM',
            'that can control UE attach', 
            'and detach',]
    function = '*please start Server First!*\r\n'
    print separator,
    for note in notes:
        print note
    print separator, function


def _initApp():
    print "1.start Client"
    print "2.start Server"
    qxdmType = raw_input("which one?: ")
    if qxdmType == "1":
        QxdmClient()
    elif qxdmType == "2":
        QxdmServer()
    else:
        print "Invalid Input"


def onKeyboardEvent(event):
    print "MessageName:", event.MessageName
    print "Message:", event.Message
    print "Time:", event.Time
    print "Window:", event.Window
    print "WindowName:", event.WindowName
    print "Ascii:", event.Ascii, chr(event.Ascii)
    print "Key:", event.Key
    print "KeyID:", event.KeyID
    print "ScanCode:", event.ScanCode
    print "Extended:", event.Extended
    print "Injected:", event.Injected
    print "Alt", event.Alt
    print "Transition", event.Transition
    print "---"


def startKeyboardListen():
    hm = pyHook.HoolManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


def main():
    _initNote()
    _initApp()
#     startKeyboardListen()


if __name__ == '__main__':
    main()
