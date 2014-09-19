import wx
import aquaupload
import thread
import os
import imp
import sys
import webbrowser
import gettext
from aquagui import BasicFrame  # , frame_1
from aquagui import MyDialog

AUQAOFORUM_PICTURE_URL = "http://www.aquaforum.nl/gallery/upload/"

	# create custom event
UPLOAD_DONE_EVENT_TYPE = wx.NewEventType() 
EVT_UPLOAD_DONE = wx.PyEventBinder(UPLOAD_DONE_EVENT_TYPE, 1) 		

class UploadDoneEvent(wx.PyCommandEvent): 
	eventType = UPLOAD_DONE_EVENT_TYPE 
	def __init__(self, windowID): 
		wx.PyCommandEvent.__init__(self, self.eventType, windowID) 

	def Clone(self): 
		self.__class__(self.GetId())  

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

class AquaForum(BasicFrame):
	def __init__(self, *args, **kargs):
		BasicFrame.__init__(self, *args, **kargs)

		wx.EVT_BUTTON(self.buttonUpload, -1, self._OnButtonUpload)
		wx.EVT_BUTTON(self.buttonSelectFile, -1, self._OnButtonSelectFile)		
		wx.EVT_BUTTON(self.button_VoorbeeldGrootte, -1, self._OnButton_VoorbeeldGrootte)
		wx.EVT_BUTTON(self.button_archief, -1, self._OnButton_archief)
		wx.EVT_BUTTON(self.button_5, -1, self._OnButton_5)
# 		self.Bind(wx.EVT_BUTTON, self._OnButton_5, self.button_5)
		EVT_UPLOAD_DONE(self, -1, self.OnEventUploadDone)

	def _OnButtonUpload(self, event):
		'''
		Do the upload in a thread
		'''
		# check whether a correct file is selected
		if not (os.path.exists(self.text_ctrl_Filepath.GetValue())):
			wx.MessageDialog(self, "Het bestand \"" + self.text_ctrl_Filepath.GetValue() + "\" bestaat niet", "Bericht", style=wx.OK).ShowModal()
			return
			
		if self.busy == False:  # not threadsafe. use semaphore. too lazy...so TODO
			self.busy = True
			thread.start_new_thread(self._doUpload, (event,))
		else:
			wx.MessageDialog(self, "Programma is nog bezig...", "Bericht", style=wx.OK).ShowModal()

	def _OnButton_5(self, event):  # wxGlade: BasicFrame.<event_handler>
		print "Dit is mijn event!!"
		event.Skip()
