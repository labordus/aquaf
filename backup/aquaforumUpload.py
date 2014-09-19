# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.3.5.1 on Wed Aug 31 13:50:35 2005

import wx
import aquaupload
import thread
import os
import imp
import sys
import webbrowser

AUQAOFORUM_PICTURE_URL="http://www.aquaforum.nl/gallery/upload/"

#create custom event
UPLOAD_DONE_EVENT_TYPE = wx.NewEventType() 
EVT_UPLOAD_DONE = wx.PyEventBinder(UPLOAD_DONE_EVENT_TYPE, 1) 

class UploadDoneEvent(wx.PyCommandEvent): 
    eventType = UPLOAD_DONE_EVENT_TYPE 
    def __init__(self, windowID): 
        wx.PyCommandEvent.__init__(self, self.eventType, windowID) 
 
    def Clone( self ): 
        self.__class__( self.GetId() ) 

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "Het bericht is geplaatst op aquaforum. Je kan de volgende code gebruiken in je bericht:")
        self.text_ctrl_Code = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_LINEWRAP)
        self.button_1 = wx.Button(self, -1, "Zet de code in het klembord (clipboard)")
        self.label_2 = wx.StaticText(self, -1, "Als je op de knop \"Zet de code in het klembord (clipboard)\" drukt, dan kan je vervolgens naar het aquaforum surfen met je browser. \nMaak een bericht waar je het plaatje in wilt hebben, klik rechts met de muis in het bericht  en kies \"plakken\" (of \"paste\"). \nDan staat de code in het bericht.")
        self.button_2 = wx.Button(self, -1, "Klaar")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("Bericht")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(0, 127, 255))
        self.label_1.SetBackgroundColour(wx.Colour(0, 127, 255))
        self.text_ctrl_Code.SetSize((400, 127))
        self.label_2.SetBackgroundColour(wx.Colour(0, 127, 255))
        # end wxGlade
        wx.EVT_BUTTON(self.button_2,-1,self._onButtonKlaar)        
        wx.EVT_BUTTON(self.button_1,-1,self._onButtonCopy)        

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(self.label_1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_6.Add(self.text_ctrl_Code, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE|wx.FIXED_MINSIZE, 0)
        sizer_6.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_5.Add(self.label_2, 0, wx.FIXED_MINSIZE, 0)
        sizer_5.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_5)
        sizer_5.Fit(self)
        sizer_5.SetSizeHints(self)
        self.Layout()
        # end wxGlade
        
    def setCode(self,text):
    	self.text_ctrl_Code.SetValue(text)
        
    def _onButtonKlaar(self,event):
      	self.EndModal(wx.ID_OK)

    def _onButtonCopy(self,event):
    	self.text_ctrl_Code.SetSelection(-1,-1) # select everything
      	self.text_ctrl_Code.Copy() #copy to clipboard
      	self.text_ctrl_Code.SetSelection(0,0)

# end of class MyDialog
def main_is_frozen():
   return (hasattr(sys, "frozen") or # new py2exe
           hasattr(sys, "importers") # old py2exe
           or imp.is_frozen("__main__")) # tools/freeze

def get_main_dir():
   result = ""
   if main_is_frozen():
       result =  os.path.dirname(sys.executable)
   else:
      result =  os.path.dirname(sys.argv[0])
   if result == "":
      result = "."
   return result

class BasicFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: BasicFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("forumbanner.gif", wx.BITMAP_TYPE_ANY))
        self.label_3 = wx.StaticText(self, -1, "Aquaforum login naam", style=wx.ALIGN_RIGHT)
        self.loginNaam = wx.TextCtrl(self, -1, "")
        self.buttonSelectFile = wx.Button(self, -1, "Selecteer bestand")
        self.text_ctrl_Filepath = wx.TextCtrl(self, -1, "")
        self.radio_box_3 = wx.RadioBox(self, -1, "Dimensies", choices=["800x600(standaard, groot)", "640x480 (middelgroot)", "320x240 (klein)", "160x120(heel klein, handig voor avatar)"], majorDimension=4, style=wx.RA_SPECIFY_ROWS)
        self.button_VoorbeeldGrootte = wx.Button(self, -1, "Voorbeeld grootte")
        self.buttonUpload = wx.Button(self, -1, "Upload bestand naar forum")
        self.label_4 = wx.StaticText(self, -1, "Als je deze knop gebruikt dan converteert het programma het plaatje naar de juiste afmetingen \nen plaatst het programma het plaatje op aquaforum. \nDit kan enige tijd duren! Zie de statusbalk onderaan voor informatie.\n\n-  Riba")
        self.button_archief = wx.Button(self, -1, "Archief van de plaatjes")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.busy = False  
        self.desiredName=""
        self.error = False
        self.errorEx = None #the exception that caused the error
        self.action=""

    def __set_properties(self):
        # begin wxGlade: BasicFrame.__set_properties
        self.SetTitle("Aquaforum upload programma")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((702, 538))
        self.SetBackgroundColour(wx.Colour(0, 127, 255))
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Aquaforum file upload programma"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        self.label_3.SetBackgroundColour(wx.Colour(0, 127, 255))
        self.text_ctrl_Filepath.SetSize((400, 21))
        self.radio_box_3.SetBackgroundColour(wx.Colour(0, 127, 255))
        self.radio_box_3.SetSelection(0)
        self.label_4.SetBackgroundColour(wx.Colour(0, 127, 255))
        # end wxGlade
        wx.EVT_BUTTON(self.buttonUpload,-1,self._OnButtonUpload)
        wx.EVT_BUTTON(self.buttonSelectFile,-1,self._OnButtonSelectFile)        
        wx.EVT_BUTTON(self.button_VoorbeeldGrootte,-1,self._OnButton_VoorbeeldGrootte)
        wx.EVT_BUTTON(self.button_archief,-1,self._OnButton_archief)
        EVT_UPLOAD_DONE( self, -1,self.OnEventUploadDone )        

    def __do_layout(self):
        # begin wxGlade: BasicFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8.Add(self.bitmap_1, 0, wx.FIXED_MINSIZE, 0)
        sizer_8.Add((20, 20), 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_2.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_3.Add(self.label_3, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_3.Add((20, 20), 0, wx.FIXED_MINSIZE, 0)
        sizer_3.Add(self.loginNaam, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_2.Add(sizer_3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.buttonSelectFile, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0)
        sizer_4.Add(self.text_ctrl_Filepath, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE|wx.FIXED_MINSIZE, 0)
        sizer_2.Add(sizer_4, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(self.radio_box_3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add((20, 20), 0, wx.FIXED_MINSIZE, 0)
        sizer_1.Add(self.button_VoorbeeldGrootte, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add(self.buttonUpload, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add((20, 20), 0, wx.FIXED_MINSIZE, 0)
        sizer_7.Add(self.label_4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_archief, 0, wx.FIXED_MINSIZE, 3)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_2)
        self.Layout()
        self.Centre()
        # end wxGlade

        
    def _OnButtonUpload(self, event):
        '''
        Do the upload in a thread
        '''
        #check whether a correct file is selected
        if not (os.path.exists(self.text_ctrl_Filepath.GetValue())):
            wx.MessageDialog(self, "Het bestand \""+self.text_ctrl_Filepath.GetValue()+"\" bestaat niet", "Bericht",style = wx.OK ).ShowModal()
            return
            
        if self.busy == False: #not threadsafe. use semaphore. too lazy...so TODO
        	self.busy = True
        	thread.start_new_thread( self._doUpload, (event,) )
        else:
        	wx.MessageDialog(self, "Programma is nog bezig...", "Bericht",style = wx.OK ).ShowModal()
	    	    	
        
    def _doUpload(self, event):
        index = self.radio_box_3.GetSelection() #zero based index
        dimensions = None
        if index == 0:
            dimensions = (800,600)
        elif index == 1:
            dimensions = (640,480)
        elif index == 2:
            dimensions = (320,240)
        else:
            dimensions = (160,120)
        self.frame_1_statusbar.SetStatusText("Het programma converteert het plaatje", 0)
        try:
            self.action = "converteren van het plaatje"
            resizedFileName=aquaupload.resizeFile( self.text_ctrl_Filepath.GetValue(),dimensions)
            self.frame_1_statusbar.SetStatusText("Het programma bekijkt het aquaforum zodat het plaatje een unieke naam heeft", 0)
            self.action = "benaderen van aquaforum webpagina"            
            self.desiredName = aquaupload.contructUploadName(self.loginNaam.GetValue(), self.text_ctrl_Filepath.GetValue())
            self.frame_1_statusbar.SetStatusText("Het programma zet het plaatje op aquaforum", 0)
            self.action = "uploaden van het plaatje"                        
            aquaupload.uploadFileToAquaforum(resizedFileName, self.desiredName)
            self.action = "Plaatje toevoegen aan archief"
            self.frame_1_statusbar.SetStatusText("Plaatje toevoegen aan archief", 0)
            aquaupload.addToHistory(AUQAOFORUM_PICTURE_URL +self.desiredName)
            self.frame_1_statusbar.SetStatusText("Klaar.....", 0)
        except Exception, er:
            self.error = True
            self.errorEx = er
        #done, send done event
        event = UploadDoneEvent(self.GetId())
        self.GetEventHandler().AddPendingEvent(event)        
	
    def OnEventUploadDone(self,event):
        '''show dialog'''
        if self.error == True:
            wx.MessageDialog(self, "Er is een fout opgetreden tijdens het "+self.action+"\n"+"De error is "+str(self.errorEx), "Bericht",style = wx.OK ).ShowModal()
            self.error = False
        else:
            dlg = MyDialog(self, -1,"Bericht")
            dlg.setCode(" [IMG]"+AUQAOFORUM_PICTURE_URL +self.desiredName+"[/IMG]")
            dlg.ShowModal()
        self.busy = False        
        
    def _OnButton_VoorbeeldGrootte(self,event):
        #import popupImage
        #index = self.radio_box_3.GetSelection() #zero based index
        #dimensions = None
        #if index == 0:
        #    dimensions = (640,480)
        #elif index == 1:
        #    dimensions = (320,240)
        #else:
        #    dimensions = (160,120)
        #
        #popupFrame = popupImage.MyFrame(None,-1,"")
        #popupFrame.SetSize(dimensions)
        #popupFrame.Show() #this one is non blocking!!
        if self.busy:
            wx.MessageDialog(self, "Programma is nog bezig...", "Bericht",style = wx.OK ).ShowModal()
            return
        import popupImage        
        index = self.radio_box_3.GetSelection() #zero based index
        dimensions = None
        if index == 0:
            dimensions = (800,600)
        elif index == 1:
            dimensions = (640,480)
        elif index == 2:
            dimensions = (320,240)
        else:
            dimensions = (160,120)
        self.frame_1_statusbar.SetStatusText("Het programma converteert het plaatje", 0)
        resizedFileName=None
        if self.text_ctrl_Filepath.GetValue()!=() and self.text_ctrl_Filepath.GetValue()!="":
            try:
                if not (os.path.exists(self.text_ctrl_Filepath.GetValue())):
                    wx.MessageDialog(self, "Het bestand \""+self.text_ctrl_Filepath.GetValue()+"\" bestaat niet", "Bericht",style = wx.OK ).ShowModal()
                    resizedFileName = None
                else:
                    self.action = "converteren van het plaatje"
                    resizedFileName=aquaupload.resizeFile( self.text_ctrl_Filepath.GetValue(),dimensions)
                    self.frame_1_statusbar.SetStatusText(" ", 0)        
            except Exception, er:
    	       resizedFileName = None
    	       wx.MessageDialog(self, "Er is een fout opgetreden tijdens het converteren\n"+"De error is "+str(er), "Bericht",style = wx.OK ).ShowModal()                	       
        #check whether a correct file is selected    	        
        popupFrame = popupImage.MyFrame(None,-1,"")
        popupFrame.SetSize((dimensions[0]+10,dimensions[1]+30))
        popupFrame.setPath(resizedFileName)
        popupFrame.Show() #this one is non blocking!!
            
        
        
    def _OnButtonSelectFile(self,e):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        dlg.SetWildcard("plaatjes (*.bmp;*.jpg;*.png;*.tiff)|*.bmp;*.jpg;*.png;*.tiff|Alles (*.*)|*.*")
        if dlg.ShowModal() == wx.ID_OK:
            self.text_ctrl_Filepath.SetValue(dlg.GetPath())
        dlg.Destroy()

    def _OnButton_archief(self,e):
        '''open archive'''
        path="file:///"
        theArchive = get_main_dir()
        theArchive = theArchive.replace("\\","/")
        if theArchive[-1]!="/":
            theArchive += "/"
        theArchive+="archive.html"
        webbrowser.open_new(theArchive)
        return

# end of class BasicFrame

if __name__ == "__main__":
    os.chdir(get_main_dir())    
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = BasicFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
