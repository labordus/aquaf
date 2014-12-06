import wx
import wx.html2
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import threading
from time import sleep


class MyServer():

    HandlerClass = SimpleHTTPRequestHandler
    ServerClass = BaseHTTPServer.HTTPServer
    Protocol = "HTTP/1.0"

    server_address = ("127.0.0.1", 8200)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    def run(self):
        #        sa = self.httpd.socket.getsockname()
        #        print "Served HTTP on", sa[0], "port", sa[1], "..."
        thread = threading.Thread(target=self.httpd.serve_forever)
        thread.deamon = True
        thread.start()
        sleep(1)

    def stop(self):
        self.httpd.shutdown()


class MyBrowser(wx.Dialog):

    def __init__(self, *args, **kwds):

        wx.Dialog.__init__(self, *args, **kwds)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = wx.html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        self.SetSizer(sizer)
        self.SetSize((700, 700))
        self.Bind(wx.EVT_CLOSE, self.oncloseMyBrowser)
        serve = MyServer()
        MyServer.run(serve)

    def oncloseMyBrowser(self, event):
        serve = MyServer()
        MyServer.stop(serve)
        event.Skip()
