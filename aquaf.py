# importing wx files
import wx
import os
import sys
import imp
from PIL import Image
import db
from archiveview import MyBrowser

# import GUI
import maingui
from maingui import dlgVoorbeeld, dlgUploadDone, dlgImport
from Dialog import Dialog

import diversen
from diversen import *

import uploaddialog
from mechanize._opener import urlopen
import importdialog
from db import DB2JSON, addURL2DB

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
        # volgende werkt niet altijd vanuit dev-environment
        #        result = os.path.dirname(sys.argv[0])
        result = os.path.dirname(__file__)
        # volgende werkt ook..
#        result = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if result == "":
        result = "."
    return result


class RedirectText(object):

    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        self.out.WriteText(string)


class AquaFrame(maingui.Mainframe):
    # constructor

    def __init__(self, parent):
        # initialize parent class
        maingui.Mainframe.__init__(self, parent)

# ######## DATABASE / IMPORT-GEBEUREN ########### #
        if db.Initialize_db() is False:
            app.Exit()
        if db.first_run() == 1:
            dlg = wx.MessageDialog(None, 'Import data van vorige versie van deze applicatie?', 'Import', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                dlg.Destroy()
                self.ShowImportDialog()

# ############################################### #

#        stripJSON()
        Initialize_JSON()

        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((702, 538))

        log = self.infoBox
        # redirect text here
        redir = RedirectText(log)
        sys.stdout = redir

        # Windows laat anders dubbele entries zien,
        # en linux laat alleen bestanden zien met specifieke casing

        if (sys.platform.startswith('win')):  # dan win32 of win64
            self.tvFiles.SetFilter("plaatjes(*.bmp;*.jpg;*.png;*.tiff;*.tif;)|*.bmp;*.jpg;*.png;*.tiff;*.tif")
        else:  # posix
            self.tvFiles.SetFilter("plaatjes(*.bmp;*.BMP;*.jpg;*.JPG;*.png;*.PNG;*.tiff;*.TIFF;*.tif;*.TIF)|*.bmp;*.BMP;*.jpg;*.JPG;*.png;*.PNG;*.tiff;*.TIFF;*.tif;*.TIF")

        self.PreviewImage(TEST_FOTO)

        userName = db.get_username()
        print "Hoi " + userName
        print "Welkom bij Aquaf v8.4"
        self.edtLoginName.SetValue(userName)

    def onmenuitemClickImport(self, event):
        self.ShowImportDialog()

    def ShowImportDialog(self):
        dlgimport = importdialog.ImportDialog(self)
        dlgimport.CenterOnParent()
        dlgimport.ShowModal()
        dlgimport.Destroy()

    def onedtLoginNameKillFocus(self, event):
        if self.edtLoginName.IsModified():
            if len(self.edtLoginName.GetValue()) == 0:
                print "Niets ingevoerd"
                self.edtLoginName.SetValue(db.get_username())
            else:
                db.set_username(self.edtLoginName.GetValue())
                self.edtLoginName.SetModified(False)
        event.Skip()

    def onbtnArchiefClick(self, event):
        #        webbrowser.get("chrome").open_new_tab(theArchive)
        #        webbrowser.get("firefox").open_new(theArchive)
        DB2JSON()
        if IsEmpty_JSON():
            print 'Niets te tonen'
            return
        weburl = "http://127.0.0.1:8000/archive.html"
        dialog = MyBrowser(None, -1)
        dialog.browser.LoadURL(weburl)
        dialog.CenterOnParent()
        dialog.ShowModal()
        dialog.Destroy()
        #        launch_archive('firefox')
        return

    def onbtnVoorbeeldClick(self, event):
        dimensions = getDimensions(self.radio_box_3.GetSelection())
        resizedFileName = None
        try:
            if not (os.path.exists(TEST_FOTO)):
                wx.MessageDialog(self, TEST_FOTO + " bestaat niet", "Bericht", style=wx.OK).ShowModal()
                resizedFileName = None
                return
            else:
                resizedFileName = ResizeImage(TEST_FOTO, dimensions)
        except Exception as er:
            resizedFileName = None
            wx.MessageDialog(
                self,
                "Er is een fout opgetreden tijdens het converteren\n" +
                "De error is " + str(er),
                "Bericht", style=wx.OK).ShowModal()
            return
        Voorbeeld = dlgVoorbeeld(self)
        Voorbeeld.SetTitle(str(dimensions))
        Voorbeeld.bitmapVoorbeeld.SetBitmap(PilImageToWxBitmap(resizedFileName))
        Voorbeeld.Fit()
        Voorbeeld.Layout()
        Voorbeeld.CenterOnParent()
        Voorbeeld.ShowModal()
        Voorbeeld.Destroy()

    def PreviewImage(self, pad):
        if pad != () and pad != "":
            # file selected
            if IsValidImage(pad):
                img = ResizeImage(pad, (400, 300))
            else:  # als geen geldige image.. return
                return
        else:  # directory selected
            img = ResizeImage(TEST_FOTO, (400, 300))

        self.bitmapSelectedFile.SetSize(img.size)
        self.bitmapSelectedFile.SetBitmap(PilImageToWxBitmap(img))

    def ontvFilesSelChanged(self, event):
        self.PreviewImage(self.tvFiles.GetFilePath())

    def onlistboxSelectedFile(self, event):
        pad = self.listboxSelectedFiles.GetClientData(self.listboxSelectedFiles.GetSelection())
        self.PreviewImage(pad)

# FOLGENDE FUNCTIE LEVERT PROBLEMEN OP MET WINDOWS
#    def onlistboxSelectedFileSetFocus(self, event):
#        if self.listboxSelectedFiles.GetSelection() == wx.NOT_FOUND:
#            return
#        pad = self.listboxSelectedFiles.GetClientData(self.listboxSelectedFiles.GetSelection())
#        self.PreviewImage(pad)

    def onbtnSelectFileClick(self, event):
        _pad = self.tvFiles.GetFilePath()

        # check of bestand al is toegevoegd..
        for _i in range(self.listboxSelectedFiles.Count):
            sPad = self.listboxSelectedFiles.GetClientData(_i)
            if _pad == sPad:
                print("Image is al toegevoegd")
                return

        if _pad != () and _pad != "":
            # file
            if not IsValidImage(_pad):
                return
            helepad = self.tvFiles.GetPath()
            bestandsnaam = os.path.basename(helepad)
            # sla het hele pad op in pyobject clientdata.. toch?
            self.listboxSelectedFiles.Append(bestandsnaam, helepad)
            print bestandsnaam + " toegevoegd"
        # else directory
        else:
            print "Geen geldige image"

    def onbtnUnselectFileClick(self, event):
        sel = self.listboxSelectedFiles.GetSelection()
        if sel < 0:  # nothing selected
            return
        # else
        bl = self.listboxSelectedFiles.GetString(sel)
#        if self.listboxSelectedFiles.getsel
        self.listboxSelectedFiles.Delete(sel)
#        bl = self.listboxSelectedFiles.GetClientData(self.listboxSelectedFiles.GetSelection())
        print bl + " verwijderd"

    def onbtnUploadClick(self, event):
        if len(self.edtLoginName.GetValue()) == 0:
            print("Geen loginnaam ingevoerd")
            return

        filecount = self.listboxSelectedFiles.GetCount()
        if filecount <= 0:
            print("Geen bestand geselecteerd")
            return

        dimensions = getDimensions(self.radio_box_3.GetSelection())
        urls = ""
        for _i in range(filecount):
            print(self.listboxSelectedFiles.GetClientData(_i))
            try:
                resizedFilename = ResizeImage(
                    self.listboxSelectedFiles.GetClientData(_i), dimensions)
                desiredName = DumpImage(resizedFilename, self.edtLoginName.GetValue(), self.listboxSelectedFiles.GetClientData(_i))
#                addToHistory(AUQAOFORUM_PICTURE_URL + desiredName)
                addURL2DB(AUQAOFORUM_PICTURE_URL + desiredName)
                urls = urls + " [IMG]" + AUQAOFORUM_PICTURE_URL + desiredName + "[/IMG]" + "\n"

            except Exception as er:
                self.error = True
                self.errorEx = er
                exit

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
