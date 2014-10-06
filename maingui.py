# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  1 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Mainframe
###########################################################################

class Mainframe ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aquaforum upload programma", pos = wx.DefaultPosition, size = wx.Size( 829,739 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		self.frame_1_statusbar = self.CreateStatusBar( 1, 0|wx.SUNKEN_BORDER, wx.ID_ANY )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bitmap_1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"forumbanner.gif", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.bitmap_1, 0, wx.FIXED_MINSIZE, 0 )
		
		
		bSizer2.AddSpacer( ( 20,  20), 0, wx.EXPAND|wx.FIXED_MINSIZE, 0 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 0 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.label_3 = wx.StaticText( self, wx.ID_ANY, u"Aquaforum login naam", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.label_3.Wrap( -2 )
		self.label_3.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer3.Add( self.label_3, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0 )
		
		self.edtLoginName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.edtLoginName.SetMaxLength( 0 ) 
		bSizer3.Add( self.edtLoginName, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND|wx.SHAPED, 0 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnSelectFile1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.btnSelectFile1, 0, wx.ALL, 5 )
		
		self.edtFile1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,21 ), 0 )
		bSizer16.Add( self.edtFile1, 0, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5 )
		
		
		bSizer1.Add( bSizer16, 1, wx.EXPAND, 0 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4.SetMinSize( wx.Size( 250,-1 ) ) 
		self.tvFiles = wx.GenericDirCtrl( self, wx.ID_ANY, u"/home/kelp/Desktop/test", wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, u"\"plaatjes (*.bmp;*.jpg;*.png;*.tiff)|*.bmp;*.jpg;*.png;*.tiff\"", 0 )
		
		self.tvFiles.ShowHidden( False )
		bSizer4.Add( self.tvFiles, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer4, 1, wx.EXPAND, 0 )
		
		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bitmapSelectedFile = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"default_foto.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.bitmapSelectedFile, 0, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		
		bSizer13.Add( bSizer152, 1, wx.EXPAND, 0 )
		
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnSelectFile = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"dagverder.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer151.Add( self.btnSelectFile, 0, wx.ALL, 5 )
		
		self.btnUnselectFile = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"dagterug.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer151.Add( self.btnUnselectFile, 0, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer151, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		listboxSelectedFilesChoices = []
		self.listboxSelectedFiles = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listboxSelectedFilesChoices, 0 )
		bSizer14.Add( self.listboxSelectedFiles, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnUpload = wx.Button( self, wx.ID_ANY, u"Upload naar aquaforum.nl", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.btnUpload, 0, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		radio_box_3Choices = [ u"800x600(standaard, groot)", u"640x480 (middelgroot)", u"320x240 (klein)", u"160x120(heel klein, handig voor avatar)" ]
		self.radio_box_3 = wx.RadioBox( self, wx.ID_ANY, u"Dimensies", wx.DefaultPosition, wx.DefaultSize, radio_box_3Choices, 4, wx.RA_SPECIFY_ROWS )
		self.radio_box_3.SetSelection( 0 )
		self.radio_box_3.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer5.Add( self.radio_box_3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer5.AddSpacer( ( 20,  20), 0, wx.FIXED_MINSIZE, 0 )
		
		self.btnVoorbeeld = wx.Button( self, wx.ID_ANY, u"Voorbeeld", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnVoorbeeld.SetDefault() 
		bSizer5.Add( self.btnVoorbeeld, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer1.Add( bSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnblablablabla = wx.Button( self, wx.ID_ANY, u"blablablablablabla", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnblablablabla.SetDefault() 
		bSizer6.Add( self.btnblablablabla, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer6.AddSpacer( ( 20,  20), 0, wx.FIXED_MINSIZE, 0 )
		
		self.label_4 = wx.StaticText( self, wx.ID_ANY, u"Als je deze knop gebruikt dan converteert het programma het plaatje naar de juiste afmetingen \nen plaatst het programma het plaatje op aquaforum. \nDit kan enige tijd duren! Zie de statusbalk onderaan voor informatie.\n", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.label_4.Wrap( -1 )
		self.label_4.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer6.Add( self.label_4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND, 0 )
		
		self.btnArchief = wx.Button( self, wx.ID_ANY, u"Archief van de plaatjes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnArchief.SetDefault() 
		bSizer1.Add( self.btnArchief, 0, wx.FIXED_MINSIZE, 3 )
		
		
		bSizer15.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer15 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.onMainframeActivate )
		self.btnSelectFile1.Bind( wx.EVT_BUTTON, self.onbtnSelectFile1Click )
		self.tvFiles.Bind( wx.EVT_TREE_SEL_CHANGED, self.ontvFilesSelChanged )
		self.btnSelectFile.Bind( wx.EVT_BUTTON, self.onbtnSelectFileClick )
		self.btnUnselectFile.Bind( wx.EVT_BUTTON, self.onbtnUnselectFileClick )
		self.listboxSelectedFiles.Bind( wx.EVT_KILL_FOCUS, self.onlistboxSelectedFileLostFocus )
		self.listboxSelectedFiles.Bind( wx.EVT_LISTBOX, self.onlistboxSelectedFile )
		self.listboxSelectedFiles.Bind( wx.EVT_SET_FOCUS, self.onlistboxSelectedFileSetFocus )
		self.btnUpload.Bind( wx.EVT_BUTTON, self.onbtnUploadClick )
		self.btnVoorbeeld.Bind( wx.EVT_BUTTON, self.onbtnVoorbeeldClick )
		self.btnblablablabla.Bind( wx.EVT_BUTTON, self.btnBlaClick )
		self.btnArchief.Bind( wx.EVT_BUTTON, self.onbtnArchiefClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onMainframeActivate( self, event ):
		event.Skip()
	
	def onbtnSelectFile1Click( self, event ):
		event.Skip()
	
	def ontvFilesSelChanged( self, event ):
		event.Skip()
	
	def onbtnSelectFileClick( self, event ):
		event.Skip()
	
	def onbtnUnselectFileClick( self, event ):
		event.Skip()
	
	def onlistboxSelectedFileLostFocus( self, event ):
		event.Skip()
	
	def onlistboxSelectedFile( self, event ):
		event.Skip()
	
	def onlistboxSelectedFileSetFocus( self, event ):
		event.Skip()
	
	def onbtnUploadClick( self, event ):
		event.Skip()
	
	def onbtnVoorbeeldClick( self, event ):
		event.Skip()
	
	def btnBlaClick( self, event ):
		event.Skip()
	
	def onbtnArchiefClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgUploadDone
###########################################################################

class dlgUploadDone ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bericht", pos = wx.DefaultPosition, size = wx.Size( 727,358 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Het bericht is geplaatst op aquaforum. Je kan de volgende code gebruiken in je bericht:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer18.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer18, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.text_ctrl_Code1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400, 127 ), wx.TE_READONLY )
		self.text_ctrl_Code1.SetMaxLength( 0 ) 
		bSizer19.Add( self.text_ctrl_Code1, 0, wx.ALL, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnCopyToClipboard = wx.Button( self, wx.ID_ANY, u"Zet de code in het klembord (clipboard)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCopyToClipboard.SetDefault() 
		bSizer21.Add( self.btnCopyToClipboard, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer19.Add( bSizer21, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer16.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Als je op de knop \"Zet de code in het klembord (clipboard)\" drukt, dan kan je vervolgens naar het aquaforum surfen met je browser. \nMaak een bericht waar je het plaatje in wilt hebben, klik rechts met de muis in het bericht  en kies \"plakken\" (of \"paste\"). \nDan staat de code in het bericht.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer20.Add( self.m_staticText6, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer16.Add( bSizer20, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer16 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class dlgVoorbeeld
###########################################################################

class dlgVoorbeeld ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.CLOSE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
		
		sizerVoorbeeld = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapVoorbeeld = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../../../mnt/syn_media/pics/inspiration/0508_1659_400.jpeg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerVoorbeeld.Add( self.bitmapVoorbeeld, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( sizerVoorbeeld )
		self.Layout()
		sizerVoorbeeld.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

