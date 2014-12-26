import wx
import wx.html2
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import threading
from time import sleep
import os
# from mechanize._mechanize import Browser

oudepad = os.getcwd()


class MyServer():
    HandlerClass = SimpleHTTPRequestHandler
    ServerClass = BaseHTTPServer.HTTPServer
    Protocol = "HTTP/1.0"
    server_address = ("127.0.0.1", 8000)
    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    def run(self):
        #        sa = self.httpd.socket.getsockname()
        #        print "Served HTTP on", sa[0], "port", sa[1], "..."
        import appdirs
        datapad = appdirs.user_data_dir('aquaf', False, False, False)
        os.chdir(datapad)

        thread = threading.Thread(target=self.httpd.serve_forever)
        thread.deamon = True
        thread.start()
        sleep(0.25)

    def stop(self):
        self.httpd.shutdown()
        os.chdir(oudepad)


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
        self.SetSize((800, 800))
        self.Bind(wx.EVT_CLOSE, self.oncloseMyBrowser)
        serve = MyServer()
        MyServer.run(serve)

    def oncloseMyBrowser(self, event):
        serve = MyServer()
        MyServer.stop(serve)
        event.Skip()

# verwijder aquaf.json
        import appdirs
        path = appdirs.user_data_dir('aquaf', False, False, False)
        filepath = os.path.join(path, 'aquaf.json')
        try:
            os.remove(filepath)
        except OSError:
            pass
