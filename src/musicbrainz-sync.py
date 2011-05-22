#!/usr/bin/env python

# TODO - integrate this with itunes-refresh

import os
import sys
import time
import traceback
import unicodedata

import iTunesApplication
#from win32com.client import Dispatch
#import pywintypes
from stat import *

import id3
import mbcache

#
# Settings
#
ALLOW_COMMIT = True

#
# Global objects
#
mbcache = mbcache.mbcache()

def usage():
    print "Usage: %s <path> <path1> ... <pathN>" % sys.argv[0]

def main():
    targetDirs = sys.argv[1:]
    if len(targetDirs) == 0:
        usage()
        return
    
    for targetDir in targetDirs:
        if not os.path.exists(targetDir):
            usage()
            return

    for targetDir in targetDirs:
        if os.path.isdir(targetDir):
            syncDir(targetDir)
        else:
            syncFile(targetDir)


def syncDir(targetDir):
    files = os.listdir(targetDir)
    for f in files:
        path = os.path.join(targetDir, f)

        try:
            if os.path.isdir(path):
                syncDir(path)
            else:
                syncFile(path)
        except:
            exc = sys.exc_info()
            print "Unexpected error:", exc[0]
            traceback.print_exception(exc[0], exc[1], exc[2], file=sys.stdout)


def syncFile(targetFile):
    (root, ext) = os.path.splitext(targetFile)
    if ext.lower() != ".mp3":
        return

    print "DEBUG: syncFile in for %s" % targetFile
    changedFile = False

    tag = id3.parse(targetFile)
    if tag == None:
        print "DEBUG: no tag available for %s" % targetFile
        return
    
    albumId = id3.getMusicBrainzId(targetFile, tag)
    if albumId == None:
        print "DEBUG: no albumId available for %s" % targetFile
        return

    try:
        release = mbcache.getReleaseByAlbumId(albumId)
    except:
        print "DEBUG: MusicBrainz lookup error for %s" % targetFile
        return

    trackNum = tag.getTrackNum()[0]
    if trackNum == None:
        print "DEBUG: couldn't find track number for %s" % targetFile
        return

    releaseTrack = release.getTracks()[trackNum - 1]
    if releaseTrack == None:
        print "DEBUG: couldn't find release track for %s" % targetFile
        return

    releaseArtist = releaseTrack.getArtist()
    if releaseArtist == None:
        releaseArtist = release.getArtist()
    if releaseArtist == None:
        print "DEBUG: couldn't find release artist for %s" % targetFile
    else:
        #print "DEBUG: releaseArtist is %s" % dir(releaseArtist)
        
        releaseArtist = translateArtist(releaseArtist)
        tagArtist = tag.getArtist()

        if releaseArtist == "":
            print "DEBUG: release artist is empty"
        elif releaseArtist != tagArtist:
            print "Tag artist:     %s" % tagArtist.encode('utf-8')
            print "Release artist: %s" % releaseArtist.encode('utf-8')
            tag.setArtist(releaseArtist)
            changedFile = True


    releaseDate = release.getEarliestReleaseDate()
    if releaseDate != None:
        # TODO - consider setting month/day in tag?
        (releaseYear, _, _) = releaseDate.partition('-')
        tagYear = tag.getYear()

        if releaseYear != tagYear:
            print "Tag year:       %s" % tagYear
            print "Release year:   %s" % releaseYear
            tag.setDate(year = releaseYear)
            changedFile = True


    releaseSongTitle = releaseTrack.getTitle()
    tagSongTitle = tag.getTitle()

    if releaseSongTitle != tagSongTitle and releaseSongTitle != "":
        print "Tag title:     %s" % tagSongTitle.encode('utf-8')
        print "Release title: %s" % releaseSongTitle.encode('utf-8')
        tag.setTitle(releaseSongTitle)
        changedFile = True

    releaseAlbum = release.getTitle()
    tagAlbum = tag.getAlbum()

    if releaseAlbum != tagAlbum and releaseAlbum != "":
        print "Tag album:     %s" % tagAlbum.encode('utf-8')
        print "Release album: %s" % releaseAlbum.encode('utf-8')
        tag.setAlbum(releaseAlbum)
        changedFile = True

    if changedFile:
        if ALLOW_COMMIT:
            id3.save(tag)
            print "DEBUG: Wrote to %s" % targetFile
        else:
            print "DEBUG: (commits disabled) Pending changes for %s" % targetFile
        sys.stdout.flush()


    #print "Release:"
    #print "- Artist: %s" % release.getArtist().getName()
    #print "- ReleaseEvents: %s" % release.getReleaseEvents()
    #print "- EarliestReleaseDate: %s" % release.getEarliestReleaseDate()
    #print "- Title: %s" % release.getTitle()

    #print "- Num: %d" % i
    #print "- Title: %s" % releaseTrack.getTitle()
    #print "- Artist: %s" % releaseTrack.getArtist()

    #print "Tag:"
    #print "- Artist: %s" % tag.getArtist()
    #print "- Title: %s" % tag.getTitle()
    #print "- Year: %s" % tag.getYear()
    #print "- TrackNum: %s" % tag.getTrackNum()
    #print "- : %s" % tag.get()


# Stolen from picard/album.py
def translateArtist(artist):
    #print "translateArtist: artist is %s" % dir(artist)
    
    name = artist.getName()
    sortName = artist.getSortName()

    #print "translateArtist: in for name %s, sortName %s" % (name.encode('utf-8'), sortName.encode('utf-8'))
    
    isLatin = True
    for c in name:
        #print "asc is %s" % ord(c)
        if ord(c) < 128:
            continue
        
        #ctg = unicodedata.category(c)
        #if ctg[0] in ['P', 'Z'] or ctg in ['Nd'] or \
        #    unicodedata.name(c).find('LATIN') != -1:
        #    continue
        #print "ctg is %s" % ';'.join(ctg)
        #print "unicodedataname is %s" % unicodedata.name(c)
        isLatin = False
        break
    if not isLatin:
        #print "translateArtist: not isLatin"
        result = []
        chunks = sortName.split('&')
        for chunk in chunks:
            result.append(reverseSortName(chunk.strip()))
        #print "translateArtist: result is %s" % str(result).encode('utf-8')
        return ' & '.join(result)
    #print "translateArtist: out with name %s" % name.encode('utf-8')
    return name


def reverseSortName(sortName):
    chunks = sortName.split(',')
    if len(chunks) == 2:
        return "%s %s" % (chunks[1].strip(), chunks[0].strip())
    if len(chunks) == 3:
        return "%s %s %s" % (chunks[2].strip(), chunks[1].strip(), \
                             chunks[0].strip())
    if len(chunks) == 4:
        return "%s %s, %s %s" % (chunks[1].strip(), chunks[0].strip(), \
                                 chunks[3].strip(), chunks[2].strip())
    else:
        return sortName


if __name__ == "__main__":
    #try:
        main()
    #except:
    #    exc = sys.exc_info()
    #    print "Unexpected error:", exc[0]
    #    traceback.print_exception(exc[0], exc[1], exc[2], file=sys.stdout)
