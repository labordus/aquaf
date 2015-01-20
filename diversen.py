import imp
import os
import string
import sys
import urllib2

import mechanize
import wx
try:
    from PIL import Image
    from PIL import JpegImagePlugin  # @UnusedImport
    from PIL import PngImagePlugin  # @UnusedImport
    from PIL import BmpImagePlugin  # @UnusedImport
    from PIL import TiffImagePlugin  # @UnusedImport
except ImportError:
    raise ImportError('Aquaf was unable to import Pil(low). Please confirm it`s installed and available on your current Python path.')

Image._initialized = 2

FORUM_UPLOAD_URL = "http://www.aquaforum.nl/ubb/scripts/upload.php"
REMOTE_SERVER = "www.github.com"
UPDATE_URL = "https://raw.githubusercontent.com/labordus/aquaf/master/version.json"
APP_VERSION_STR = "0_85"
APP_VERSION = "0.85"
USER_PREVIEW = 1
USER_USERNAME = ''
USER_WEBNIEUW = 1
USER_FIRSTRUN = 1
USER_IMPORTED = 0
USER_UPDATECHECK = 1
USER_FOLDER = ''
USER_TOOLTIP = 1
ALLOWED_CHARS = "qwertyuioplkjhgfdsazxcvbnm0123456789._"

ALPHA_ONLY = 1
DIGIT_ONLY = 2


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers")  # old py2exe
            or imp.is_frozen("__main__"))  # tools/freeze


def get_main_dir():
    result = ""
    if main_is_frozen():
        result = os.path.dirname(sys.executable)
    else:
        # volgende werkt niet altijd vanuit dev-environment
        #        result = os.path.dirname(sys.argv[0])
        result = os.path.dirname(__file__)
        # volgende werkt ook..
#        result = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if result == "":
        result = "."
    return result


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


def StringToTupleDimensions(sDim):
    if sDim == '800x600':
        tDim = (800, 600)
    if sDim == '640x480':
        tDim = (640, 480)
    if sDim == '320x240':
        tDim = (320, 240)
    if sDim == '160x120':
        tDim = (160, 120)
    return tDim


def ResizeImage(pad, dim):
    # try:
    #    original = Image.open("Lenna.png")
    # except:
    #    print "Unable to load image"
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


def DumpImage(im, username, filename):
    import tempfile
    fd, path = tempfile.mkstemp()
    # quality hoger dan 95 heeft geen nut,
    # zie http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html
    kwaliteit = [95, 94, 93, 92, 91, 90, 88, 86, 84, 82, 80, 78, 76,
                 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50,
                 48, 46, 44, 42, 40, 38, 36]
    for _x in kwaliteit:
        try:
            if im.mode != "RGB":
                im = im.convert("RGB")
            im.save(path, "JPEG", quality=_x, optimize=True)
            filesize = os.path.getsize(path)
            dimWidth, dimHeight = (im.size[0], im.size[1])
            if filesize <= 200000:
                break
        except IOError as er:
            print("ERROR : " + str(er))
            os.close(fd)
            os.remove(path)
            return
    desiredName = constructUploadName(username, filename)
    uploadFileToAquaforum(path, desiredName)
    return desiredName, dimWidth, dimHeight


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
    resultName = string.lower(loginname + "_" + APP_VERSION_STR + "_" + filename)  # prepend loginname
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
            print "Geen ondersteund image-formaat"
            return False
        return True


def is_connected():
    import socket
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(REMOTE_SERVER)
        # connect to the host -- tells us if the host is actually
        # reachable
        _s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False


def UpdateAvailable():
    from urllib2 import URLError
    import json
    if not is_connected():
        print 'update-server is onbereikbaar'
        return ('', '', '')
    try:
        req = urllib2.Request(UPDATE_URL)
    #        req = urllib2.Request("https://gist.githubusercontent.com/labordus/5c67b729991f8b585632/raw/0798969844ff4ad6d5b13365a03d9bf48a669bf6/aquaf_version")
        opener = urllib2.build_opener()
        f = opener.open(req, timeout=5)
        t = f.read()
        json = json.loads(t)
        ReleaseVersion = json['version']
        ReleaseDate = json['date']
        ReleaseChanges = json['changes']
        if APP_VERSION == ReleaseVersion:
            return ('', '', '')
        return (ReleaseVersion, ReleaseDate, ReleaseChanges)
    except URLError:  # Waarschijnlijk timeout-error maar doe net alsof er geen update is..
        return ('', '', '')
        #        print e.reason
        #        print e.code
        #        print e.read()


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


def WxImageToPilImage(wxImage):
    """ trans Wx.Image to PIL Image
        GetData() -> PyProject: Returns a string containing a copy of the RGB bytes of the image.
    """
    pilImage = Image.new('RGB', wxImage.GetSize())  # new
    pilImage.fromstring(wxImage.GetData())  # copy
    return pilImage


def WxBitmapToWxImage(wxBitmap):
    """ trans wx.Bitmap to wx.Image """
    return wx.ImageFromBitmap(wxBitmap)


def WxBitmapToPilImage(wxBitmap):
    """ trans wx.Bitmap to PIL Image """
    return WxImageToPilImage(WxBitmapToWxImage(wxBitmap))
