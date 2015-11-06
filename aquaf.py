import db

# import GUI
import maingui
from maingui import dlgVoorbeeld

import diversen
from diversen import *

import uploaddialog
import confdialog
import updatedialog
from db import DB2JSON, DB2Webfile, addDATA2DB, getUserDimensieID, getDimensies
from db import FillGlobals
from wx import ToolTip
AUQAOFORUM_PICTURE_URL = "http://www.aquaforum.nl/gallery/upload/"
TEST_FOTO = "test.jpg"
FRONT_FOTO = "front.jpg"
ROTATE_IMAGE = 0
DIM_IMAGE = ''
PREVIEW_ON = False
ONLINE_PREVIEW = 0
ONLINE_TEMPFILE = ''
FOTO_IN_PREVIEW = ''


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

        FillGlobals()

#        diversen.USER_WEBNIEUW = getUserWebNieuw()

        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
#        self.SetSize((702, 538))

        log = self.infoBox
        # redirect text here
        redir = RedirectText(log)
        sys.stdout = redir

        # Windows laat anders dubbele entries zien,
        # en linux laat alleen bestanden zien met specifieke casing

        if (sys.platform.startswith('win')):  # dan win32 of win64
            self.tvFiles.SetFilter("plaatjes(*.bmp;*.jpg;*.png;*.tiff;*.tif;*.gif;*.ico;)|*.bmp;*.jpg;*.png;*.tiff;*.tif;*.gif;*.ico")
        else:  # posix
            self.tvFiles.SetFilter("plaatjes(*.bmp;*.BMP;*.jpg;*.JPG;*.png;*.PNG;*.tiff;*.TIFF;*.tif;*.TIF;*.gif;*.GIF;*.ico;*.ICO)|*.bmp;*.BMP;*.jpg;*.JPG;*.png;*.PNG;*.tiff;*.TIFF;*.tif;*.TIF;*.gif;*.GIF;*.ico;*.ICO")

        print "Hoi " + diversen.USER_USERNAME
        print "Welkom bij Aquaf " + APP_VERSION

        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)
        ToolTip.Enable(diversen.USER_TOOLTIP)

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
        self.listFiles.InsertColumn(2, 'Rotatie', width=60)
        self.listFiles.InsertColumn(3, 'Pad', width=140)

        self.SetPreview(diversen.USER_PREVIEW)

        if diversen.USER_UPDATECHECK:
            ReleaseVersion, ReleaseDate, ReleaseChanges = UpdateAvailable()
            if ReleaseVersion != '':
                update = updatedialog.Update(self)
                update.LoadText(ReleaseVersion, ReleaseDate, ReleaseChanges)
                update.CenterOnParent()
                update.ShowModal()
                update.Destroy()

# Hier zet ik de size van frame KEIHARD.. conform "bestsize" zoals aangegeven door WIT.
        self.SetSize((1130, 800))

#        self.SendSizeEvent()
#        self.SetAutoLayout(True)
#        self.Layout()
#        self.Fit()

        # for wxMSW
#        self.tvFiles.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OntvFilesRightClick)
        # for wxGTK
#        self.tvFiles.Bind(wx.EVT_RIGHT_UP, self.OntvFilesRightClick)

    def OntvFilesRightClick(self, event):
        #        self.log.WriteText("OnRightClick %s\n" % self.list.GetItemText(self.currentItem))
        # only do this part the first time so the events are only bound once
        if not hasattr(self.tvFiles, "popupUploadList"):
            self.tvFiles.popupUploadList = wx.NewId()
#            self.tvFiles.popupStandaardMap = wx.NewId()
            self.tvFiles.Bind(wx.EVT_MENU, self.OnPopupUploadList, id=self.tvFiles.popupUploadList)
#            self.tvFiles.Bind(wx.EVT_MENU, self.OnPopupStandaardMap, id=self.tvFiles.popupStandaardMap)

        menu = wx.Menu()
        menu.Append(self.tvFiles.popupUploadList, "Zet in uploadlijst")
#        menu.Append(self.tvFiles.popupStandaardMap, "Maak standaard map")

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.tvFiles.PopupMenu(menu)
        menu.Destroy()

    def OnPopupUploadList(self, event):
        self.onbtnToevoegenClick(event)

    def onmenuitemClickConf(self, event):
        conf = confdialog.Configure(self)
        conf.CenterOnParent()
        conf.ShowModal()
        conf.Destroy()

        ToolTip.Enable(diversen.USER_TOOLTIP)
        self.choiceDimensie.SetSelection(getUserDimensieID() - 1)
