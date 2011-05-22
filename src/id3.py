import eyeD3
import eyeD3.frames


def parse(location):
    tag = eyeD3.Tag()
    tagFound = tag.link(location)
    if tagFound:
        tag.setTextEncoding(eyeD3.frames.UTF_16_ENCODING)
        return tag

    raise Exception("Failed to parse id3 tag")


def getMusicBrainzId(location, tag=None):
    if tag == None:
        tag = parse(location)
    
    userTextFrames = tag.getUserTextFrames()
    for frame in userTextFrames:
        #print "Frame: %s: %s" % (frame.description, frame.text)
        if frame.description == "MusicBrainz Album Id":
            return frame.text
    return None


def showInfo(location):
    tag = parse(location)

    print "Artist: %s" % tag.getArtist()
    print "Title: %s" % tag.getTitle()
    print "Date: %s" % tag.getDate()
    print "Genre: %s" % tag.getGenre()
    print "TrackNum: %s" % tag.getTrackNum()
    print "Comments: %s" % tag.getComments()
    print "Images: %s" % tag.getImages()
    
    userTextFrames = tag.getUserTextFrames()
    for frame in userTextFrames:
        print "UserFrame[%s]: %s" % (frame.description, frame.text)


def save(tag):
    tag.update(version = eyeD3.ID3_V2_3, backup = True)
