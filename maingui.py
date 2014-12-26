# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  7 2014)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aquaforum upload programma", pos = wx.DefaultPosition, size = wx.Size( 850,750 ), style = wx.CAPTION|wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.Size( 850,750 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bitmap_1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"forumbanner.gif", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.bitmap_1, 0, wx.FIXED_MINSIZE, 0 )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.infoBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		self.infoBox.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
		self.infoBox.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.infoBox.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		bSizer25.Add( self.infoBox, 1, wx.ALL|wx.EXPAND, 1 )
		
		
		bSizer2.Add( bSizer25, 1, wx.ALL|wx.EXPAND, 1 )
		
		
		bSizer1.Add( bSizer2, 1, wx.ALL|wx.EXPAND, 0 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 0 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer13.SetMinSize( wx.Size( -1,350 ) ) 
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4.SetMinSize( wx.Size( 250,-1 ) ) 
		self.tvFiles = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SUNKEN_BORDER, wx.EmptyString, 0 )
		
		self.tvFiles.ShowHidden( False )
		bSizer4.Add( self.tvFiles, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer4, 1, wx.EXPAND, 0 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapSelectedFile = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bitmapSelectedFile.SetMinSize( wx.Size( 400,300 ) )
		
		bSizer152.Add( self.bitmapSelectedFile, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 0 )
		
		
		bSizer22.Add( bSizer152, 1, wx.ALL|wx.EXPAND|wx.SHAPED, 0 )
		
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnSelectFile = wx.Button( self, wx.ID_ANY, u"Toevoegen aan uploadlijst ->", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.btnSelectFile, 0, wx.ALL, 5 )
		
		self.btnUnselectFile = wx.Button( self, wx.ID_ANY, u"<- Verwijderen van uploadlijst", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.btnUnselectFile, 0, wx.ALL, 5 )
		
		
		bSizer22.Add( bSizer151, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer13.Add( bSizer22, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		listboxSelectedFilesChoices = []
		self.listboxSelectedFiles = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listboxSelectedFilesChoices, 0 )
		bSizer14.Add( self.listboxSelectedFiles, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer14.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		radio_box_3Choices = [ u"800x600(standaard, groot)", u"640x480 (middelgroot)", u"320x240 (klein)", u"160x120(heel klein, handig voor avatar)" ]
		self.radio_box_3 = wx.RadioBox( self, wx.ID_ANY, u"Dimensies", wx.DefaultPosition, wx.DefaultSize, radio_box_3Choices, 4, wx.RA_SPECIFY_ROWS )
		self.radio_box_3.SetSelection( 0 )
		self.radio_box_3.SetBackgroundColour( wx.Colour( 0, 127, 255 ) )
		
		bSizer5.Add( self.radio_box_3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer5.AddSpacer( ( 20,  20), 0, wx.FIXED_MINSIZE, 0 )
		
		self.btnVoorbeeld = wx.Button( self, wx.ID_ANY, u"Voorbeeld van upload-dimensie", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnVoorbeeld.SetDefault() 
		bSizer5.Add( self.btnVoorbeeld, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer5.AddSpacer( ( 20,  20), 1, wx.EXPAND, 5 )
		
		self.m_button811 = wx.Button( self, wx.ID_ANY, u"Upload naar aquaforum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button811.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_button811.SetForegroundColour( wx.Colour( 116, 113, 162 ) )
		self.m_button811.SetBackgroundColour( wx.Colour( 172, 1, 1 ) )
		
		bSizer5.Add( self.m_button811, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 0 )
		
		
		bSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		self.btnArchief = wx.Button( self, wx.ID_ANY, u"Archief van de plaatjes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnArchief.SetDefault() 
		bSizer1.Add( self.btnArchief, 0, wx.FIXED_MINSIZE, 3 )
		
		
		bSizer15.Add( bSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer15 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuitemConf = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Configuratie", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menuitemConf )
		
		self.m_menu1.AppendSeparator()
		
		self.menuAbout = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Info", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menuAbout )
		
		self.m_menubar1.Append( self.m_menu1, u"Menu" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.tvFiles.Bind( wx.EVT_TREE_SEL_CHANGED, self.ontvFilesSelChanged )
		self.btnSelectFile.Bind( wx.EVT_BUTTON, self.onbtnSelectFileClick )
		self.btnUnselectFile.Bind( wx.EVT_BUTTON, self.onbtnUnselectFileClick )
		self.listboxSelectedFiles.Bind( wx.EVT_LISTBOX, self.onlistboxSelectedFile )
		self.listboxSelectedFiles.Bind( wx.EVT_SET_FOCUS, self.onlistboxSelectedFileSetFocus )
		self.btnVoorbeeld.Bind( wx.EVT_BUTTON, self.onbtnVoorbeeldClick )
		self.m_button811.Bind( wx.EVT_BUTTON, self.onbtnUploadClick )
		self.btnArchief.Bind( wx.EVT_BUTTON, self.onbtnArchiefClick )
		self.Bind( wx.EVT_MENU, self.onmenuitemClickConf, id = self.menuitemConf.GetId() )
		self.Bind( wx.EVT_MENU, self.onmenuitemClickAbout, id = self.menuAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ontvFilesSelChanged( self, event ):
		event.Skip()
	
	def onbtnSelectFileClick( self, event ):
		event.Skip()
	
	def onbtnUnselectFileClick( self, event ):
		event.Skip()
	
	def onlistboxSelectedFile( self, event ):
		event.Skip()
	
	def onlistboxSelectedFileSetFocus( self, event ):
		event.Skip()
	
	def onbtnVoorbeeldClick( self, event ):
		event.Skip()
	
	def onbtnUploadClick( self, event ):
		event.Skip()
	
	def onbtnArchiefClick( self, event ):
		event.Skip()
	
	def onmenuitemClickConf( self, event ):
		event.Skip()
	
	def onmenuitemClickAbout( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgImport
###########################################################################

class dlgImport ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.CLOSE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Alleen voor gebruikers van Aquaforumuploader van Riba!\n\nHier kun je de oude data importeren in het nieuwe data-bestand.\n\nHet data-bestand heet \"IMAGES.JSON\" en zal te vinden zijn op de volgende locatie..\nC:\\Program Files\\AquaforumUploader\\\n(tenzij er tijdens de installatie is gekozen voor een ander locatie)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer25.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		
		bSizer23.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnSelectJSON = wx.Button( self, wx.ID_ANY, u"Selecteer en importeer data-bestand \"IMAGES.JSON\"", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnSelectJSON, 0, wx.ALL, 5 )
		
		self.btnAfsluiten = wx.Button( self, wx.ID_ANY, u"Afsluiten", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnAfsluiten, 0, wx.ALL, 5 )
		
		
		bSizer23.Add( bSizer27, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer23 )
		self.Layout()
		bSizer23.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSelectJSON.Bind( wx.EVT_BUTTON, self.onclickselectjson )
		self.btnAfsluiten.Bind( wx.EVT_BUTTON, self.onbtnAfsluitenCLick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onclickselectjson( self, event ):
		event.Skip()
	
	def onbtnAfsluitenCLick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgUploadDone
###########################################################################

class dlgUploadDone ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bericht", pos = wx.DefaultPosition, size = wx.Size( 727,358 ), style = wx.CAPTION|wx.CLOSE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Het bericht is geplaatst op aquaforum. Je kan de volgende code gebruiken in je bericht:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer18.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer18, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.text_ctrl_Code1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE )
		self.text_ctrl_Code1.SetMinSize( wx.Size( -1,127 ) )
		
		bSizer19.Add( self.text_ctrl_Code1, 0, wx.ALL|wx.EXPAND, 5 )
		
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
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnKlaar = wx.Button( self, wx.ID_ANY, u"Klaar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.btnKlaar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer191, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer16 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.oninitdlgUploadDone )
		self.btnCopyToClipboard.Bind( wx.EVT_BUTTON, self.onbtnCopyToClipboardClick )
		self.btnKlaar.Bind( wx.EVT_BUTTON, self.onbtnKlaarClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def oninitdlgUploadDone( self, event ):
		event.Skip()
	
	def onbtnCopyToClipboardClick( self, event ):
		event.Skip()
	
	def onbtnKlaarClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgVoorbeeld
###########################################################################

class dlgVoorbeeld ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.CLOSE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
		
		sizerVoorbeeld = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapVoorbeeld = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"test.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerVoorbeeld.Add( self.bitmapVoorbeeld, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( sizerVoorbeeld )
		self.Layout()
		sizerVoorbeeld.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class dlgConf
###########################################################################

class dlgConf ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuratiescherm", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.CLOSE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer381 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.confedtLoginName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.confedtLoginName.SetMaxLength( 0 ) 
		bSizer381.Add( self.confedtLoginName, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer381, 0, wx.EXPAND, 5 )
		
		bSizer391 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.dirpickFolder = wx.DirPickerCtrl( self, wx.ID_ANY, u"/home/kelp", u"Selecteer een folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_USE_TEXTCTRL )
		bSizer391.Add( self.dirpickFolder, 0, 0, 5 )
		
		
		bSizer26.Add( bSizer391, 0, wx.EXPAND, 5 )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkPreview = wx.CheckBox( self, wx.ID_ANY, u"Preview foto's?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.checkPreview, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer38, 0, wx.EXPAND, 5 )
		
		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
		
		choiceDimensieChoices = []
		self.choiceDimensie = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDimensieChoices, 0 )
		self.choiceDimensie.SetSelection( 0 )
		bSizer39.Add( self.choiceDimensie, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer39, 0, wx.EXPAND, 5 )
		
		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnImport = wx.Button( self, wx.ID_ANY, u"Importeer", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer40.Add( self.btnImport, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer40, 0, wx.EXPAND, 5 )
		
		
		bSizer35.Add( bSizer26, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer35.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer441 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"Gebruikersnaam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		bSizer441.Add( self.m_staticText151, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer441, 1, wx.EXPAND, 5 )
		
		bSizer401 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Standaard folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer401.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer401, 1, wx.EXPAND, 5 )
		
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Wil je een preview zien bij het selecteren van een foto?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer44.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer44, 1, wx.EXPAND, 5 )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Standaardwaarde voor dimensies", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer45.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer45, 1, wx.EXPAND, 5 )
		
		bSizer47 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Importeer data van Riba's-versie van deze applicatie.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer47.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer47, 1, wx.EXPAND, 5 )
		
		
		bSizer35.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		
		bSizer42.Add( bSizer35, 0, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer34.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.btnAfsluiten = wx.Button( self, wx.ID_ANY, u"Afsluiten", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer34.Add( self.btnAfsluiten, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer42.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer42 )
		self.Layout()
		bSizer42.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.oninitConfDialog )
		self.confedtLoginName.Bind( wx.EVT_KILL_FOCUS, self.onconfedtLoginNameKillFocus )
		self.checkPreview.Bind( wx.EVT_CHECKBOX, self.oncheckPreviewClick )
		self.choiceDimensie.Bind( wx.EVT_CHOICE, self.onChoiceDimensies )
		self.btnImport.Bind( wx.EVT_BUTTON, self.onbtnImportClick )
		self.btnAfsluiten.Bind( wx.EVT_BUTTON, self.onbtnAfsluitenClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def oninitConfDialog( self, event ):
		event.Skip()
	
	def onconfedtLoginNameKillFocus( self, event ):
		event.Skip()
	
	def oncheckPreviewClick( self, event ):
		event.Skip()
	
	def onChoiceDimensies( self, event ):
		event.Skip()
	
	def onbtnImportClick( self, event ):
		event.Skip()
	
	def onbtnAfsluitenClick( self, event ):
		event.Skip()
	

