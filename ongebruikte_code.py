def DB2JSONSeperateFile():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')
    dbpath = path_to_db()
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("SELECT * FROM tblLink")
    rows = cursor.fetchall()
    if len(rows) == 0:  # Geen data? Return False
        return False

    rowarray_list = []
    for row in rows:
        t = str((row[1]))  # link
        d = str((row[2]))  # stamp
        rowarray_list.append({"link": t, "stamp": d})
    j = json.dumps({'items': rowarray_list}, indent=2, separators=(',', ': '))

    try:
        fp = open(filepath, "w")
    except IOError:
        # If not exists, create the file
        fp = open(filepath, "w+")
    fp.write(j)
    fp.close()
    connection.close()

    return True

#############################################################################

# class MyServer():
#     HandlerClass = SimpleHTTPRequestHandler
#     ServerClass = BaseHTTPServer.HTTPServer
#     Protocol = "HTTP/1.0"
#     server_address = ("127.0.0.1", 8000)
#     HandlerClass.protocol_version = Protocol
#     httpd = ServerClass(server_address, HandlerClass)
#
#     def run(self):
# sa = self.httpd.socket.getsockname()
# print "Served HTTP on", sa[0], "port", sa[1], "..."
#         import appdirs
#         datapad = appdirs.user_data_dir('aquaf', False, False, False)
#         os.chdir(datapad)
#
#         thread = threading.Thread(target=self.httpd.serve_forever)
#         thread.deamon = True
#         thread.start()
#         sleep(0.25)
#
#     def stop(self):
#         self.httpd.shutdown()
#         os.chdir(oudepad)

class MyBrowser(wx.Dialog):

    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
