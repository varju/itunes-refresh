2009-04-10

Python 2.5.4 - http://www.python.org/download/releases/2.5.4/
- Note that 2.6.x has issues getting MySQL going right now
- Installation: Run installer

pyWin32 build 212 - http://sourceforge.net/projects/pywin32/
- Installation: Run installer

pyMusicBrainz2 0.6.0 - http://users.musicbrainz.org/~matt/
- Installation: python setup.py install

eyeD3 0.6.17 - http://eyed3.nicfit.net/releases/
  cd eyeD3-0.6.17
  ./configure
  make
  make install

setuptools 0.6c9 - http://pypi.python.org/pypi/setuptools
- Installation: Run installer


mySQL
- Theoretical install: export PATH=$PATH:/c/Python25/Scripts; easy_install MySQL-python
  - This didn't work because there is no .egg for Windows
- Ran the old MySQL-python.exe-1.2.2b2.win32-py2.5.exe installer I had lying around


iTunes COM interface
- Run PythonWin
  - Tools > COM Makepy utility
  - Find 'iTunes xx Type Library'
- Generation:
  python c:/Python25/Lib/site-packages/win32com/client/makepy.py -o iTunesApplication.py "iTunes 1.12 Type Library"


Apple COM interface:
- Documented at http://developer.apple.com/sdk/itunescomsdk.html
  - Downloads > Developer Tools





Old


Python 2.5 - http://www.python.org/download/windows/

pyWin32 build 210 - http://sourceforge.net/projects/pywin32/
- http://aspn.activestate.com/ASPN/docs/ActivePython/2.4/pywin32/PyWin32.html
- http://thor.prohosting.com/~pboddie/Python/COM.html

pyMusicBrainz2 0.4.0 - http://users.musicbrainz.org/~matt/
- API: http://users.musicbrainz.org/~matt/python-musicbrainz2/html/
- python setup.py install

#pyMusicBrainz2 dependencies:
#http://users.musicbrainz.org/~luks/libdiscid-0.1.0-win32bin.zip

eyeD3 - http://eyed3.nicfit.net/releases/eyeD3-0.6.12.tar.gz
  cd eyeD3-0.6.12
  ./configure
  make
  make install





Use:
python c:/Python25/Lib/site-packages/win32com/client/makepy.py -o iTunesApplication.py "iTunes 1.9 Type Library"




playcount:
  http://sourceforge.net/projects/mysql-python
  - Used unofficial Python 2.5 build from here: http://www.guildmanus.com/uploaded/MySQL-python.exe-1.2.2b2.win32-py2.5.exe