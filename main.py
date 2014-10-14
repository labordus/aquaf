# importing wx files
import wx
import os
import sys
import imp
import webbrowser

# import GUI
import maingui
from maingui import dlgVoorbeeld, dlgUploadDone
from Dialog import Dialog

import diversen
import uploaddialog
from wx.lib.pubsub.pub import validate
#from diversen import ValideerInvoer
#from telnetlib import theNULL

AUQAOFORUM_PICTURE_URL = "http://www.aquaforum.nl/gallery/upload/"
TEST_FOTO = "test.jpg"

# create custom event
UPLOAD_DONE_EVENT_TYPE = wx.NewEventType()
EVT_UPLOAD_DONE = wx.PyEventBinder(UPLOAD_DONE_EVENT_TYPE, 1)

###########################################################################
# class UploadDoneEvent(wx.PyCommandEvent):
###########################################################################


class UploadDoneEvent(wx.PyCommandEvent):
    eventType = UPLOAD_DONE_EVENT_TYPE

    def __init__(self, windowID):
        wx.PyCommandEvent.__init__(self, self.eventType, windowID)

    def Clone(self):
        self.__class__(self.GetId())

###########################################################################
# def main_is_frozen():
###########################################################################


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers")  # old py2exe
            or imp.is_frozen("__main__"))  # tools/freeze

###########################################################################
# def get_main_dir():
###########################################################################


def get_main_dir():
    result = ""
    if main_is_frozen():
        result = os.path.dirname(sys.executable)
    else:
        result = os.path.dirname(sys.argv[0])
    if result == "":
        result = "."
    return result

###########################################################################
# class AquaFrame(maingui.Mainframe):
###########################################################################
# inherit from the MainFrame created in wxFowmBuilder and create AquaFrame


class AquaFrame(maingui.Mainframe):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.Mainframe.__init__(self, parent)

        self.Bind(EVT_UPLOAD_DONE, self.OnEventUploadDone)
        EVT_UPLOAD_DONE(self, -1, self.OnEventUploadDone)

        # bind validator to edtLogin-Invoerbox
        # self.edtLoginName.SetValidator(ValideerInvoer(diversen.ALPHA_ONLY))


###########################################################################
# def onbtnArchiefClick(self, event):
###########################################################################
    def onbtnArchiefClick(self, event):
        #        try:
        #            print 'print: onbtnArchiefClick'
        #        except Exception:
        #            print 'error'
        '''open archive'''
#        path = "file:///"
        theArchive = get_main_dir()
        theArchive = theArchive.replace("\\", "/")
        if theArchive[-1] != "/":
            theArchive += "/"
        theArchive += "archive.html"
        webbrowser.open_new(theArchive)
        return

###########################################################################
# def onbtnSelectFile1Click(self, event):
###########################################################################
    def onbtnSelectFile1Click(self, event):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname,
                            "", "*.*", wx.OPEN)
        dlg.SetWildcard(
            "plaatjes (*.bmp;*.jpg;*.png;*.tiff)|*.bmp;*.jpg;*.png;*.tiff|Alles (*.*)|*.*")
        if dlg.ShowModal() == wx.ID_OK:
            self.edtFile1.SetValue(dlg.GetPath())
        dlg.Destroy()

###########################################################################
# def onbtnVoorbeeldClick(self, event):
###########################################################################
    def onbtnVoorbeeldClick(self, event):
        #        filepath = self.edtFile1.GetValue()

        dimensions = self.getDimensions()
#        self.frame_1_statusbar.SetStatusText("Het programma converteert het plaatje", 0)
        resizedFileName = None

#        if self.edtFile1.GetValue() != () and self.edtFile1.GetValue() != "":
        try:
            if not (os.path.exists(TEST_FOTO)):
                wx.MessageDialog(self, TEST_FOTO + " bestaat niet", "Bericht", style=wx.OK).ShowModal()
                resizedFileName = None
                return
            else:
                resizedFileName = diversen.resizeFile(TEST_FOTO, dimensions)
