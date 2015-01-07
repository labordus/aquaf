import wx
import wx.html2
import os

oudepad = os.getcwd()


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

    def oncloseMyBrowser(self, event):
        # verwijder archive.html
        import appdirs
        path = appdirs.user_data_dir('aquaf', False, False, False)
        filepath = os.path.join(path, 'archive.html')
        try:
            os.remove(filepath)
        except OSError:
            pass

        event.Skip()