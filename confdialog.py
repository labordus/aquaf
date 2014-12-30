#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import maingui
import db
from db import getDimensies, getUserDimensieID, setUserDimensie, getUserPreview,\
    setUserFolder, getUserFolder, getUserTooltip
import importdialog
import diversen


class Configure(maingui.dlgConf):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.dlgConf.__init__(self, parent)

    def oninitConfDialog(self, event):
        dims = getDimensies()
        self.choiceDimensie.SetItems(dims)
        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)  # index loopt anders dus -1
        self.checkPreview.SetValue(getUserPreview())
        self.checkTooltip.SetValue(getUserTooltip())
        userName = db.getUsername()
        self.confedtLoginName.SetValue(userName)

        if diversen.USER_FOLDER:
            self.dirpickFolder.SetPath(diversen.USER_FOLDER)
        else:
            from os.path import expanduser
            pad = expanduser("~")
            self.dirpickFolder.SetPath(pad)

        pick = self.dirpickFolder.GetPickerCtrl()
        if pick is not None:
            pick.SetLabel('Selecteer')

    def ondirpickFolderChange(self, event):
        setUserFolder(self.dirpickFolder.GetPath())

    def onChoiceDimensies(self, event):
        setUserDimensie(self.choiceDimensie.GetStringSelection())

    def onbtnImportClick(self, event):
        if db.IfAlreadyImported():
            dlg = wx.MessageDialog(None, """Je hebt al eens eerder geimporteerd \n""" +
                                   """Nogmaals importeren heeft alleen zin als je \r""" +
                                   """foto's hebt geimporteerd met Riba's versie. \r""" +
                                   """Dubbele entries zullen worden voorkomen. \r""" +
                                   """Nogmaal importeren?""", 'Import', wx.YES_NO | wx.ICON_QUESTION)
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
                self.confedtLoginName.SetValue(db.getUsername())
            else:
                db.setUsername(self.confedtLoginName.GetValue())
                self.confedtLoginName.SetModified(False)
        event.Skip()

    def oncheckPreviewClick(self, event):
        db.setUserPreview(self.checkPreview.IsChecked())

    def oncheckTooltipClick(self, event):
        db.setUserTooltip(self.checkTooltip.IsChecked())

    def onbtnAfsluitenClick(self, event):
        self.EndModal(wx.ID_OK)
