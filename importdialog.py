#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import sys
import maingui
from db import ImportJSON2DB, setUserImported


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
                busyDlg = wx.BusyInfo("""Bezig met importeren van foto's...""")
                totaal, mislukt = ImportJSON2DB(oudeJSON)
                del busyDlg

                teksie = str(totaal - mislukt) + """ van de """ + str(totaal) + """ foto's zijn geimporteerd, dit venster kan nu afgesloten worden."""
#                if mislukt != 0:
#                    teksie = teksie + '/r' + 'Dan waren er ' + mislukt + ' dubbel aanwezig'
                self.m_staticText4.Label = teksie

                setUserImported()
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
