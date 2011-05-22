import musicbrainz2.webservice as mbws

# TODO - cache releases locally to cut down load on server

class mbcache:
    def __init__(self):
        self.releases = {}
        self.query = mbws.Query()
 
    def getReleaseByAlbumId(self, albumId):
        #print "DEBUG: getReleaseByAlbumId in with albumId %s" % albumId
        if self.releases.has_key(albumId):
            return self.releases[albumId]
        
        inc = mbws.ReleaseIncludes(artist=True, releaseEvents=True, discs=True, tracks=True)
        release = self.query.getReleaseById(albumId, inc)
        self.releases[albumId] = release
        return release
