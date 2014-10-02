# importing wx files
import wx
import os
import sys
import imp
import webbrowser
 
# import the newly created GUI file
import maingui

def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
           hasattr(sys, "importers")  # old py2exe
           or imp.is_frozen("__main__"))  # tools/freeze

def get_main_dir():
    result = ""
    if main_is_frozen():
        result = os.path.dirname(sys.executable)
    else:
        result = os.path.dirname(sys.argv[0])
    if result == "":
        result = "."
    return result

# inherit from the MainFrame created in wxFowmBuilder and create AquaFrame
class AquaFrame(maingui.Mainframe):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        maingui.Mainframe.__init__(self, parent)
 
    def onbtnArchiefClick(self, event):
#        try:
#            print 'print: onbtnArchiefClick'
#        except Exception:
#            print 'error'
        '''open archive'''
        path = "file:///"
        theArchive = get_main_dir()
        theArchive = theArchive.replace("\\", "/")
        if theArchive[-1] != "/":
            theArchive += "/"
        theArchive += "archive.html"
        webbrowser.open_new(theArchive)
        return
            
    def onbtnSelectFileClick(self, event):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        dlg.SetWildcard("plaatjes (*.bmp;*.jpg;*.png;*.tiff)|*.bmp;*.jpg;*.png;*.tiff|Alles (*.*)|*.*")
        if dlg.ShowModal() == wx.ID_OK:
            self.text_ctrl_Filepath.SetValue(dlg.GetPath())
        dlg.Destroy()
 
    def onbtnVoorbeeldClick(self, event):
        try:
            print 'print: onbtnVoorbeeldClick'
        except Exception:
            print 'error'
 
# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
app = wx.App(False)
 
# create an object of AquaFrame
frame = AquaFrame(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
