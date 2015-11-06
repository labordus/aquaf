# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  1 2015)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aquaforum upload programma", pos = wx.DefaultPosition, size = wx.Size( -1,800 ), style = wx.CAPTION|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 795,800 ), wx.Size( -1,800 ) )
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
		
		fgSizer1 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Online Foto:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer36.Add( self.m_staticText13, 0, wx.ALIGN_CENTER, 0 )
		
		self.edtURL = wx.TextCtrl( self, wx.ID_ANY, u"http://www.aqua-rebell.com/images/aquascaping/aquascaping-art-of-the-planted-aquarium-adrie-01.jpg", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer36.Add( self.edtURL, 1, 0, 0 )
		
		self.btnPreviewOnline = wx.Button( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnPreviewOnline.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnPreviewOnline.SetForegroundColour( wx.Colour( 25, 120, 11 ) )
		
		bSizer36.Add( self.btnPreviewOnline, 0, wx.ALL, 0 )
		
		
		fgSizer1.Add( bSizer36, 0, wx.EXPAND, 0 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnClearList = wx.Button( self, wx.ID_ANY, u"Wis uploadlijst", wx.DefaultPosition, wx.Size( -1,24 ), wx.BU_EXACTFIT )
		fgSizer1.Add( self.btnClearList, 0, wx.ALIGN_RIGHT|wx.ALL, 3 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4.SetMinSize( wx.Size( 300,-1 ) ) 
		self.tvFiles = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.DIRCTRL_MULTIPLE|wx.DIRCTRL_SELECT_FIRST|wx.SUNKEN_BORDER, wx.EmptyString, 0 )
		
		self.tvFiles.ShowHidden( True )
		bSizer4.Add( self.tvFiles, 1, wx.EXPAND |wx.ALL, 3 )
		
		
		fgSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer22.AddSpacer( ( 0, 0), 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelPreview = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.panelPreview.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer152.SetMinSize( wx.Size( 400,300 ) ) 
		bSizer401 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnEditmodeOff = wx.Button( self.panelPreview, wx.ID_ANY, u"Sluit bewerking", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnEditmodeOff.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.btnEditmodeOff.SetForegroundColour( wx.Colour( 10, 43, 233 ) )
		
		bSizer401.Add( self.btnEditmodeOff, 0, wx.ALL|wx.EXPAND, 0 )
		
		
		bSizer152.Add( bSizer401, 0, wx.EXPAND, 5 )
		
		self.bitmapSelectedFile = wx.StaticBitmap( self.panelPreview, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer152.Add( self.bitmapSelectedFile, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 0 )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
		
		choiceDimensieChoices = []
		self.choiceDimensie = wx.Choice( self.panelPreview, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDimensieChoices, 0 )
		self.choiceDimensie.SetSelection( 0 )
		self.choiceDimensie.SetToolTipString( u"De betreffende foto's zullen in de gekozen dimensies worden ge-upload naar de aquaforum-server.\n\nLet op: De conversie verkleind (zo nodig) een foto naar (maximaal) de geselecteerde dimensies.\nAls de originele dimensies van een foto kleiner zijn dan de gekozen dimensie dan zal er geen conversie plaatsvinden.\nM.a.w. foto-formaten worden niet vergroot ;)" )
		
		bSizer301.Add( self.choiceDimensie, 0, wx.ALL, 5 )
		
		self.btnRotate = wx.Button( self.panelPreview, wx.ID_ANY, u"Roteer", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer301.Add( self.btnRotate, 0, wx.ALL, 5 )
		
		
		bSizer151.Add( bSizer301, 1, wx.EXPAND, 0 )
		
		
		bSizer42.Add( bSizer151, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer152.Add( bSizer42, 0, wx.EXPAND, 5 )
		
		
		self.panelPreview.SetSizer( bSizer152 )
		self.panelPreview.Layout()
		bSizer152.Fit( self.panelPreview )
		bSizer45.Add( self.panelPreview, 0, 0, 0 )
		
		
		bSizer22.Add( bSizer45, 1, wx.ALL|wx.EXPAND, 0 )
		
		self.panelPreviewInfo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelPreviewInfo.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnEditmodeOn = wx.Button( self.panelPreviewInfo, wx.ID_ANY, u"Bewerk", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnEditmodeOn.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.btnEditmodeOn.SetForegroundColour( wx.Colour( 10, 43, 233 ) )
		
		bSizer40.Add( self.btnEditmodeOn, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblDimensie = wx.StaticText( self.panelPreviewInfo, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDimensie.Wrap( -1 )
		bSizer38.Add( self.lblDimensie, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		self.lblRotatie = wx.StaticText( self.panelPreviewInfo, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblRotatie.Wrap( -1 )
		bSizer38.Add( self.lblRotatie, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		
		bSizer40.Add( bSizer38, 1, wx.EXPAND, 5 )
		
		
		self.panelPreviewInfo.SetSizer( bSizer40 )
		self.panelPreviewInfo.Layout()
		bSizer40.Fit( self.panelPreviewInfo )
		bSizer22.Add( self.panelPreviewInfo, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 0 )
		
		bSizer361 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnVoorbeeld = wx.Button( self, wx.ID_ANY, u" Preview ", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnVoorbeeld.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnVoorbeeld.SetForegroundColour( wx.Colour( 10, 43, 233 ) )
		self.btnVoorbeeld.SetToolTipString( u"Preview hoe de betreffende foto eruit zal zien\nmet de gekozen dimensie en rotatie." )
		
		bSizer361.Add( self.btnVoorbeeld, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		self.btnToevoegen = wx.Button( self, wx.ID_ANY, u"Toevoegen  ->", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnToevoegen.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnToevoegen.SetForegroundColour( wx.Colour( 25, 120, 11 ) )
		self.btnToevoegen.SetToolTipString( u"Voeg foto's toe aan uploadlijst" )
		
		bSizer361.Add( self.btnToevoegen, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 2 )
		
		self.btnVerwijderen = wx.Button( self, wx.ID_ANY, u"<- Verwijderen", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnVerwijderen.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnVerwijderen.SetForegroundColour( wx.Colour( 241, 26, 15 ) )
		self.btnVerwijderen.SetToolTipString( u"Verwijder foto van uploadlijst" )
		
		bSizer361.Add( self.btnVerwijderen, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 2 )
		
		
		bSizer22.Add( bSizer361, 1, wx.ALIGN_BOTTOM|wx.BOTTOM|wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer22, 0, wx.EXPAND, 0 )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer39.SetMinSize( wx.Size( 300,-1 ) ) 
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.listFiles = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT )
		self.listFiles.SetMaxSize( wx.Size( 400,-1 ) )
		
		bSizer28.Add( self.listFiles, 1, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer39.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer13, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnArchief = wx.Button( self, wx.ID_ANY, u"Archief van de foto's", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnArchief.SetToolTipString( u"Klik hier voor een overzicht van de foto's\ndie op de server van aquaforum.nl staan." )
		
		bSizer29.Add( self.btnArchief, 0, wx.ALIGN_LEFT|wx.EXPAND, 3 )
		
		
		bSizer29.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnClearLog = wx.Button( self, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.btnClearLog, 0, wx.ALL, 5 )
		
		self.btnWIT = wx.Button( self, wx.ID_ANY, u"WIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.btnWIT, 0, wx.ALL, 5 )
		
		self.btnUpload = wx.Button( self, wx.ID_ANY, u"Upload naar aquaforum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnUpload.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnUpload.SetForegroundColour( wx.Colour( 255, 42, 0 ) )
		self.btnUpload.SetBackgroundColour( wx.Colour( 242, 195, 8 ) )
		self.btnUpload.SetToolTipString( u"De foto's in de uploadlijst zullen (zo nodig) worden geconverteerd naar de gekozen dimensies en dan\nworden ge-upload naar de server van aquaforum.nl" )
		
		bSizer29.Add( self.btnUpload, 0, wx.ALIGN_RIGHT|wx.EXPAND, 3 )
		
		
		bSizer1.Add( bSizer29, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer30.Add( bSizer1, 1, wx.ALL|wx.EXPAND, 3 )
		
		
		self.SetSizer( bSizer30 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuitemConf = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Configuratie", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menuitemConf )
		
		self.menuitemAfsluiten = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Afsluiten", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menuitemAfsluiten )
		
		self.m_menu1.AppendSeparator()
		
		self.menuitemAbout = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Info", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menuitemAbout )
		
		self.m_menubar1.Append( self.m_menu1, u"Menu" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.oncloseMainframe )
		self.btnPreviewOnline.Bind( wx.EVT_BUTTON, self.onbtnPreviewOnlineClick )
		self.btnClearList.Bind( wx.EVT_BUTTON, self.onbtnClearListClick )
		self.tvFiles.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.ontvFilesItemActivate )
		self.tvFiles.Bind( wx.EVT_TREE_ITEM_MENU, self.OntvFilesRightClick )
		self.tvFiles.Bind( wx.EVT_TREE_SEL_CHANGED, self.ontvFilesSelChanged )
		self.btnEditmodeOff.Bind( wx.EVT_BUTTON, self.onbtneditmodeoff )
		self.btnRotate.Bind( wx.EVT_BUTTON, self.onbtnRotateClick )
		self.btnEditmodeOn.Bind( wx.EVT_BUTTON, self.onbtneditmodeon )
		self.btnVoorbeeld.Bind( wx.EVT_BUTTON, self.onbtnVoorbeeldClick )
		self.btnToevoegen.Bind( wx.EVT_BUTTON, self.onbtnToevoegenClick )
		self.btnVerwijderen.Bind( wx.EVT_BUTTON, self.onbtnVerwijderenClick )
		self.listFiles.Bind( wx.EVT_LIST_ITEM_FOCUSED, self.onlistFilesFocused )
		self.listFiles.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onlistFilesSelected )
		self.btnArchief.Bind( wx.EVT_BUTTON, self.onbtnArchiefClick )
		self.btnClearLog.Bind( wx.EVT_BUTTON, self.onbtnClearLogClick )
		self.btnWIT.Bind( wx.EVT_BUTTON, self.onbtnWITclick )
		self.btnUpload.Bind( wx.EVT_BUTTON, self.onbtnUploadClick )
		self.Bind( wx.EVT_MENU, self.onmenuitemClickConf, id = self.menuitemConf.GetId() )
		self.Bind( wx.EVT_MENU, self.onmenuitemClickAfsluiten, id = self.menuitemAfsluiten.GetId() )
		self.Bind( wx.EVT_MENU, self.onmenuitemClickAbout, id = self.menuitemAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def oncloseMainframe( self, event ):
		event.Skip()
	
	def onbtnPreviewOnlineClick( self, event ):
		event.Skip()
	
	def onbtnClearListClick( self, event ):
		event.Skip()
	
	def ontvFilesItemActivate( self, event ):
		event.Skip()
	
	def OntvFilesRightClick( self, event ):
		event.Skip()
	
	def ontvFilesSelChanged( self, event ):
		event.Skip()
	
	def onbtneditmodeoff( self, event ):
		event.Skip()
	
	def onbtnRotateClick( self, event ):
		event.Skip()
	
	def onbtneditmodeon( self, event ):
		event.Skip()
	
	def onbtnVoorbeeldClick( self, event ):
		event.Skip()
	
	def onbtnToevoegenClick( self, event ):
		event.Skip()
	
	def onbtnVerwijderenClick( self, event ):
		event.Skip()
	
	def onlistFilesFocused( self, event ):
		event.Skip()
	
	def onlistFilesSelected( self, event ):
		event.Skip()
	
	def onbtnArchiefClick( self, event ):
		event.Skip()
	
	def onbtnClearLogClick( self, event ):
		event.Skip()
	
	def onbtnWITclick( self, event ):
		event.Skip()
	
	def onbtnUploadClick( self, event ):
		event.Skip()
	
	def onmenuitemClickConf( self, event ):
		event.Skip()
	
	def onmenuitemClickAfsluiten( self, event ):
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Upload gelukt", pos = wx.DefaultPosition, size = wx.Size( 727,380 ), style = wx.CAPTION|wx.CLOSE_BOX )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"De foto's zijn geplaatst op de server van aquaforum.nl. Je kan de volgende code gebruiken in je bericht:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer18.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer18, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.text_ctrl_Code1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.text_ctrl_Code1.SetMinSize( wx.Size( -1,127 ) )
		
		bSizer19.Add( self.text_ctrl_Code1, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnCopyToClipboard = wx.Button( self, wx.ID_ANY, u"Zet de code in het klembord (clipboard)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCopyToClipboard.SetDefault() 
		bSizer21.Add( self.btnCopyToClipboard, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer19.Add( bSizer21, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer16.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Als je op de knop \"Zet de code in het klembord (clipboard)\" drukt, dan kan je vervolgens naar het aquaforum surfen met je browser. \nMaak een bericht waar je de foto in wilt hebben, klik rechts met de muis in het bericht  en kies \"plakken\" (of \"paste\"). \nDan staat de code in het bericht.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer20.Add( self.m_staticText6, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer16.Add( bSizer20, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnKlaar = wx.Button( self, wx.ID_ANY, u"Afsluiten", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.btnKlaar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer191, 0, wx.EXPAND, 5 )
		
		
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuratiescherm", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.confedtLoginName = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.confedtLoginName.SetMaxLength( 0 ) 
		gSizer1.Add( self.confedtLoginName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText151 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"aquaforum.nl gebruikersnaam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		gSizer1.Add( self.m_staticText151, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.dirpickFolder = wx.DirPickerCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, u"Selecteer een map", wx.Point( -1,-1 ), wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST|wx.DIRP_USE_TEXTCTRL )
		self.dirpickFolder.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		gSizer1.Add( self.dirpickFolder, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Standaard map", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer1.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choiceDimensieChoices = []
		self.choiceDimensie = wx.Choice( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDimensieChoices, 0 )
		self.choiceDimensie.SetSelection( 0 )
		gSizer1.Add( self.choiceDimensie, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Standaardwaarde voor dimensies", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gSizer1.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.checkPreview = wx.CheckBox( self.m_panel4, wx.ID_ANY, u"Bij aanklikken van een foto bewerkingsmodus tonen.", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.checkPreview, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gSizer1.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.checkWebNieuw = wx.CheckBox( self.m_panel4, wx.ID_ANY, u"Gebruik nieuwe archiefpagina (experimenteel).", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.checkWebNieuw, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.checkTooltip = wx.CheckBox( self.m_panel4, wx.ID_ANY, u"Tooltips laten zien bij mouseover.", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.checkTooltip, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		gSizer1.Add( self.m_staticText91, 0, wx.ALL, 5 )
		
		self.btnImport = wx.Button( self.m_panel4, wx.ID_ANY, u"Importeer foto's uit AquaForumUploader van Riba.", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer1.Add( self.btnImport, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer1.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( gSizer1 )
		self.m_panel4.Layout()
		gSizer1.Fit( self.m_panel4 )
		bSizer42.Add( self.m_panel4, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.checkUpdate = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Bij opstart applicatie controleren of er een update is.", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.checkUpdate, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCheckForUpdate = wx.Button( self.m_panel3, wx.ID_ANY, u"Controleer voor update", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer35.Add( self.btnCheckForUpdate, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtVersie = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Huidige applicatie-versie: ", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txtVersie.Wrap( -1 )
		bSizer35.Add( self.txtVersie, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer35.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_hyperlink4 = wx.HyperlinkCtrl( self.m_panel3, wx.ID_ANY, u"Aquaf downloads", u"https://github.com/labordus/aquaf/releases/latest", wx.DefaultPosition, wx.DefaultSize, wx.HL_CONTEXTMENU|wx.HL_DEFAULT_STYLE )
		bSizer35.Add( self.m_hyperlink4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer33.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer33 )
		self.m_panel3.Layout()
		bSizer33.Fit( self.m_panel3 )
		bSizer42.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND, 0 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.Colour( 116, 113, 162 ) )
		
		bSizer341 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer341.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.btnAfsluiten = wx.Button( self.m_panel5, wx.ID_ANY, u"Afsluiten", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer341.Add( self.btnAfsluiten, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( bSizer341 )
		self.m_panel5.Layout()
		bSizer341.Fit( self.m_panel5 )
		bSizer34.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer42.Add( bSizer34, 0, wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer42 )
		self.Layout()
		bSizer42.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.oninitConfDialog )
		self.confedtLoginName.Bind( wx.EVT_KILL_FOCUS, self.onconfedtLoginNameKillFocus )
		self.dirpickFolder.Bind( wx.EVT_DIRPICKER_CHANGED, self.ondirpickFolderChange )
		self.choiceDimensie.Bind( wx.EVT_CHOICE, self.onChoiceDimensies )
		self.checkPreview.Bind( wx.EVT_CHECKBOX, self.oncheckPreviewClick )
		self.checkWebNieuw.Bind( wx.EVT_CHECKBOX, self.oncheckWebNieuwClick )
		self.checkTooltip.Bind( wx.EVT_CHECKBOX, self.oncheckTooltipClick )
		self.btnImport.Bind( wx.EVT_BUTTON, self.onbtnImportClick )
		self.checkUpdate.Bind( wx.EVT_CHECKBOX, self.oncheckUpdateClick )
		self.btnCheckForUpdate.Bind( wx.EVT_BUTTON, self.onbtnCheckForUpdateClick )
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
	
	def onChoiceDimensies( self, event ):
		event.Skip()
	
	def oncheckPreviewClick( self, event ):
		event.Skip()
	
	def oncheckWebNieuwClick( self, event ):
		event.Skip()
	
	def oncheckTooltipClick( self, event ):
		event.Skip()
	
	def onbtnImportClick( self, event ):
		event.Skip()
	
	def oncheckUpdateClick( self, event ):
		event.Skip()
	
	def onbtnCheckForUpdateClick( self, event ):
		event.Skip()
	
	def onbtnAfsluitenClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgUpdate
###########################################################################

class dlgUpdate ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Update", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Er is een update beschikbaar..", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer33.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_hyperlink4 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"Aquaf downloads", u"https://github.com/labordus/aquaf/releases/latest", wx.DefaultPosition, wx.DefaultSize, wx.HL_CONTEXTMENU|wx.HL_DEFAULT_STYLE )
		bSizer33.Add( self.m_hyperlink4, 0, wx.ALL, 5 )
		
		
		bSizer32.Add( bSizer33, 0, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.textUpdate = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH )
		self.textUpdate.SetMinSize( wx.Size( 250,250 ) )
		
		bSizer34.Add( self.textUpdate, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer32.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		self.btnAfsluiten = wx.Button( self, wx.ID_ANY, u"Afsluiten", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnAfsluiten.SetDefault() 
		bSizer32.Add( self.btnAfsluiten, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer32 )
		self.Layout()
		bSizer32.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnAfsluiten.Bind( wx.EVT_BUTTON, self.onbtnAfsluitenClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onbtnAfsluitenClick( self, event ):
		event.Skip()
	

