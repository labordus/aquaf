#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import maingui
import db
from db import getDimensies, getUserDimensieID, setUserDimensie, setUserFolder
import importdialog
import diversen
from diversen import APP_VERSION, UpdateAvailable
import updatedialog


class Configure(maingui.dlgConf):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.dlgConf.__init__(self, parent)

    def oninitConfDialog(self, event):
        dims = getDimensies()
        self.choiceDimensie.SetItems(dims)
        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)  # index loopt anders dus -1
        self.checkPreview.SetValue(diversen.USER_PREVIEW)
        self.checkTooltip.SetValue(diversen.USER_TOOLTIP)
        self.checkWebNieuw.SetValue(diversen.USER_WEBNIEUW)
        self.checkUpdate.SetValue(diversen.USER_UPDATECHECK)
        self.confedtLoginName.SetValue(diversen.USER_USERNAME)
        self.txtVersie.SetLabel(self.txtVersie.GetLabelText() + APP_VERSION)

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
                                   """Alleen nog niet bestaande foto's zullen worden geimporteerd. \r""" +
                                   """Nogmaals importeren?""", 'Import', wx.YES_NO | wx.ICON_QUESTION)
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
                self.confedtLoginName.SetValue(diversen.USER_USERNAME)
            else:
                db.setUsername(self.confedtLoginName.GetValue())
                self.confedtLoginName.SetModified(False)
        event.Skip()

    def oncheckPreviewClick(self, event):
        db.setUserPreview(self.checkPreview.IsChecked())

    def oncheckTooltipClick(self, event):
        db.setUserTooltip(self.checkTooltip.IsChecked())

    def oncheckWebNieuwClick(self, event):
        db.setUserWebNieuw(self.checkWebNieuw.IsChecked())

    def oncheckUpdateClick(self, event):
        db.setUserUpdateCheck(self.checkUpdate.IsChecked())

    def onbtnCheckForUpdateClick(self, event):

        ReleaseVersion, ReleaseDate, ReleaseChanges = UpdateAvailable()
        if ReleaseVersion != '':
            self.txtVersie.SetForegroundColour(wx.RED)
            self.txtVersie.SetLabel('''Versie: ''' + ReleaseVersion + ''' is beschikbaar, bezoek website voor download.''')
            update = updatedialog.Update(self)
            update.LoadText(ReleaseVersion, ReleaseDate, ReleaseChanges)
            update.CenterOnParent()
            update.ShowModal()
            update.Destroy()
        else:
            self.txtVersie.SetForegroundColour('#078910')
            self.txtVersie.SetLabel('Geen update beschikbaar, je gebruik de nieuwste versie.')

    def onbtnAfsluitenClick(self, event):
        self.EndModal(wx.ID_OK)
