# importing wx files
# import wx
# import os
# import sys
# import imp
# from PIL import Image
import db
# import wx.lib.agw.ultimatelistctrl as ULC

# import GUI
import maingui
from maingui import dlgVoorbeeld  # , dlgUploadDone, dlgImport, dlgConf
# from Dialog import Dialog

import diversen
from diversen import *

import uploaddialog
# from mechanize._opener import urlopen
import confdialog
from db import DB2JSON, addURL2DB, getUserDimensieID, getUserName, getDimensies  # DBVersion
from db import getUserFolder
from wx import ToolTip

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

#        listTEST = ULC.UltimateListCtrl(self, wx.ID_ANY, agwStyle=wx.LC_REPORT | wx.LC_VRULES | wx.LC_HRULES | wx.LC_SINGLE_SEL | ULC.ULC_HAS_VARIABLE_ROW_HEIGHT)
#        listTEST.InsertColumn(0, "Column 1")
#        listTEST.InsertColumn(1, "Column 2")
#        index = listTEST.InsertStringItem(sys.maxsize, "Item 1")
#        listTEST.SetStringItem(index, 1, "Sub-item 1")
#        index = listTEST.InsertStringItem(sys.maxsize, "Item 2")
#        listTEST.SetStringItem(index, 1, "Sub-item 2")
#        choice = wx.Choice(listTEST, -1, choices=["one", "two"])
#        index = listTEST.InsertStringItem(sys.maxsize, "A widget")
#        listTEST.SetItemWindow(index, 1, choice, expand=True)

#        sizer = wx.BoxSizer(wx.VERTICAL)
# sizer = self.m_panel1.GetSizer()
#        sizer.Add(listTEST, 1, wx.EXPAND)
#        self.SetSizer(sizer)

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

        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)
        ToolTip.Enable(diversen.USER_TOOLTIP)

# ##########

        diversen.USER_FOLDER = getUserFolder()
        if diversen.USER_FOLDER == '' or diversen.USER_FOLDER is None:
            from os.path import expanduser
            pad = expanduser("~")
            # SetPath() triggert ontvFilesSelChanged()
            # en dus ook PreviewImage()
        else:
            pad = diversen.USER_FOLDER
        self.tvFiles.SetPath(pad)

# ##########

        dims = getDimensies()
        self.choiceDimensie.SetItems(dims)
        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)  # index loopt anders dus -1

        self.listFiles.InsertColumn(0, 'Bestand', width=150)
        self.listFiles.InsertColumn(1, 'Dimensie', width=75)
        # hidden-column(2) om het hele pad in te zetten.
        self.listFiles.InsertColumn(2, 'Pad', width=140)

