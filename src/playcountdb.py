#!/usr/bin/env python

import MySQLdb
import re

DBHOST = "www"
DBUSER = "itunes"
DBPASS = "password"
DBNAME = "itunes"

class entry:
    def __init__(self, entryid, playDate, url):
        self.id = entryid
        self.playDate = int(playDate / 1000)
        self.url = url

class db:
    def __init__(self):
        self.conn = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DBNAME)

    #def getUnusedEntries(self, shortName):
    #    entries = []
    #    cursor = self.conn.cursor()
    #    cursor.execute("select id, play_date, url from songs where url = %s and used = 0", (shortName))
    #    for row in cursor.fetchall():
    #        curr = entry(row[0], row[1], row[2])
    #        entries.append(curr)
    #    cursor.close()
    #    return entries
    def getUnusedEntries(self, shortName):
        if self.unusedEntries.has_key(shortName):
            return self.unusedEntries[shortName]
        return []

    def loadAllUnusedEntries(self, slowSearch=False):
        self.unusedEntries = {}
        cursor = self.conn.cursor()
        cursor.execute("select id, play_date, url from songs where used = 0")
        for row in cursor.fetchall():
            id = row[0]
            play_date = row[1]
            url = row[2]
            if slowSearch:
                url = self.mungeUrl(url)
            curr = entry(id, play_date, url)
            if self.unusedEntries.has_key(url):
                self.unusedEntries[url].append(curr)
            else:
                self.unusedEntries[url] = [curr]
        cursor.close()

    def consume(self, entry):
        cursor = self.conn.cursor()
        cursor.execute("update songs set used = 1 where id = %s", (entry.id))
        cursor.close()

    def delete(self, entry):
        cursor = self.conn.cursor()
        cursor.execute("delete from songs where id = %s", (entry.id))
        cursor.close()

    def updateUrl(self, entry):
        cursor = self.conn.cursor()
        cursor.execute("update songs set url = %s where id = %s", (entry.url, entry.id))
        cursor.close()

    def mungeUrl(self, url):
        return re.sub(r'[^\w/]+', "", url)
