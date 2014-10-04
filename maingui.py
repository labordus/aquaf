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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aquaforum upload programma", pos = wx.DefaultPosition, size = wx.Size( 829,651 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		self.frame_1_statusbar = self.CreateStatusBar( 1, 0|wx.SUNKEN_BORDER, wx.ID_ANY )
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
		self.tvFiles = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, u"\"plaatjes (*.bmp;*.jpg;*.png;*.tiff)|*.bmp;*.jpg;*.png;*.tiff\"", 0 )
		
		self.tvFiles.ShowHidden( False )
		bSizer4.Add( self.tvFiles, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer4, 1, wx.EXPAND, 0 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bitmapSelectedFile = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"default_foto.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.bitmapSelectedFile, 0, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		
		bSizer13.Add( bSizer15, 1, wx.EXPAND, 0 )
		
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnSelectFile = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"dagverder.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnSelectFile.Enable( False )
		
		bSizer151.Add( self.btnSelectFile, 0, wx.ALL, 5 )
		
		self.btnUnselectFile = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"dagterug.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnUnselectFile.Enable( False )
		
		bSizer151.Add( self.btnUnselectFile, 0, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer151, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer14.Add( self.m_listBox1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
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
		
		self.btnUpload = wx.Button( self, wx.ID_ANY, u"Upload bestand naar forum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnUpload.SetDefault() 
		bSizer6.Add( self.btnUpload, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer6.AddSpacer( ( 20,  20), 0, wx.FIXED_MINSIZE, 0 )
		
		self.label_4 = wx.StaticText( self, wx.ID_ANY, u"Als je deze knop gebruikt dan converteert het programma het plaatje naar de juiste afmetingen \nen plaatst het programma het plaatje op aquaforum. \nDit kan enige tijd duren! Zie de statusbalk onderaan voor informatie.\n", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.label_4.Wrap( -1 )
		self.label_4.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer6.Add( self.label_4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND, 0 )
		
		self.btnArchief = wx.Button( self, wx.ID_ANY, u"Archief van de plaatjes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnArchief.SetDefault() 
		bSizer1.Add( self.btnArchief, 0, wx.FIXED_MINSIZE, 3 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSelectFile1.Bind( wx.EVT_BUTTON, self.onbtnSelectFile1Click )
		self.tvFiles.Bind( wx.EVT_TREE_SEL_CHANGED, self.ontvFilesSelChanged )
		self.btnVoorbeeld.Bind( wx.EVT_BUTTON, self.onbtnVoorbeeldClick )
		self.btnUpload.Bind( wx.EVT_BUTTON, self.onbtnUploadClick )
		self.btnArchief.Bind( wx.EVT_BUTTON, self.onbtnArchiefClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onbtnSelectFile1Click( self, event ):
		event.Skip()
	
	def ontvFilesSelChanged( self, event ):
		event.Skip()
	
	def onbtnVoorbeeldClick( self, event ):
		event.Skip()
	
	def onbtnUploadClick( self, event ):
		event.Skip()
	
	def onbtnArchiefClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgUploadDone
###########################################################################

class dlgUploadDone ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bericht", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.label_1 = wx.StaticText( self, wx.ID_ANY, u"Het bericht is geplaatst op aquaforum. Je kan de volgende code gebruiken in je bericht:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_1.Wrap( 0 )
		self.label_1.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer7.Add( self.label_1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.text_ctrl_Code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400, 127 ), wx.TE_READONLY|wx.TE_LINEWRAP )
		self.text_ctrl_Code.SetMaxLength( 0 ) 
		bSizer8.Add( self.text_ctrl_Code, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0 )
		
		self.button_1 = wx.Button( self, wx.ID_ANY, u"Zet de code in het klembord (clipboard)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_1.SetDefault() 
		bSizer8.Add( self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 0 )
		
		self.label_2 = wx.StaticText( self, wx.ID_ANY, u"Als je op de knop \"Zet de code in het klembord (clipboard)\" drukt, dan kan je vervolgens naar het aquaforum surfen met je browser. \nMaak een bericht waar je het plaatje in wilt hebben, klik rechts met de muis in het bericht  en kies \"plakken\" (of \"paste\"). \nDan staat de code in het bericht.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_2.Wrap( 0 )
		self.label_2.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer7.Add( self.label_2, 0, wx.FIXED_MINSIZE, 0 )
		
		self.button_2 = wx.Button( self, wx.ID_ANY, u"Klaar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_2.SetDefault() 
		bSizer7.Add( self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 0 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )
	
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
	