# 		wx.MessageDialog(self, "Dit is een test...", "Bericht", style=wx.OK).ShowModal()					
		
	def _doUpload(self, event):
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
		self.frame_1_statusbar.SetStatusText("Het programma converteert het plaatje", 0)
		try:
			self.action = "converteren van het plaatje"
			resizedFileName = aquaupload.resizeFile(self.text_ctrl_Filepath.GetValue(), dimensions)
			self.frame_1_statusbar.SetStatusText("Het programma bekijkt het aquaforum zodat het plaatje een unieke naam heeft", 0)
			self.action = "benaderen van aquaforum webpagina"			
			self.desiredName = aquaupload.contructUploadName(self.loginNaam.GetValue(), self.text_ctrl_Filepath.GetValue())
			self.frame_1_statusbar.SetStatusText("Het programma zet het plaatje op aquaforum", 0)
			self.action = "uploaden van het plaatje"						
			aquaupload.uploadFileToAquaforum(resizedFileName, self.desiredName)
			self.action = "Plaatje toevoegen aan archief"
			self.frame_1_statusbar.SetStatusText("Plaatje toevoegen aan archief", 0)
			aquaupload.addToHistory(AUQAOFORUM_PICTURE_URL + self.desiredName)
			self.frame_1_statusbar.SetStatusText("Klaar.....", 0)
		except Exception, er:
			self.error = True
			self.errorEx = er
		# done, send done event
		event = UploadDoneEvent(self.GetId())
		self.GetEventHandler().AddPendingEvent(event)		
	
	def OnEventUploadDone(self, event):
		'''show dialog'''
		if self.error == True:
			wx.MessageDialog(self, "Er is een fout opgetreden tijdens het " + self.action + "\n" + "De error is " + str(self.errorEx), "Bericht", style=wx.OK).ShowModal()
			self.error = False
		else:
			dlg = MyDialog(self, -1, "Bericht")
			dlg.setCode(" [IMG]" + AUQAOFORUM_PICTURE_URL + self.desiredName + "[/IMG]")
			dlg.ShowModal()
		self.busy = False		
		
	def _OnButton_VoorbeeldGrootte(self, event):
		# import popupImage
		# index = self.radio_box_3.GetSelection() #zero based index
		# dimensions = None
		# if index == 0:
		# 	dimensions = (640,480)
		# elif index == 1:
		# 	dimensions = (320,240)
		# else:
		# 	dimensions = (160,120)
		#
		# popupFrame = popupImage.MyFrame(None,-1,"")
		# popupFrame.SetSize(dimensions)
		# popupFrame.Show() #this one is non blocking!!
		if self.busy:
			wx.MessageDialog(self, "Programma is nog bezig...", "Bericht", style=wx.OK).ShowModal()
			return
		import popupImage		
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
		self.frame_1_statusbar.SetStatusText("Het programma converteert het plaatje", 0)
		resizedFileName = None
		if self.text_ctrl_Filepath.GetValue() != () and self.text_ctrl_Filepath.GetValue() != "":
			try:
				if not (os.path.exists(self.text_ctrl_Filepath.GetValue())):
					wx.MessageDialog(self, "Het bestand \"" + self.text_ctrl_Filepath.GetValue() + "\" bestaat niet", "Bericht", style=wx.OK).ShowModal()
					resizedFileName = None
				else:
					self.action = "converteren van het plaatje"
					resizedFileName = aquaupload.resizeFile(self.text_ctrl_Filepath.GetValue(), dimensions)
					self.frame_1_statusbar.SetStatusText(" ", 0)		
			except Exception, er:
				resizedFileName = None
				wx.MessageDialog(self, "Er is een fout opgetreden tijdens het converteren\n" + "De error is " + str(er), "Bericht", style=wx.OK).ShowModal()						   
		# check whether a correct file is selected				
		popupFrame = popupImage.MyFrame(None, -1, "")
		popupFrame.SetSize((dimensions[0] + 10, dimensions[1] + 30))
		popupFrame.setPath(resizedFileName)
		popupFrame.Show()  # this one is non blocking!!
			
		
		
	def _OnButtonSelectFile(self, e):
		""" Open a file"""
		self.dirname = ''
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
		dlg.SetWildcard("plaatjes (*.bmp;*.jpg;*.png;*.tiff)|*.bmp;*.jpg;*.png;*.tiff|Alles (*.*)|*.*")
		if dlg.ShowModal() == wx.ID_OK:
			self.text_ctrl_Filepath.SetValue(dlg.GetPath())
		dlg.Destroy()

	def _OnButton_archief(self, e):
		'''open archive'''
		path = "file:///"
		theArchive = get_main_dir()
		theArchive = theArchive.replace("\\", "/")
		if theArchive[-1] != "/":
			theArchive += "/"
		theArchive += "archive.html"
		webbrowser.open_new(theArchive)
		return

if __name__ == "__main__":
	gettext.install("app")  # replace with the appropriate catalog name
	os.chdir(get_main_dir())
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frmMain = BasicFrame(None, wx.ID_ANY, "")
	app.SetTopWindow(frmMain)
	frmMain.Show()
	app.MainLoop()

# if __name__ == "__main__":
# 	os.chdir(get_main_dir())	
# 	app = wx.PySimpleApp(0)
# 	wx.InitAllImageHandlers()
# 	frame_1 = BasicFrame(None, -1, "")
# 	app.SetTopWindow(frame_1)
# 	frame_1.Show()
# 	app.MainLoop()