#        self.SetWindowStyleFlag(wx.RESIZE_BORDER)
#        self.SetWindowStyle(wx.RESIZE_BORDER | wx.CAPTION)
        self.SetWindowStyleFlag(wx.RESIZE_BORDER | wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = wx.html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        self.SetSizer(sizer)
        self.SetSize((800, 900))
        self.Bind(wx.EVT_CLOSE, self.oncloseMyBrowser)
#        serve = MyServer()
#        MyServer.run(serve)

    def oncloseMyBrowser(self, event):
        #         serve = MyServer()
        #         MyServer.stop(serve)
        #         event.Skip()

        # verwijder aquaf.json
#         import appdirs
#         path = appdirs.user_data_dir('aquaf', False, False, False)
#         filepath = os.path.join(path, 'archive.html')
#         try:
#             os.remove(filepath)
#         except OSError:
#             pass

#############################################################################

def IsEmpty_JSON():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')

    f = open(filepath, 'r')
    content = f.read()
    f.close()
    if content.find("link") != -1:
        # already got content
        return False
    else:
        return True

##############################################################################

def Initialize_JSON():
    path = appdirs.user_data_dir('aquaf', False, False, False)
#    check_path_exists(os.path.join(path, 'aquaf.db'))
    filepath = os.path.join(path, 'aquaf.json')
    text = '''{ items: [
]}
'''
    try:
        fp = open(filepath)
    except IOError:
        # If not exists, create the file
        fp = open(filepath, "w+")
        fp.write(text)
    fp.close()

##############################################################################

def addToHistory(url):
    # ########### Add to DB!!! #############
    '''adds the url to the json archive
    '''
    path = appdirs.user_data_dir('aquaf', False, False, False)
#    check_path_exists(os.path.join(path, 'aquaf.db'))
    filepath = os.path.join(path, 'aquaf.json')

#    f = open('images.json', 'r')
    f = open(filepath, 'r')
    content = f.read()
    f.close()
    text = ""
    if content.find("link") != -1:
        # already got content
        text = ","
    template = '''
        {
      "link":"%s"
    }
]}

''' % url
    text = text + template
    content = content.replace("]}", text)
#    f = open('aquaf.json', 'w')
    f = open(filepath, 'w')
    f.write(content)
    f.close()
    return

##############################################################################
    
    def onclickselectjson(self, event):
        import appdirs
        if (sys.platform.startswith('win')):  # dan win32 of win64
            standaarddir = "C:\Program Files\AquaforumUploader"
        else:  # posix
            standaarddir = "@HOME/.local/share"  # dit werkt niet

        dlg = wx.FileDialog(
            self, message="Selecteer images.json",
            #            defaultDir=os.getcwd(),
            defaultDir=standaarddir,
            defaultFile="",
            wildcard='images.json',
            style=wx.OPEN
        )

        if dlg.ShowModal() == wx.ID_OK:
            oudejson = dlg.GetPath()
            # nog effe voor de zekerheid testen..
            head, tail = os.path.split(oudejson)
            if tail != 'images.json':
                print 'verkeerd bestand gekozen'
            else:
                path = appdirs.user_data_dir('aquaf', False, False, False)
                #    check_path_exists(os.path.join(path, 'aquaf.db'))
                filepath = os.path.join(path, 'aquaf.json')
                with open(oudejson) as f:
                    with open(filepath, "w") as f1:
                        for line in f:
                            #                            if "]}" in line:
                            #                            f1.write(rstrip(line))
                            f1.write(line)
                self.m_staticText4.Label = 'Data is geimporteerd, je kunt dit venster nu afsluiten'
# else: # wx.ID_CANCEL
        dlg.Destroy()

##############################################################################

def DB2JSONONGEBUIKT():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')
    connection = sqlite3.connect('/home/kelp/.local/share/aquaf/aquaftest.db')
    cursor = connection.cursor()
    cursor.execute("select linkURL from tblLink")
    rows = cursor.fetchall()
    voortext = '''{ "items": [
'''
    linktext = ""
    for row in rows:
        linktext = linktext + '''
        {
      "link":"%s"
    }
,''' % row[0]

    achtertext = '''
]}
'''
    text = voortext + linktext[:-1] + achtertext

    try:
        fp = open(filepath, "w")
    except IOError:
        # If not exists, create the file
        fp = open(filepath, "w+")
    fp.write(text)
    fp.close()
    connection.close()



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


###############################################################################

def get_executable_path(executable_names):
    '''Look for an executable given a list of the possible names.
    '''
    path = None
    for name in executable_names:
        path = find_executable(name)
        if path:
            break
    return path


def find_chrome():
    """ Find the Chrome executable. """
    path = '/Applications/Google Chrome.app/Contents/MacOS' \
        + os.pathsep \
        + "C:\Program Files\Google\Chrome\Application" \
        + os.pathsep \
        + "C:\Program Files (x86)\Google\Chrome\Application" \
        + os.pathsep \
        + os.environ['PATH']

    # Windows7
    USERPROFILE = os.getenv("USERPROFILE")
    if USERPROFILE:
        path += os.pathsep \
            + USERPROFILE + '\AppData\Local\Google\Chrome\Application'

    exe_names = ('chrome', 'chrome.exe', 'Google Chrome',
                 'google-chrome', 'chromium-browser')

    for name in exe_names:
        pathname = find_executable(name, path)
        if pathname:
            break

    return pathname


def launch_archive(preferred_browser=None):
    ''' Launch web browser on specified port.
        Try to use preferred browser if specified; fall back to default.
        (Chrome will launch in "app mode".)
    '''
    theArchive = get_main_dir()
    theArchive = theArchive.replace("\\", "/")
    if theArchive[-1] != "/":
        theArchive += "/"
    theArchive += "archive.html"

    url = theArchive
    print 'Opening URL in browser: ' + url + ' (pid=' + str(os.getpid()) + ')'

    # webbrowser doesn't know about chrome, so try to find it, use app mode if possible
    if preferred_browser and preferred_browser.lower() == 'chrome':
        chrome_path = find_chrome()
        if chrome_path:
            if sys.platform == 'win32':
                preferred_browser = chrome_path.replace('\\', '\\\\') + ' --app=%s &'
            elif sys.platform == 'darwin':
                chrome_path = chrome_path.replace('Google Chrome', 'Google\ Chrome')
                preferred_browser = 'open -a ' + chrome_path + ' %s'
            elif sys.platform == 'linux2':
                preferred_browser = chrome_path + ' --app=%s &'

    # try to get preferred browser, fall back to default
    if preferred_browser:
        try:
            browser = webbrowser.get(preferred_browser)
        except:
            print "Couldn't get preferred browser (" + preferred_browser + "), using default..."
            browser = webbrowser.get()
    else:
        browser = webbrowser.get()

    # open new browser window (may open in a tab depending on user preferences, etc.)
    if browser:
        browser.open(url, 1, True)
        try:
            print "Opened in", browser.name
        except AttributeError:
            pass  # Happens with safari.
    else:
        print "Couldn't launch browser: " + str(browser)

###############################################################################

class ValideerInvoer(wx.PyValidator):

    def __init__(self, flag=None, pyVar=None):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        return ValideerInvoer(self.flag)

    def Validate(self, win):
        tc = self.GetWindow()
        val = tc.GetValue()

        if self.flag == ALPHA_ONLY:
            for x in val:
                if x not in string.letters:
                    return False

        elif self.flag == DIGIT_ONLY:
            for x in val:
                if x not in string.digits:
                    return False

        return True

    def OnChar(self, event):
        key = event.GetKeyCode()

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if self.flag == ALPHA_ONLY and chr(key) in string.letters:
            event.Skip()
            return

        if self.flag == DIGIT_ONLY and chr(key) in string.digits:
            event.Skip()
            return

        if not wx.Validator_IsSilent():
            wx.Bell()

        # Returning without calling even.Skip eats the event before it
        # gets to the text control
        return