#                  self.frame_1_statusbar.SetStatusText(" ", 0)
        except Exception as er:
            resizedFileName = None
            wx.MessageDialog(
                self,
                "Er is een fout opgetreden tijdens het converteren\n" +
                "De error is " +
                str(er),
                "Bericht",
                style=wx.OK).ShowModal()

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
        Voorbeeld.SetTitle(TEST_FOTO)
        Voorbeeld.bitmapVoorbeeld.SetBitmap(wx.BitmapFromImage(img))
        Voorbeeld.Fit()
        Voorbeeld.Layout()
        Voorbeeld.Show()

###########################################################################
# def getDimensions(self):
###########################################################################
    def getDimensions(self):
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
        return dimensions

###########################################################################
# def ontvFilesSelChanged(self, event):
###########################################################################
    def ontvFilesSelChanged(self, event):
        pad = self.tvFiles.GetFilePath()
        dimensions = self.bitmapSelectedFile.GetSize()
        if pad != () and pad != "":
            # file selected
            scaled_file = diversen.resizeFile(pad, dimensions)
            img = wx.Image(scaled_file, wx.BITMAP_TYPE_ANY)
            self.bitmapSelectedFile.SetBitmap(wx.BitmapFromImage(img))
#            self.btnSelectFile.Enable()
            self.frame_1_statusbar.SetStatusText("bestand geselecteerd", 0)
            self.action = "benaderen van aquaforum webpagina"
        else:
            # directory selected
            scaled_file = diversen.resizeFile("default_foto.jpg", dimensions)
            img = wx.Image(scaled_file, wx.BITMAP_TYPE_ANY)
            self.bitmapSelectedFile.SetBitmap(wx.BitmapFromImage(img))
#            self.btnSelectFile.Disable()
            print "directory"

###########################################################################
# def onbtnSelectFileClick(self, event):
###########################################################################
    def onbtnSelectFileClick(self, event):
        # check of bestand al is toegevoegd..
        # sla het hele pad op in..? pyobject clientdata
        helepad = self.tvFiles.GetPath()
        bestandsnaam = os.path.basename(helepad)
        self.listboxSelectedFiles.Append(bestandsnaam, helepad)

###########################################################################
# def onlistboxSelectedFile(self, event):
###########################################################################
#    def onlistboxSelectedFile(self, event):
# print "You     selected: " +
# self.listboxSelectedFiles.GetStringSelection()

#        helepad = self.listboxSelectedFiles.GetClientData(
#            self.listboxSelectedFiles.GetSelection())

#        print helepad
#        self.btnUnselectFile.Enable(True)
#        self.listboxSelectedFiles.Delete(self.listboxSelectedFiles.GetSelection())

###########################################################################
# def onbtnUnselectFileClick(self, event):
###########################################################################
    def onbtnUnselectFileClick(self, event):
        self.listboxSelectedFiles.Delete(
            self.listboxSelectedFiles.GetSelection())
#       self.btnUnselectFile.Enable(False)

#   def onlistboxSelectedFileLostFocus(self, event):
#       self.btnUnselectFile.Enable(False)

#   def onlistboxSelectedFileSetFocus(self, event):
#       self.btnUnselectFile.Enable(True)


