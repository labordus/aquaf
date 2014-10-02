# importing wx files
import wx
 
# import the newly created GUI file
import maingui


# inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class CalcFrame(maingui.Mainframe):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        maingui.Mainframe.__init__(self, parent)
 
    # what to when 'Solve' is clicked
    # wx calls this function with and 'event' object
    def onbtnArchiefClick(self, event):
        try:
            print 'print: onbtnArchiefClick'
        except Exception:
            print 'error'
 
# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)
 
# create an object of CalcFrame
frame = CalcFrame(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
