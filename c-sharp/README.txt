2006-11-27
itunes-refresh

This tool will examine all tracks in your iTunes library, looking for
entries that have been changed on disk since the last time iTunes
loaded the file.  Any modified entries will be reloaded into iTunes,
updating the track metadata while preserving play counts, etc.  If an
entry no longer exists on disk, it will be removed from the library.

Tested against iTunes 7.0.

Usage:
1. Start iTunes
2. Run itunes-refresh

Known limitations:
- Currently I assume that all tracks represent files.  Exceptions will
  probably be thrown for URL entries.

WWW: http://www.varju.ca/alex/code/itunes-refresh/
