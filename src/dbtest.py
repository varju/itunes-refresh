#!/usr/bin/env python

import sys
import time
import traceback
import pywintypes
import MySQLdb

import iTunesApplication

import amazon
import id3
import mbcache

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
mbcache = mbcache.mbcache()

def main():
    conn = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DBNAME)
    cursor = conn.cursor()
    cursor.execute("select id, play_date, url, used from songs where id > %s", (18590))
    for row in cursor.fetchall():
        print "row: %s" % str(row)

    cursor.close ()
    conn.close ()



if __name__ == "__main__":
    main()
