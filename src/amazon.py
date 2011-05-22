import os
import sys
import urllib

CACHE_DIR = "d:/temp/.cache/amazon"

# TODO - only initialize once
def init():
    try:
        targetDir = os.path.dirname(targetFile)
        os.makedirs(targetDir)
    except:
        # TODO - check if it exists and throw an error if it doesn't
        pass


# Returns a list of potential filenames
def getFilename(asin):
    # TODO - figure out how to detect small images surrounded by large white border
    # larger images - ".01._SS500_SCLZZZZZZZ_V1127167167_.jpg"
    suffixes = [".01._AA130_SCMZZZZZZZ_.jpg", ".02._AA240_SCLZZZZZZZ_.jpg",
                ".01._AA240_SCLZZZZZZZ_.jpg", ".01._AA240_SCLZZZZZZZ_V56729926_.jpg"]
    return [asin + suffix for suffix in suffixes]


def getCacheFile(asinFile):
    return os.path.join(CACHE_DIR, asinFile).replace("/", "\\")


def getUrl(asinFile):
    return "http://images.amazon.com/images/P/" + asinFile


def fetchItem(sourceUrl, targetFile):
    try:
        init()
        urllib.urlretrieve(sourceUrl, targetFile)
        print "DEBUG: fetchItem downloaded %s to %s" % (sourceUrl, targetFile)
    except:
        print "DEBUG: urlretrieve failed", sys.exc_info()[0]
        raise


def getArtwork(asin):
    asinFiles = getFilename(asin)
    for asinFile in asinFiles:
        cacheFile = getCacheFile(asinFile)
        if not os.path.exists(cacheFile):
            url = getUrl(asinFile)
            fetchItem(url, cacheFile)

        if not isBadArtworkFile(cacheFile):
            return cacheFile
        
    # TODO - is there any other graceful recovery available here?
    # TODO - is there a difference between bad images and no images found?
    print "DEBUG: bad artwork downloaded!"
    return None


def isBadArtwork(asin):
    #cacheFile = getCacheFile(asin, bigImage, getAlternate)
    #return isBadArtworkFile(cacheFile)

    # TODO - this needs to be rewritten
    return False

    # One idea, but it won't work because this doesn't differentiate between no images found and bad images
    #artwork = getArtwork(asin, False)
    #return (artwork == None)


def isBadArtworkFile(filePath):
    if os.path.exists(filePath):
        size = os.path.getsize(filePath)
        if size == 807:
            # This is the stock "no image available" image
            return True

        if size < 500:
            # Likely an HTTP error message
            return True

    return False
