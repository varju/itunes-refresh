#!/usr/bin/env python

import filecmp
import os
import sys
import time
import traceback
from stat import *

import iTunesApplication

import amazon
import id3
import mbcache

#
# Settings
#
# CHECK_FILES: If true, modified files will be reloaded
CHECK_FILES = True
# CHECK_TIMESTAMP: If false, all files will be reloaded, regardless of modification time
CHECK_TIMESTAMP = True
# OUTPUT_FREQUENCY: How often status should be updated
OUTPUT_FREQUENCY = 100
# FIND_COVER_ART: Should we search for missing cover art?
FIND_COVER_ART = False
# FIND_BAD_COVER_ART: Should we verify that the cover art is okay?
FIND_BAD_COVER_ART = False
# DELETE_BAD_ART: Allow the script to delete bad artwork
DELETE_BAD_ART = False

TEMP_ART_FILE = "d:\\temp\\.artwork.tmp"

MAX_FILES_MODIFIED = 1000

#
# Global objects
#
mbcache = mbcache.mbcache()
deleteList = []

def main():
    iTunesApp = iTunesApplication.iTunesApp()
    library = iTunesApp.LibraryPlaylist;

    i = 0
    for track in library.Tracks:
        i = i + 1

        if (i % OUTPUT_FREQUENCY) == 0:
            print "Working on track %d" % i
            sys.stdout.flush()

        # Can't handle podcast cover art
        findCoverArt = FIND_COVER_ART and not isPodcast(track)

        if not hasattr(track, 'Location'):
            print "DEBUG: no Location attribute for %s" % prettyTrack(track)
            continue

        #if not track.Album == 'Laid':
        #    continue

        #try:
        examineTrack(track, CHECK_FILES, FIND_COVER_ART)
        #except:
            #exc = sys.exc_info()
            #try:
            #    print "Unexpected error with %s:" % prettyTrack(track), exc[0]
            #except:
            #    print "Unexpected error:", exc[0]
            #traceback.print_exception(exc[0], exc[1], exc[2], file=sys.stdout)

    for track in deleteList:
        try:
            print "Not Deleting (%s)" % prettyTrack(track)
            #track.Delete()
        except:
            exc = sys.exc_info()
            try:
                print "Unexpected error with %s:" % prettyTrack(track), exc[0]
            except:
                print "Unexpected error:", exc[0]
            traceback.print_exception(exc[0], exc[1], exc[2], file=sys.stdout)


def examineTrack(track, checkFiles, findCoverArt):
    if checkFiles:
        filestat = checkTrackExistence(track)
        if filestat == None:
            return

        checkTimestamps(track, filestat)

    if findCoverArt:
        checkArtwork(track)

    sys.stdout.flush()


# Returns os.stat output if file exists, None otherwise
# - Deletes track from iTunes if the file does not exist
def checkTrackExistence(track):
    try:
        return os.stat(track.Location)
    except WindowsError:
        if not os.path.exists(track.Location):
            print "DEBUG: Queued (%s) for deletion" % prettyTrack(track)
            deleteList.append(track)
        else:
            print "os.stat failed for %s" % prettyTrack(track)

    return None


def checkTimestamps(track, filestat):
    if CHECK_TIMESTAMP:
        dbTimestamp = int(track.ModificationDate)
        fileTimestamp = filestat[ST_MTIME]

        # iTunes appears to get confused about daylight savings
        if time.localtime(fileTimestamp)[8] == 1:
            dbTimestamp = dbTimestamp + 3600;

        #print "DEBUG: mtime of %s is (%d < %d)" % (track.location, dbTimestamp, fileTimestamp)
        if dbTimestamp >= fileTimestamp:
            return
        
    print "Updated %s" % prettyTrack(track)
    track.UpdateInfoFromFile()


def checkArtwork(track):
    if not hasattr(track, 'Artwork'):
        print "DEBUG: no artwork attribute for %s" % prettyTrack(track)
        return

    artworkCollection = track.Artwork
    if not FIND_BAD_COVER_ART and artworkCollection.Count > 0:
        # album already has art
        return

    albumId = id3.getMusicBrainzId(track.Location)
    if albumId == None:
        print "DEBUG: no albumId available for %s" % prettyTrack(track)
        return

    try:
        release = mbcache.getReleaseByAlbumId(albumId)
    except:
        print "DEBUG: MusicBrainz lookup error for %s" % prettyTrack(track)
        return

    asin = release.getAsin()
    if asin == None:
        print "DEBUG: no amazon ID for %s" % prettyTrack(track)
        return

    imageFile = amazon.getArtwork(asin)
    if imageFile == None:
        print "DEBUG: bad art for %s" % prettyTrack(track)
        #if artworkCollection.Count > 0:
        #    print "DEBUG: consider deleting this file's artwork"
        return

    if FIND_BAD_COVER_ART and artworkCollection.Count > 0:
        if artworkCollection.Count > 1:
            print "DEBUG: findBadCoverArt - too many items for %s" % prettyTrack(track)
            return

        artwork = artworkCollection.Item(1)
        artwork.SaveArtworkToFile(TEMP_ART_FILE)
        #print "DEBUG: saved %s to %s" % (prettyTrack(track), TEMP_ART_FILE)

        oldFileStat = os.stat(TEMP_ART_FILE)
        newFileStat = os.stat(imageFile)

        if oldFileStat[ST_SIZE] == newFileStat[ST_SIZE] or filecmp.cmp(TEMP_ART_FILE, imageFile):
            #print "DEBUG: findBadCoverArt - no change needed for %s" % prettyTrack(track)
            return

        if oldFileStat[ST_SIZE] > newFileStat[ST_SIZE]:
            print "DEBUG: findBadCoverArt - old file is bigger than new file (%d vs %d) for %s" % (oldFileStat[ST_SIZE], newFileStat[ST_SIZE], prettyTrack(track))
            #return

        if DELETE_BAD_ART:
            print "DEBUG: findBadCoverArt - deleting art from %s" % prettyTrack(track)
            artwork.Delete()
        else:
            print "DEBUG: findBadCoverArt - should delete art from %s" % prettyTrack(track)
            return

        
    print "DEBUG: Adding artwork from %s" % (imageFile)
    track.AddArtworkFromFile(imageFile)
    print "Added artwork for %s (%s)" % (prettyTrack(track), albumId)


def prettyTrack(track):
    if hasattr(track, 'Location') and track.Location != "":
        result = track.Location
    else:
        result = "(%s; %s; %s)" % (track.Artist, track.Album, track.Name)
    return result.encode('utf-8')


def isPodcast(track):
    if hasattr(track, 'Podcast') and track.Podcast:
        return True
    return False


if __name__ == "__main__":
    main()
