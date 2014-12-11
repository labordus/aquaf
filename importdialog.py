#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import os
import imp
import sys
import maingui


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
        import appdirs
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
            oudejson = dlg.GetPath()
            # nog effe voor de zekerheid testen..
            head, tail = os.path.split(oudejson)
            if tail != 'images.json':
                print 'verkeerd bestand gekozen'
            else:
                path = appdirs.user_data_dir('aquaf', False, False, False)
                #    check_path_exists(os.path.join(path, 'aquaf.db'))
                filepath = os.path.join(path, 'aquaf.json')
                with open(oudejson) as f:
                    with open(filepath, "w") as f1:
                        for line in f:
                            #                            if "]}" in line:
                            #                            f1.write(rstrip(line))
                            f1.write(line)
                self.m_staticText4.Label = 'Data is geimporteerd, je kunt dit venster nu afsluiten'
# else: # wx.ID_CANCEL
        dlg.Destroy()

    def onbtnAfsluitenCLick(self, event):
        self.EndModal(wx.ID_OK)
#        self.Destroy()
#        self.btnCopyToClipboard.Hide(True)
