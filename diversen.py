import Image
import PngImagePlugin
import BmpImagePlugin
import IcoImagePlugin
import JpegImagePlugin
import MpegImagePlugin
import PcxImagePlugin
import PdfImagePlugin
import PpmImagePlugin
import PsdImagePlugin
import TgaImagePlugin
import TiffImagePlugin

Image._initialized = 2

#-------------------------resize file if necessary
def resizeFile(filename, dimensions):
    '''
    returns filename of resized file
    '''
    im = Image.open(filename)  # load the image
    dim = im.size
    # create temporaty file, resize 
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
    #    # try again, without optimization
    try:
        im.save(resizedFileName, "JPEG", quality=60)    
    except IOError:
    #    # try again, without optimization
        im.draft("RGB", im.size)
        im = im.convert("RGB")
        im.save(resizedFileName, "JPEG", quality=60)    
    return resizedFileName
