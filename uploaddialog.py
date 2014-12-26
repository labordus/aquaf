#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import maingui


class UploadDoneDialog(maingui.dlgUploadDone):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.dlgUploadDone.__init__(self, parent)

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
