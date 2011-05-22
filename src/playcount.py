#!/usr/bin/env python

import string
import sys
import traceback
import pywintypes

import iTunesApplication
#import win32com.client
import os

import playcountdb

#
# Settings
#
# OUTPUT_FREQUENCY: How often status should be updated
OUTPUT_FREQUENCY = 100
# SLOW_SEARCH: Do a slower DB search for matching records
SLOW_SEARCH = False
# DELETE_AFTER_CONSUMPTION: Use this if re-importing an iTunes library that has already been consumed once
DELETE_AFTER_CONSUMPTION = True

DBHOST = "www"
DBUSER = "itunes"
DBPASS = "password"
DBNAME = "itunes"

#
# Global objects
#

def main():
    #iTunesApp = win32com.client.gencache.EnsureDispatch("iTunes.Application")
    iTunesApp = iTunesApplication.iTunesApp()
    library = iTunesApp.LibraryPlaylist;

    current = iTunesApp.CurrentTrack
    print current

    foo = library.Tracks.Item(1)
    print foo
    os._exit(0)

    db = playcountdb.db()
    db.loadAllUnusedEntries(SLOW_SEARCH)

    i = 0
    for track in library.Tracks:
        i = i + 1

        if (i % OUTPUT_FREQUENCY) == 0:
            print "Working on track %d" % i
            sys.stdout.flush()

        if isPodcast(track):
            continue

        print track
        #print track.Kind
        #print dir(track)
        continue


        if not hasattr(track, 'Location'):
            print "DEBUG: no Location attribute for %s" % prettyTrack(track)
            continue

        #if track.Location.find("unloaded") == -1:
        #    continue
        #if track.Album != "Across a Wire (disc 1: VH1 Storytellers)":
        #    continue
        #if track.Name != "Ghost Train":
        #    continue
        # Play count: 2; Last played: 2006-11-25 8:16 PM

        examineTrack(db, track)
        try:
            pass
        except:
            exc = sys.exc_info()
            try:
                print "Unexpected error with %s:" % prettyTrack(track), exc[0]
            except:
                print "Unexpected error:", exc[0]
            traceback.print_exception(exc[0], exc[1], exc[2], file=sys.stdout)


def examineTrack(db, track):

    shortName = getShortName(track)
    #if shortName.find("Stabbing") == -1:
    #    return
   
    #print "DEBUG: Looking for entries for shortName %s, track %s" % (shortName, prettyTrack(track))
    if SLOW_SEARCH:
        shortName = db.mungeUrl(shortName);

    entries = db.getUnusedEntries(shortName)
    if len(entries) == 0:
        return
    
    print "DEBUG: Found entries for track %s" % (prettyTrack(track))
    #for entry in entries:
    #    incrementPlayCount(track, entry)
    #    if DELETE_AFTER_CONSUMPTION:
    #        db.delete(entry)
    #    else:
    #        db.consume(entry)

        #sys.exit(0)



def getShortName(track):
    location = track.Location.replace("\\", "/")
    parts = location.split("/")
    if parts[0].lower() == "m:":
        parts = parts[1:]
    if parts[0].lower() == "ipod" or parts[0].lower() == "farm":
        parts = parts[1:]
    if parts[0].lower() == "loaded" or parts[0].lower() == "unloaded":
        parts = parts[1:]
    return string.join(parts, "/")


def incrementPlayCount(track, entry):
    print "DEBUG: Incrementing play count (%d -> %d)" % (track.PlayedCount, track.PlayedCount + 1)
    track.PlayedCount = track.PlayedCount + 1

    #if date == None:
    #    date = time.localtime()
    # TODO - only use the newest date
    #track.PlayedDate = pywintypes.Time(date)

    entryDate = pywintypes.Time(entry.playDate)
    #print "- entrydate is %s" % str(entryDate)
    #print "- trackdate is %s" % str(track.PlayedDate)

    if entryDate > track.PlayedDate:
        print "DEBUG: Replacing track date (%s) with entry date (%s)" % (str(track.PlayedDate), str(entryDate))
        track.PlayedDate = entryDate


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
