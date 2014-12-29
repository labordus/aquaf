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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aquaforum upload programma", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 850,800 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bitmap_1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"forumbanner.gif", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.bitmap_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE, 0 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.infoBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		self.infoBox.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
		self.infoBox.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.infoBox.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.infoBox.SetMinSize( wx.Size( 150,80 ) )
		self.infoBox.SetMaxSize( wx.Size( 200,-1 ) )
		
		bSizer25.Add( self.infoBox, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 1 )
		
		
		bSizer2.Add( bSizer25, 1, wx.ALL|wx.EXPAND, 1 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4.SetMinSize( wx.Size( 300,-1 ) ) 
		self.tvFiles = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.SUNKEN_BORDER, wx.EmptyString, 0 )
		
		self.tvFiles.ShowHidden( True )
		bSizer4.Add( self.tvFiles, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer4, 0, wx.EXPAND, 0 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelPreview = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.panelPreview.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapSelectedFile = wx.StaticBitmap( self.panelPreview, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bitmapSelectedFile.SetMinSize( wx.Size( 400,300 ) )
		
		bSizer152.Add( self.bitmapSelectedFile, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 0 )
		
		
		self.panelPreview.SetSizer( bSizer152 )
		self.panelPreview.Layout()
		bSizer152.Fit( self.panelPreview )
		bSizer22.Add( self.panelPreview, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
		
		choiceDimensieChoices = []
		self.choiceDimensie = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDimensieChoices, 0 )
		self.choiceDimensie.SetSelection( 0 )
		self.choiceDimensie.SetToolTipString( u"De betreffende foto zal in de gekozen dimensies worden\nge-upload naar de server van aquaforum.nl\n\nLet op: De conversie verkleind (zo nodig) een foto naar (maximaal) de geselecteerde dimensies.\nAls de originele dimensies van een foto kleiner zijn dan de gekozen dimensie dan zal er geen conversie plaatsvinden.\nM.a.w. foto-formaten worden niet vergroot ;)" )
		
		bSizer301.Add( self.choiceDimensie, 0, wx.ALL, 5 )
		
		self.btnVoorbeeld = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"icon.ico", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnVoorbeeld.SetToolTipString( u"Preview hoe de betreffende foto eruit zal zien\nmet de gekozen dimensies." )
		
		bSizer301.Add( self.btnVoorbeeld, 0, wx.ALL, 5 )
		
		
		bSizer151.Add( bSizer301, 1, wx.EXPAND, 5 )
		
		self.btnSelectFile = wx.Button( self, wx.ID_ANY, u"Toevoegen  ->", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnSelectFile.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnSelectFile.SetForegroundColour( wx.Colour( 60, 130, 50 ) )
		self.btnSelectFile.SetToolTipString( u"Voeg foto toe aan uploadlijst" )
		
		bSizer151.Add( self.btnSelectFile, 0, wx.ALL, 5 )
		
		self.btnUnselectFile = wx.Button( self, wx.ID_ANY, u"<- Verwijderen", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnUnselectFile.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnUnselectFile.SetForegroundColour( wx.Colour( 31, 37, 181 ) )
		self.btnUnselectFile.SetToolTipString( u"Verwijder foto van uploadlijst" )
		
		bSizer151.Add( self.btnUnselectFile, 0, wx.ALL, 5 )
		
		
		bSizer42.Add( bSizer151, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer22.Add( bSizer42, 0, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer22, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer39.SetMinSize( wx.Size( 300,-1 ) ) 
		self.listFiles = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.listFiles.SetMaxSize( wx.Size( 400,-1 ) )
		
		bSizer39.Add( self.listFiles, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnUpload = wx.Button( self, wx.ID_ANY, u"Upload naar aquaforum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnUpload.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnUpload.SetForegroundColour( wx.Colour( 255, 42, 0 ) )
		self.btnUpload.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.btnUpload.SetToolTipString( u"De foto's in de uploadlijst zullen (zo nodig) worden geconverteerd naar de gekozen dimensies en dan\nworden ge-upload naar de server van aquaforum.nl" )
		
		bSizer39.Add( self.btnUpload, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer39, 0, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer13, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnArchief = wx.Button( self, wx.ID_ANY, u"Archief van de plaatjes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnArchief.SetToolTipString( u"Klik hier voor een overzicht van alle foto's\ndie (met dit programma) zijn ge-upload\nnaar de server van aquaforum.nl" )
		
		bSizer29.Add( self.btnArchief, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 3 )
		
		
		bSizer28.Add( bSizer29, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer28.Add( bSizer20, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		
		bSizer30.Add( bSizer1, 1, wx.ALL|wx.EXPAND, 3 )
		
		
		self.SetSizer( bSizer30 )
		self.Layout()
		bSizer30.Fit( self )
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
		self.tvFiles.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.ontvFilesItemActivate )
		self.tvFiles.Bind( wx.EVT_TREE_SEL_CHANGED, self.ontvFilesSelChanged )
		self.btnVoorbeeld.Bind( wx.EVT_BUTTON, self.onbtnVoorbeeldClick )
		self.btnSelectFile.Bind( wx.EVT_BUTTON, self.onbtnSelectFileClick )
		self.btnUnselectFile.Bind( wx.EVT_BUTTON, self.onbtnUnselectFileClick )
		self.listFiles.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onlistFilesSelected )
		self.btnUpload.Bind( wx.EVT_BUTTON, self.onbtnUploadClick )
		self.btnArchief.Bind( wx.EVT_BUTTON, self.onbtnArchiefClick )
		self.Bind( wx.EVT_MENU, self.onmenuitemClickConf, id = self.menuitemConf.GetId() )
		self.Bind( wx.EVT_MENU, self.onmenuitemClickAbout, id = self.menuAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ontvFilesItemActivate( self, event ):
		event.Skip()
	
	def ontvFilesSelChanged( self, event ):
		event.Skip()
	
	def onbtnVoorbeeldClick( self, event ):
		event.Skip()
	
	def onbtnSelectFileClick( self, event ):
		event.Skip()
	
	def onbtnUnselectFileClick( self, event ):
		event.Skip()
	
	def onlistFilesSelected( self, event ):
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
		self.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
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
		self.btnAfsluiten.SetDefault() 
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
		self.SetBackgroundColour( wx.Colour( 141, 139, 178 ) )
		
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuratiescherm", pos = wx.DefaultPosition, size = wx.Size( 579,266 ), style = wx.CAPTION|wx.CLOSE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 141, 139, 178 ) )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.confedtLoginName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.confedtLoginName.SetMaxLength( 0 ) 
		gSizer1.Add( self.confedtLoginName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"Gebruikersnaam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		gSizer1.Add( self.m_staticText151, 0, wx.ALL, 5 )
		
		self.dirpickFolder = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Selecteer een folder", wx.Point( -1,-1 ), wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST|wx.DIRP_USE_TEXTCTRL )
		self.dirpickFolder.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		gSizer1.Add( self.dirpickFolder, 0, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Standaard folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.checkPreview = wx.CheckBox( self, wx.ID_ANY, u"Preview foto's?", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.checkPreview, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Preview aan/uitzetten", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gSizer1.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		choiceDimensieChoices = []
		self.choiceDimensie = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDimensieChoices, 0 )
		self.choiceDimensie.SetSelection( 0 )
		gSizer1.Add( self.choiceDimensie, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Standaardwaarde voor dimensies", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gSizer1.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.checkTooltip = wx.CheckBox( self, wx.ID_ANY, u"Tooltips laten zien?", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.checkTooltip, 0, wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Tooltips aan/uitzetten", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		gSizer1.Add( self.m_staticText91, 0, wx.ALL, 5 )
		
		self.btnImport = wx.Button( self, wx.ID_ANY, u"Importeer", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.btnImport, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Importeer gegevens van Riba's-versie.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer1.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
		bSizer42.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer34.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.btnAfsluiten = wx.Button( self, wx.ID_ANY, u"Afsluiten", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnAfsluiten.SetDefault() 
		bSizer34.Add( self.btnAfsluiten, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer42.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer42 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.oninitConfDialog )
		self.confedtLoginName.Bind( wx.EVT_KILL_FOCUS, self.onconfedtLoginNameKillFocus )
		self.dirpickFolder.Bind( wx.EVT_DIRPICKER_CHANGED, self.ondirpickFolderChange )
		self.checkPreview.Bind( wx.EVT_CHECKBOX, self.oncheckPreviewClick )
		self.choiceDimensie.Bind( wx.EVT_CHOICE, self.onChoiceDimensies )
		self.checkTooltip.Bind( wx.EVT_CHECKBOX, self.oncheckTooltipClick )
		self.btnImport.Bind( wx.EVT_BUTTON, self.onbtnImportClick )
		self.btnAfsluiten.Bind( wx.EVT_BUTTON, self.onbtnAfsluitenClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def oninitConfDialog( self, event ):
		event.Skip()
	
	def onconfedtLoginNameKillFocus( self, event ):
		event.Skip()
	
	def ondirpickFolderChange( self, event ):
		event.Skip()
	
	def oncheckPreviewClick( self, event ):
		event.Skip()
	
	def onChoiceDimensies( self, event ):
		event.Skip()
	
	def oncheckTooltipClick( self, event ):
		event.Skip()
	
	def onbtnImportClick( self, event ):
		event.Skip()
	
	def onbtnAfsluitenClick( self, event ):
		event.Skip()
	

