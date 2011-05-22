# itunes-refresh

## Update

This code is being imported for posterity, but I don't actually use it anymore, and don't know if it still works.


## Overview

I have a decent amount of music stored on my computer, which gets shared between a number of different devices and media players. Recently I've become obsessed with retagging everything using the [MusicBrainz](http://musicbrainz.org) database. Unfortunately, I found it very difficult to convince iTunes to reload the updated ID3 tags, and I wasn't willing to lose all my play count history.

Using the [iTunes COM SDK](http://developer.apple.com/sdk/itunescomsdk.html), I've thrown together a tool that will examine all tracks in your iTunes library, looking for entries that have been changed on disk since the last time iTunes loaded the file. Any modified entries will be reloaded into iTunes, updating the track metadata while preserving play counts, etc. If an entry no longer exists on disk, it will be removed from the library.

This tool was written and tested against iTunes 7.0 on a Windows XP machine.

## Usage

Start iTunes
Run itunes-refresh

## Known limitations

Currently I assume that all tracks represent files. Exceptions will probably be thrown for URL entries. Despite the exception, it should just move on to the next track and keep processing.
