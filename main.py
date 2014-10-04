# importing wx files
import wx
import os
import sys
import imp
import webbrowser
 
# import the newly created GUI file
import maingui
from maingui import dlgVoorbeeld
from maingui import dlgUploadDone
import diversen

AUQAOFORUM_PICTURE_URL = "http://www.aquaforum.nl/gallery/upload/"

# create custom event
UPLOAD_DONE_EVENT_TYPE = wx.NewEventType() 
EVT_UPLOAD_DONE = wx.PyEventBinder(UPLOAD_DONE_EVENT_TYPE, 1) 

class UploadDoneEvent(wx.PyCommandEvent): 
    eventType = UPLOAD_DONE_EVENT_TYPE 
    def __init__(self, windowID): 
        wx.PyCommandEvent.__init__(self, self.eventType, windowID) 

    def Clone(self): 
        self.__class__(self.GetId())

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

        index = self.radio_box_3.GetSelection()  # zero based index
        dimensions = None
        if index == 0:
            dimensions = (800, 600)
        elif index == 1:
            dimensions = (640, 480)
        elif index == 2:
            dimensions = (320, 240)
        else:
            dimensions = (160, 120)
#        self.frame_1_statusbar.SetStatusText("Het programma converteert het plaatje", 0)
        resizedFileName = None
        
        if self.text_ctrl_Filepath.GetValue() != () and self.text_ctrl_Filepath.GetValue() != "":
            try:
                if not (os.path.exists(self.text_ctrl_Filepath.GetValue())):
                    wx.MessageDialog(self, "Het bestand \"" + self.text_ctrl_Filepath.GetValue() + "\" bestaat niet", "Bericht", style=wx.OK).ShowModal()
                    resizedFileName = None
                    return
                else:
#                 self.action = "converteren van het plaatje"
                    resizedFileName = diversen.resizeFile(filepath, dimensions)
#                  self.frame_1_statusbar.SetStatusText(" ", 0)
                    print 'print: onbtnArchiefClick'
            except Exception, er:
                resizedFileName = None
                wx.MessageDialog(self, "Er is een fout opgetreden tijdens het converteren\n" + "De error is " + str(er), "Bericht", style=wx.OK).ShowModal()
                
#        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        img = wx.Image(resizedFileName, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
#        W = img.GetWidth()
#        H = img.GetHeight()
#        PhotoMaxSize = 1000
#        if W > H:
#            NewW = PhotoMaxSize
#            NewH = PhotoMaxSize * H / W
#        else:
#            NewH = PhotoMaxSize
#            NewW = PhotoMaxSize * W / H
#        img = img.Scale(W, H)
#        size = (W, H)
        Voorbeeld = dlgVoorbeeld(self)
        Voorbeeld.SetTitle(self.text_ctrl_Filepath.GetValue())
        Voorbeeld.bitmapVoorbeeld.SetBitmap(wx.BitmapFromImage(img))
#        Voorbeeld.SetMinSize(size)
#        Voorbeeld.SetMaxSize(size)
        Voorbeeld.Fit()
        Voorbeeld.Layout()
        Voorbeeld.Show()                 

    def onbtnUploadClick(self, event):
        index = self.radio_box_3.GetSelection()  # zero based index
        dimensions = None
        if index == 0:
            dimensions = (800, 600)
        elif index == 1:
            dimensions = (640, 480)
        elif index == 2:
            dimensions = (320, 240)
        else:
            dimensions = (160, 120)
        self.frame_1_statusbar.SetStatusText("Het programma converteert het plaatje", 0)
        try:
            self.action = "converteren van het plaatje"
            resizedFileName = diversen.resizeFile(self.text_ctrl_Filepath.GetValue(), dimensions)
            self.frame_1_statusbar.SetStatusText("Het programma bekijkt het aquaforum zodat het plaatje een unieke naam heeft", 0)
            self.action = "benaderen van aquaforum webpagina"            
            self.desiredName = diversen.contructUploadName(self.loginNaam.GetValue(), self.text_ctrl_Filepath.GetValue())
            self.frame_1_statusbar.SetStatusText("Het programma zet het plaatje op aquaforum", 0)
            self.action = "uploaden van het plaatje"                        
            diversen.uploadFileToAquaforum(resizedFileName, self.desiredName)
            self.action = "Plaatje toevoegen aan archief"
            self.frame_1_statusbar.SetStatusText("Plaatje toevoegen aan archief", 0)
            diversen.addToHistory(AUQAOFORUM_PICTURE_URL + self.desiredName)
            self.frame_1_statusbar.SetStatusText("Klaar....", 0)
        except Exception, er:
            self.error = True
            self.errorEx = er
        # done, send done event
        event = UploadDoneEvent(self.GetId())
        self.GetEventHandler().AddPendingEvent(event)        
    
    def OnEventUploadDone(self, event):
        '''show dialog'''
        if self.error == True:
            wx.MessageDialog(self, "Er is een fout opgetreden tijdens het " + self.action + "\n" + "De error is " + str(self.errorEx), "Bericht", style=wx.OK).ShowModal()
            self.error = False
        else:
            dlg = dlgUploadDone(self, -1, "Bericht")
            dlg.setCode(" [IMG]" + AUQAOFORUM_PICTURE_URL + self.desiredName + "[/IMG]")
            dlg.ShowModal()
        self.busy = False
 
# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
app = wx.App(False)
 
# create an object of AquaFrame
frame = AquaFrame(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