#        if diversen.USER_FOLDER:
#            self.tvFiles.SetPath(diversen.USER_FOLDER)
#        if self.panelPreview.IsShown() != diversen.USER_PREVIEW:
#            self.panelPreview.Show(diversen.USER_PREVIEW)
#            self.Fit()
        self.SetPreview(diversen.USER_PREVIEW)

    def SetPreview(self, prv=False):
        #        if self.panelPreview.IsShown() == prv:  # reset nodig?
        #            return
        #        else:
        #            if not prv:
        global PREVIEW_ON
        PREVIEW_ON = prv
        # self.lblDimensie.SetLabelText(self.choiceDimensie.GetString(self.choiceDimensie.GetSelection()))
        self.lblDimensie.SetLabelText(DIM_IMAGE)
        self.lblRotatie.SetLabelText(str(ROTATE_IMAGE))

        self.panelPreview.Show(prv)
        self.panelPreviewInfo.Show(not prv)
        self.Fit()

        if not prv:  # geen Preview dan..
            self.btnToevoegen.SetLabel('-->')
            self.btnVerwijderen.SetLabel('<--')
            self.btnVoorbeeld.SetLabel('Prv')
        else:  # als Preview dan..
            self.btnToevoegen.SetLabel('Toevoegen  ->')
            self.btnVerwijderen.SetLabel('<- Verwijderen')
            self.btnVoorbeeld.SetLabel(' Preview ')

    def onbtneditmodeon(self, event):
        PREVIEW_ON = True
        self.SetPreview(True)

    def onbtneditmodeoff(self, event):
        PREVIEW_ON = False
        self.SetPreview(False)

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

        if ONLINE_PREVIEW == 1:  # als actieve view een online foto is..
            PLAATJE = ONLINE_TEMPFILE
        else:
            # Als er een plaatje is geselecteerd..
            # gebruik die voor de preview
            _pad = ''
            padjes = self.tvFiles.GetFilePaths()
            for pad in padjes:
                _pad = pad
                break

    #        _pad = self.tvFiles.GetFilePath()
            if _pad != () and _pad != "":
                if IsValidImage(_pad):
                    #                PLAATJE = self.tvFiles.GetFilePath()
                    PLAATJE = _pad
                else:
                    PLAATJE = TEST_FOTO
            else:
                PLAATJE = TEST_FOTO

#            if not diversen.USER_PREVIEW:
            if not PREVIEW_ON:
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
        resizedFileName = resizedFileName.rotate(ROTATE_IMAGE)
        Voorbeeld.bitmapVoorbeeld.SetBitmap(PilImageToWxBitmap(resizedFileName))
        Voorbeeld.Fit()
        Voorbeeld.Layout()
        Voorbeeld.CenterOnParent()
        Voorbeeld.ShowModal()
        Voorbeeld.Destroy()

    def onbtnRotateClick(self, event):
        global ROTATE_IMAGE
        if ROTATE_IMAGE == 270:
            ROTATE_IMAGE = 0
        else:
            ROTATE_IMAGE += 90

        if ONLINE_PREVIEW:
            self.PreviewImage(ONLINE_TEMPFILE)
        else:
            #            padjes = self.tvFiles.GetFilePaths()
            #            for pad in padjes:
            #                self.PreviewImage(pad)
            #                return
            self.PreviewImage(FOTO_IN_PREVIEW)

    def PreviewImage(self, pad='', forcepreview=False):
        global FOTO_IN_PREVIEW
        FOTO_IN_PREVIEW = pad
        #        if not diversen.USER_PREVIEW:
        if not PREVIEW_ON:
            self.lblRotatie.SetLabelText(str(ROTATE_IMAGE))
            # self.lblDimensie.SetLabelText(self.choiceDimensie.GetString(self.choiceDimensie.GetSelection()))
            self.lblDimensie.SetLabelText(DIM_IMAGE)
            self.bitmapSelectedFile.SetBitmap(wx.Bitmap(FRONT_FOTO))
            return
        global ROTATE_IMAGE

        if pad != () and pad != "":
            # file selected
            if IsValidImage(pad):
                #                busyDlg = wx.BusyInfo('Bezig met genereren preview...')
                try:
                    img = ResizeImage(pad, (400, 300))
                except Exception as IOError:
                    print 'onbekend formaat'
                    img = WxBitmapToPilImage(wx.Bitmap(FRONT_FOTO))
                    ROTATE_IMAGE = 0
