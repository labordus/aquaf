import mechanize
import os
import wx
import string

try:
    from PIL import Image
    from PIL import JpegImagePlugin  # @UnusedImport
    from PIL import PngImagePlugin  # @UnusedImport
    from PIL import BmpImagePlugin  # @UnusedImport
    from PIL import TiffImagePlugin  # @UnusedImport
except ImportError:
    raise ImportError('Aquaf was unable to import Pil(low). Please confirm it`s installed and available on your current Python path.')

Image._initialized = 2

# FORUM_UPLOAD_URL = "http://www.aquaforum.nl/gallery/upload.php"
FORUM_UPLOAD_URL = "http://www.aquaforum.nl/ubb/scripts/upload.php"
VERSION = "0_83"
ALLOWED_CHARS = "qwertyuioplkjhgfdsazxcvbnm0123456789._"

ALPHA_ONLY = 1
DIGIT_ONLY = 2


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


def getDimensions(index):
    dimensions = None
    if index == 0:
        dimensions = (800, 600)
    elif index == 1:
        dimensions = (640, 480)
    elif index == 2:
        dimensions = (320, 240)
    else:
        dimensions = (160, 120)
    return dimensions


def ResizeImage(pad, dim):
    # try except
    img = Image.open(pad)
    # scale the image, preserving the aspect ratio
    originalDimensions = img.size
    xRatio = float(dim[0]) / originalDimensions[0]
    yRatio = float(dim[1]) / originalDimensions[1]
    if xRatio < 1 or yRatio < 1:
        # only resize when needed
        minimumRatio = min([xRatio, yRatio])
        img = img.resize(
            (
                int(originalDimensions[0] * minimumRatio),
                int(originalDimensions[1] * minimumRatio)
            ), Image.ANTIALIAS)  # resize
    return img


def SaveJPEGToTemp(im):
    #    kwal = 95
    #    try:
    #        im.save(resizedFileName, "JPEG", quality=kwal, optimize=True)
    #    except IOError:
    # try again, without optimization
    #        im.draft("RGB", im.size)
    #        im = im.convert("RGB")
    #        im.save(resizedFileName, "JPEG", quality=kwal, optimize=False)
    #############################################################################
    resizedFileName = "tempfile.dat"
    # quality hoger dan 95 heeft geen nut,
    # zie http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html
    kwaliteit = [95, 94, 93, 92, 91, 90, 88, 86, 84, 82, 80, 78, 76,
                 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50,
                 48, 46, 44, 42, 40, 38, 36]
    for _x in kwaliteit:
        try:
            im.save(resizedFileName, "JPEG", quality=_x, optimize=True)
            filesize = os.path.getsize(resizedFileName)
            if filesize <= 200000:
                break
        except IOError as er:
            wx.MessageDialog(
                "Er is een fout opgetreden tijdens het converteren\n" +
                "De error is " + str(er),
                "Bericht", style=wx.OK).ShowModal()
            break
# FIXME: error-handling voor als bestand toch nog groter is dan 200kb
#    if filesize > 200000:
#        print "kon niet klein genoeg worden gemaakt"
#    print "quality = " + str(_x)
    return resizedFileName
#############################################################################


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


def constructUploadName(loginname, requestedfilename):
    # construct name
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


def IsValidImage(pad):
    import imghdr
    image_type = imghdr.what(pad)
    if not image_type:
        print "error.. geen image-bestand"
        return False
    else:
        # check of bv.. IMAGE.PNG ook echt een PNG is.. anders return.
        # extract extension en maak lowercase
        ext = os.path.splitext(pad)[-1].lower()
        if image_type == 'jpeg':
            if (ext != '.jpg' and
                    ext != '.jpeg'):
                print "filetype JPG heeft geen JPG-extensie"
                return False
        elif image_type == 'bmp':
            if ext != '.bmp':
                print "filetype BMP heeft geen BMP-extensie"
                return False
        elif image_type == 'png':
            if ext != '.png':
                print "filetype PNG heeft geen PNG-extensie"
                return False
        elif image_type == 'tiff':
            if (ext != '.tiff' and
                    ext != '.tif'):
                print "filetype TIF(F) heeft geen TIFF-extensie"
                return False
        else:
            print "Geen ondersteund image format"
            return False
        return True


def PilImageToWxBitmap(myPilImage):
    return WxImageToWxBitmap(PilImageToWxImage(myPilImage))


def WxImageToWxBitmap(myWxImage):
    return myWxImage.ConvertToBitmap()


def PilImageToWxImage(myPilImage, copyAlpha=True):
    hasAlpha = myPilImage.mode[-1] == 'A'
    if copyAlpha and hasAlpha:  # Make sure there is an alpha layer copy.
        myWxImage = wx.EmptyImage(*myPilImage.size)
        myPilImageCopyRGBA = myPilImage.copy()
        myPilImageCopyRGB = myPilImageCopyRGBA.convert('RGB')    # RGBA --> RGB
        myPilImageRgbData = myPilImageCopyRGB.tostring()
        myWxImage.SetData(myPilImageRgbData)
        myWxImage.SetAlphaData(myPilImageCopyRGBA.tostring()[3::4])  # Create layer and insert alpha values.
    else:    # The resulting image will not have alpha.
        myWxImage = wx.EmptyImage(*myPilImage.size)
        myPilImageCopy = myPilImage.copy()
        myPilImageCopyRGB = myPilImageCopy.convert('RGB')    # Discard any alpha from the PIL image.
        myPilImageRgbData = myPilImageCopyRGB.tostring()
        myWxImage.SetData(myPilImageRgbData)
    return myWxImage
