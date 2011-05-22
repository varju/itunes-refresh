#!/usr/bin/env python

import playcountdb

#
# Settings
#
# OUTPUT_FREQUENCY: How often status should be updated
OUTPUT_FREQUENCY = 100

DBHOST = "www"
DBUSER = "itunes"
DBPASS = "password"
DBNAME = "itunes"

#
# Global objects
#

def main():
    db = playcountdb.db()
    db.loadAllUnusedEntries()

    for entryName in db.unusedEntries:
        origUrl = entryName
        entryName = entryName.replace(':', '-')
        for char in ('*', '?', '"', '<', '>', '|'):
            entryName = entryName.replace(char, '')
        for char in ('\\'):
            entryName = entryName.replace(char, ' ')

        while entryName.find("./") != -1:
            entryName = entryName.replace("./", "/")

        entryName = entryName.replace(" /", "/")

        entryName = entryName.replace("/mp3/shared/varju/", "")
        entryName = entryName.replace("Various -2000-C - Canadian Music, eh/", "00_singles/")
        entryName = entryName.replace("Various -2000-C - Disco/", "00_singles/")
        entryName = entryName.replace("The Jesus And Mary Chain -1999-LP- Honey's Dead", "Jesus And Mary Chain, The -1992-LP- Honey's Dead")
        entryName = entryName.replace("The Verve - Urban Hymns", "Verve -1997-LP- Urban Hymns")
        entryName = entryName.replace("Thrush Hermit - Clayton Park", "Thrush Hermit -1999-LP- Clayton Park")
        entryName = entryName.replace("The Strokes -2001-LP- Is This It", "Strokes -2001-LP- Is This It")
        entryName = entryName.replace("The Special Guests -2001-LP- First Album", "The Special Guests -2000-LP- First Album")
        #entryName = entryName.replace("", "")
        #entryName = entryName.replace("", "")
        #entryName = entryName.replace("", "")
        #entryName = entryName.replace("", "")
        #entryName = entryName.replace("", "")
        
        if origUrl != entryName:
            print "Changing URL from %s to %s" % (origUrl, entryName)
            for entry in db.unusedEntries[origUrl]:
                entry.url = entryName
                db.updateUrl(entry)
                print "- updated entry ID %d" % entry.id

if __name__ == "__main__":
    main()
