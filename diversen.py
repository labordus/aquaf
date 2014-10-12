import mechanize
import os
import wx
import string
import Image
import PngImagePlugin  # @UnusedImport
import BmpImagePlugin  # @UnusedImport
import IcoImagePlugin  # @UnusedImport
import JpegImagePlugin  # @UnusedImport
import MpegImagePlugin  # @UnusedImport
import PcxImagePlugin  # @UnusedImport
import PdfImagePlugin  # @UnusedImport
import PpmImagePlugin  # @UnusedImport
import PsdImagePlugin  # @UnusedImport
import TgaImagePlugin  # @UnusedImport
import TiffImagePlugin  # @UnusedImport

Image._initialized = 2

# FORUM_UPLOAD_URL = "http://www.aquaforum.nl/gallery/upload.php"
FORUM_UPLOAD_URL = "http://www.aquaforum.nl/ubb/scripts/upload.php"
VERSION = "0_83"
ALLOWED_CHARS = "qwertyuioplkjhgfdsazxcvbnm0123456789._"

ALPHA_ONLY = 1
DIGIT_ONLY = 2

###########################################################################
# class ValideerInvoer(wx.PyValidator):
###########################################################################


class ValideerInvoer(wx.PyValidator):

    def __init__(self, flag=None, pyVar=None):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        return ValideerInvoer(self.flag)

    def Validate(self, win):
        tc = self.GetWindow()
        val = tc.GetValue()

        if self.flag == ALPHA_ONLY:
            for x in val:
                if x not in string.letters:
                    return False

        elif self.flag == DIGIT_ONLY:
            for x in val:
                if x not in string.digits:
                    return False

        return True

    def OnChar(self, event):
        key = event.GetKeyCode()

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if self.flag == ALPHA_ONLY and chr(key) in string.letters:
            event.Skip()
            return

        if self.flag == DIGIT_ONLY and chr(key) in string.digits:
            event.Skip()
            return

        if not wx.Validator_IsSilent():
            wx.Bell()

        # Returning without calling even.Skip eats the event before it
        # gets to the text control
        return


###########################################################################
# def resizeFile(filename, dimensions):
###########################################################################
def resizeFile(filename, dimensions):
    '''
    returns filename of resized file
    '''
    im = Image.open(filename)  # load the image
#    dim = im.size
    # create temporary file, resize
    resizedFileName = "tempfile.dat"
    # im.thumbnail(dimensions)
    originalDimensions = im.size
    xRatio = float(dimensions[0]) / originalDimensions[0]
    yRatio = float(dimensions[1]) / originalDimensions[1]
    if xRatio < 1 or yRatio < 1:
        # only resize when needed
        minimumRatio = min([xRatio, yRatio])
        im = im.resize(
            (
                int(originalDimensions[0] * minimumRatio),
                int(originalDimensions[1] * minimumRatio)
            ), Image.ANTIALIAS)  # resize
    # try:
    #    im.save(resizedFileName,"JPEG",quality=100,optimize=1)
    # except IOError:
    # try again, without optimization
    try:
        im.save(resizedFileName, "JPEG", quality=60)
    except IOError:
        # try again, without optimization
        im.draft("RGB", im.size)
        im = im.convert("RGB")
        im.save(resizedFileName, "JPEG", quality=60)
    return resizedFileName


###########################################################################
# def addToHistory(url):
###########################################################################
def addToHistory(url):
    '''adds the url to the json archive
    '''
    f = open('images.json', 'r')
    content = f.read()
    f.close()
    text = ""
    if content.find("link") != -1:
        # already got content
        text = ","
    template = '''
        {
      "link":"%s"
    }
]}

''' % url
    text = text + template
    content = content.replace("]}", text)
    f = open('images.json', 'w')
    f.write(content)
    f.close()
    return


###########################################################################
# def uploadFileToAquaforum(uploadFilename, requestedFileName):
###########################################################################
def uploadFileToAquaforum(uploadFilename, requestedFileName):
    '''
    returns response page
    '''

    # build opener. Can be extended to handle cookies/proxies
    opener = mechanize.build_opener()
    # goto upload page
    request3 = mechanize.Request(FORUM_UPLOAD_URL)
    response3 = opener.open(request3)

    # parse form on upload page and add file
    forms = mechanize.ParseResponse(response3, backwards_compat=False)
    form = forms[0]
    filectr = form.find_control("imgfile")
    # filectr.add_file(open('/home/jasper/avatar.jpg'),"image/jpeg","avatar.jpg")
    theFile = file(uploadFilename, 'rb')
    filectr.add_file(theFile, "image/jpeg", os.path.split(
        requestedFileName)[-1])
    # obtain form data
    request4 = form.click()  # urllib2.Request object
    theFile.close()
    request4.add_header('Referer', response3.geturl())
    response4 = opener.open(request4)
    return response4.read()


###########################################################################
# def constructUploadName(loginname, requestedfilename):
###########################################################################
def constructUploadName(loginname, requestedfilename):
    '''
    '''
    # construct name

#    import os
    import string
    import random
    filename = os.path.split(requestedfilename)[1]
    filename = filename[:string.find(filename, ".")] + ".jpg"  # construct jpg extension
    resultName = string.lower(loginname + "_" + VERSION + "_" + filename)  # prepend loginname
    resultName = string.replace(resultName, " ", "_")  # replace spaces
    resultName = string.replace(resultName, "'", "_")  # replace '
    # resultName = urllib.quote(resultName) #make safe url
    theResult = ""
    for theChar in resultName:
        if theChar in ALLOWED_CHARS:
            theResult += theChar
    resultName = theResult
    # check whether ok
    # build opener. Can be extended to handle cookies/proxies
    opener = mechanize.build_opener()
    # goto upload page
    request3 = mechanize.Request(FORUM_UPLOAD_URL)
    response3 = opener.open(request3)
#    page = string.lower(response3.read())
    response3.close()
    random.seed()
    # while not name ok, permutate
    for _i in range(6):
        resultName = str(random.random())[-1] + resultName  # prepend with random number
    # while string.find(page,resultName)<>-1:
    return resultName
