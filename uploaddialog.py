#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import os
import imp
import sys
import maingui
# from maingui import dlgUploadDone


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers")  # old py2exe
            or imp.is_frozen("__main__"))  # tools/freeze


def get_main_dir():
    if main_is_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(sys.argv[0])


class UploadDoneDialog(maingui.dlgUploadDone):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.dlgUploadDone.__init__(self, parent)

#    def oninitdlgUploadDone(self, event):
#        maingui.dlgUploadDone.oninitdlgUploadDone(self, event)
#        print "oninitdlgUploadDone"

    def setCode(self, text):
        self.text_ctrl_Code1.SetValue(text)

    def onbtnKlaarClick(self, event):
        self.EndModal(wx.ID_OK)
#        self.Destroy()
#        self.btnCopyToClipboard.Hide(True)

    def onbtnCopyToClipboardClick(self, event):
        # maingui.dlgUploadDone.onbtnCopyToClipboardClick(self, event) _onButtonCopy(self,event):
        self.text_ctrl_Code1.SetSelection(-1, -1)  # select everything
        self.text_ctrl_Code1.Copy()  # copy to clipboard
        self.text_ctrl_Code1.SetSelection(0, 0)
