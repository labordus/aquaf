#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import wx
import os
import sys
import imp
import maingui


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

    def onbtnAfsluitenClick(self, event):
        self.EndModal(wx.ID_OK)