###########################################################################
# def onbtnUploadClick(self, event):
###########################################################################
    def onbtnUploadClick(self, event):
        # TODO: Check of gebruikernaam is ingevoerd.
        # TODO: Check of er bestanden zijn geselecteerd.

        if len(self.edtLoginName.GetValue()) == 0:
            print "Geen loginnaam ingevoerd"
            return

        # hier meerdere bestanden kunnen oploaden..
        filecount = self.listboxSelectedFiles.GetCount()
        if filecount <= 0:
            self.frame_1_statusbar.SetStatusText(
                "Geen bestand geselecteerd", 0)
            return

        dimensions = self.getDimensions()
        urls = ""
        for _i in range(filecount):
            print self.listboxSelectedFiles.GetClientData(_i)
            try:
                resizedFileName = diversen.resizeFile(
                    self.listboxSelectedFiles.GetClientData(_i),
                    dimensions)
                self.desiredName = diversen.constructUploadName(
                    self.edtLoginName.GetValue(),
                    self.listboxSelectedFiles.GetClientData(_i))
                diversen.uploadFileToAquaforum(resizedFileName, self.desiredName)
                diversen.addToHistory(AUQAOFORUM_PICTURE_URL + self.desiredName)
                urls = urls + " [IMG]" + AUQAOFORUM_PICTURE_URL + self.desiredName + "[/IMG]" + "\n"

            except Exception as er:
                self.error = True
                self.errorEx = er
                # done, send done event

                #        event = UploadDoneEvent(self.GetId())
                #        self.GetEventHandler().AddPendingEvent(event)

        dlg = uploaddialog.UploadDoneDialog(self)
        dlg.setCode(urls)
        self.listboxSelectedFiles.Clear()
        dlg.ShowModal()  # this one is non blocking!!


#         self.frame_1_statusbar.SetStatusText("Het programma converteert het plaatje", 0)
#         try:
#             self.action = "converteren van het plaatje"
#             resizedFileName = diversen.resizeFile(self.edtFile1.GetValue(), dimensions)
#             self.frame_1_statusbar.SetStatusText("Het programma bekijkt het aquaforum zodat het plaatje een unieke naam heeft", 0)
#             self.action = "benaderen van aquaforum webpagina"
#             self.desiredName = diversen.constructUploadName(self.edtLoginName.GetValue(), self.edtFile1.GetValue())
#             self.frame_1_statusbar.SetStatusText("Het programma zet het plaatje op aquaforum", 0)
#             self.action = "uploaden van het plaatje"
#             diversen.uploadFileToAquaforum(resizedFileName, self.desiredName)
#             self.action = "Plaatje toevoegen aan archief"
#             self.frame_1_statusbar.SetStatusText("Plaatje toevoegen aan archief", 0)
#             diversen.addToHistory(AUQAOFORUM_PICTURE_URL + self.desiredName)
#             self.frame_1_statusbar.SetStatusText("Klaar....", 0)

###########################################################################
# def OnEventUploadDone(self, event):
###########################################################################
    def OnEventUploadDone(self, event):
        #        if self.error == True:
        #            wx.MessageDialog(self, "Er is een fout opgetreden tijdens het " + self.action + "\n" + "De error is " + str(self.errorEx), "Bericht", style=wx.OK).ShowModal()
        #            self.error = False
        #        else:
        #            dlg = dlgUploadDone(self, -1, "Bericht")

        dlg = uploaddialog.UploadDoneDialog(self)
        urls = ""
        stringlist = self.listboxSelectedFiles.GetCount()
        dimensions = self.getDimensions()
        for _i in range(stringlist):
            resizedFileName = diversen.resizeFile(
                self.listboxSelectedFiles.GetClientData(_i),
                dimensions)
            desiredName = diversen.constructUploadName(
                self.edtLoginName.GetValue(),
                resizedFileName)
            urls = urls + " [IMG]" + AUQAOFORUM_PICTURE_URL + \
                desiredName + "[/IMG]" + "\n"
# #
        dlg.setCode(urls)
# dlg.setCode(" [IMG]" + AUQAOFORUM_PICTURE_URL + self.desiredName + "[/IMG]")
# dlg.ShowModal()
# self.busy = False

        # check whether a correct file is selected
#        popupFrame = popupImage.MyFrame(None,-1,"")
#        popupFrame.SetSize((dimensions[0]+10,dimensions[1]+30))
#        popupFrame.setPath(resizedFileName)
        self.listboxSelectedFiles.Clear()
        dlg.ShowModal()  # this one is non blocking!!
#            dlg.Destroy()

# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
app = wx.App(False)

# create an object of AquaFrame
frame = AquaFrame(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
