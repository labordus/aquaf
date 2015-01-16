#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import maingui


class Update(maingui.dlgUpdate):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.dlgUpdate.__init__(self, parent)

    def LoadText(self, ReleaseVersion, ReleaseDate, ReleaseChanges):
        text = self.textUpdate
        text.AppendText("Nieuwe versie : ")
        text.SetDefaultStyle(wx.TextAttr(wx.RED))
        text.AppendText(str(ReleaseVersion) + '\n')
        text.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        text.AppendText("Datum : ")
        text.AppendText(str(ReleaseDate) + '\n')
        text.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        text.AppendText("Veranderingen : \n")
        for row in ReleaseChanges:
            #            sPoep = str((row[0]))
            sRegel = str(row)
            text.AppendText(sRegel + '\n')

    def onbtnAfsluitenClick(self, event):
        self.EndModal(wx.ID_OK)
