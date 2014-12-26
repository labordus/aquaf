# importing wx files
# import wx
# import os
# import sys
# import imp
# from PIL import Image
import db

# import GUI
import maingui
from maingui import dlgVoorbeeld  # , dlgUploadDone, dlgImport, dlgConf
# from Dialog import Dialog

import diversen
from diversen import *

import uploaddialog
# from mechanize._opener import urlopen
import confdialog
from db import DB2JSON, addURL2DB, getUserDimensieID, getUserName  # DBVersion

AUQAOFORUM_PICTURE_URL = "http://www.aquaforum.nl/gallery/upload/"
TEST_FOTO = "test.jpg"
FRONT_FOTO = "front.jpg"


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

        if db.Initialize_db() is False:
            app.Exit()
#        if db.first_run() == 1:
#            dlg = wx.MessageDialog(None, 'Import data van vorige versie van deze applicatie?', 'Import', wx.YES_NO | wx.ICON_QUESTION)
#            result = dlg.ShowModal()
#            if result == wx.ID_YES:
#                dlg.Destroy()

        diversen.PREVIEW = db.getUserPreview()

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

        userName = db.getUsername()
        print "Hoi " + userName
        print "Welkom bij Aquaf " + APP_VERSION

        self.radio_box_3.SetSelection(getUserDimensieID() - 1)

        from os.path import expanduser
        home = expanduser("~")
        # SetPath() triggert ontvFilesSelChanged()
        # en dus ook PreviewImage()
        self.tvFiles.SetPath(home)

    def onmenuitemClickImport(self, event):
        self.ShowImportDialog()

    def onmenuitemClickConf(self, event):
        conf = confdialog.Configure(self)
        conf.CenterOnParent()
        conf.ShowModal()
        conf.Destroy()
        self.radio_box_3.SetSelection(getUserDimensieID() - 1)

    def onmenuitemClickAbout(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "Aquaf"
        info.Version = APP_VERSION
        info.Copyright = "(C) 2010-2014"
        info.Description = "Voor het uploaden van plaatjes naar http://www.aquaforum.nl/" + "\n" "en ook het (op de computer) opslaan van een persoonlijk archief van plaatjes die zijn ge-upload."
#        info.Description = wordwrap(
#            "Voor het uploaden van foto's naar http://www.aquaforum.nl/ "
#            "en ook het (op de computer) opslaan van een persoonlijk archief "
#            "van foto's die zijn ge-upload. ",
#            400, wx.ClientDC(self))
        info.WebSite = ("https://github.com/labordus/aquaf", "Aquaf home page")
        info.Developers = ["Riba",
                           "kellemes"]

        wx.AboutBox(info)

    def onbtnArchiefClick(self, event):
        #        webbrowser.get("chrome").open_new_tab(theArchive)
        #        webbrowser.get("firefox").open_new(theArchive)
        if not DB2JSON():
            print 'Niets te tonen'
            return

        from archiveview import MyBrowser
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
        if not diversen.PREVIEW:
            self.bitmapSelectedFile.SetBitmap(wx.Bitmap(FRONT_FOTO))
            return

        if pad != () and pad != "":
            # file selected
            if IsValidImage(pad):
                #                busyDlg = wx.BusyInfo('Bezig met genereren preview...')
                img = ResizeImage(pad, (400, 300))
#                del busyDlg
            else:  # als geen geldige image..
                #                img = ResizeImage(TEST_FOTO, (400, 300))
                img = WxBitmapToPilImage(wx.Bitmap(FRONT_FOTO))
        else:  # directory selected
            #            img = ResizeImage(TEST_FOTO, (400, 300))
            img = WxBitmapToPilImage(wx.Bitmap(FRONT_FOTO))
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
        #        if len(self.edtLoginName.GetValue()) == 0:
        if not getUserName():
            dlg = wx.TextEntryDialog(
                self, 'Voer hier je aquaforum.nl gebruikersnaam in..',
                'Gebruikersnaam')
            if dlg.ShowModal() == wx.ID_OK:
                if dlg.GetValue() == "":
                    print("Geen gebruikersnaam ingevoerd")
                    dlg.Destroy()
                    return
                else:
                    db.setUsername(dlg.GetValue())
            else:
                print("Geen gebruikersnaam ingevoerd")
                dlg.Destroy()
                return
            dlg.Destroy()

#        db.set_username(sUsername)
#        db.set_username(self.edtLoginName.GetValue())

        filecount = self.listboxSelectedFiles.GetCount()
        if filecount <= 0:
            print("Geen bestand geselecteerd")
            return

        busyDlg = wx.BusyInfo('Bezig met converten en uploaden van de plaatjes...')
        dimensions = getDimensions(self.radio_box_3.GetSelection())
        urls = ""
        for _i in range(filecount):
            print(self.listboxSelectedFiles.GetClientData(_i))
            try:
                resizedFilename = ResizeImage(
                    self.listboxSelectedFiles.GetClientData(_i), dimensions)
                desiredName = DumpImage(resizedFilename, self.edtLoginName.GetValue(), self.listboxSelectedFiles.GetClientData(_i))
                addURL2DB(AUQAOFORUM_PICTURE_URL + desiredName)
                urls = urls + " [IMG]" + AUQAOFORUM_PICTURE_URL + desiredName + "[/IMG]" + "\n"

            except Exception as er:
                self.error = True
                self.errorEx = er
                del busyDlg
                exit

        del busyDlg
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