#                del busyDlg
            else:  # als geen geldige image..
                #                img = ResizeImage(TEST_FOTO, (400, 300))
                img = WxBitmapToPilImage(wx.Bitmap(FRONT_FOTO))
                ROTATE_IMAGE = 0
        else:  # directory selected
            #            img = ResizeImage(TEST_FOTO, (400, 300))
            img = WxBitmapToPilImage(wx.Bitmap(FRONT_FOTO))
#        img = img.rotate(90, expand=True)
#        img = img.rotate(270)
        if pad == FRONT_FOTO:
            ROTATE_IMAGE = 0
        img = img.rotate(ROTATE_IMAGE)
        self.bitmapSelectedFile.SetSize(img.size)
        self.bitmapSelectedFile.SetBitmap(PilImageToWxBitmap(img))
        self.bitmapSelectedFile.Center()

        self.Layout()

    def onbtnClearLogClick(self, event):
        self.infoBox.Clear()

    def ontvFilesSelChanged(self, event):
        global ONLINE_PREVIEW
        ONLINE_PREVIEW = 0
        global ROTATE_IMAGE
        ROTATE_IMAGE = 0

        padjes = self.tvFiles.GetFilePaths()
        if len(padjes) > 1:
            self.PreviewImage(FRONT_FOTO)
            return
        for pad in padjes:
            self.PreviewImage(pad)

        self.deselectItems()
        #        self.PreviewImage(self.tvFiles.GetFilePath())

#        padjes = self.tvFiles.GetFilePaths()
#        print padjes

        #        padjes = self.tvFiles.GetFilePaths()
        #        for pad in padjes:
        #            print pad
#        print('SelChange')

    def onlistFilesFocused(self, event):
        print 'onlistFilesFocused'

    def onlistFilesSelected(self, event):
        print 'onlistFilesSelected'
        self.tvFiles.UnselectAll()
        if self.listFiles.SelectedItemCount > 1:
            self.PreviewImage(FRONT_FOTO)
            return

        global ROTATE_IMAGE
        pad = os.path.join(self.listFiles.GetItemText(self.listFiles.GetFirstSelected(), 3),
                           self.listFiles.GetItemText(self.listFiles.GetFirstSelected(), 0))
        ROTATE_IMAGE = int(self.listFiles.GetItemText(self.listFiles.GetFirstSelected(), 2))
        dim = self.listFiles.GetItemText(self.listFiles.GetFirstSelected(), 1)
        global DIM_IMAGE
        DIM_IMAGE = dim
        self.PreviewImage(pad)
        global FOTO_IN_PREVIEW
        FOTO_IN_PREVIEW = pad
# ############################################

#         index = self.choiceDimensie.GetSelection()
#         dimensions = getDimensions(index)
#         resizedFileName = None
#         try:
#             if not (os.path.exists(pad)):
#                 wx.MessageDialog(self, pad + " bestaat niet", "Bericht", style=wx.OK).ShowModal()
#                 resizedFileName = None
#                 return
#             else:
#                 resizedFileName = ResizeImage(pad, dimensions)
#         except Exception as er:
#             resizedFileName = None
#             wx.MessageDialog(
#                 self,
#                 "Er is een fout opgetreden tijdens het converteren\n" +
#                 "De error is " + str(er),
#                 "Bericht", style=wx.OK).ShowModal()
#             return
#         Voorbeeld = dlgVoorbeeld(self)
#         Voorbeeld.SetTitle(str(dimensions))
#         resizedFileName = resizedFileName.rotate(ROTATE_IMAGE)
#         Voorbeeld.bitmapVoorbeeld.SetBitmap(PilImageToWxBitmap(resizedFileName))
#         Voorbeeld.Fit()
#         Voorbeeld.Layout()
#         Voorbeeld.CenterOnParent()
#         Voorbeeld.ShowModal()
#         Voorbeeld.Destroy()
# ############################################


