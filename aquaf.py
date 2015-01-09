import db

# import GUI
import maingui
from maingui import dlgVoorbeeld

import diversen
from diversen import *

import uploaddialog
import confdialog
from db import DB2Webfile, addDATA2DB, getUserDimensieID, getUserName, getDimensies  # DBVersion
from db import getUserFolder, getUserTooltip
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
        diversen.USER_TOOLTIP = getUserTooltip()
        ToolTip.Enable(diversen.USER_TOOLTIP)

        diversen.USER_FOLDER = getUserFolder()
        if diversen.USER_FOLDER == '' or diversen.USER_FOLDER is None:
            from os.path import expanduser

            pad = expanduser("~")
            # SetPath() triggert ontvFilesSelChanged()
            # en dus ook PreviewImage()
        else:
            pad = diversen.USER_FOLDER
        self.tvFiles.SetPath(pad)

        dims = getDimensies()
        self.choiceDimensie.SetItems(dims)
        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)  # index loopt anders dus -1

        self.listFiles.InsertColumn(0, 'Bestand', width=150)
        self.listFiles.InsertColumn(1, 'Dimensie', width=75)
        self.listFiles.InsertColumn(2, 'Pad', width=140)

#        self.Layout()
        self.panelPreview.Show(diversen.PREVIEW)
        self.Fit()

    def onmenuitemClickConf(self, event):
        conf = confdialog.Configure(self)
        conf.CenterOnParent()
        conf.ShowModal()
        conf.Destroy()

        ToolTip.Enable(diversen.USER_TOOLTIP)
        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)
#        if diversen.USER_FOLDER:
#            self.tvFiles.SetPath(diversen.USER_FOLDER)

        self.panelPreview.Show(diversen.PREVIEW)
        self.Fit()

    def onmenuitemClickAbout(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "Aquaf"
        info.Version = APP_VERSION
        info.Copyright = "(C) 2009-2014"
        info.Description = """Voor het uploaden van foto's naar http://www.aquaforum.nl/""" + """\n""" """en ook het (op de computer) opslaan van een persoonlijk archief van foto's die zijn ge-upload."""
        info.WebSite = ("https://github.com/labordus/aquaf", "Aquaf home page")
        info.Developers = ["Riba (2009)",
                           "kellemes (2014-2015)"]

        wx.AboutBox(info)

    def onbtnVoorbeeldClick(self, event):
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
                print("""Foto is al toegevoegd""")
                return

        if _pad != () and _pad != "":
            # file
            if not IsValidImage(_pad):
                return
            helepad = self.tvFiles.GetPath()
            bestandsnaam = os.path.basename(helepad)

            index = self.listFiles.InsertStringItem(sys.maxsize, bestandsnaam)
            s = self.choiceDimensie.GetString(self.choiceDimensie.GetSelection())
            self.listFiles.SetStringItem(index, 1, s)
            self.listFiles.SetStringItem(index, 2, helepad)

            print bestandsnaam + " toegevoegd"

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

        filecount = self.listFiles.GetItemCount()
        if filecount <= 0:
            print("Geen bestand geselecteerd")
            return

        busyDlg = wx.BusyInfo("""Bezig met converten en uploaden van de foto's...""")
        urls = ""
        for _i in range(filecount):
            print('Uploading ' + self.listFiles.GetItemText(_i, 0))
            try:
                dimensions = StringToTupleDimensions(self.listFiles.GetItemText(_i, 1))
                resizedFilename = ResizeImage(
                    self.listFiles.GetItemText(_i, 2), dimensions)
                desiredName, dimWidth, dimHeight = DumpImage(resizedFilename, getUserName(), self.listFiles.GetItemText(_i, 2))
                url = AUQAOFORUM_PICTURE_URL + desiredName
                addDATA2DB(url, dimWidth, dimHeight)
                urls = urls + " [IMG]" + AUQAOFORUM_PICTURE_URL + desiredName + "[/IMG]" + "\n"

            except Exception as er:
                self.error = True
                self.errorEx = er
                del busyDlg
                exit
        self.listFiles.ClearAll()
        del busyDlg
        dlg = uploaddialog.UploadDoneDialog(self)
        dlg.setCode(urls)
        dlg.CenterOnParent()
        dlg.ShowModal()  # this one is non blocking!!
        dlg.Destroy()

    def onbtnArchiefClick(self, event):
        import appdirs
        path = appdirs.user_data_dir('aquaf', False, False, False)
# constructie van URL cross-safe?
        weburl = "file://" + os.path.join(path, 'archive.html')

        if not DB2Webfile():
            print 'Niets te tonen'
            return

        from archiveview import MyBrowser

        dialog = MyBrowser(None, -1)
        dialog.browser.LoadURL(weburl)
        dialog.CenterOnParent()
        dialog.ShowModal()
        dialog.Destroy()
        return

app = wx.App(False)

frame = AquaFrame(None)
frame.Show(True)
app.MainLoop()
