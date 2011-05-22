#!/usr/bin/env python

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
# OUTPUT_FREQUENCY: How often status should be updated
OUTPUT_FREQUENCY = 100

#
# Global objects
#
mbcache = mbcache.mbcache()

def main():
    iTunesApp = iTunesApplication.iTunesApp()
    library = iTunesApp.LibraryPlaylist;

    i = 0
    for track in library.Tracks:
        i = i + 1

        if (i % OUTPUT_FREQUENCY) == 0:
            print "Working on track %d" % i
            sys.stdout.flush()

        if isPodcast(track):
            continue

        if not hasattr(track, 'Location'):
            print "DEBUG: no Location attribute for %s" % prettyTrack(track)
            continue

        try:
            examineTrack(track)
        except:
            exc = sys.exc_info()
            try:
                print "Unexpected error with %s:" % prettyTrack(track), exc[0]
            except:
                print "Unexpected error:", exc[0]
            traceback.print_exception(exc[0], exc[1], exc[2], file=sys.stdout)


def examineTrack(track):
    if not hasattr(track, 'Artwork'):
        print "No artwork1 for %s" % prettyTrack(track)
        return

    artworkCollection = track.Artwork
    if artworkCollection.Count <= 0:
        print "No artwork2 for %s" % prettyTrack(track)
        return


def prettyTrack(track):
    result = "%s; %s; %s" % (track.Artist, track.Album, track.Name)
    if hasattr(track, 'Location') and track.Location != "":
        result = result + " (" + track.Location + ")"
    return result.encode('utf-8')


def isPodcast(track):
    if hasattr(track, 'Podcast') and track.Podcast:
        return True
    return False


if __name__ == "__main__":
    main()