#        self.Layout()
        self.panelPreview.Show(diversen.PREVIEW)
        self.Fit()

    def onmenuitemClickImport(self, event):
        self.ShowImportDialog()

    def onmenuitemClickConf(self, event):
        conf = confdialog.Configure(self)
        conf.CenterOnParent()
        conf.ShowModal()
        conf.Destroy()

        ToolTip.Enable(diversen.USER_TOOLTIP)
        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)
        if diversen.USER_FOLDER:
            self.tvFiles.SetPath(diversen.USER_FOLDER)

        self.panelPreview.Show(diversen.PREVIEW)
        self.Fit()

    def onmenuitemClickAbout(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "Aquaf"
        info.Version = APP_VERSION
        info.Copyright = "(C) 2009-2014"
        info.Description = "Voor het uploaden van plaatjes naar http://www.aquaforum.nl/" + "\n" "en ook het (op de computer) opslaan van een persoonlijk archief van plaatjes die zijn ge-upload."
#        info.Description = wordwrap(
#            "Voor het uploaden van foto's naar http://www.aquaforum.nl/ "
#            "en ook het (op de computer) opslaan van een persoonlijk archief "
#            "van foto's die zijn ge-upload. ",
#            400, wx.ClientDC(self))
        info.WebSite = ("https://github.com/labordus/aquaf", "Aquaf home page")
        info.Developers = ["Riba (2009)",
                           "kellemes (2014-2015)"]

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
        #        dimensions = getDimensions(self.radio_box_3.GetSelection())
        # Als er een plaatje is geselecteerd..
        # gebruik die voor de preview
        _pad = self.tvFiles.GetFilePath()
        if _pad != () and _pad != "":
            if IsValidImage(_pad):
                PLAATJE = self.tvFiles.GetFilePath()
            else:
                PLAATJE = TEST_FOTO
        else:
            PLAATJE = TEST_FOTO

        index = self.choiceDimensie.GetSelection()
        dimensions = getDimensions(index)
        resizedFileName = None
        try:
            if not (os.path.exists(PLAATJE)):
                wx.MessageDialog(self, PLAATJE + " bestaat niet", "Bericht", style=wx.OK).ShowModal()
                resizedFileName = None
                return
            else:
                resizedFileName = ResizeImage(PLAATJE, dimensions)
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

    def onlistFilesSelected(self, event):
        pad = self.listFiles.GetItemText(self.listFiles.GetFirstSelected(), 2)
        self.PreviewImage(pad)

# FOLGENDE FUNCTIE LEVERT PROBLEMEN OP MET WINDOWS
#    def onlistboxSelectedFileSetFocus(self, event):
#        if self.listboxSelectedFiles.GetSelection() == wx.NOT_FOUND:
#            return
#        pad = self.listboxSelectedFiles.GetClientData(self.listboxSelectedFiles.GetSelection())
#        self.PreviewImage(pad)

    def ontvFilesItemActivate(self, event):
        self.onbtnSelectFileClick(event)
        event.Skip()

    def onbtnSelectFileClick(self, event):
        _pad = self.tvFiles.GetFilePath()

        for _i in range(self.listFiles.ItemCount):
            sPad = self.listFiles.GetItemText(_i, 2)
            if _pad == sPad:
                print("Image is al toegevoegd")
                return

        # check of bestand al is toegevoegd..
#        for _i in range(self.listboxSelectedFiles.Count):
#            sPad = self.listboxSelectedFiles.GetClientData(_i)
#            if _pad == sPad:
#                print("Image is al toegevoegd")
#                return

        if _pad != () and _pad != "":
            # file
            if not IsValidImage(_pad):
                return
            helepad = self.tvFiles.GetPath()
            bestandsnaam = os.path.basename(helepad)
            # sla het hele pad op in pyobject clientdata.. toch?
#            self.listboxSelectedFiles.Append(bestandsnaam, helepad)

            index = self.listFiles.InsertStringItem(sys.maxsize, bestandsnaam)
            s = self.choiceDimensie.GetString(self.choiceDimensie.GetSelection())
            self.listFiles.SetStringItem(index, 1, s)
            # Zet het hele pad in de hidden-column(2)
            self.listFiles.SetStringItem(index, 2, helepad)

            print bestandsnaam + " toegevoegd"
        # else directory
#        else:
#            print "Geen geldige image"

    def onbtnUnselectFileClick(self, event):

        sel2 = self.listFiles.GetFirstSelected()
        if sel2 == -1:
            return
        bl = self.listFiles.GetItemText(sel2, 0)
        self.listFiles.DeleteItem(sel2)
        print bl + " verwijderd"

#        sel = self.listboxSelectedFiles.GetSelection()
# if sel < 0:  # nothing selected
#            return
        # else
#        bl = self.listboxSelectedFiles.GetString(sel)
#        if self.listboxSelectedFiles.getsel
#        self.listboxSelectedFiles.Delete(sel)
#        bl = self.listboxSelectedFiles.GetClientData(self.listboxSelectedFiles.GetSelection())

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

#        filecount = self.listboxSelectedFiles.GetCount()
        filecount = self.listFiles.GetItemCount()
        if filecount <= 0:
            print("Geen bestand geselecteerd")
            return

        busyDlg = wx.BusyInfo('Bezig met converten en uploaden van de plaatjes...')
        urls = ""
        for _i in range(filecount):
            print('Uploading ' + self.listFiles.GetItemText(_i, 0))
            try:
                #                resizedFilename = ResizeImage(
                #                    self.listboxSelectedFiles.GetClientData(_i), dimensions)
                dimensions = StringToTupleDimensions(self.listFiles.GetItemText(_i, 1))
                resizedFilename = ResizeImage(
                    self.listFiles.GetItemText(_i, 2), dimensions)
                desiredName = DumpImage(resizedFilename, getUserName(), self.listFiles.GetItemText(_i, 2))
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
