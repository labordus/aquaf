#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import os
import sys
import imp
import maingui
import db
from db import getDimensies, getUserDimensie, setUserDimensie
from _codecs import encode, decode


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers")  # old py2exe
            or imp.is_frozen("__main__"))  # tools/freeze


def get_main_dir():
    if main_is_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(sys.argv[0])


class ConfDialog(maingui.dlgConf):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.dlgConf.__init__(self, parent)

    def oninitConfDialog(self, event):
        dims = getDimensies()
        self.choiceDimensie.SetItems(dims)
#        self.choiceDimensie.SetSelection(3)
        self.choiceDimensie.SetStringSelection(getUserDimensie())

    def onChoiceDimensies(self, event):
        setUserDimensie(self.choiceDimensie.GetStringSelection())

    def onbtnAfsluitenClick(self, event):
        self.EndModal(wx.ID_OK)
