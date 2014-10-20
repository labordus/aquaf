# importing wx files
import wx
import os
import sys
import imp
import webbrowser
from PIL import Image

# import GUI
import maingui
from maingui import dlgVoorbeeld, dlgUploadDone
from Dialog import Dialog

import diversen
from diversen import *

import uploaddialog
# from wx.lib.pubsub.pub import validate
# from wx import BITMAP_TYPE_TIF
# from diversen import ValideerInvoer
# from telnetlib import theNULL

AUQAOFORUM_PICTURE_URL = "http://www.aquaforum.nl/gallery/upload/"
TEST_FOTO = "test.jpg"


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


class AquaFrame(maingui.Mainframe):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.Mainframe.__init__(self, parent)

        # bind validator to edtLogin-Invoerbox
        # self.edtLoginName.SetValidator(ValideerInvoer(diversen.ALPHA_ONLY))

        # Windows laat anders dubbele entries zien,
        # en linux laat alleen bestanden zien met specifieke casing
        if (sys.platform == 'win32'):  # weet niet of dit ook Win 7/8 meeneemt
            self.tvFiles.SetFilter("plaatjes(*.bmp;*.jpg;*.png;*.tiff;*.tif;)|*.bmp;*.jpg;*.png;*.tiff;*.tif")
        else:  # posix
            self.tvFiles.SetFilter("plaatjes(*.bmp;*.BMP;*.jpg;*.JPG;*.png;*.PNG;*.tiff;*.TIFF;*.tif;*.TIF)|*.bmp;*.BMP;*.jpg;*.JPG;*.png;*.PNG;*.tiff;*.TIFF;*.tif;*.TIF")

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

        self.ShowVoorbeeld(img, dimensions)


########################################
    def ShowVoorbeeld(self, img, dimensions):
        Voorbeeld = dlgVoorbeeld(self)
        Voorbeeld.SetTitle(TEST_FOTO)
        Voorbeeld.m_staticText6.Label = "Dimensie=" + str(dimensions)
        Voorbeeld.bitmapVoorbeeld.SetBitmap(wx.BitmapFromImage(img))
        Voorbeeld.Fit()
        Voorbeeld.Layout()
        Voorbeeld.CenterOnParent()
#        Voorbeeld.Show()
        Voorbeeld.ShowModal()
        Voorbeeld.Destroy()

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

    def ResizeImage(self, pad, dim):
        img = Image.open(pad)
        # scale the image, preserving the aspect ratio
        originalDimensions = img.size
        xRatio = float(dim[0]) / originalDimensions[0]
        yRatio = float(dim[1]) / originalDimensions[1]
        if xRatio < 1 or yRatio < 1:
            # only resize when needed
            minimumRatio = min([xRatio, yRatio])
            img = img.resize(
                (
                    int(originalDimensions[0] * minimumRatio),
                    int(originalDimensions[1] * minimumRatio)
                ), Image.ANTIALIAS)  # resize
        self.bitmapSelectedFile.SetSize(img.size)
        self.bitmapSelectedFile.SetBitmap(PilImageToWxBitmap(img))

    def PreviewImage(self, pad):
        #        dimensions = self.bitmapSelectedFile.GetSize()
        if pad != () and pad != "":
            # file selected
            if IsValidImage(pad):
                self.ResizeImage(pad, (400, 300))
            else:  # als geen geldige image
                return
        else:  # dir
            self.ResizeImage(TEST_FOTO, (400, 300))

    def ontvFilesSelChanged(self, event):
        self.PreviewImage(self.tvFiles.GetFilePath())
#        print platform.platform(aliased=0, terse=0)

    def onlistboxSelectedFile(self, event):
        pad = self.listboxSelectedFiles.GetClientData(self.listboxSelectedFiles.GetSelection())
        self.PreviewImage(pad)

    def onbtnSelectFileClick(self, event):
        _pad = self.tvFiles.GetFilePath()

        # TODO: check of bestand al is toegevoegd..
        for _i in range(self.listboxSelectedFiles.Count):
            sPad = self.listboxSelectedFiles.GetClientData(_i)
            if _pad == sPad:
                print "image is al toegevoegd"
                return

        if _pad != () and _pad != "":
            # file
            if not IsValidImage(_pad):
                return
            helepad = self.tvFiles.GetPath()
            bestandsnaam = os.path.basename(helepad)
            # sla het hele pad op in pyobject clientdata.. toch?
            self.listboxSelectedFiles.Append(bestandsnaam, helepad)
        # else directory en doe niks

    def onbtnUnselectFileClick(self, event):
        self.listboxSelectedFiles.Delete(self.listboxSelectedFiles.GetSelection())

    def onbtnUploadClick(self, event):
        if len(self.edtLoginName.GetValue()) == 0:
            print "Geen loginnaam ingevoerd"
            return

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
#                diversen.uploadFileToAquaforum(resizedFileName, self.desiredName)
#                diversen.addToHistory(AUQAOFORUM_PICTURE_URL + self.desiredName)
                urls = urls + " [IMG]" + AUQAOFORUM_PICTURE_URL + self.desiredName + "[/IMG]" + "\n"

            except Exception as er:
                self.error = True
                self.errorEx = er

        dlg = uploaddialog.UploadDoneDialog(self)
        dlg.setCode(urls)
        self.listboxSelectedFiles.Clear()
        dlg.CenterOnParent()
        dlg.ShowModal()  # this one is non blocking!!
        dlg.Destroy()


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
app = wx.App(False)

# create an object of AquaFrame
frame = AquaFrame(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