# FOLGENDE FUNCTIE LEVERT PROBLEMEN OP MET WINDOWS
#    def onlistboxSelectedFileSetFocus(self, event):
#        if self.listboxSelectedFiles.GetSelection() == wx.NOT_FOUND:
#            return
#        pad = self.listboxSelectedFiles.GetClientData(self.listboxSelectedFiles.GetSelection())
#        self.PreviewImage(pad)

    def ontvFilesItemActivate(self, event):
        self.onbtnToevoegenClick(event)
        event.Skip()

    def VoegPadToe(self, pad):
        #                helepad = self.tvFiles.GetPath()
        helepad = os.path.dirname(pad)
        bestandsnaam = os.path.basename(pad)

        index = self.listFiles.InsertStringItem(sys.maxsize, bestandsnaam)
        dim = self.choiceDimensie.GetString(self.choiceDimensie.GetSelection())
        r = str(ROTATE_IMAGE)
        self.listFiles.SetStringItem(index, 1, dim)
        self.listFiles.SetStringItem(index, 2, r)
        self.listFiles.SetStringItem(index, 3, helepad)
        return index

    def onbtnToevoegenClick(self, event):
        if ONLINE_PREVIEW == 1:  # online file to handel
            if len(self.edtURL.GetValue()) == 0:
                print "Niets ingevoerd"
            else:
                #                if not ONLINE_TEMPFILE == '':
                #                    os.remove(ONLINE_TEMPFILE)
                path = ONLINE_TEMPFILE  # online_image_temp(self.edtURL.GetValue())
                if path == '':
                    print 'Foto niet gevonden op de server'
                else:  # Er is iets gevonden.. is dit de foto?
                    #                if IsValidImage(path):
                    self.edtURL.Clear()
                    idx = self.VoegPadToe(path)
                    self.deselectItems()
                    self.listFiles.Select(idx, 1)
#                    self.tvFiles.UnselectAll()
#                    self.SetPreview(diversen.USER_PREVIEW)
        else:  # check of (lokaal) bestand al is toegevoegd.
            # ALS ER GEEN SELECTIE IS IN TVFILES MAAR WEL EEN FOTO_IN_PREVIEW.. AFHANDELEN!!
            breaker = 0
            padjes = self.tvFiles.GetFilePaths()
            for _pad in padjes:
                for _i in range(self.listFiles.ItemCount):
                    breaker = 0
                    sPad = os.path.join(self.listFiles.GetItemText(_i, 3),
                                        self.listFiles.GetItemText(_i, 0))
                    if _pad == sPad:  # Foto is al toegevoegd.. updaten?
                        dlg = wx.MessageDialog(None, """Foto is al toegevoegd. \n""" +
                                               """Bestaande foto updaten?""", 'Updaten', wx.YES_NO | wx.ICON_QUESTION)
                        result = dlg.ShowModal()
                        if result == wx.ID_NO:
                            dlg.Destroy()
                            breaker = 1
                            break
                        else:  # update
                            self.listFiles.SetStringItem(_i, 1, self.choiceDimensie.GetString(self.choiceDimensie.GetSelection()))  # dim
                            self.listFiles.SetStringItem(_i, 2, str(ROTATE_IMAGE))  # rotation
#                            self.listFiles.Select(_i, 1)
#                             self.listFiles.DeleteItem(_i)
#                             if IsValidImage(_pad):
#                                 idx = self.VoegPadToe(_pad)
#                                 self.deselectItems()
#                                 self.listFiles.Select(idx, 1)
                            breaker = 1
                            break
                if breaker == 0:  # Geen zelfde foto gevonden in de uploadlijst.
                    if IsValidImage(_pad):
                        idx = self.VoegPadToe(_pad)
                        self.deselectItems()
                        self.listFiles.Select(idx, 1)
            self.tvFiles.UnselectAll()

# #####################################################################################
    def deselectItems(self):
        sel = self.listFiles.GetFirstSelected()
        while sel != -1:
            self.listFiles.SetItemState(sel, 0, wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED)
            sel = self.listFiles.GetNextSelected(sel)

    def onbtnPreviewOnlineClick(self, event):
        global ROTATE_IMAGE
        ROTATE_IMAGE = 0
        if len(self.edtURL.GetValue()) == 0:
            print "Niets ingevoerd"
        else:
            #            if not ONLINE_TEMPFILE == '':
            #                os.remove(ONLINE_TEMPFILE)
            path = online_image_temp(self.edtURL.GetValue())
            global ONLINE_TEMPFILE
            ONLINE_TEMPFILE = path
            if path == '':
                # 'http://www.aquaforum.nl/gallery/upload/339568kellemes_0_85_download.jpg'
                #        if not image_exists('http://blog.webboda.es/wp-content/uploads/2030/01/fotorama-foto-5.jpeg'):
                print 'Foto niet gevonden op de server'
            else:  # Er is iets gevonden.. is dit de foto?
                #                if IsValidImage(path):
                global ONLINE_PREVIEW
                ONLINE_PREVIEW = 1
