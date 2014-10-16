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
from wx import BITMAP_TYPE_TIF
#from diversen import ValideerInvoer
#from telnetlib import theNULL

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
#        Voorbeeld.CenterOnParent()
        Voorbeeld.Fit()
        Voorbeeld.Layout()
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

    def ontvFilesSelChanged(self, event):
        import imghdr
        pad = self.tvFiles.GetFilePath()
        dimensions = self.bitmapSelectedFile.GetSize()
        if pad != () and pad != "":
            # file selected

            # TODO: Checken wat voor image dit is.. if image at all.
            #            image_type = imghdr.what(pad)
            #            if not image_type:
            #                print "error.. geen image-bestand"
            #                return
            #            else:
            image_type = imghdr.what(pad)
            if not image_type:
                print "error.. geen image-bestand"
                return
            else:
                # check of bv.. IMAGE.PNG ook echt een PNG is.. anders return.
                # extract extension en maak lowercase
                ext = os.path.splitext(pad)[-1].lower()
                print image_type
                if image_type == 'jpeg':
                    if (ext != '.jpg' and
                            ext != '.jpeg'):
                        print "filetype JPG heeft geen JPG-extensie"
                        return
                elif image_type == 'bmp':
                    if ext != '.bmp':
                        print "filetype BMP heeft geen BMP-extensie"
                        return
                elif image_type == 'png':
                    if ext != '.png':
                        print "filetype PNG heeft geen PNG-extensie"
                        return
                elif image_type == 'tiff':
                    if (ext != '.tiff' and
                            ext != '.tif'):
                        print "filetype TIF(F) heeft geen TIFF-extensie"
                        return
                else:
                    print "Geen ondersteund image format"
                    return

##########################

            scaled_file = diversen.resizeFile(pad, dimensions)
#            img = wx.Image(scaled_file, wx.BITMAP_TYPE_ANY)
            img = wx.Image(scaled_file, wx.BITMAP_TYPE_ANY)
            self.bitmapSelectedFile.SetBitmap(wx.BitmapFromImage(img))
#            self.bitmapSelectedFile.Fit()
#            self.bitmapSelectedFile.Layout()
#            self.btnSelectFile.Enable()
            self.frame_1_statusbar.SetStatusText("bestand geselecteerd", 0)
            self.action = "benaderen van aquaforum webpagina"
        else:
            # directory selected
            scaled_file = diversen.resizeFile("test.jpg", dimensions)
            # TODO: imgType jpg?
            img = wx.Image(scaled_file, wx.BITMAP_TYPE_ANY)
            self.bitmapSelectedFile.SetBitmap(wx.BitmapFromImage(img))
#            self.Fit()
#            self.Layout()
#            self.btnSelectFile.Disable()

    def onbtnSelectFileClick(self, event):
        # TODO: check of bestand al is toegevoegd..
        # sla het hele pad op in..? pyobject clientdata

        _pad = self.tvFiles.GetFilePath()
        if _pad != () and _pad != "":
            # file
            helepad = self.tvFiles.GetPath()
            bestandsnaam = os.path.basename(helepad)
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
