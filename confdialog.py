#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import os
import sys
import imp
import maingui
import db
from db import getDimensies, getUserDimensieID, setUserDimensie, getUserPreview
from _codecs import encode, decode
import importdialog


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers")  # old py2exe
            or imp.is_frozen("__main__"))  # tools/freeze


def get_main_dir():
    if main_is_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(sys.argv[0])


class Configure(maingui.dlgConf):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.dlgConf.__init__(self, parent)

    def oninitConfDialog(self, event):
        dims = getDimensies()
        self.choiceDimensie.SetItems(dims)
#        self.choiceDimensie.SetSelection(3)
#        self.choiceDimensie.SetStringSelection(getUserDimensie())
        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)  # index loopt anders dus -1
        self.checkPreview.SetValue(getUserPreview())
        userName = db.get_username()
        self.confedtLoginName.SetValue(userName)

    def onChoiceDimensies(self, event):
        setUserDimensie(self.choiceDimensie.GetStringSelection())

    def onbtnImportClick(self, event):
        if db.IfAlreadyImported():
            dlg = wx.MessageDialog(None, 'Je hebt al eens eerder geimporteerd \n' +
                                   'Nogmaals importeren betekend dat de oude gegevens nogmaals ' +
                                   'zullen worden toegevoegd aan de huidige database, met dubbele entries tot gevolg.' +
                                   'Weet je zeker dat je dit wilt doen?', 'Import', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                dlg.Destroy()
                return

        dlgimport = importdialog.ImportDialog(self)
        dlgimport.CenterOnParent()
        dlgimport.ShowModal()
        dlgimport.Destroy()

    def onconfedtLoginNameKillFocus(self, event):
        if self.confedtLoginName.IsModified():
            if len(self.confedtLoginName.GetValue()) == 0:
                print "Niets ingevoerd"
                self.confedtLoginName.SetValue(db.get_username())
            else:
                db.set_username(self.confedtLoginName.GetValue())
                self.confedtLoginName.SetModified(False)
        event.Skip()

    def oncheckPreviewClick(self, event):
        db.setUserPreview(self.checkPreview.GetValue)

    def onbtnAfsluitenClick(self, event):
        self.EndModal(wx.ID_OK)
