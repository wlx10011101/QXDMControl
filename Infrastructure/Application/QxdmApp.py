# coding=utf-8
'''
Created on 2017220

@author: wlx
'''
import logging
import re

from pywinauto.application import Application
from Infrastructure.Application.APPBase import AppBase


logging.basicConfig(level=logging.DEBUG)


class QXDM(AppBase):

    def __init__(self, qxdmPath, qxdmProcess=None, qxdmHandle=None):
        super(QXDM, self).__init__(qxdmPath, qxdmProcess, qxdmHandle)

    def _startApp(self):
        try:
            self._app = Application().Start(self._appPath)
            return True
        except Exception:
            logging.warning("Start QXDM Fail!")
            return False

    def _connectApp(self):
        try:
            self._app = Application().Connect(process=self._appProcess,
                                              handle=self._appHandle,
                                              path=self._appPath)
            return True
        except Exception:
            logging.warning("Connect QXDM Fail")
            return False

    def _findCommandWindow(self):
        return self._app.window_(title_re="QXDM").window_(class_name=u"Edit", control_id=0x3E9)

    def sendCommand(self, command):
        try:
            commandWindow = self._findCommandWindow()
            commandWindow.TypeKeys(command if re.search(r'.*~^', command) else (command + '~'))
        except Exception:
            logging.info("QXDM COMMAND ERROR:{0}".format(Exception))

if __name__ == "__main__":
    '''
#      app = Application().Start("notepad.exe")
#     test = {"process": 6120}
#     app = Application().connect(path="D:\\python\\pythonw.exe")
#     app.UntitledNotepad.menu_select(u"help->About IDLE")
#     app.UntitledNotepad.Edit.type_keys("pywinauto works", with_apaces=True)
#     qxdm = QXDM("C:\\Program Files (x86)\\QUALCOMM\\QXDM4\\QXDM.exe")
#     qxdm.start()
#     qxdm_class_name = u"Afx:002B0000:0"
#     qxdm_command_class_name = u"AfxControlBar100u"
#     qxdm_command_control_id = 0xE81B
#     chorm_class_name = u"Chrome_WidgetWin_1"
#     Notpad_windows = u"Notepad"
#     Notpad_Edit = u"Edit"
#     app = Application().Connect(process=2676)
#     about_dlg = app.window_(title_re="QXDM")
#     app[Notpad_windows][Notpad_Edit].TypeKeys(u"hello world\r")
#     about_dlg.print_control_identifiers()
#     app[Notpad_Edit].TypeKeys(u"hello world")
#     about_dlg = about_dlg.window_(class_name=qxdm_command_class_name, control_id=qxdm_command_control_id)
#     about_dlg = about_dlg.window_(class_name=u"#32770", control_id=0xD4)

#     about_dlg_go = about_dlg[class_name = u"Button"]

#     about_dlg_edit = about_dlg.window_(class_name=u"AfxWnd100u", control_id=0xE900)
#     about_dlg_edit.TypeKeys(u"122343~")
#     about_dlg_edit.TypeKeys('\r')
#     about_dlg_go.Click()
#     about_dlg[u"Go!"].Click()
#     about_dlg_edit.print_control_identifiers()
    '''
    pass
