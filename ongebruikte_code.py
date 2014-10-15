###############################################################################

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

###############################################################################

###########################################################################
# def onbtnSelectFile1Click(self, event):
###########################################################################
#     def onbtnSelectFile1Click(self, event):
#         """ Open a file"""
#         self.dirname = ''
#         dlg = wx.FileDialog(self, "Choose a file", self.dirname,
#                             "", "*.*", wx.OPEN)
#         dlg.SetWildcard(
#             "plaatjes (*.bmp;*.jpg;*.png;*.tiff)|*.bmp;*.jpg;*.png;*.tiff|Alles (*.*)|*.*")
#         if dlg.ShowModal() == wx.ID_OK:
#             self.edtFile1.SetValue(dlg.GetPath())
#         dlg.Destroy()

###############################################################################

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

###############################################################################

# create custom event
UPLOAD_DONE_EVENT_TYPE = wx.NewEventType()
EVT_UPLOAD_DONE = wx.PyEventBinder(UPLOAD_DONE_EVENT_TYPE, 1)

###############################################################################

        self.Bind(EVT_UPLOAD_DONE, self.OnEventUploadDone)
        EVT_UPLOAD_DONE(self, -1, self.OnEventUploadDone)


##########################################################

###########################################################################
# class UploadDoneEvent(wx.PyCommandEvent):
###########################################################################


class UploadDoneEvent(wx.PyCommandEvent):
    eventType = UPLOAD_DONE_EVENT_TYPE

    def __init__(self, windowID):
        wx.PyCommandEvent.__init__(self, self.eventType, windowID)

    def Clone(self):
        self.__class__(self.GetId())

###########################################################
                # done, send done event

                #        event = UploadDoneEvent(self.GetId())
                #        self.GetEventHandler().AddPendingEvent(event)

###########################################################

#    def oninitdlgUploadDone(self, event):
#        maingui.dlgUploadDone.oninitdlgUploadDone(self, event)
#        print "oninitdlgUploadDone"

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


###############################################################################

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
