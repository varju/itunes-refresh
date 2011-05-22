#!/usr/bin/env python

import os
import sys
import time
import traceback

import iTunesApplication
#from win32com.client import Dispatch
#import pywintypes
from stat import *

import amazon
import id3
import mbcache

#
# Settings
#
# OUTPUT_FREQUENCY: How often status should be updated
OUTPUT_FREQUENCY = 100

#
# Global objects
#
mbcache = mbcache.mbcache()

def main():
    iTunesApp = iTunesApplication.iTunesApp()
    #iTunesApp = Dispatch("iTunes.Application")
    library = iTunesApp.LibraryPlaylist;

    i = 0
    for track in library.Tracks:
        i = i + 1

        if (i % OUTPUT_FREQUENCY) == 0:
            print "Working on track %d" % i
            sys.stdout.flush()

        if isPodcast(track):
            continue

        try:
            validateTrackArtwork(track)
        except:
            exc = sys.exc_info()
            try:
                print "Unexpected error with %s:" % prettyTrack(track), exc[0]
            except:
                print "Unexpected error:", exc[0]
            traceback.print_exception(exc[0], exc[1], exc[2], file=sys.stdout)


# In certain cases, Amazon will return bad artwork.  I allowed this into my tracks before I realized it was happening...
def validateTrackArtwork(track):
    validateArtwork(track)
    sys.stdout.flush()


def validateArtwork(track):
    #print "DEBUG: validateArtwork in 1"
    #sys.stdout.flush()
    artworkCollection = track.Artwork
    if artworkCollection.Count == 0:
        return
    #print "DEBUG: validateArtwork in 2"
    #sys.stdout.flush()

    artwork = artworkCollection.Item(1)
    #print "DEBUG: validateArtwork in 2.1"
    if artwork.IsDownloadedArtwork:
        return
    #print "DEBUG: validateArtwork in 2.2"

    albumId = id3.getMusicBrainzId(track.Location)
    if albumId == None:
        print "DEBUG: no albumId available for %s" % prettyTrack(track)
        return
    #print "DEBUG: validateArtwork in 3"
    #sys.stdout.flush()
    
    release = mbcache.getReleaseByAlbumId(albumId)
    #print "DEBUG: validateArtwork in 4"
    #sys.stdout.flush()
    asin = release.getAsin()
    #print "DEBUG: validateArtwork in 5"
    #sys.stdout.flush()
    if not asin == None:
        if amazon.isBadArtwork(asin):
            print "Bad artwork in %s" % prettyTrack(track)
            artwork.Delete()
    #print "DEBUG: validateArtwork in 6"
    #sys.stdout.flush()


def prettyTrack(track):
    if hasattr(track, 'Location'):
        return track.Location
    else:
        return "(%s; %s; %s)" % (track.Artist, track.Album, track.Name)


def isPodcast(track):
    if hasattr(track, 'Podcast') and track.Podcast:
        return True
    return False


if __name__ == "__main__":
    main()
