import mechanize
import os
import wx
import string
import sys
import imp
import appdirs

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
VERSION = "0_84"
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


def DumpImage(im, username, filename):
    import tempfile
    busyDlg = wx.BusyInfo('Bezig met converten en uploaden van de plaatjes...')
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
            if filesize <= 200000:
                break
        except IOError as er:
            print("ERROR : " + str(er))
            os.close(fd)
            os.remove(path)
            return

    desiredName = constructUploadName(username, filename)
    uploadFileToAquaforum(path, desiredName)
    del busyDlg
    return desiredName


def Initialize_JSON():
    path = appdirs.user_data_dir('aquaf', False, False, False)
#    check_path_exists(os.path.join(path, 'aquaf.db'))
    filepath = os.path.join(path, 'aquaf.json')
    text = '''{ items: [
]}
'''
    try:
        fp = open(filepath)
    except IOError:
        # If not exists, create the file
        fp = open(filepath, "w+")
        fp.write(text)
    fp.close()


def IsEmpty_JSON():
    path = appdirs.user_data_dir('aquaf', False, False, False)
    filepath = os.path.join(path, 'aquaf.json')

    f = open(filepath, 'r')
    content = f.read()
    f.close()
    if content.find("link") != -1:
        # already got content
        return False
    else:
        return True


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
            print "Geen ondersteund image-formaat"
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