#                self.choiceDimensie.SetSelection(0)
                self.SetPreview(True)
                self.PreviewImage(path)

    def onbtnVerwijderenClick(self, event):
        # Zet hier de lijst met geselecteerde items in een array, en gebruik die array
        # later in REVERSED-ORDER voor het wissen van de items.
        # Dit aangezien bij het wissen van items ook de item-index veranderd..
        # Zie hier: https://wiki.wxwidgets.org/WxListCtrl#Deleting_Selected_Rows
        selItems = []
        item = self.listFiles.GetFirstSelected()
        while item != -1:
            selItems.append(item)
            item = self.listFiles.GetNextSelected(item)

        for _i in reversed(selItems):
            self.listFiles.DeleteItem(_i)

    def onbtnUploadClick(self, event):
        filecount = self.listFiles.GetItemCount()
        if filecount <= 0:
            print("Geen bestand geselecteerd")
            return

        if not diversen.USER_USERNAME:
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

        busyDlg = wx.BusyInfo("""Bezig met converten en uploaden van de foto's...""")
        urls = ""
        for _i in range(filecount):
            print('Uploading ' + self.listFiles.GetItemText(_i, 0))
            try:
                dimensions = StringToTupleDimensions(self.listFiles.GetItemText(_i, 1))
                resizedFilename = ResizeImage(os.path.join(self.listFiles.GetItemText(_i, 3),
                                                           self.listFiles.GetItemText(_i, 0)), dimensions)
                # ROTEREN
                resizedFilename = resizedFilename.rotate(int(self.listFiles.GetItemText(_i, 2)))
                # ##
                desiredName, dimWidth, dimHeight = DumpImage(resizedFilename, diversen.USER_USERNAME, self.listFiles.GetItemText(_i, 3))
                url = AUQAOFORUM_PICTURE_URL + desiredName
                addDATA2DB(url, dimWidth, dimHeight)
                urls = urls + " [IMG]" + AUQAOFORUM_PICTURE_URL + desiredName + "[/IMG]" + "\n"

            except Exception as er:
                self.error = True
                self.errorEx = er
                del busyDlg
                exit
#        self.listFiles.ClearAll()
        diversen.delete_tempfiles()
        self.listFiles.DeleteAllItems()
        del busyDlg
        dlg = uploaddialog.UploadDoneDialog(self)
        dlg.setCode(urls)
        dlg.CenterOnParent()
        dlg.ShowModal()  # this one is non blocking!!
        dlg.Destroy()

    def onbtnArchiefClick(self, event):

        if diversen.USER_WEBNIEUW:
            # ########### NIEUWE WEBSITE ####################
            import appdirs
            path = appdirs.user_data_dir('aquaf', False, False, False)
            # constructie van URL cross-safe?
            weburl = "file://" + os.path.join(path, 'archivenew.html')

            if not DB2Webfile():
                print 'Niets te tonen'
                return

            from archiveview import MyBrowserNew

            dialog = MyBrowserNew(None, -1)
            dialog.browser.LoadURL(weburl)
            dialog.CenterOnParent()
            dialog.ShowModal()
            dialog.Destroy()
            return
        else:
            # ########### OUDE WEBSITE ####################
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

    def onbtnClearListClick(self, event):
        #        self.listFiles.ClearAll()
        diversen.delete_tempfiles()
        self.listFiles.DeleteAllItems()
#        global FOTO_IN_PREVIEW
#        FOTO_IN_PREVIEW = ''
        padjes = self.tvFiles.GetFilePaths()
        for _pad in padjes:
            self.PreviewImage(_pad)

    def onmenuitemClickAfsluiten(self, event):
        self.Close()

    def onbtnWITclick(self, event):
        import wx.lib.inspection
        wx.lib.inspection.InspectionTool().Show()

    def oncloseMainframe(self, event):
        # checken of er nog foto's klaar staan in de uploadlijst.
        if self.listFiles.GetItemCount() != 0:
            dlg = wx.MessageDialog(None, '''Je hebt nog foto's in de uploadlijst staan \n''' +
                                   '''Wil je toch afsluiten?''', 'Afsluiten of upload?', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                return
        diversen.delete_tempfiles()
        event.Skip()

app = wx.App(False)

frame = AquaFrame(None)
frame.Show(True)
app.MainLoop()
