# importing wx files
import wx
import os
import sys
import imp
import webbrowser
 
# import the newly created GUI file
import maingui
from maingui import dlgVoorbeeld
import diversen

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
        filepath = self.text_ctrl_Filepath.GetValue()
        dimensions = (800, 600)
        if self.text_ctrl_Filepath.GetValue() != () and self.text_ctrl_Filepath.GetValue() != "":
            try:
                if not (os.path.exists(self.text_ctrl_Filepath.GetValue())):
                    wx.MessageDialog(self, "Het bestand \"" + self.text_ctrl_Filepath.GetValue() + "\" bestaat niet", "Bericht", style=wx.OK).ShowModal()
                    resizedFileName = None
                    return
                else:
#                 self.action = "converteren van het plaatje"
#                    resizedFileName = diversen.resizeFile(self.text_ctrl_Filepath.GetValue(), dimensions)
#                  self.frame_1_statusbar.SetStatusText(" ", 0)
                    print 'print: onbtnArchiefClick'
            except Exception, er:
#                resizedFileName = None
#                wx.MessageDialog(self, "Er is een fout opgetreden tijdens het converteren\n" + "De error is " + str(er), "Bericht", style=wx.OK).ShowModal()
                    print 'print: onbtnArchiefClick'

#        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        resizedFileName = diversen.resizeFile('bike.png', dimensions)
        img = wx.Image(self.text_ctrl_Filepath.GetValue(), wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
#        PhotoMaxSize = 1000
#        if W > H:
#            NewW = PhotoMaxSize
#            NewH = PhotoMaxSize * H / W
#        else:
#            NewH = PhotoMaxSize
#            NewW = PhotoMaxSize * W / H
        img = img.Scale(W, H)
#        size = (W, H)
        Voorbeeld = dlgVoorbeeld(self)
        Voorbeeld.SetTitle(self.text_ctrl_Filepath.GetValue())
        Voorbeeld.bitmapVoorbeeld.SetBitmap(wx.BitmapFromImage(img))
#        Voorbeeld.SetMinSize(size)
#        Voorbeeld.SetMaxSize(size)
        Voorbeeld.Fit()
        Voorbeeld.Layout()
        Voorbeeld.Show()                 
 
# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
app = wx.App(False)
 
# create an object of AquaFrame
frame = AquaFrame(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
