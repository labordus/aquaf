#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import os
import imp
import sys
import maingui
from db import ImportJSON2DB, SetImported


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers")  # old py2exe
            or imp.is_frozen("__main__"))  # tools/freeze


def get_main_dir():
    if main_is_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(sys.argv[0])


class ImportDialog(maingui.dlgImport):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.dlgImport.__init__(self, parent)

    def onclickselectjson(self, event):
        if (sys.platform.startswith('win')):  # dan win32 of win64
            standaarddir = "C:\Program Files\AquaforumUploader"
        else:  # posix
            standaarddir = "@HOME/.local/share"  # dit werkt niet

        dlg = wx.FileDialog(
            self, message="Selecteer images.json",
            #            defaultDir=os.getcwd(),
            defaultDir=standaarddir,
            defaultFile="",
            wildcard='images.json',
            style=wx.OPEN
        )

        if dlg.ShowModal() == wx.ID_OK:
            oudeJSON = dlg.GetPath()
            self.btnSelectJSON.Disable()
            try:
                busyDlg = wx.BusyInfo('Bezig met importeren van plaatjes...')
                aantal = ImportJSON2DB(oudeJSON)
                del busyDlg
                self.m_staticText4.Label = 'Er zijn ' + str(aantal) + ' plaatjes geimporteerd, dit venster kan nu afgesloten worden.'
                SetImported()
            except Exception as e:
                self.e = e
                print('Run-time error:', e)
                self.m_staticText4.Label = 'Data kon niet worden geimporteerd, bordumar@gmail.com'
# else: # wx.ID_CANCEL
        dlg.Destroy()

    def onbtnAfsluitenCLick(self, event):
        self.EndModal(wx.ID_OK)
#        self.Destroy()
#        self.btnCopyToClipboard.Hide(True)
