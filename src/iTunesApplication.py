# -*- coding: mbcs -*-
# Created by makepy.py version 0.4.98
# By python version 2.5.4 (r254:67916, Dec 23 2008, 15:10:54) [MSC v.1310 32 bit (Intel)]
# From type library 'iTunes.exe'
# On Fri Apr 10 16:33:01 2009
"""iTunes 1.12 Type Library"""
makepy_version = '0.4.98'
python_version = 0x20504f0

import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{9E93C96F-CF0D-43F6-8BA8-B807A3370712}')
MajorVersion = 1
MinorVersion = 12
LibraryFlags = 8
LCID = 0x0

class constants:
	ITPlayerStateFastForward      =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0001
	ITPlayerStatePlaying          =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0001
	ITPlayerStateRewind           =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0001
	ITPlayerStateStopped          =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0001
	ITVisualSizeLarge             =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0002
	ITVisualSizeMedium            =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0002
	ITVisualSizeSmall             =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0002
	ITCOMDisabledReasonDialog     =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0003
	ITCOMDisabledReasonOther      =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0003
	ITCOMDisabledReasonQuitting   =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0003
	ITPlayButtonStatePauseDisabled=0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0004
	ITPlayButtonStatePauseEnabled =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0004
	ITPlayButtonStatePlayDisabled =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0004
	ITPlayButtonStatePlayEnabled  =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0004
	ITPlayButtonStateStopDisabled =0x5        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0004
	ITPlayButtonStateStopEnabled  =0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0004
	ITPlayerButtonNext            =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0005
	ITPlayerButtonPlay            =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0005
	ITPlayerButtonPrevious        =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0005
	ITPlayerButtonModifierKeyAlt  =0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0006
	ITPlayerButtonModifierKeyCapsLock=0x8        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0006
	ITPlayerButtonModifierKeyControl=0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0006
	ITPlayerButtonModifierKeyNone =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0006
	ITPlayerButtonModifierKeyShift=0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0272_0006
	ITEventAboutToPromptUserToQuit=0x9        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventCOMCallsDisabled       =0x6        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventCOMCallsEnabled        =0x7        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventDatabaseChanged        =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventPlayerPlay             =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventPlayerPlayingTrackChanged=0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventPlayerStop             =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventQuitting               =0x8        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventSoundVolumeChanged     =0xa        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITEventUserInterfaceEnabled   =0x5        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0275_0001
	ITConvertOperationComplete    =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0276_0001
	ITConvertOperationStatusChanged=0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0276_0001
	ITArtworkFormatBMP            =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0277_0001
	ITArtworkFormatJPEG           =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0277_0001
	ITArtworkFormatPNG            =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0277_0001
	ITArtworkFormatUnknown        =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0277_0001
	ITPlaylistKindCD              =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0001
	ITPlaylistKindDevice          =0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0001
	ITPlaylistKindLibrary         =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0001
	ITPlaylistKindRadioTuner      =0x5        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0001
	ITPlaylistKindUnknown         =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0001
	ITPlaylistKindUser            =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0001
	ITPlaylistRepeatModeAll       =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0002
	ITPlaylistRepeatModeOff       =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0002
	ITPlaylistRepeatModeOne       =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0002
	ITPlaylistPrintKindAlbumlist  =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0003
	ITPlaylistPrintKindInsert     =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0003
	ITPlaylistPrintKindPlaylist   =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0003
	ITPlaylistSearchFieldAlbums   =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0004
	ITPlaylistSearchFieldAll      =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0004
	ITPlaylistSearchFieldArtists  =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0004
	ITPlaylistSearchFieldComposers=0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0004
	ITPlaylistSearchFieldSongNames=0x5        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0004
	ITPlaylistSearchFieldVisible  =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0283_0004
	ITUserPlaylistSpecialKindAudiobooks=0x9        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindFolder=0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindMovies=0x7        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindMusic=0x6        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindNone =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindPartyShuffle=0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindPodcasts=0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindPurchasedMusic=0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindTVShows=0x8        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITUserPlaylistSpecialKindVideos=0x5        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0285_0001
	ITSourceKindAudioCD           =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0288_0001
	ITSourceKindDevice            =0x5        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0288_0001
	ITSourceKindIPod              =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0288_0001
	ITSourceKindLibrary           =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0288_0001
	ITSourceKindMP3CD             =0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0288_0001
	ITSourceKindRadioTuner        =0x6        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0288_0001
	ITSourceKindSharedLibrary     =0x7        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0288_0001
	ITSourceKindUnknown           =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0288_0001
	ITTrackKindCD                 =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0001
	ITTrackKindDevice             =0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0001
	ITTrackKindFile               =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0001
	ITTrackKindSharedLibrary      =0x5        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0001
	ITTrackKindURL                =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0001
	ITTrackKindUnknown            =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0001
	ITVideoKindMovie              =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0002
	ITVideoKindMusicVideo         =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0002
	ITVideoKindNone               =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0002
	ITVideoKindTVShow             =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0002
	ITRatingKindComputed          =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0003
	ITRatingKindUser              =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0291_0003
	ITWindowKindArtwork           =0x4        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0297_0001
	ITWindowKindBrowser           =0x1        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0297_0001
	ITWindowKindEQ                =0x3        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0297_0001
	ITWindowKindNowPlaying        =0x5        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0297_0001
	ITWindowKindPlaylist          =0x2        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0297_0001
	ITWindowKindUnknown           =0x0        # from enum __MIDL___MIDL_itf_iTunesCOMInterface_0297_0001

from win32com.client import DispatchBaseClass
class IITArtwork(DispatchBaseClass):
	"""IITArtwork Interface"""
	CLSID = IID('{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}')
	coclass_clsid = None

	def Delete(self):
		"""Delete this piece of artwork from the track."""
		return self._oleobj_.InvokeTypes(1610743808, LCID, 1, (24, 0), (),)

	def SaveArtworkToFile(self, filePath=defaultNamedNotOptArg):
		"""Save artwork data to an image file."""
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), ((8, 1),),filePath
			)

	def SetArtworkFromFile(self, filePath=defaultNamedNotOptArg):
		"""Replace existing artwork data with new artwork from an image file."""
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (24, 0), ((8, 1),),filePath
			)

	_prop_map_get_ = {
		"Description": (1610743813, 2, (8, 0), (), "Description", None),
		"Format": (1610743811, 2, (3, 0), (), "Format", None),
		"IsDownloadedArtwork": (1610743812, 2, (11, 0), (), "IsDownloadedArtwork", None),
	}
	_prop_map_put_ = {
		"Description": ((1610743813, LCID, 4, 0),()),
	}

class IITArtworkCollection(DispatchBaseClass):
	"""IITArtworkCollection Interface"""
	CLSID = IID('{BF2742D7-418C-4858-9AF9-2981B062D23E}')
	coclass_clsid = None

	# Result is of type IITArtwork
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Returns an IITArtwork object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Returns an IITArtwork object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IITAudioCDPlaylist(DispatchBaseClass):
	"""IITAudioCDPlaylist Interface"""
	CLSID = IID('{CF496DF3-0FED-4D7D-9BD8-529B6E8A082E}')
	coclass_clsid = None

	def Delete(self):
		"""Delete this playlist."""
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (24, 0), (),)

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	def PlayFirstTrack(self):
		"""Start playing the first track in this playlist."""
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (24, 0), (),)

	def Print(self, showPrintDialog=defaultNamedNotOptArg, printKind=defaultNamedNotOptArg, theme=defaultNamedNotOptArg):
		"""Print this playlist."""
		return self._oleobj_.InvokeTypes(1610809346, LCID, 1, (24, 0), ((11, 1), (3, 1), (8, 1)),showPrintDialog
			, printKind, theme)

	def Reveal(self):
		"""Reveal the CD playlist in the main browser window."""
		return self._oleobj_.InvokeTypes(1610874887, LCID, 1, (24, 0), (),)

	# Result is of type IITTrackCollection
	def Search(self, searchText=defaultNamedNotOptArg, searchFields=defaultNamedNotOptArg):
		"""Search tracks in this playlist for the specified string."""
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 1, (9, 0), ((8, 1), (3, 1)),searchText
			, searchFields)
		if ret is not None:
			ret = Dispatch(ret, u'Search', '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Artist": (1610874880, 2, (8, 0), (), "Artist", None),
		"Compilation": (1610874881, 2, (11, 0), (), "Compilation", None),
		"Composer": (1610874882, 2, (8, 0), (), "Composer", None),
		"DiscCount": (1610874883, 2, (3, 0), (), "DiscCount", None),
		"DiscNumber": (1610874884, 2, (3, 0), (), "DiscNumber", None),
		"Duration": (1610809350, 2, (3, 0), (), "Duration", None),
		"Genre": (1610874885, 2, (8, 0), (), "Genre", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809348, 2, (3, 0), (), "Kind", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"Shuffle": (1610809351, 2, (11, 0), (), "Shuffle", None),
		"Size": (1610809353, 2, (5, 0), (), "Size", None),
		"SongRepeat": (1610809354, 2, (3, 0), (), "SongRepeat", None),
		# Method 'Source' returns object of type 'IITSource'
		"Source": (1610809349, 2, (9, 0), (), "Source", '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}'),
		"Time": (1610809356, 2, (8, 0), (), "Time", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		# Method 'Tracks' returns object of type 'IITTrackCollection'
		"Tracks": (1610809358, 2, (9, 0), (), "Tracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
		"Visible": (1610809357, 2, (11, 0), (), "Visible", None),
		"Year": (1610874886, 2, (3, 0), (), "Year", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Name": ((1610743809, LCID, 4, 0),()),
		"Shuffle": ((1610809351, LCID, 4, 0),()),
		"SongRepeat": ((1610809354, LCID, 4, 0),()),
	}

class IITBrowserWindow(DispatchBaseClass):
	"""IITBrowserWindow Interface"""
	CLSID = IID('{C999F455-C4D5-4AA4-8277-F99753699974}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Bottom": (1610743825, 2, (3, 0), (), "Bottom", None),
		"Height": (1610743831, 2, (3, 0), (), "Height", None),
		"Kind": (1610743809, 2, (3, 0), (), "Kind", None),
		"Left": (1610743823, 2, (3, 0), (), "Left", None),
		"Maximizable": (1610743815, 2, (11, 0), (), "Maximizable", None),
		"Maximized": (1610743816, 2, (11, 0), (), "Maximized", None),
		"MiniPlayer": (1610809344, 2, (11, 0), (), "MiniPlayer", None),
		"Minimized": (1610743813, 2, (11, 0), (), "Minimized", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Resizable": (1610743812, 2, (11, 0), (), "Resizable", None),
		"Right": (1610743827, 2, (3, 0), (), "Right", None),
		# Method 'SelectedPlaylist' returns object of type 'IITPlaylist'
		"SelectedPlaylist": (1610809347, 2, (9, 0), (), "SelectedPlaylist", '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}'),
		# Method 'SelectedTracks' returns object of type 'IITTrackCollection'
		"SelectedTracks": (1610809346, 2, (9, 0), (), "SelectedTracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
		"Top": (1610743821, 2, (3, 0), (), "Top", None),
		"Visible": (1610743810, 2, (11, 0), (), "Visible", None),
		"Width": (1610743829, 2, (3, 0), (), "Width", None),
		"Zoomable": (1610743818, 2, (11, 0), (), "Zoomable", None),
		"Zoomed": (1610743819, 2, (11, 0), (), "Zoomed", None),
	}
	_prop_map_put_ = {
		"Bottom": ((1610743825, LCID, 4, 0),()),
		"Height": ((1610743831, LCID, 4, 0),()),
		"Left": ((1610743823, LCID, 4, 0),()),
		"Maximized": ((1610743816, LCID, 4, 0),()),
		"MiniPlayer": ((1610809344, LCID, 4, 0),()),
		"Minimized": ((1610743813, LCID, 4, 0),()),
		"Right": ((1610743827, LCID, 4, 0),()),
		"SelectedPlaylist": ((1610809347, LCID, 4, 0),()),
		"Top": ((1610743821, LCID, 4, 0),()),
		"Visible": ((1610743810, LCID, 4, 0),()),
		"Width": ((1610743829, LCID, 4, 0),()),
		"Zoomed": ((1610743819, LCID, 4, 0),()),
	}

class IITConvertOperationStatus(DispatchBaseClass):
	"""IITConvertOperationStatus Interface"""
	CLSID = IID('{7063AAF6-ABA0-493B-B4FC-920A9F105875}')
	coclass_clsid = IID('{D06596AD-C900-41B2-BC68-1B486450FC56}')

	def GetConversionStatus(self, trackName=pythoncom.Missing, progressValue=pythoncom.Missing, maxProgressValue=pythoncom.Missing):
		"""Returns the current conversion status."""
		return self._ApplyTypes_(1610809344, 1, (24, 0), ((16392, 2), (16387, 2), (16387, 2)), u'GetConversionStatus', None,trackName
			, progressValue, maxProgressValue)

	def StopConversion(self):
		"""Stops the current conversion operation."""
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"InProgress": (1610743808, 2, (11, 0), (), "InProgress", None),
		# Method 'Tracks' returns object of type 'IITTrackCollection'
		"Tracks": (1610743809, 2, (9, 0), (), "Tracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
		"maxProgressValue": (1610809348, 2, (3, 0), (), "maxProgressValue", None),
		"progressValue": (1610809347, 2, (3, 0), (), "progressValue", None),
		"trackName": (1610809346, 2, (8, 0), (), "trackName", None),
	}
	_prop_map_put_ = {
	}

class IITEQPreset(DispatchBaseClass):
	"""IITEQPreset Interface"""
	CLSID = IID('{5BE75F4F-68FA-4212-ACB7-BE44EA569759}')
	coclass_clsid = None

	def Delete(self, updateAllTracks=defaultNamedNotOptArg):
		"""Delete this EQ preset."""
		return self._oleobj_.InvokeTypes(1610743832, LCID, 1, (24, 0), ((11, 1),),updateAllTracks
			)

	def Rename(self, newName=defaultNamedNotOptArg, updateAllTracks=defaultNamedNotOptArg):
		"""Rename this EQ preset."""
		return self._oleobj_.InvokeTypes(1610743833, LCID, 1, (24, 0), ((8, 1), (11, 1)),newName
			, updateAllTracks)

	_prop_map_get_ = {
		"Band1": (1610743812, 2, (5, 0), (), "Band1", None),
		"Band10": (1610743830, 2, (5, 0), (), "Band10", None),
		"Band2": (1610743814, 2, (5, 0), (), "Band2", None),
		"Band3": (1610743816, 2, (5, 0), (), "Band3", None),
		"Band4": (1610743818, 2, (5, 0), (), "Band4", None),
		"Band5": (1610743820, 2, (5, 0), (), "Band5", None),
		"Band6": (1610743822, 2, (5, 0), (), "Band6", None),
		"Band7": (1610743824, 2, (5, 0), (), "Band7", None),
		"Band8": (1610743826, 2, (5, 0), (), "Band8", None),
		"Band9": (1610743828, 2, (5, 0), (), "Band9", None),
		"Modifiable": (1610743809, 2, (11, 0), (), "Modifiable", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Preamp": (1610743810, 2, (5, 0), (), "Preamp", None),
	}
	_prop_map_put_ = {
		"Band1": ((1610743812, LCID, 4, 0),()),
		"Band10": ((1610743830, LCID, 4, 0),()),
		"Band2": ((1610743814, LCID, 4, 0),()),
		"Band3": ((1610743816, LCID, 4, 0),()),
		"Band4": ((1610743818, LCID, 4, 0),()),
		"Band5": ((1610743820, LCID, 4, 0),()),
		"Band6": ((1610743822, LCID, 4, 0),()),
		"Band7": ((1610743824, LCID, 4, 0),()),
		"Band8": ((1610743826, LCID, 4, 0),()),
		"Band9": ((1610743828, LCID, 4, 0),()),
		"Preamp": ((1610743810, LCID, 4, 0),()),
	}

class IITEQPresetCollection(DispatchBaseClass):
	"""IITEQPresetCollection Interface"""
	CLSID = IID('{AEF4D111-3331-48DA-B0C2-B468D5D61D08}')
	coclass_clsid = None

	# Result is of type IITEQPreset
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Returns an IITEQPreset object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{5BE75F4F-68FA-4212-ACB7-BE44EA569759}', UnicodeToString=0)
		return ret

	# Result is of type IITEQPreset
	# The method ItemByName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByName(self, Name=defaultNamedNotOptArg):
		"""Returns an IITEQPreset object with the specified name."""
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByName', '{5BE75F4F-68FA-4212-ACB7-BE44EA569759}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Returns an IITEQPreset object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5BE75F4F-68FA-4212-ACB7-BE44EA569759}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{5BE75F4F-68FA-4212-ACB7-BE44EA569759}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{5BE75F4F-68FA-4212-ACB7-BE44EA569759}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IITEncoder(DispatchBaseClass):
	"""IITEncoder Interface"""
	CLSID = IID('{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Format": (1610743809, 2, (8, 0), (), "Format", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}

class IITEncoderCollection(DispatchBaseClass):
	"""IITEncoderCollection Interface"""
	CLSID = IID('{8862BCA9-168D-4549-A9D5-ADB35E553BA6}')
	coclass_clsid = None

	# Result is of type IITEncoder
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Returns an IITEncoder object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}', UnicodeToString=0)
		return ret

	# Result is of type IITEncoder
	# The method ItemByName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByName(self, Name=defaultNamedNotOptArg):
		"""Returns an IITEncoder object with the specified name."""
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByName', '{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Returns an IITEncoder object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IITFileOrCDTrack(DispatchBaseClass):
	"""IITFileOrCDTrack Interface"""
	CLSID = IID('{00D7FE99-7868-4CC7-AD9E-ACFD70D09566}')
	coclass_clsid = None

	# Result is of type IITArtwork
	def AddArtworkFromFile(self, filePath=defaultNamedNotOptArg):
		"""Add artwork from an image file to this track."""
		ret = self._oleobj_.InvokeTypes(1610809346, LCID, 1, (9, 0), ((8, 1),),filePath
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddArtworkFromFile', '{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}', UnicodeToString=0)
		return ret

	def Delete(self):
		"""Delete this track."""
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (24, 0), (),)

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	def Play(self):
		"""Start playing this track."""
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (24, 0), (),)

	def Reveal(self):
		"""Reveal the track in the main browser window."""
		return self._oleobj_.InvokeTypes(1610874932, LCID, 1, (24, 0), (),)

	def UpdateInfoFromFile(self):
		"""Update this track's information with the information stored in its file."""
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), (),)

	def UpdatePodcastFeed(self):
		"""Update the podcast feed for this track."""
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Album": (1610809349, 2, (8, 0), (), "Album", None),
		"AlbumArtist": (1610874906, 2, (8, 0), (), "AlbumArtist", None),
		"AlbumRating": (1610874933, 2, (3, 0), (), "AlbumRating", None),
		"AlbumRatingKind": (1610874935, 2, (3, 0), (), "AlbumRatingKind", None),
		"Artist": (1610809351, 2, (8, 0), (), "Artist", None),
		# Method 'Artwork' returns object of type 'IITArtworkCollection'
		"Artwork": (1610809400, 2, (9, 0), (), "Artwork", '{BF2742D7-418C-4858-9AF9-2981B062D23E}'),
		"BPM": (1610809354, 2, (3, 0), (), "BPM", None),
		"BitRate": (1610809353, 2, (3, 0), (), "BitRate", None),
		"BookmarkTime": (1610874896, 2, (3, 0), (), "BookmarkTime", None),
		"Category": (1610874890, 2, (8, 0), (), "Category", None),
		"Comment": (1610809356, 2, (8, 0), (), "Comment", None),
		"Compilation": (1610809358, 2, (11, 0), (), "Compilation", None),
		"Composer": (1610809360, 2, (8, 0), (), "Composer", None),
		"DateAdded": (1610809362, 2, (7, 0), (), "DateAdded", None),
		"Description": (1610874892, 2, (8, 0), (), "Description", None),
		"DiscCount": (1610809363, 2, (3, 0), (), "DiscCount", None),
		"DiscNumber": (1610809365, 2, (3, 0), (), "DiscNumber", None),
		"Duration": (1610809367, 2, (3, 0), (), "Duration", None),
		"EQ": (1610809370, 2, (8, 0), (), "EQ", None),
		"Enabled": (1610809368, 2, (11, 0), (), "Enabled", None),
		"EpisodeID": (1610874912, 2, (8, 0), (), "EpisodeID", None),
		"EpisodeNumber": (1610874914, 2, (3, 0), (), "EpisodeNumber", None),
		"ExcludeFromShuffle": (1610874886, 2, (11, 0), (), "ExcludeFromShuffle", None),
		"Finish": (1610809372, 2, (3, 0), (), "Finish", None),
		"Genre": (1610809374, 2, (8, 0), (), "Genre", None),
		"Grouping": (1610809376, 2, (8, 0), (), "Grouping", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809347, 2, (3, 0), (), "Kind", None),
		"KindAsString": (1610809378, 2, (8, 0), (), "KindAsString", None),
		"Location": (1610874880, 2, (8, 0), (), "Location", None),
		"LongDescription": (1610874894, 2, (8, 0), (), "LongDescription", None),
		"Lyrics": (1610874888, 2, (8, 0), (), "Lyrics", None),
		"ModificationDate": (1610809379, 2, (7, 0), (), "ModificationDate", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"PartOfGaplessAlbum": (1610874904, 2, (11, 0), (), "PartOfGaplessAlbum", None),
		"PlayOrderIndex": (1610809384, 2, (3, 0), (), "PlayOrderIndex", None),
		"PlayedCount": (1610809380, 2, (3, 0), (), "PlayedCount", None),
		"PlayedDate": (1610809382, 2, (7, 0), (), "PlayedDate", None),
		# Method 'Playlist' returns object of type 'IITPlaylist'
		"Playlist": (1610809348, 2, (9, 0), (), "Playlist", '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}'),
		# Method 'Playlists' returns object of type 'IITPlaylistCollection'
		"Playlists": (1610874937, 2, (9, 0), (), "Playlists", '{FF194254-909D-4437-9C50-3AAC2AE6305C}'),
		"Podcast": (1610874882, 2, (11, 0), (), "Podcast", None),
		"Rating": (1610809385, 2, (3, 0), (), "Rating", None),
		"ReleaseDate": (1610874939, 2, (7, 0), (), "ReleaseDate", None),
		"RememberBookmark": (1610874884, 2, (11, 0), (), "RememberBookmark", None),
		"SampleRate": (1610809387, 2, (3, 0), (), "SampleRate", None),
		"SeasonNumber": (1610874910, 2, (3, 0), (), "SeasonNumber", None),
		"Show": (1610874908, 2, (8, 0), (), "Show", None),
		"Size": (1610809388, 2, (3, 0), (), "Size", None),
		"Size64High": (1610874916, 2, (3, 0), (), "Size64High", None),
		"Size64Low": (1610874917, 2, (3, 0), (), "Size64Low", None),
		"SkippedCount": (1610874900, 2, (3, 0), (), "SkippedCount", None),
		"SkippedDate": (1610874902, 2, (7, 0), (), "SkippedDate", None),
		"SortAlbum": (1610874920, 2, (8, 0), (), "SortAlbum", None),
		"SortAlbumArtist": (1610874922, 2, (8, 0), (), "SortAlbumArtist", None),
		"SortArtist": (1610874924, 2, (8, 0), (), "SortArtist", None),
		"SortComposer": (1610874926, 2, (8, 0), (), "SortComposer", None),
		"SortName": (1610874928, 2, (8, 0), (), "SortName", None),
		"SortShow": (1610874930, 2, (8, 0), (), "SortShow", None),
		"Start": (1610809389, 2, (3, 0), (), "Start", None),
		"Time": (1610809391, 2, (8, 0), (), "Time", None),
		"TrackCount": (1610809392, 2, (3, 0), (), "TrackCount", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		"TrackNumber": (1610809394, 2, (3, 0), (), "TrackNumber", None),
		"Unplayed": (1610874918, 2, (11, 0), (), "Unplayed", None),
		"VideoKind": (1610874898, 2, (3, 0), (), "VideoKind", None),
		"VolumeAdjustment": (1610809396, 2, (3, 0), (), "VolumeAdjustment", None),
		"Year": (1610809398, 2, (3, 0), (), "Year", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"ratingKind": (1610874936, 2, (3, 0), (), "ratingKind", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Album": ((1610809349, LCID, 4, 0),()),
		"AlbumArtist": ((1610874906, LCID, 4, 0),()),
		"AlbumRating": ((1610874933, LCID, 4, 0),()),
		"Artist": ((1610809351, LCID, 4, 0),()),
		"BPM": ((1610809354, LCID, 4, 0),()),
		"BookmarkTime": ((1610874896, LCID, 4, 0),()),
		"Category": ((1610874890, LCID, 4, 0),()),
		"Comment": ((1610809356, LCID, 4, 0),()),
		"Compilation": ((1610809358, LCID, 4, 0),()),
		"Composer": ((1610809360, LCID, 4, 0),()),
		"Description": ((1610874892, LCID, 4, 0),()),
		"DiscCount": ((1610809363, LCID, 4, 0),()),
		"DiscNumber": ((1610809365, LCID, 4, 0),()),
		"EQ": ((1610809370, LCID, 4, 0),()),
		"Enabled": ((1610809368, LCID, 4, 0),()),
		"EpisodeID": ((1610874912, LCID, 4, 0),()),
		"EpisodeNumber": ((1610874914, LCID, 4, 0),()),
		"ExcludeFromShuffle": ((1610874886, LCID, 4, 0),()),
		"Finish": ((1610809372, LCID, 4, 0),()),
		"Genre": ((1610809374, LCID, 4, 0),()),
		"Grouping": ((1610809376, LCID, 4, 0),()),
		"Location": ((1610874880, LCID, 4, 0),()),
		"LongDescription": ((1610874894, LCID, 4, 0),()),
		"Lyrics": ((1610874888, LCID, 4, 0),()),
		"Name": ((1610743809, LCID, 4, 0),()),
		"PartOfGaplessAlbum": ((1610874904, LCID, 4, 0),()),
		"PlayedCount": ((1610809380, LCID, 4, 0),()),
		"PlayedDate": ((1610809382, LCID, 4, 0),()),
		"Rating": ((1610809385, LCID, 4, 0),()),
		"RememberBookmark": ((1610874884, LCID, 4, 0),()),
		"SeasonNumber": ((1610874910, LCID, 4, 0),()),
		"Show": ((1610874908, LCID, 4, 0),()),
		"SkippedCount": ((1610874900, LCID, 4, 0),()),
		"SkippedDate": ((1610874902, LCID, 4, 0),()),
		"SortAlbum": ((1610874920, LCID, 4, 0),()),
		"SortAlbumArtist": ((1610874922, LCID, 4, 0),()),
		"SortArtist": ((1610874924, LCID, 4, 0),()),
		"SortComposer": ((1610874926, LCID, 4, 0),()),
		"SortName": ((1610874928, LCID, 4, 0),()),
		"SortShow": ((1610874930, LCID, 4, 0),()),
		"Start": ((1610809389, LCID, 4, 0),()),
		"TrackCount": ((1610809392, LCID, 4, 0),()),
		"TrackNumber": ((1610809394, LCID, 4, 0),()),
		"Unplayed": ((1610874918, LCID, 4, 0),()),
		"VideoKind": ((1610874898, LCID, 4, 0),()),
		"VolumeAdjustment": ((1610809396, LCID, 4, 0),()),
		"Year": ((1610809398, LCID, 4, 0),()),
	}

class IITIPodSource(DispatchBaseClass):
	"""IITIPodSource Interface"""
	CLSID = IID('{CF4D8ACE-1720-4FB9-B0AE-9877249E89B0}')
	coclass_clsid = None

	def EjectIPod(self):
		"""Eject the iPod."""
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), (),)

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	def UpdateIPod(self):
		"""Update the contents of the iPod."""
		return self._oleobj_.InvokeTypes(1610874880, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Capacity": (1610809345, 2, (5, 0), (), "Capacity", None),
		"FreeSpace": (1610809346, 2, (5, 0), (), "FreeSpace", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809344, 2, (3, 0), (), "Kind", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		# Method 'Playlists' returns object of type 'IITPlaylistCollection'
		"Playlists": (1610809347, 2, (9, 0), (), "Playlists", '{FF194254-909D-4437-9C50-3AAC2AE6305C}'),
		"SoftwareVersion": (1610874882, 2, (8, 0), (), "SoftwareVersion", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Name": ((1610743809, LCID, 4, 0),()),
	}

class IITLibraryPlaylist(DispatchBaseClass):
	"""IITLibraryPlaylist Interface"""
	CLSID = IID('{53AE1704-491C-4289-94A0-958815675A3D}')
	coclass_clsid = None

	# Result is of type IITOperationStatus
	def AddFile(self, filePath=defaultNamedNotOptArg):
		"""Add the specified file path to the library."""
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),filePath
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddFile', '{206479C9-FE32-4F9B-A18A-475AC939B479}', UnicodeToString=0)
		return ret

	# Result is of type IITOperationStatus
	def AddFiles(self, filePaths=defaultNamedNotOptArg):
		"""Add the specified array of file paths to the library. filePaths can be of type VT_ARRAY|VT_VARIANT, where each entry is a VT_BSTR, or VT_ARRAY|VT_BSTR.  You can also pass a JScript Array object."""
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 1, (9, 0), ((16396, 1),),filePaths
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddFiles', '{206479C9-FE32-4F9B-A18A-475AC939B479}', UnicodeToString=0)
		return ret

	# Result is of type IITTrack
	def AddTrack(self, iTrackToAdd=defaultNamedNotOptArg):
		"""Add the specified track to the library.  iTrackToAdd is a VARIANT of type VT_DISPATCH that points to an IITTrack."""
		ret = self._oleobj_.InvokeTypes(1610874883, LCID, 1, (9, 0), ((16396, 1),),iTrackToAdd
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddTrack', '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}', UnicodeToString=0)
		return ret

	# Result is of type IITURLTrack
	def AddURL(self, URL=defaultNamedNotOptArg):
		"""Add the specified streaming audio URL to the library."""
		ret = self._oleobj_.InvokeTypes(1610874882, LCID, 1, (9, 0), ((8, 1),),URL
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddURL', '{1116E3B5-29FD-4393-A7BD-454E5E327900}', UnicodeToString=0)
		return ret

	def Delete(self):
		"""Delete this playlist."""
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (24, 0), (),)

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	def PlayFirstTrack(self):
		"""Start playing the first track in this playlist."""
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (24, 0), (),)

	def Print(self, showPrintDialog=defaultNamedNotOptArg, printKind=defaultNamedNotOptArg, theme=defaultNamedNotOptArg):
		"""Print this playlist."""
		return self._oleobj_.InvokeTypes(1610809346, LCID, 1, (24, 0), ((11, 1), (3, 1), (8, 1)),showPrintDialog
			, printKind, theme)

	# Result is of type IITTrackCollection
	def Search(self, searchText=defaultNamedNotOptArg, searchFields=defaultNamedNotOptArg):
		"""Search tracks in this playlist for the specified string."""
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 1, (9, 0), ((8, 1), (3, 1)),searchText
			, searchFields)
		if ret is not None:
			ret = Dispatch(ret, u'Search', '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Duration": (1610809350, 2, (3, 0), (), "Duration", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809348, 2, (3, 0), (), "Kind", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"Shuffle": (1610809351, 2, (11, 0), (), "Shuffle", None),
		"Size": (1610809353, 2, (5, 0), (), "Size", None),
		"SongRepeat": (1610809354, 2, (3, 0), (), "SongRepeat", None),
		# Method 'Source' returns object of type 'IITSource'
		"Source": (1610809349, 2, (9, 0), (), "Source", '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}'),
		"Time": (1610809356, 2, (8, 0), (), "Time", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		# Method 'Tracks' returns object of type 'IITTrackCollection'
		"Tracks": (1610809358, 2, (9, 0), (), "Tracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
		"Visible": (1610809357, 2, (11, 0), (), "Visible", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Name": ((1610743809, LCID, 4, 0),()),
		"Shuffle": ((1610809351, LCID, 4, 0),()),
		"SongRepeat": ((1610809354, LCID, 4, 0),()),
	}

class IITObject(DispatchBaseClass):
	"""IITObject Interface"""
	CLSID = IID('{9FAB0E27-70D7-4E3A-9965-B0C8B8869BB6}')
	coclass_clsid = None

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	_prop_map_get_ = {
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Name": ((1610743809, LCID, 4, 0),()),
	}

class IITOperationStatus(DispatchBaseClass):
	"""IITOperationStatus Interface"""
	CLSID = IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')
	coclass_clsid = None

	_prop_map_get_ = {
		"InProgress": (1610743808, 2, (11, 0), (), "InProgress", None),
		# Method 'Tracks' returns object of type 'IITTrackCollection'
		"Tracks": (1610743809, 2, (9, 0), (), "Tracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
	}
	_prop_map_put_ = {
	}

class IITPlaylist(DispatchBaseClass):
	"""IITPlaylist Interface"""
	CLSID = IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')
	coclass_clsid = None

	def Delete(self):
		"""Delete this playlist."""
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (24, 0), (),)

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	def PlayFirstTrack(self):
		"""Start playing the first track in this playlist."""
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (24, 0), (),)

	def Print(self, showPrintDialog=defaultNamedNotOptArg, printKind=defaultNamedNotOptArg, theme=defaultNamedNotOptArg):
		"""Print this playlist."""
		return self._oleobj_.InvokeTypes(1610809346, LCID, 1, (24, 0), ((11, 1), (3, 1), (8, 1)),showPrintDialog
			, printKind, theme)

	# Result is of type IITTrackCollection
	def Search(self, searchText=defaultNamedNotOptArg, searchFields=defaultNamedNotOptArg):
		"""Search tracks in this playlist for the specified string."""
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 1, (9, 0), ((8, 1), (3, 1)),searchText
			, searchFields)
		if ret is not None:
			ret = Dispatch(ret, u'Search', '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Duration": (1610809350, 2, (3, 0), (), "Duration", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809348, 2, (3, 0), (), "Kind", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"Shuffle": (1610809351, 2, (11, 0), (), "Shuffle", None),
		"Size": (1610809353, 2, (5, 0), (), "Size", None),
		"SongRepeat": (1610809354, 2, (3, 0), (), "SongRepeat", None),
		# Method 'Source' returns object of type 'IITSource'
		"Source": (1610809349, 2, (9, 0), (), "Source", '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}'),
		"Time": (1610809356, 2, (8, 0), (), "Time", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		# Method 'Tracks' returns object of type 'IITTrackCollection'
		"Tracks": (1610809358, 2, (9, 0), (), "Tracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
		"Visible": (1610809357, 2, (11, 0), (), "Visible", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Name": ((1610743809, LCID, 4, 0),()),
		"Shuffle": ((1610809351, LCID, 4, 0),()),
		"SongRepeat": ((1610809354, LCID, 4, 0),()),
	}

class IITPlaylistCollection(DispatchBaseClass):
	"""IITPlaylistCollection Interface"""
	CLSID = IID('{FF194254-909D-4437-9C50-3AAC2AE6305C}')
	coclass_clsid = None

	# Result is of type IITPlaylist
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Returns an IITPlaylist object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	# Result is of type IITPlaylist
	# The method ItemByName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByName(self, Name=defaultNamedNotOptArg):
		"""Returns an IITPlaylist object with the specified name."""
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByName', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	# Result is of type IITPlaylist
	# The method ItemByPersistentID is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByPersistentID(self, highID=defaultNamedNotOptArg, lowID=defaultNamedNotOptArg):
		"""Returns an IITPlaylist object with the specified persistent ID."""
		ret = self._oleobj_.InvokeTypes(1610743812, LCID, 2, (9, 0), ((3, 1), (3, 1)),highID
			, lowID)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByPersistentID', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Returns an IITPlaylist object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IITPlaylistWindow(DispatchBaseClass):
	"""IITPlaylistWindow Interface"""
	CLSID = IID('{349CBB45-2E5A-4822-8E4A-A75555A186F7}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Bottom": (1610743825, 2, (3, 0), (), "Bottom", None),
		"Height": (1610743831, 2, (3, 0), (), "Height", None),
		"Kind": (1610743809, 2, (3, 0), (), "Kind", None),
		"Left": (1610743823, 2, (3, 0), (), "Left", None),
		"Maximizable": (1610743815, 2, (11, 0), (), "Maximizable", None),
		"Maximized": (1610743816, 2, (11, 0), (), "Maximized", None),
		"Minimized": (1610743813, 2, (11, 0), (), "Minimized", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		# Method 'Playlist' returns object of type 'IITPlaylist'
		"Playlist": (1610809345, 2, (9, 0), (), "Playlist", '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}'),
		"Resizable": (1610743812, 2, (11, 0), (), "Resizable", None),
		"Right": (1610743827, 2, (3, 0), (), "Right", None),
		# Method 'SelectedTracks' returns object of type 'IITTrackCollection'
		"SelectedTracks": (1610809344, 2, (9, 0), (), "SelectedTracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
		"Top": (1610743821, 2, (3, 0), (), "Top", None),
		"Visible": (1610743810, 2, (11, 0), (), "Visible", None),
		"Width": (1610743829, 2, (3, 0), (), "Width", None),
		"Zoomable": (1610743818, 2, (11, 0), (), "Zoomable", None),
		"Zoomed": (1610743819, 2, (11, 0), (), "Zoomed", None),
	}
	_prop_map_put_ = {
		"Bottom": ((1610743825, LCID, 4, 0),()),
		"Height": ((1610743831, LCID, 4, 0),()),
		"Left": ((1610743823, LCID, 4, 0),()),
		"Maximized": ((1610743816, LCID, 4, 0),()),
		"Minimized": ((1610743813, LCID, 4, 0),()),
		"Right": ((1610743827, LCID, 4, 0),()),
		"Top": ((1610743821, LCID, 4, 0),()),
		"Visible": ((1610743810, LCID, 4, 0),()),
		"Width": ((1610743829, LCID, 4, 0),()),
		"Zoomed": ((1610743819, LCID, 4, 0),()),
	}

class IITSource(DispatchBaseClass):
	"""IITSource Interface"""
	CLSID = IID('{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}')
	coclass_clsid = None

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	_prop_map_get_ = {
		"Capacity": (1610809345, 2, (5, 0), (), "Capacity", None),
		"FreeSpace": (1610809346, 2, (5, 0), (), "FreeSpace", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809344, 2, (3, 0), (), "Kind", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		# Method 'Playlists' returns object of type 'IITPlaylistCollection'
		"Playlists": (1610809347, 2, (9, 0), (), "Playlists", '{FF194254-909D-4437-9C50-3AAC2AE6305C}'),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Name": ((1610743809, LCID, 4, 0),()),
	}

class IITSourceCollection(DispatchBaseClass):
	"""IITSourceCollection Interface"""
	CLSID = IID('{2FF6CE20-FF87-4183-B0B3-F323D047AF41}')
	coclass_clsid = None

	# Result is of type IITSource
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Returns an IITSource object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}', UnicodeToString=0)
		return ret

	# Result is of type IITSource
	# The method ItemByName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByName(self, Name=defaultNamedNotOptArg):
		"""Returns an IITSource object with the specified name."""
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByName', '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}', UnicodeToString=0)
		return ret

	# Result is of type IITSource
	# The method ItemByPersistentID is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByPersistentID(self, highID=defaultNamedNotOptArg, lowID=defaultNamedNotOptArg):
		"""Returns an IITSource object with the specified persistent ID."""
		ret = self._oleobj_.InvokeTypes(1610743812, LCID, 2, (9, 0), ((3, 1), (3, 1)),highID
			, lowID)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByPersistentID', '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Returns an IITSource object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IITTrack(DispatchBaseClass):
	"""IITTrack Interface"""
	CLSID = IID('{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')
	coclass_clsid = None

	# Result is of type IITArtwork
	def AddArtworkFromFile(self, filePath=defaultNamedNotOptArg):
		"""Add artwork from an image file to this track."""
		ret = self._oleobj_.InvokeTypes(1610809346, LCID, 1, (9, 0), ((8, 1),),filePath
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddArtworkFromFile', '{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}', UnicodeToString=0)
		return ret

	def Delete(self):
		"""Delete this track."""
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (24, 0), (),)

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	def Play(self):
		"""Start playing this track."""
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Album": (1610809349, 2, (8, 0), (), "Album", None),
		"Artist": (1610809351, 2, (8, 0), (), "Artist", None),
		# Method 'Artwork' returns object of type 'IITArtworkCollection'
		"Artwork": (1610809400, 2, (9, 0), (), "Artwork", '{BF2742D7-418C-4858-9AF9-2981B062D23E}'),
		"BPM": (1610809354, 2, (3, 0), (), "BPM", None),
		"BitRate": (1610809353, 2, (3, 0), (), "BitRate", None),
		"Comment": (1610809356, 2, (8, 0), (), "Comment", None),
		"Compilation": (1610809358, 2, (11, 0), (), "Compilation", None),
		"Composer": (1610809360, 2, (8, 0), (), "Composer", None),
		"DateAdded": (1610809362, 2, (7, 0), (), "DateAdded", None),
		"DiscCount": (1610809363, 2, (3, 0), (), "DiscCount", None),
		"DiscNumber": (1610809365, 2, (3, 0), (), "DiscNumber", None),
		"Duration": (1610809367, 2, (3, 0), (), "Duration", None),
		"EQ": (1610809370, 2, (8, 0), (), "EQ", None),
		"Enabled": (1610809368, 2, (11, 0), (), "Enabled", None),
		"Finish": (1610809372, 2, (3, 0), (), "Finish", None),
		"Genre": (1610809374, 2, (8, 0), (), "Genre", None),
		"Grouping": (1610809376, 2, (8, 0), (), "Grouping", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809347, 2, (3, 0), (), "Kind", None),
		"KindAsString": (1610809378, 2, (8, 0), (), "KindAsString", None),
		"ModificationDate": (1610809379, 2, (7, 0), (), "ModificationDate", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"PlayOrderIndex": (1610809384, 2, (3, 0), (), "PlayOrderIndex", None),
		"PlayedCount": (1610809380, 2, (3, 0), (), "PlayedCount", None),
		"PlayedDate": (1610809382, 2, (7, 0), (), "PlayedDate", None),
		# Method 'Playlist' returns object of type 'IITPlaylist'
		"Playlist": (1610809348, 2, (9, 0), (), "Playlist", '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}'),
		"Rating": (1610809385, 2, (3, 0), (), "Rating", None),
		"SampleRate": (1610809387, 2, (3, 0), (), "SampleRate", None),
		"Size": (1610809388, 2, (3, 0), (), "Size", None),
		"Start": (1610809389, 2, (3, 0), (), "Start", None),
		"Time": (1610809391, 2, (8, 0), (), "Time", None),
		"TrackCount": (1610809392, 2, (3, 0), (), "TrackCount", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		"TrackNumber": (1610809394, 2, (3, 0), (), "TrackNumber", None),
		"VolumeAdjustment": (1610809396, 2, (3, 0), (), "VolumeAdjustment", None),
		"Year": (1610809398, 2, (3, 0), (), "Year", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Album": ((1610809349, LCID, 4, 0),()),
		"Artist": ((1610809351, LCID, 4, 0),()),
		"BPM": ((1610809354, LCID, 4, 0),()),
		"Comment": ((1610809356, LCID, 4, 0),()),
		"Compilation": ((1610809358, LCID, 4, 0),()),
		"Composer": ((1610809360, LCID, 4, 0),()),
		"DiscCount": ((1610809363, LCID, 4, 0),()),
		"DiscNumber": ((1610809365, LCID, 4, 0),()),
		"EQ": ((1610809370, LCID, 4, 0),()),
		"Enabled": ((1610809368, LCID, 4, 0),()),
		"Finish": ((1610809372, LCID, 4, 0),()),
		"Genre": ((1610809374, LCID, 4, 0),()),
		"Grouping": ((1610809376, LCID, 4, 0),()),
		"Name": ((1610743809, LCID, 4, 0),()),
		"PlayedCount": ((1610809380, LCID, 4, 0),()),
		"PlayedDate": ((1610809382, LCID, 4, 0),()),
		"Rating": ((1610809385, LCID, 4, 0),()),
		"Start": ((1610809389, LCID, 4, 0),()),
		"TrackCount": ((1610809392, LCID, 4, 0),()),
		"TrackNumber": ((1610809394, LCID, 4, 0),()),
		"VolumeAdjustment": ((1610809396, LCID, 4, 0),()),
		"Year": ((1610809398, LCID, 4, 0),()),
	}

class IITTrackCollection(DispatchBaseClass):
	"""IITTrackCollection Interface"""
	CLSID = IID('{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}')
	coclass_clsid = None

	# Result is of type IITTrack
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Returns an IITTrack object corresponding to the given fixed index, where the index is independent of the play order (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}', UnicodeToString=0)
		return ret

	# Result is of type IITTrack
	# The method ItemByName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByName(self, Name=defaultNamedNotOptArg):
		"""Returns an IITTrack object with the specified name."""
		ret = self._oleobj_.InvokeTypes(1610743811, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByName', '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}', UnicodeToString=0)
		return ret

	# Result is of type IITTrack
	# The method ItemByPersistentID is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByPersistentID(self, highID=defaultNamedNotOptArg, lowID=defaultNamedNotOptArg):
		"""Returns an IITTrack object with the specified persistent ID."""
		ret = self._oleobj_.InvokeTypes(1610743813, LCID, 2, (9, 0), ((3, 1), (3, 1)),highID
			, lowID)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByPersistentID', '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}', UnicodeToString=0)
		return ret

	# Result is of type IITTrack
	# The method ItemByPlayOrder is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByPlayOrder(self, Index=defaultNamedNotOptArg):
		"""Returns an IITTrack object corresponding to the given index, where the index is defined by the play order of the playlist containing the track collection (1-based)."""
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByPlayOrder', '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Returns an IITTrack object corresponding to the given fixed index, where the index is independent of the play order (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IITURLTrack(DispatchBaseClass):
	"""IITURLTrack Interface"""
	CLSID = IID('{1116E3B5-29FD-4393-A7BD-454E5E327900}')
	coclass_clsid = None

	# Result is of type IITArtwork
	def AddArtworkFromFile(self, filePath=defaultNamedNotOptArg):
		"""Add artwork from an image file to this track."""
		ret = self._oleobj_.InvokeTypes(1610809346, LCID, 1, (9, 0), ((8, 1),),filePath
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddArtworkFromFile', '{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}', UnicodeToString=0)
		return ret

	def Delete(self):
		"""Delete this track."""
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (24, 0), (),)

	def DownloadPodcastEpisode(self):
		"""Start downloading the podcast episode that corresponds to this track."""
		return self._oleobj_.InvokeTypes(1610874884, LCID, 1, (24, 0), (),)

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	def Play(self):
		"""Start playing this track."""
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (24, 0), (),)

	def Reveal(self):
		"""Reveal the track in the main browser window."""
		return self._oleobj_.InvokeTypes(1610874891, LCID, 1, (24, 0), (),)

	def UpdatePodcastFeed(self):
		"""Update the podcast feed for this track."""
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Album": (1610809349, 2, (8, 0), (), "Album", None),
		"AlbumRating": (1610874892, 2, (3, 0), (), "AlbumRating", None),
		"AlbumRatingKind": (1610874894, 2, (3, 0), (), "AlbumRatingKind", None),
		"Artist": (1610809351, 2, (8, 0), (), "Artist", None),
		# Method 'Artwork' returns object of type 'IITArtworkCollection'
		"Artwork": (1610809400, 2, (9, 0), (), "Artwork", '{BF2742D7-418C-4858-9AF9-2981B062D23E}'),
		"BPM": (1610809354, 2, (3, 0), (), "BPM", None),
		"BitRate": (1610809353, 2, (3, 0), (), "BitRate", None),
		"Category": (1610874885, 2, (8, 0), (), "Category", None),
		"Comment": (1610809356, 2, (8, 0), (), "Comment", None),
		"Compilation": (1610809358, 2, (11, 0), (), "Compilation", None),
		"Composer": (1610809360, 2, (8, 0), (), "Composer", None),
		"DateAdded": (1610809362, 2, (7, 0), (), "DateAdded", None),
		"Description": (1610874887, 2, (8, 0), (), "Description", None),
		"DiscCount": (1610809363, 2, (3, 0), (), "DiscCount", None),
		"DiscNumber": (1610809365, 2, (3, 0), (), "DiscNumber", None),
		"Duration": (1610809367, 2, (3, 0), (), "Duration", None),
		"EQ": (1610809370, 2, (8, 0), (), "EQ", None),
		"Enabled": (1610809368, 2, (11, 0), (), "Enabled", None),
		"Finish": (1610809372, 2, (3, 0), (), "Finish", None),
		"Genre": (1610809374, 2, (8, 0), (), "Genre", None),
		"Grouping": (1610809376, 2, (8, 0), (), "Grouping", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809347, 2, (3, 0), (), "Kind", None),
		"KindAsString": (1610809378, 2, (8, 0), (), "KindAsString", None),
		"LongDescription": (1610874889, 2, (8, 0), (), "LongDescription", None),
		"ModificationDate": (1610809379, 2, (7, 0), (), "ModificationDate", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"PlayOrderIndex": (1610809384, 2, (3, 0), (), "PlayOrderIndex", None),
		"PlayedCount": (1610809380, 2, (3, 0), (), "PlayedCount", None),
		"PlayedDate": (1610809382, 2, (7, 0), (), "PlayedDate", None),
		# Method 'Playlist' returns object of type 'IITPlaylist'
		"Playlist": (1610809348, 2, (9, 0), (), "Playlist", '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}'),
		# Method 'Playlists' returns object of type 'IITPlaylistCollection'
		"Playlists": (1610874896, 2, (9, 0), (), "Playlists", '{FF194254-909D-4437-9C50-3AAC2AE6305C}'),
		"Podcast": (1610874882, 2, (11, 0), (), "Podcast", None),
		"Rating": (1610809385, 2, (3, 0), (), "Rating", None),
		"SampleRate": (1610809387, 2, (3, 0), (), "SampleRate", None),
		"Size": (1610809388, 2, (3, 0), (), "Size", None),
		"Start": (1610809389, 2, (3, 0), (), "Start", None),
		"Time": (1610809391, 2, (8, 0), (), "Time", None),
		"TrackCount": (1610809392, 2, (3, 0), (), "TrackCount", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		"TrackNumber": (1610809394, 2, (3, 0), (), "TrackNumber", None),
		"URL": (1610874880, 2, (8, 0), (), "URL", None),
		"VolumeAdjustment": (1610809396, 2, (3, 0), (), "VolumeAdjustment", None),
		"Year": (1610809398, 2, (3, 0), (), "Year", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"ratingKind": (1610874895, 2, (3, 0), (), "ratingKind", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Album": ((1610809349, LCID, 4, 0),()),
		"AlbumRating": ((1610874892, LCID, 4, 0),()),
		"Artist": ((1610809351, LCID, 4, 0),()),
		"BPM": ((1610809354, LCID, 4, 0),()),
		"Category": ((1610874885, LCID, 4, 0),()),
		"Comment": ((1610809356, LCID, 4, 0),()),
		"Compilation": ((1610809358, LCID, 4, 0),()),
		"Composer": ((1610809360, LCID, 4, 0),()),
		"Description": ((1610874887, LCID, 4, 0),()),
		"DiscCount": ((1610809363, LCID, 4, 0),()),
		"DiscNumber": ((1610809365, LCID, 4, 0),()),
		"EQ": ((1610809370, LCID, 4, 0),()),
		"Enabled": ((1610809368, LCID, 4, 0),()),
		"Finish": ((1610809372, LCID, 4, 0),()),
		"Genre": ((1610809374, LCID, 4, 0),()),
		"Grouping": ((1610809376, LCID, 4, 0),()),
		"LongDescription": ((1610874889, LCID, 4, 0),()),
		"Name": ((1610743809, LCID, 4, 0),()),
		"PlayedCount": ((1610809380, LCID, 4, 0),()),
		"PlayedDate": ((1610809382, LCID, 4, 0),()),
		"Rating": ((1610809385, LCID, 4, 0),()),
		"Start": ((1610809389, LCID, 4, 0),()),
		"TrackCount": ((1610809392, LCID, 4, 0),()),
		"TrackNumber": ((1610809394, LCID, 4, 0),()),
		"URL": ((1610874880, LCID, 4, 0),()),
		"VolumeAdjustment": ((1610809396, LCID, 4, 0),()),
		"Year": ((1610809398, LCID, 4, 0),()),
	}

class IITUserPlaylist(DispatchBaseClass):
	"""IITUserPlaylist Interface"""
	CLSID = IID('{0A504DED-A0B5-465A-8A94-50E20D7DF692}')
	coclass_clsid = None

	# Result is of type IITOperationStatus
	def AddFile(self, filePath=defaultNamedNotOptArg):
		"""Add the specified file path to the user playlist."""
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),filePath
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddFile', '{206479C9-FE32-4F9B-A18A-475AC939B479}', UnicodeToString=0)
		return ret

	# Result is of type IITOperationStatus
	def AddFiles(self, filePaths=defaultNamedNotOptArg):
		"""Add the specified array of file paths to the user playlist. filePaths can be of type VT_ARRAY|VT_VARIANT, where each entry is a VT_BSTR, or VT_ARRAY|VT_BSTR.  You can also pass a JScript Array object."""
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 1, (9, 0), ((16396, 1),),filePaths
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddFiles', '{206479C9-FE32-4F9B-A18A-475AC939B479}', UnicodeToString=0)
		return ret

	# Result is of type IITTrack
	def AddTrack(self, iTrackToAdd=defaultNamedNotOptArg):
		"""Add the specified track to the user playlist.  iTrackToAdd is a VARIANT of type VT_DISPATCH that points to an IITTrack."""
		ret = self._oleobj_.InvokeTypes(1610874883, LCID, 1, (9, 0), ((16396, 1),),iTrackToAdd
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddTrack', '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}', UnicodeToString=0)
		return ret

	# Result is of type IITURLTrack
	def AddURL(self, URL=defaultNamedNotOptArg):
		"""Add the specified streaming audio URL to the user playlist."""
		ret = self._oleobj_.InvokeTypes(1610874882, LCID, 1, (9, 0), ((8, 1),),URL
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddURL', '{1116E3B5-29FD-4393-A7BD-454E5E327900}', UnicodeToString=0)
		return ret

	# Result is of type IITPlaylist
	def CreateFolder(self, folderName=defaultNamedNotOptArg):
		"""Creates a new folder in a folder playlist."""
		ret = self._oleobj_.InvokeTypes(1610874890, LCID, 1, (9, 0), ((8, 1),),folderName
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreateFolder', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	# Result is of type IITPlaylist
	def CreatePlaylist(self, playlistName=defaultNamedNotOptArg):
		"""Creates a new playlist in a folder playlist."""
		ret = self._oleobj_.InvokeTypes(1610874889, LCID, 1, (9, 0), ((8, 1),),playlistName
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreatePlaylist', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	def Delete(self):
		"""Delete this playlist."""
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (24, 0), (),)

	def GetITObjectIDs(self, sourceID=pythoncom.Missing, playlistID=pythoncom.Missing, trackID=pythoncom.Missing, databaseID=pythoncom.Missing):
		"""Returns the four IDs that uniquely identify this object."""
		return self._ApplyTypes_(1610743808, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetITObjectIDs', None,sourceID
			, playlistID, trackID, databaseID)

	def PlayFirstTrack(self):
		"""Start playing the first track in this playlist."""
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (24, 0), (),)

	def Print(self, showPrintDialog=defaultNamedNotOptArg, printKind=defaultNamedNotOptArg, theme=defaultNamedNotOptArg):
		"""Print this playlist."""
		return self._oleobj_.InvokeTypes(1610809346, LCID, 1, (24, 0), ((11, 1), (3, 1), (8, 1)),showPrintDialog
			, printKind, theme)

	def Reveal(self):
		"""Reveal the user playlist in the main browser window."""
		return self._oleobj_.InvokeTypes(1610874892, LCID, 1, (24, 0), (),)

	# Result is of type IITTrackCollection
	def Search(self, searchText=defaultNamedNotOptArg, searchFields=defaultNamedNotOptArg):
		"""Search tracks in this playlist for the specified string."""
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 1, (9, 0), ((8, 1), (3, 1)),searchText
			, searchFields)
		if ret is not None:
			ret = Dispatch(ret, u'Search', '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Duration": (1610809350, 2, (3, 0), (), "Duration", None),
		"Index": (1610743811, 2, (3, 0), (), "Index", None),
		"Kind": (1610809348, 2, (3, 0), (), "Kind", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'IITUserPlaylist'
		"Parent": (1610874888, 2, (9, 0), (), "Parent", '{0A504DED-A0B5-465A-8A94-50E20D7DF692}'),
		"Shared": (1610874884, 2, (11, 0), (), "Shared", None),
		"Shuffle": (1610809351, 2, (11, 0), (), "Shuffle", None),
		"Size": (1610809353, 2, (5, 0), (), "Size", None),
		"Smart": (1610874886, 2, (11, 0), (), "Smart", None),
		"SongRepeat": (1610809354, 2, (3, 0), (), "SongRepeat", None),
		# Method 'Source' returns object of type 'IITSource'
		"Source": (1610809349, 2, (9, 0), (), "Source", '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}'),
		"SpecialKind": (1610874887, 2, (3, 0), (), "SpecialKind", None),
		"Time": (1610809356, 2, (8, 0), (), "Time", None),
		"TrackDatabaseID": (1610743815, 2, (3, 0), (), "TrackDatabaseID", None),
		# Method 'Tracks' returns object of type 'IITTrackCollection'
		"Tracks": (1610809358, 2, (9, 0), (), "Tracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
		"Visible": (1610809357, 2, (11, 0), (), "Visible", None),
		"playlistID": (1610743813, 2, (3, 0), (), "playlistID", None),
		"sourceID": (1610743812, 2, (3, 0), (), "sourceID", None),
		"trackID": (1610743814, 2, (3, 0), (), "trackID", None),
	}
	_prop_map_put_ = {
		"Name": ((1610743809, LCID, 4, 0),()),
		"Parent": ((1610874888, LCID, 4, 0),()),
		"Shared": ((1610874884, LCID, 4, 0),()),
		"Shuffle": ((1610809351, LCID, 4, 0),()),
		"SongRepeat": ((1610809354, LCID, 4, 0),()),
	}

class IITVisual(DispatchBaseClass):
	"""IITVisual Interface"""
	CLSID = IID('{340F3315-ED72-4C09-9ACF-21EB4BDF9931}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}

class IITVisualCollection(DispatchBaseClass):
	"""IITVisualCollection Interface"""
	CLSID = IID('{88A4CCDD-114F-4043-B69B-84D4E6274957}')
	coclass_clsid = None

	# Result is of type IITVisual
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Returns an IITVisual object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{340F3315-ED72-4C09-9ACF-21EB4BDF9931}', UnicodeToString=0)
		return ret

	# Result is of type IITVisual
	# The method ItemByName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByName(self, Name=defaultNamedNotOptArg):
		"""Returns an IITVisual object with the specified name."""
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByName', '{340F3315-ED72-4C09-9ACF-21EB4BDF9931}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Returns an IITVisual object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{340F3315-ED72-4C09-9ACF-21EB4BDF9931}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{340F3315-ED72-4C09-9ACF-21EB4BDF9931}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{340F3315-ED72-4C09-9ACF-21EB4BDF9931}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IITWindow(DispatchBaseClass):
	"""IITWindow Interface"""
	CLSID = IID('{370D7BE0-3A89-4A42-B902-C75FC138BE09}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Bottom": (1610743825, 2, (3, 0), (), "Bottom", None),
		"Height": (1610743831, 2, (3, 0), (), "Height", None),
		"Kind": (1610743809, 2, (3, 0), (), "Kind", None),
		"Left": (1610743823, 2, (3, 0), (), "Left", None),
		"Maximizable": (1610743815, 2, (11, 0), (), "Maximizable", None),
		"Maximized": (1610743816, 2, (11, 0), (), "Maximized", None),
		"Minimized": (1610743813, 2, (11, 0), (), "Minimized", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Resizable": (1610743812, 2, (11, 0), (), "Resizable", None),
		"Right": (1610743827, 2, (3, 0), (), "Right", None),
		"Top": (1610743821, 2, (3, 0), (), "Top", None),
		"Visible": (1610743810, 2, (11, 0), (), "Visible", None),
		"Width": (1610743829, 2, (3, 0), (), "Width", None),
		"Zoomable": (1610743818, 2, (11, 0), (), "Zoomable", None),
		"Zoomed": (1610743819, 2, (11, 0), (), "Zoomed", None),
	}
	_prop_map_put_ = {
		"Bottom": ((1610743825, LCID, 4, 0),()),
		"Height": ((1610743831, LCID, 4, 0),()),
		"Left": ((1610743823, LCID, 4, 0),()),
		"Maximized": ((1610743816, LCID, 4, 0),()),
		"Minimized": ((1610743813, LCID, 4, 0),()),
		"Right": ((1610743827, LCID, 4, 0),()),
		"Top": ((1610743821, LCID, 4, 0),()),
		"Visible": ((1610743810, LCID, 4, 0),()),
		"Width": ((1610743829, LCID, 4, 0),()),
		"Zoomed": ((1610743819, LCID, 4, 0),()),
	}

class IITWindowCollection(DispatchBaseClass):
	"""IITWindowCollection Interface"""
	CLSID = IID('{3D8DE381-6C0E-481F-A865-E2385F59FA43}')
	coclass_clsid = None

	# Result is of type IITWindow
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Returns an IITWindow object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{370D7BE0-3A89-4A42-B902-C75FC138BE09}', UnicodeToString=0)
		return ret

	# Result is of type IITWindow
	# The method ItemByName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByName(self, Name=defaultNamedNotOptArg):
		"""Returns an IITWindow object with the specified name."""
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByName', '{370D7BE0-3A89-4A42-B902-C75FC138BE09}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		"Count": (1610743808, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Returns an IITWindow object corresponding to the given index (1-based)."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{370D7BE0-3A89-4A42-B902-C75FC138BE09}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{370D7BE0-3A89-4A42-B902-C75FC138BE09}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{370D7BE0-3A89-4A42-B902-C75FC138BE09}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743808, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IiTunes(DispatchBaseClass):
	"""IiTunes Interface"""
	CLSID = IID('{9DD6680B-3EDC-40DB-A771-E6FE4832E34A}')
	coclass_clsid = IID('{DC0C2640-1415-4644-875C-6F4D769839BA}')

	def Authorize(self, numElems=defaultNamedNotOptArg, data=defaultNamedNotOptArg, names=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743829, LCID, 1, (24, 0), ((3, 1), (16396, 1), (16392, 1)),numElems
			, data, names)

	def BackTrack(self):
		"""Reposition to the beginning of the current track or go to the previous track if already at start of current track."""
		return self._oleobj_.InvokeTypes(1610743808, LCID, 1, (24, 0), (),)

	# The method CanSetShuffle is actually a property, but must be used as a method to correctly pass the arguments
	def CanSetShuffle(self, iPlaylist=defaultNamedNotOptArg):
		"""True if the Shuffle property is writable for the specified playlist."""
		return self._oleobj_.InvokeTypes(1610743880, LCID, 2, (11, 0), ((16396, 1),),iPlaylist
			)

	# The method CanSetSongRepeat is actually a property, but must be used as a method to correctly pass the arguments
	def CanSetSongRepeat(self, iPlaylist=defaultNamedNotOptArg):
		"""True if the SongRepeat property is writable for the specified playlist."""
		return self._oleobj_.InvokeTypes(1610743881, LCID, 2, (11, 0), ((16396, 1),),iPlaylist
			)

	def CheckVersion(self, majorVersion=defaultNamedNotOptArg, minorVersion=defaultNamedNotOptArg):
		"""Returns true if this version of the iTunes type library is compatible with the specified version."""
		return self._oleobj_.InvokeTypes(1610743823, LCID, 1, (11, 0), ((3, 1), (3, 1)),majorVersion
			, minorVersion)

	# Result is of type IITOperationStatus
	def ConvertFile(self, filePath=defaultNamedNotOptArg):
		"""Start converting the specified file path."""
		ret = self._oleobj_.InvokeTypes(1610743819, LCID, 1, (9, 0), ((8, 1),),filePath
			)
		if ret is not None:
			ret = Dispatch(ret, u'ConvertFile', '{206479C9-FE32-4F9B-A18A-475AC939B479}', UnicodeToString=0)
		return ret

	# Result is of type IITConvertOperationStatus
	def ConvertFile2(self, filePath=defaultNamedNotOptArg):
		"""Start converting the specified file path."""
		ret = self._oleobj_.InvokeTypes(1610743868, LCID, 1, (9, 0), ((8, 1),),filePath
			)
		if ret is not None:
			ret = Dispatch(ret, u'ConvertFile2', '{7063AAF6-ABA0-493B-B4FC-920A9F105875}', UnicodeToString=0)
		return ret

	# Result is of type IITOperationStatus
	def ConvertFiles(self, filePaths=defaultNamedNotOptArg):
		"""Start converting the specified array of file paths. filePaths can be of type VT_ARRAY|VT_VARIANT, where each entry is a VT_BSTR, or VT_ARRAY|VT_BSTR.  You can also pass a JScript Array object."""
		ret = self._oleobj_.InvokeTypes(1610743820, LCID, 1, (9, 0), ((16396, 1),),filePaths
			)
		if ret is not None:
			ret = Dispatch(ret, u'ConvertFiles', '{206479C9-FE32-4F9B-A18A-475AC939B479}', UnicodeToString=0)
		return ret

	# Result is of type IITConvertOperationStatus
	def ConvertFiles2(self, filePaths=defaultNamedNotOptArg):
		"""Start converting the specified array of file paths. filePaths can be of type VT_ARRAY|VT_VARIANT, where each entry is a VT_BSTR, or VT_ARRAY|VT_BSTR.  You can also pass a JScript Array object."""
		ret = self._oleobj_.InvokeTypes(1610743869, LCID, 1, (9, 0), ((16396, 1),),filePaths
			)
		if ret is not None:
			ret = Dispatch(ret, u'ConvertFiles2', '{7063AAF6-ABA0-493B-B4FC-920A9F105875}', UnicodeToString=0)
		return ret

	# Result is of type IITOperationStatus
	def ConvertTrack(self, iTrackToConvert=defaultNamedNotOptArg):
		"""Start converting the specified track.  iTrackToConvert is a VARIANT of type VT_DISPATCH that points to an IITTrack."""
		ret = self._oleobj_.InvokeTypes(1610743821, LCID, 1, (9, 0), ((16396, 1),),iTrackToConvert
			)
		if ret is not None:
			ret = Dispatch(ret, u'ConvertTrack', '{206479C9-FE32-4F9B-A18A-475AC939B479}', UnicodeToString=0)
		return ret

	# Result is of type IITConvertOperationStatus
	def ConvertTrack2(self, iTrackToConvert=defaultNamedNotOptArg):
		"""Start converting the specified track.  iTrackToConvert is a VARIANT of type VT_DISPATCH that points to an IITTrack."""
		ret = self._oleobj_.InvokeTypes(1610743870, LCID, 1, (9, 0), ((16396, 1),),iTrackToConvert
			)
		if ret is not None:
			ret = Dispatch(ret, u'ConvertTrack2', '{7063AAF6-ABA0-493B-B4FC-920A9F105875}', UnicodeToString=0)
		return ret

	# Result is of type IITOperationStatus
	def ConvertTracks(self, iTracksToConvert=defaultNamedNotOptArg):
		"""Start converting the specified tracks.  iTracksToConvert is a VARIANT of type VT_DISPATCH that points to an IITTrackCollection."""
		ret = self._oleobj_.InvokeTypes(1610743822, LCID, 1, (9, 0), ((16396, 1),),iTracksToConvert
			)
		if ret is not None:
			ret = Dispatch(ret, u'ConvertTracks', '{206479C9-FE32-4F9B-A18A-475AC939B479}', UnicodeToString=0)
		return ret

	# Result is of type IITConvertOperationStatus
	def ConvertTracks2(self, iTracksToConvert=defaultNamedNotOptArg):
		"""Start converting the specified tracks.  iTracksToConvert is a VARIANT of type VT_DISPATCH that points to an IITTrackCollection."""
		ret = self._oleobj_.InvokeTypes(1610743871, LCID, 1, (9, 0), ((16396, 1),),iTracksToConvert
			)
		if ret is not None:
			ret = Dispatch(ret, u'ConvertTracks2', '{7063AAF6-ABA0-493B-B4FC-920A9F105875}', UnicodeToString=0)
		return ret

	# Result is of type IITEQPreset
	def CreateEQPreset(self, eqPresetName=defaultNamedNotOptArg):
		"""Create a new EQ preset."""
		ret = self._oleobj_.InvokeTypes(1610743876, LCID, 1, (9, 0), ((8, 1),),eqPresetName
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreateEQPreset', '{5BE75F4F-68FA-4212-ACB7-BE44EA569759}', UnicodeToString=0)
		return ret

	# Result is of type IITPlaylist
	def CreateFolder(self, folderName=defaultNamedNotOptArg):
		"""Creates a new folder in the main library."""
		ret = self._oleobj_.InvokeTypes(1610743885, LCID, 1, (9, 0), ((8, 1),),folderName
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreateFolder', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	# Result is of type IITPlaylist
	def CreateFolderInSource(self, folderName=defaultNamedNotOptArg, iSource=defaultNamedNotOptArg):
		"""Creates a new folder in an existing source."""
		ret = self._oleobj_.InvokeTypes(1610743886, LCID, 1, (9, 0), ((8, 1), (16396, 1)),folderName
			, iSource)
		if ret is not None:
			ret = Dispatch(ret, u'CreateFolderInSource', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	# Result is of type IITPlaylist
	def CreatePlaylist(self, playlistName=defaultNamedNotOptArg):
		"""Creates a new playlist in the main library."""
		ret = self._oleobj_.InvokeTypes(1610743825, LCID, 1, (9, 0), ((8, 1),),playlistName
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreatePlaylist', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	# Result is of type IITPlaylist
	def CreatePlaylistInSource(self, playlistName=defaultNamedNotOptArg, iSource=defaultNamedNotOptArg):
		"""Creates a new playlist in an existing source."""
		ret = self._oleobj_.InvokeTypes(1610743877, LCID, 1, (9, 0), ((8, 1), (16396, 1)),playlistName
			, iSource)
		if ret is not None:
			ret = Dispatch(ret, u'CreatePlaylistInSource', '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}', UnicodeToString=0)
		return ret

	def FastForward(self):
		"""Skip forward in a playing track."""
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (24, 0), (),)

	# Result is of type IITObject
	def GetITObjectByID(self, sourceID=defaultNamedNotOptArg, playlistID=defaultNamedNotOptArg, trackID=defaultNamedNotOptArg, databaseID=defaultNamedNotOptArg):
		"""Returns an IITObject corresponding to the specified IDs."""
		ret = self._oleobj_.InvokeTypes(1610743824, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),sourceID
			, playlistID, trackID, databaseID)
		if ret is not None:
			ret = Dispatch(ret, u'GetITObjectByID', '{9FAB0E27-70D7-4E3A-9965-B0C8B8869BB6}', UnicodeToString=0)
		return ret

	def GetITObjectPersistentIDs(self, iObject=defaultNamedNotOptArg, highID=pythoncom.Missing, lowID=pythoncom.Missing):
		"""Returns the high and low 32 bits of the persistent ID of the specified IITObject."""
		return self._ApplyTypes_(1610743891, 1, (24, 0), ((16396, 1), (16387, 2), (16387, 2)), u'GetITObjectPersistentIDs', None,iObject
			, highID, lowID)

	def GetPlayerButtonsState(self, previousEnabled=pythoncom.Missing, playPauseStopState=pythoncom.Missing, nextEnabled=pythoncom.Missing):
		"""Retrieves the current state of the player buttons."""
		return self._ApplyTypes_(1610743878, 1, (24, 0), ((16395, 2), (16387, 2), (16395, 2)), u'GetPlayerButtonsState', None,previousEnabled
			, playPauseStopState, nextEnabled)

	def GotoMusicStoreHomePage(self):
		"""Go to the iTunes Store home page."""
		return self._oleobj_.InvokeTypes(1610743827, LCID, 1, (24, 0), (),)

	# The method ITObjectPersistentIDHigh is actually a property, but must be used as a method to correctly pass the arguments
	def ITObjectPersistentIDHigh(self, iObject=defaultNamedNotOptArg):
		"""Returns the high 32 bits of the persistent ID of the specified IITObject."""
		return self._oleobj_.InvokeTypes(1610743889, LCID, 2, (3, 0), ((16396, 1),),iObject
			)

	# The method ITObjectPersistentIDLow is actually a property, but must be used as a method to correctly pass the arguments
	def ITObjectPersistentIDLow(self, iObject=defaultNamedNotOptArg):
		"""Returns the low 32 bits of the persistent ID of the specified IITObject."""
		return self._oleobj_.InvokeTypes(1610743890, LCID, 2, (3, 0), ((16396, 1),),iObject
			)

	def NextTrack(self):
		"""Advance to the next track in the current playlist."""
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), (),)

	def OpenURL(self, URL=defaultNamedNotOptArg):
		"""Open the specified iTunes Store or streaming audio URL."""
		return self._oleobj_.InvokeTypes(1610743826, LCID, 1, (24, 0), ((8, 1),),URL
			)

	def Pause(self):
		"""Pause playback."""
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (24, 0), (),)

	def Play(self):
		"""Play the currently targeted track."""
		return self._oleobj_.InvokeTypes(1610743812, LCID, 1, (24, 0), (),)

	def PlayFile(self, filePath=defaultNamedNotOptArg):
		"""Play the specified file path, adding it to the library if not already present."""
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((8, 1),),filePath
			)

	def PlayPause(self):
		"""Toggle the playing/paused state of the current track."""
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (24, 0), (),)

	def PlayerButtonClicked(self, playerButton=defaultNamedNotOptArg, playerButtonModifierKeys=defaultNamedNotOptArg):
		"""Simulate click on a player control button."""
		return self._oleobj_.InvokeTypes(1610743879, LCID, 1, (24, 0), ((3, 1), (3, 1)),playerButton
			, playerButtonModifierKeys)

	def PreviousTrack(self):
		"""Return to the previous track in the current playlist."""
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (24, 0), (),)

	def Quit(self):
		"""Exits the iTunes application."""
		return self._oleobj_.InvokeTypes(1610743830, LCID, 1, (24, 0), (),)

	def Resume(self):
		"""Disable fast forward/rewind and resume playback, if playing."""
		return self._oleobj_.InvokeTypes(1610743816, LCID, 1, (24, 0), (),)

	def Rewind(self):
		"""Skip backwards in a playing track."""
		return self._oleobj_.InvokeTypes(1610743817, LCID, 1, (24, 0), (),)

	def SetOptions(self, options=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743867, LCID, 1, (24, 0), ((3, 1),),options
			)

	def Stop(self):
		"""Stop playback."""
		return self._oleobj_.InvokeTypes(1610743818, LCID, 1, (24, 0), (),)

	def SubscribeToPodcast(self, URL=defaultNamedNotOptArg):
		"""Subscribe to the specified podcast feed URL."""
		return self._oleobj_.InvokeTypes(1610743883, LCID, 1, (24, 0), ((8, 1),),URL
			)

	def UpdateIPod(self):
		"""Update the contents of the iPod."""
		return self._oleobj_.InvokeTypes(1610743828, LCID, 1, (24, 0), (),)

	def UpdatePodcastFeeds(self):
		"""Update all podcast feeds."""
		return self._oleobj_.InvokeTypes(1610743884, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AppCommandMessageProcessingEnabled": (1610743872, 2, (11, 0), (), "AppCommandMessageProcessingEnabled", None),
		# Method 'BrowserWindow' returns object of type 'IITBrowserWindow'
		"BrowserWindow": (1610743859, 2, (9, 0), (), "BrowserWindow", '{C999F455-C4D5-4AA4-8277-F99753699974}'),
		# Method 'ConvertOperationStatus' returns object of type 'IITConvertOperationStatus'
		"ConvertOperationStatus": (1610743882, 2, (9, 0), (), "ConvertOperationStatus", '{7063AAF6-ABA0-493B-B4FC-920A9F105875}'),
		# Method 'CurrentEQPreset' returns object of type 'IITEQPreset'
		"CurrentEQPreset": (1610743855, 2, (9, 0), (), "CurrentEQPreset", '{5BE75F4F-68FA-4212-ACB7-BE44EA569759}'),
		# Method 'CurrentEncoder' returns object of type 'IITEncoder'
		"CurrentEncoder": (1610743843, 2, (9, 0), (), "CurrentEncoder", '{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}'),
		# Method 'CurrentPlaylist' returns object of type 'IITPlaylist'
		"CurrentPlaylist": (1610743864, 2, (9, 0), (), "CurrentPlaylist", '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}'),
		"CurrentStreamTitle": (1610743857, 2, (8, 0), (), "CurrentStreamTitle", None),
		"CurrentStreamURL": (1610743858, 2, (8, 0), (), "CurrentStreamURL", None),
		# Method 'CurrentTrack' returns object of type 'IITTrack'
		"CurrentTrack": (1610743863, 2, (9, 0), (), "CurrentTrack", '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}'),
		# Method 'CurrentVisual' returns object of type 'IITVisual'
		"CurrentVisual": (1610743851, 2, (9, 0), (), "CurrentVisual", '{340F3315-ED72-4C09-9ACF-21EB4BDF9931}'),
		"EQEnabled": (1610743853, 2, (11, 0), (), "EQEnabled", None),
		# Method 'EQPresets' returns object of type 'IITEQPresetCollection'
		"EQPresets": (1610743833, 2, (9, 0), (), "EQPresets", '{AEF4D111-3331-48DA-B0C2-B468D5D61D08}'),
		# Method 'EQWindow' returns object of type 'IITWindow'
		"EQWindow": (1610743860, 2, (9, 0), (), "EQWindow", '{370D7BE0-3A89-4A42-B902-C75FC138BE09}'),
		# Method 'Encoders' returns object of type 'IITEncoderCollection'
		"Encoders": (1610743832, 2, (9, 0), (), "Encoders", '{8862BCA9-168D-4549-A9D5-ADB35E553BA6}'),
		"ForceToForegroundOnDialog": (1610743874, 2, (11, 0), (), "ForceToForegroundOnDialog", None),
		"FullScreenVisuals": (1610743847, 2, (11, 0), (), "FullScreenVisuals", None),
		# Method 'LibraryPlaylist' returns object of type 'IITLibraryPlaylist'
		"LibraryPlaylist": (1610743862, 2, (9, 0), (), "LibraryPlaylist", '{53AE1704-491C-4289-94A0-958815675A3D}'),
		# Method 'LibrarySource' returns object of type 'IITSource'
		"LibrarySource": (1610743861, 2, (9, 0), (), "LibrarySource", '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}'),
		"LibraryXMLPath": (1610743888, 2, (8, 0), (), "LibraryXMLPath", None),
		"Mute": (1610743838, 2, (11, 0), (), "Mute", None),
		"PlayerPosition": (1610743841, 2, (3, 0), (), "PlayerPosition", None),
		"PlayerState": (1610743840, 2, (3, 0), (), "PlayerState", None),
		# Method 'SelectedTracks' returns object of type 'IITTrackCollection'
		"SelectedTracks": (1610743865, 2, (9, 0), (), "SelectedTracks", '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}'),
		"SoundVolume": (1610743836, 2, (3, 0), (), "SoundVolume", None),
		"SoundVolumeControlEnabled": (1610743887, 2, (11, 0), (), "SoundVolumeControlEnabled", None),
		# Method 'Sources' returns object of type 'IITSourceCollection'
		"Sources": (1610743831, 2, (9, 0), (), "Sources", '{2FF6CE20-FF87-4183-B0B3-F323D047AF41}'),
		"Version": (1610743866, 2, (8, 0), (), "Version", None),
		"VisualSize": (1610743849, 2, (3, 0), (), "VisualSize", None),
		# Method 'Visuals' returns object of type 'IITVisualCollection'
		"Visuals": (1610743834, 2, (9, 0), (), "Visuals", '{88A4CCDD-114F-4043-B69B-84D4E6274957}'),
		"VisualsEnabled": (1610743845, 2, (11, 0), (), "VisualsEnabled", None),
		# Method 'Windows' returns object of type 'IITWindowCollection'
		"Windows": (1610743835, 2, (9, 0), (), "Windows", '{3D8DE381-6C0E-481F-A865-E2385F59FA43}'),
	}
	_prop_map_put_ = {
		"AppCommandMessageProcessingEnabled": ((1610743872, LCID, 4, 0),()),
		"CurrentEQPreset": ((1610743855, LCID, 4, 0),()),
		"CurrentEncoder": ((1610743843, LCID, 4, 0),()),
		"CurrentVisual": ((1610743851, LCID, 4, 0),()),
		"EQEnabled": ((1610743853, LCID, 4, 0),()),
		"ForceToForegroundOnDialog": ((1610743874, LCID, 4, 0),()),
		"FullScreenVisuals": ((1610743847, LCID, 4, 0),()),
		"Mute": ((1610743838, LCID, 4, 0),()),
		"PlayerPosition": ((1610743841, LCID, 4, 0),()),
		"SoundVolume": ((1610743836, LCID, 4, 0),()),
		"VisualSize": ((1610743849, LCID, 4, 0),()),
		"VisualsEnabled": ((1610743845, LCID, 4, 0),()),
	}

class _IITConvertOperationStatusEvents:
	"""_IITConvertOperationStatusEvents Interface"""
	CLSID = CLSID_Sink = IID('{5C47A705-8E8A-45A1-9EED-71C993F0BF60}')
	coclass_clsid = IID('{D06596AD-C900-41B2-BC68-1B486450FC56}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnConvertOperationStatusChangedEvent",
		        2 : "OnConvertOperationCompleteEvent",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnConvertOperationStatusChangedEvent(self, trackName=defaultNamedNotOptArg, progressValue=defaultNamedNotOptArg, maxProgressValue=defaultNamedNotOptArg):
#		"""Fired when status about the conversion operation has changed."""
#	def OnConvertOperationCompleteEvent(self):
#		"""Fired when the conversion operation has completed."""


class _IiTunesEvents:
	"""_IiTunesEvents Interface"""
	CLSID = CLSID_Sink = IID('{5846EB78-317E-4B6F-B0C3-11EE8C8FEEF2}')
	coclass_clsid = IID('{DC0C2640-1415-4644-875C-6F4D769839BA}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        8 : "OnQuittingEvent",
		        7 : "OnCOMCallsEnabledEvent",
		        5 : "OnUserInterfaceEnabledEvent",
		        1 : "OnDatabaseChangedEvent",
		        4 : "OnPlayerPlayingTrackChangedEvent",
		        6 : "OnCOMCallsDisabledEvent",
		       10 : "OnSoundVolumeChangedEvent",
		        3 : "OnPlayerStopEvent",
		        9 : "OnAboutToPromptUserToQuitEvent",
		        2 : "OnPlayerPlayEvent",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnQuittingEvent(self):
#		"""Fired when iTunes is about to quit."""
#	def OnCOMCallsEnabledEvent(self):
#		"""Fired when calls to the iTunes COM interface will no longer be deferred."""
#	def OnUserInterfaceEnabledEvent(self):
#		"""Fired when the iTunes user interface is no longer disabled."""
#	def OnDatabaseChangedEvent(self, deletedObjectIDs=defaultNamedNotOptArg, changedObjectIDs=defaultNamedNotOptArg):
#		"""Fired when a database change occurs."""
#	def OnPlayerPlayingTrackChangedEvent(self, iTrack=defaultNamedNotOptArg):
#		"""Fired when information about the currently playing track has changed."""
#	def OnCOMCallsDisabledEvent(self, reason=defaultNamedNotOptArg):
#		"""Fired when calls to the iTunes COM interface will be deferred."""
#	def OnSoundVolumeChangedEvent(self, newVolume=defaultNamedNotOptArg):
#		"""Fired when the sound output volume has changed."""
#	def OnPlayerStopEvent(self, iTrack=defaultNamedNotOptArg):
#		"""Fired when a track has stopped playing."""
#	def OnAboutToPromptUserToQuitEvent(self):
#		"""Fired when iTunes is about to prompt the user to quit."""
#	def OnPlayerPlayEvent(self, iTrack=defaultNamedNotOptArg):
#		"""Fired when a track has started playing."""


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'iTunes.Application.1'
class iTunesApp(CoClassBaseClass): # A CoClass
	# iTunesApp Class
	CLSID = IID('{DC0C2640-1415-4644-875C-6F4D769839BA}')
	coclass_sources = [
		_IiTunesEvents,
	]
	default_source = _IiTunesEvents
	coclass_interfaces = [
		IiTunes,
	]
	default_interface = IiTunes

class iTunesConvertOperationStatus(CoClassBaseClass): # A CoClass
	# iTunesConvertOperationStatus Class
	CLSID = IID('{D06596AD-C900-41B2-BC68-1B486450FC56}')
	coclass_sources = [
		_IITConvertOperationStatusEvents,
	]
	default_source = _IITConvertOperationStatusEvents
	coclass_interfaces = [
		IITConvertOperationStatus,
	]
	default_interface = IITConvertOperationStatus

IITArtwork_vtables_dispatch_ = 1
IITArtwork_vtables_ = [
	(( u'Delete' , ), 1610743808, (1610743808, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'SetArtworkFromFile' , u'filePath' , ), 1610743809, (1610743809, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SaveArtworkToFile' , u'filePath' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Format' , u'Format' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'IsDownloadedArtwork' , u'IsDownloadedArtwork' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Description' , u'Description' , ), 1610743813, (1610743813, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Description' , u'Description' , ), 1610743813, (1610743813, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

IITArtworkCollection_vtables_dispatch_ = 1
IITArtworkCollection_vtables_ = [
	(( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'iArtwork' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'iEnumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 1 , )),
]

IITAudioCDPlaylist_vtables_dispatch_ = 1
IITAudioCDPlaylist_vtables_ = [
	(( u'Artist' , u'Artist' , ), 1610874880, (1610874880, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Compilation' , u'isCompiliation' , ), 1610874881, (1610874881, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'Composer' , u'Composer' , ), 1610874882, (1610874882, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'DiscCount' , u'DiscCount' , ), 1610874883, (1610874883, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'DiscNumber' , u'DiscNumber' , ), 1610874884, (1610874884, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'Genre' , u'Genre' , ), 1610874885, (1610874885, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'Year' , u'Year' , ), 1610874886, (1610874886, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'Reveal' , ), 1610874887, (1610874887, (), [ ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
]

IITBrowserWindow_vtables_dispatch_ = 1
IITBrowserWindow_vtables_ = [
	(( u'MiniPlayer' , u'isMiniPlayer' , ), 1610809344, (1610809344, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'MiniPlayer' , u'isMiniPlayer' , ), 1610809344, (1610809344, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'SelectedTracks' , u'iTrackCollection' , ), 1610809346, (1610809346, (), [ (16393, 10, None, "IID('{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SelectedPlaylist' , u'iPlaylist' , ), 1610809347, (1610809347, (), [ (16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'SelectedPlaylist' , u'iPlaylist' , ), 1610809347, (1610809347, (), [ (16396, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IITConvertOperationStatus_vtables_dispatch_ = 1
IITConvertOperationStatus_vtables_ = [
	(( u'GetConversionStatus' , u'trackName' , u'progressValue' , u'maxProgressValue' , ), 1610809344, (1610809344, (), [ 
			(16392, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'StopConversion' , ), 1610809345, (1610809345, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'trackName' , u'trackName' , ), 1610809346, (1610809346, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'progressValue' , u'progressValue' , ), 1610809347, (1610809347, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'maxProgressValue' , u'maxProgressValue' , ), 1610809348, (1610809348, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

IITEQPreset_vtables_dispatch_ = 1
IITEQPreset_vtables_ = [
	(( u'Name' , u'Name' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Modifiable' , u'isModifiable' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Preamp' , u'level' , ), 1610743810, (1610743810, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Preamp' , u'level' , ), 1610743810, (1610743810, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Band1' , u'level' , ), 1610743812, (1610743812, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Band1' , u'level' , ), 1610743812, (1610743812, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Band2' , u'level' , ), 1610743814, (1610743814, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Band2' , u'level' , ), 1610743814, (1610743814, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Band3' , u'level' , ), 1610743816, (1610743816, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'Band3' , u'level' , ), 1610743816, (1610743816, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Band4' , u'level' , ), 1610743818, (1610743818, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Band4' , u'level' , ), 1610743818, (1610743818, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Band5' , u'level' , ), 1610743820, (1610743820, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'Band5' , u'level' , ), 1610743820, (1610743820, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Band6' , u'level' , ), 1610743822, (1610743822, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'Band6' , u'level' , ), 1610743822, (1610743822, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Band7' , u'level' , ), 1610743824, (1610743824, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'Band7' , u'level' , ), 1610743824, (1610743824, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Band8' , u'level' , ), 1610743826, (1610743826, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'Band8' , u'level' , ), 1610743826, (1610743826, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Band9' , u'level' , ), 1610743828, (1610743828, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'Band9' , u'level' , ), 1610743828, (1610743828, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Band10' , u'level' , ), 1610743830, (1610743830, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'Band10' , u'level' , ), 1610743830, (1610743830, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Delete' , u'updateAllTracks' , ), 1610743832, (1610743832, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'Rename' , u'newName' , u'updateAllTracks' , ), 1610743833, (1610743833, (), [ (8, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IITEQPresetCollection_vtables_dispatch_ = 1
IITEQPresetCollection_vtables_ = [
	(( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'iEQPreset' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{5BE75F4F-68FA-4212-ACB7-BE44EA569759}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ItemByName' , u'Name' , u'iEQPreset' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{5BE75F4F-68FA-4212-ACB7-BE44EA569759}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'iEnumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 1 , )),
]

IITEncoder_vtables_dispatch_ = 1
IITEncoder_vtables_ = [
	(( u'Name' , u'Name' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Format' , u'Format' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

IITEncoderCollection_vtables_dispatch_ = 1
IITEncoderCollection_vtables_ = [
	(( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'iEncoder' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ItemByName' , u'Name' , u'iEncoder' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'iEnumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 1 , )),
]

IITFileOrCDTrack_vtables_dispatch_ = 1
IITFileOrCDTrack_vtables_ = [
	(( u'Location' , u'Location' , ), 1610874880, (1610874880, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( u'UpdateInfoFromFile' , ), 1610874881, (1610874881, (), [ ], 1 , 1 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
	(( u'Podcast' , u'isPodcast' , ), 1610874882, (1610874882, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( u'UpdatePodcastFeed' , ), 1610874883, (1610874883, (), [ ], 1 , 1 , 4 , 0 , 300 , (3, 0, None, None) , 0 , )),
	(( u'RememberBookmark' , u'RememberBookmark' , ), 1610874884, (1610874884, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( u'RememberBookmark' , u'RememberBookmark' , ), 1610874884, (1610874884, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 308 , (3, 0, None, None) , 0 , )),
	(( u'ExcludeFromShuffle' , u'ExcludeFromShuffle' , ), 1610874886, (1610874886, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( u'ExcludeFromShuffle' , u'ExcludeFromShuffle' , ), 1610874886, (1610874886, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 316 , (3, 0, None, None) , 0 , )),
	(( u'Lyrics' , u'Lyrics' , ), 1610874888, (1610874888, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( u'Lyrics' , u'Lyrics' , ), 1610874888, (1610874888, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 324 , (3, 0, None, None) , 0 , )),
	(( u'Category' , u'Category' , ), 1610874890, (1610874890, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( u'Category' , u'Category' , ), 1610874890, (1610874890, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 332 , (3, 0, None, None) , 0 , )),
	(( u'Description' , u'Description' , ), 1610874892, (1610874892, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( u'Description' , u'Description' , ), 1610874892, (1610874892, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 340 , (3, 0, None, None) , 0 , )),
	(( u'LongDescription' , u'LongDescription' , ), 1610874894, (1610874894, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( u'LongDescription' , u'LongDescription' , ), 1610874894, (1610874894, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 348 , (3, 0, None, None) , 0 , )),
	(( u'BookmarkTime' , u'BookmarkTime' , ), 1610874896, (1610874896, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( u'BookmarkTime' , u'BookmarkTime' , ), 1610874896, (1610874896, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 356 , (3, 0, None, None) , 0 , )),
	(( u'VideoKind' , u'VideoKind' , ), 1610874898, (1610874898, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( u'VideoKind' , u'VideoKind' , ), 1610874898, (1610874898, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 364 , (3, 0, None, None) , 0 , )),
	(( u'SkippedCount' , u'SkippedCount' , ), 1610874900, (1610874900, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( u'SkippedCount' , u'SkippedCount' , ), 1610874900, (1610874900, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 372 , (3, 0, None, None) , 0 , )),
	(( u'SkippedDate' , u'SkippedDate' , ), 1610874902, (1610874902, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( u'SkippedDate' , u'SkippedDate' , ), 1610874902, (1610874902, (), [ (7, 1, None, None) , ], 1 , 4 , 4 , 0 , 380 , (3, 0, None, None) , 0 , )),
	(( u'PartOfGaplessAlbum' , u'PartOfGaplessAlbum' , ), 1610874904, (1610874904, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( u'PartOfGaplessAlbum' , u'PartOfGaplessAlbum' , ), 1610874904, (1610874904, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 388 , (3, 0, None, None) , 0 , )),
	(( u'AlbumArtist' , u'AlbumArtist' , ), 1610874906, (1610874906, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( u'AlbumArtist' , u'AlbumArtist' , ), 1610874906, (1610874906, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 396 , (3, 0, None, None) , 0 , )),
	(( u'Show' , u'showName' , ), 1610874908, (1610874908, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( u'Show' , u'showName' , ), 1610874908, (1610874908, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 404 , (3, 0, None, None) , 0 , )),
	(( u'SeasonNumber' , u'SeasonNumber' , ), 1610874910, (1610874910, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( u'SeasonNumber' , u'SeasonNumber' , ), 1610874910, (1610874910, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 412 , (3, 0, None, None) , 0 , )),
	(( u'EpisodeID' , u'EpisodeID' , ), 1610874912, (1610874912, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( u'EpisodeID' , u'EpisodeID' , ), 1610874912, (1610874912, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 420 , (3, 0, None, None) , 0 , )),
	(( u'EpisodeNumber' , u'EpisodeNumber' , ), 1610874914, (1610874914, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( u'EpisodeNumber' , u'EpisodeNumber' , ), 1610874914, (1610874914, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 428 , (3, 0, None, None) , 0 , )),
	(( u'Size64High' , u'sizeHigh' , ), 1610874916, (1610874916, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( u'Size64Low' , u'sizeLow' , ), 1610874917, (1610874917, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 436 , (3, 0, None, None) , 0 , )),
	(( u'Unplayed' , u'isUnplayed' , ), 1610874918, (1610874918, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( u'Unplayed' , u'isUnplayed' , ), 1610874918, (1610874918, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 444 , (3, 0, None, None) , 0 , )),
	(( u'SortAlbum' , u'Album' , ), 1610874920, (1610874920, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( u'SortAlbum' , u'Album' , ), 1610874920, (1610874920, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 452 , (3, 0, None, None) , 0 , )),
	(( u'SortAlbumArtist' , u'AlbumArtist' , ), 1610874922, (1610874922, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( u'SortAlbumArtist' , u'AlbumArtist' , ), 1610874922, (1610874922, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 460 , (3, 0, None, None) , 0 , )),
	(( u'SortArtist' , u'Artist' , ), 1610874924, (1610874924, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( u'SortArtist' , u'Artist' , ), 1610874924, (1610874924, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 468 , (3, 0, None, None) , 0 , )),
	(( u'SortComposer' , u'Composer' , ), 1610874926, (1610874926, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( u'SortComposer' , u'Composer' , ), 1610874926, (1610874926, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 476 , (3, 0, None, None) , 0 , )),
	(( u'SortName' , u'Name' , ), 1610874928, (1610874928, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( u'SortName' , u'Name' , ), 1610874928, (1610874928, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 484 , (3, 0, None, None) , 0 , )),
	(( u'SortShow' , u'showName' , ), 1610874930, (1610874930, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( u'SortShow' , u'showName' , ), 1610874930, (1610874930, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 492 , (3, 0, None, None) , 0 , )),
	(( u'Reveal' , ), 1610874932, (1610874932, (), [ ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( u'AlbumRating' , u'Rating' , ), 1610874933, (1610874933, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 500 , (3, 0, None, None) , 0 , )),
	(( u'AlbumRating' , u'Rating' , ), 1610874933, (1610874933, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( u'AlbumRatingKind' , u'ratingKind' , ), 1610874935, (1610874935, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 508 , (3, 0, None, None) , 0 , )),
	(( u'ratingKind' , u'ratingKind' , ), 1610874936, (1610874936, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( u'Playlists' , u'iPlaylistCollection' , ), 1610874937, (1610874937, (), [ (16393, 10, None, "IID('{FF194254-909D-4437-9C50-3AAC2AE6305C}')") , ], 1 , 2 , 4 , 0 , 516 , (3, 0, None, None) , 0 , )),
	(( u'Location' , u'Location' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( u'ReleaseDate' , u'ReleaseDate' , ), 1610874939, (1610874939, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 524 , (3, 0, None, None) , 0 , )),
]

IITIPodSource_vtables_dispatch_ = 1
IITIPodSource_vtables_ = [
	(( u'UpdateIPod' , ), 1610874880, (1610874880, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'EjectIPod' , ), 1610874881, (1610874881, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SoftwareVersion' , u'SoftwareVersion' , ), 1610874882, (1610874882, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
]

IITLibraryPlaylist_vtables_dispatch_ = 1
IITLibraryPlaylist_vtables_ = [
	(( u'AddFile' , u'filePath' , u'iStatus' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'AddFiles' , u'filePaths' , u'iStatus' , ), 1610874881, (1610874881, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')") , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'AddURL' , u'URL' , u'iURLTrack' , ), 1610874882, (1610874882, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{1116E3B5-29FD-4393-A7BD-454E5E327900}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'AddTrack' , u'iTrackToAdd' , u'iAddedTrack' , ), 1610874883, (1610874883, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')") , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
]

IITObject_vtables_dispatch_ = 1
IITObject_vtables_ = [
	(( u'GetITObjectIDs' , u'sourceID' , u'playlistID' , u'trackID' , u'databaseID' , 
			), 1610743808, (1610743808, (), [ (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'Name' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'Name' , ), 1610743809, (1610743809, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Index' , u'Index' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'sourceID' , u'sourceID' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'playlistID' , u'playlistID' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'trackID' , u'trackID' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'TrackDatabaseID' , u'databaseID' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IITOperationStatus_vtables_dispatch_ = 1
IITOperationStatus_vtables_ = [
	(( u'InProgress' , u'isInProgress' , ), 1610743808, (1610743808, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Tracks' , u'iTrackCollection' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

IITPlaylist_vtables_dispatch_ = 1
IITPlaylist_vtables_ = [
	(( u'Delete' , ), 1610809344, (1610809344, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'PlayFirstTrack' , ), 1610809345, (1610809345, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Print' , u'showPrintDialog' , u'printKind' , u'theme' , ), 1610809346, (1610809346, (), [ 
			(11, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Search' , u'searchText' , u'searchFields' , u'iTrackCollection' , ), 1610809347, (1610809347, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Kind' , u'Kind' , ), 1610809348, (1610809348, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'Source' , u'iSource' , ), 1610809349, (1610809349, (), [ (16393, 10, None, "IID('{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Duration' , u'Duration' , ), 1610809350, (1610809350, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'Shuffle' , u'isShuffle' , ), 1610809351, (1610809351, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Shuffle' , u'isShuffle' , ), 1610809351, (1610809351, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'Size' , u'Size' , ), 1610809353, (1610809353, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'SongRepeat' , u'repeatMode' , ), 1610809354, (1610809354, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'SongRepeat' , u'repeatMode' , ), 1610809354, (1610809354, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Time' , u'Time' , ), 1610809356, (1610809356, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'Visible' , u'isVisible' , ), 1610809357, (1610809357, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Tracks' , u'iTrackCollection' , ), 1610809358, (1610809358, (), [ (16393, 10, None, "IID('{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}')") , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
]

IITPlaylistCollection_vtables_dispatch_ = 1
IITPlaylistCollection_vtables_ = [
	(( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'iPlaylist' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ItemByName' , u'Name' , u'iPlaylist' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'iEnumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 1 , )),
	(( u'ItemByPersistentID' , u'highID' , u'lowID' , u'iPlaylist' , ), 1610743812, (1610743812, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

IITPlaylistWindow_vtables_dispatch_ = 1
IITPlaylistWindow_vtables_ = [
	(( u'SelectedTracks' , u'iTrackCollection' , ), 1610809344, (1610809344, (), [ (16393, 10, None, "IID('{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Playlist' , u'iPlaylist' , ), 1610809345, (1610809345, (), [ (16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
]

IITSource_vtables_dispatch_ = 1
IITSource_vtables_ = [
	(( u'Kind' , u'Kind' , ), 1610809344, (1610809344, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'Capacity' , u'Capacity' , ), 1610809345, (1610809345, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'FreeSpace' , u'FreeSpace' , ), 1610809346, (1610809346, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Playlists' , u'iPlaylistCollection' , ), 1610809347, (1610809347, (), [ (16393, 10, None, "IID('{FF194254-909D-4437-9C50-3AAC2AE6305C}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IITSourceCollection_vtables_dispatch_ = 1
IITSourceCollection_vtables_ = [
	(( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'iSource' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ItemByName' , u'Name' , u'iSource' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'iEnumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 1 , )),
	(( u'ItemByPersistentID' , u'highID' , u'lowID' , u'iSource' , ), 1610743812, (1610743812, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

IITTrack_vtables_dispatch_ = 1
IITTrack_vtables_ = [
	(( u'Delete' , ), 1610809344, (1610809344, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'Play' , ), 1610809345, (1610809345, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AddArtworkFromFile' , u'filePath' , u'iArtwork' , ), 1610809346, (1610809346, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Kind' , u'Kind' , ), 1610809347, (1610809347, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Playlist' , u'iPlaylist' , ), 1610809348, (1610809348, (), [ (16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'Album' , u'Album' , ), 1610809349, (1610809349, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Album' , u'Album' , ), 1610809349, (1610809349, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'Artist' , u'Artist' , ), 1610809351, (1610809351, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Artist' , u'Artist' , ), 1610809351, (1610809351, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'BitRate' , u'BitRate' , ), 1610809353, (1610809353, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'BPM' , u'beatsPerMinute' , ), 1610809354, (1610809354, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'BPM' , u'beatsPerMinute' , ), 1610809354, (1610809354, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Comment' , u'Comment' , ), 1610809356, (1610809356, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'Comment' , u'Comment' , ), 1610809356, (1610809356, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Compilation' , u'isCompilation' , ), 1610809358, (1610809358, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'Compilation' , u'isCompilation' , ), 1610809358, (1610809358, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Composer' , u'Composer' , ), 1610809360, (1610809360, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'Composer' , u'Composer' , ), 1610809360, (1610809360, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'DateAdded' , u'DateAdded' , ), 1610809362, (1610809362, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'DiscCount' , u'DiscCount' , ), 1610809363, (1610809363, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'DiscCount' , u'DiscCount' , ), 1610809363, (1610809363, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'DiscNumber' , u'DiscNumber' , ), 1610809365, (1610809365, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'DiscNumber' , u'DiscNumber' , ), 1610809365, (1610809365, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'Duration' , u'Duration' , ), 1610809367, (1610809367, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'Enabled' , u'isEnabled' , ), 1610809368, (1610809368, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'Enabled' , u'isEnabled' , ), 1610809368, (1610809368, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'EQ' , u'EQ' , ), 1610809370, (1610809370, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'EQ' , u'EQ' , ), 1610809370, (1610809370, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'Finish' , u'Finish' , ), 1610809372, (1610809372, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'Finish' , u'Finish' , ), 1610809372, (1610809372, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'Genre' , u'Genre' , ), 1610809374, (1610809374, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'Genre' , u'Genre' , ), 1610809374, (1610809374, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'Grouping' , u'Grouping' , ), 1610809376, (1610809376, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'Grouping' , u'Grouping' , ), 1610809376, (1610809376, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'KindAsString' , u'Kind' , ), 1610809378, (1610809378, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'ModificationDate' , u'dateModified' , ), 1610809379, (1610809379, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'PlayedCount' , u'PlayedCount' , ), 1610809380, (1610809380, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'PlayedCount' , u'PlayedCount' , ), 1610809380, (1610809380, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'PlayedDate' , u'PlayedDate' , ), 1610809382, (1610809382, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( u'PlayedDate' , u'PlayedDate' , ), 1610809382, (1610809382, (), [ (7, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'PlayOrderIndex' , u'Index' , ), 1610809384, (1610809384, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( u'Rating' , u'Rating' , ), 1610809385, (1610809385, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'Rating' , u'Rating' , ), 1610809385, (1610809385, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( u'SampleRate' , u'SampleRate' , ), 1610809387, (1610809387, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'Size' , u'Size' , ), 1610809388, (1610809388, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( u'Start' , u'Start' , ), 1610809389, (1610809389, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'Start' , u'Start' , ), 1610809389, (1610809389, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( u'Time' , u'Time' , ), 1610809391, (1610809391, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'TrackCount' , u'TrackCount' , ), 1610809392, (1610809392, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( u'TrackCount' , u'TrackCount' , ), 1610809392, (1610809392, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( u'TrackNumber' , u'TrackNumber' , ), 1610809394, (1610809394, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( u'TrackNumber' , u'TrackNumber' , ), 1610809394, (1610809394, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( u'VolumeAdjustment' , u'VolumeAdjustment' , ), 1610809396, (1610809396, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( u'VolumeAdjustment' , u'VolumeAdjustment' , ), 1610809396, (1610809396, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( u'Year' , u'Year' , ), 1610809398, (1610809398, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( u'Year' , u'Year' , ), 1610809398, (1610809398, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( u'Artwork' , u'iArtworkCollection' , ), 1610809400, (1610809400, (), [ (16393, 10, None, "IID('{BF2742D7-418C-4858-9AF9-2981B062D23E}')") , ], 1 , 2 , 4 , 0 , 284 , (3, 0, None, None) , 0 , )),
]

IITTrackCollection_vtables_dispatch_ = 1
IITTrackCollection_vtables_ = [
	(( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'iTrack' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ItemByPlayOrder' , u'Index' , u'iTrack' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'ItemByName' , u'Name' , u'iTrack' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'iEnumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 1 , )),
	(( u'ItemByPersistentID' , u'highID' , u'lowID' , u'iTrack' , ), 1610743813, (1610743813, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')") , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

IITURLTrack_vtables_dispatch_ = 1
IITURLTrack_vtables_ = [
	(( u'URL' , u'URL' , ), 1610874880, (1610874880, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( u'URL' , u'URL' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
	(( u'Podcast' , u'isPodcast' , ), 1610874882, (1610874882, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( u'UpdatePodcastFeed' , ), 1610874883, (1610874883, (), [ ], 1 , 1 , 4 , 0 , 300 , (3, 0, None, None) , 0 , )),
	(( u'DownloadPodcastEpisode' , ), 1610874884, (1610874884, (), [ ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( u'Category' , u'Category' , ), 1610874885, (1610874885, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 308 , (3, 0, None, None) , 0 , )),
	(( u'Category' , u'Category' , ), 1610874885, (1610874885, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( u'Description' , u'Description' , ), 1610874887, (1610874887, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 316 , (3, 0, None, None) , 0 , )),
	(( u'Description' , u'Description' , ), 1610874887, (1610874887, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( u'LongDescription' , u'LongDescription' , ), 1610874889, (1610874889, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 324 , (3, 0, None, None) , 0 , )),
	(( u'LongDescription' , u'LongDescription' , ), 1610874889, (1610874889, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( u'Reveal' , ), 1610874891, (1610874891, (), [ ], 1 , 1 , 4 , 0 , 332 , (3, 0, None, None) , 0 , )),
	(( u'AlbumRating' , u'Rating' , ), 1610874892, (1610874892, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( u'AlbumRating' , u'Rating' , ), 1610874892, (1610874892, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 340 , (3, 0, None, None) , 0 , )),
	(( u'AlbumRatingKind' , u'ratingKind' , ), 1610874894, (1610874894, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( u'ratingKind' , u'ratingKind' , ), 1610874895, (1610874895, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 348 , (3, 0, None, None) , 0 , )),
	(( u'Playlists' , u'iPlaylistCollection' , ), 1610874896, (1610874896, (), [ (16393, 10, None, "IID('{FF194254-909D-4437-9C50-3AAC2AE6305C}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
]

IITUserPlaylist_vtables_dispatch_ = 1
IITUserPlaylist_vtables_ = [
	(( u'AddFile' , u'filePath' , u'iStatus' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'AddFiles' , u'filePaths' , u'iStatus' , ), 1610874881, (1610874881, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')") , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'AddURL' , u'URL' , u'iURLTrack' , ), 1610874882, (1610874882, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{1116E3B5-29FD-4393-A7BD-454E5E327900}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'AddTrack' , u'iTrackToAdd' , u'iAddedTrack' , ), 1610874883, (1610874883, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')") , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'Shared' , u'isShared' , ), 1610874884, (1610874884, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'Shared' , u'isShared' , ), 1610874884, (1610874884, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'Smart' , u'isSmart' , ), 1610874886, (1610874886, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'SpecialKind' , u'SpecialKind' , ), 1610874887, (1610874887, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'Parent' , u'iParentPlayList' , ), 1610874888, (1610874888, (), [ (16393, 10, None, "IID('{0A504DED-A0B5-465A-8A94-50E20D7DF692}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'CreatePlaylist' , u'playlistName' , u'iPlaylist' , ), 1610874889, (1610874889, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'CreateFolder' , u'folderName' , u'iFolder' , ), 1610874890, (1610874890, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'Parent' , u'iParentPlayList' , ), 1610874888, (1610874888, (), [ (16396, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'Reveal' , ), 1610874892, (1610874892, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IITVisual_vtables_dispatch_ = 1
IITVisual_vtables_ = [
	(( u'Name' , u'Name' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
]

IITVisualCollection_vtables_dispatch_ = 1
IITVisualCollection_vtables_ = [
	(( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'iVisual' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{340F3315-ED72-4C09-9ACF-21EB4BDF9931}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ItemByName' , u'Name' , u'iVisual' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{340F3315-ED72-4C09-9ACF-21EB4BDF9931}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'iEnumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 1 , )),
]

IITWindow_vtables_dispatch_ = 1
IITWindow_vtables_ = [
	(( u'Name' , u'Name' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Kind' , u'Kind' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Visible' , u'isVisible' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Visible' , u'isVisible' , ), 1610743810, (1610743810, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Resizable' , u'isResizable' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Minimized' , u'isMinimized' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Minimized' , u'isMinimized' , ), 1610743813, (1610743813, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Maximizable' , u'isMaximizable' , ), 1610743815, (1610743815, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Maximized' , u'isMaximized' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'Maximized' , u'isMaximized' , ), 1610743816, (1610743816, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Zoomable' , u'isZoomable' , ), 1610743818, (1610743818, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Zoomed' , u'isZoomed' , ), 1610743819, (1610743819, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Zoomed' , u'isZoomed' , ), 1610743819, (1610743819, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'Top' , u'Top' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Top' , u'Top' , ), 1610743821, (1610743821, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'Left' , u'Left' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Left' , u'Left' , ), 1610743823, (1610743823, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'Bottom' , u'Bottom' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Bottom' , u'Bottom' , ), 1610743825, (1610743825, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'Right' , u'Right' , ), 1610743827, (1610743827, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Right' , u'Right' , ), 1610743827, (1610743827, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'Width' , u'Width' , ), 1610743829, (1610743829, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Width' , u'Width' , ), 1610743829, (1610743829, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'Height' , u'Height' , ), 1610743831, (1610743831, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Height' , u'Height' , ), 1610743831, (1610743831, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
]

IITWindowCollection_vtables_dispatch_ = 1
IITWindowCollection_vtables_ = [
	(( u'Count' , u'Count' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'iWindow' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{370D7BE0-3A89-4A42-B902-C75FC138BE09}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ItemByName' , u'Name' , u'iWindow' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{370D7BE0-3A89-4A42-B902-C75FC138BE09}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'iEnumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 1 , )),
]

IiTunes_vtables_dispatch_ = 1
IiTunes_vtables_ = [
	(( u'BackTrack' , ), 1610743808, (1610743808, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'FastForward' , ), 1610743809, (1610743809, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'NextTrack' , ), 1610743810, (1610743810, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Pause' , ), 1610743811, (1610743811, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Play' , ), 1610743812, (1610743812, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'PlayFile' , u'filePath' , ), 1610743813, (1610743813, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'PlayPause' , ), 1610743814, (1610743814, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'PreviousTrack' , ), 1610743815, (1610743815, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Resume' , ), 1610743816, (1610743816, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'Rewind' , ), 1610743817, (1610743817, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Stop' , ), 1610743818, (1610743818, (), [ ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'ConvertFile' , u'filePath' , u'iStatus' , ), 1610743819, (1610743819, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'ConvertFiles' , u'filePaths' , u'iStatus' , ), 1610743820, (1610743820, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'ConvertTrack' , u'iTrackToConvert' , u'iStatus' , ), 1610743821, (1610743821, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'ConvertTracks' , u'iTracksToConvert' , u'iStatus' , ), 1610743822, (1610743822, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{206479C9-FE32-4F9B-A18A-475AC939B479}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'CheckVersion' , u'majorVersion' , u'minorVersion' , u'isCompatible' , ), 1610743823, (1610743823, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'GetITObjectByID' , u'sourceID' , u'playlistID' , u'trackID' , u'databaseID' , 
			u'iObject' , ), 1610743824, (1610743824, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (16393, 10, None, "IID('{9FAB0E27-70D7-4E3A-9965-B0C8B8869BB6}')") , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'CreatePlaylist' , u'playlistName' , u'iPlaylist' , ), 1610743825, (1610743825, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'OpenURL' , u'URL' , ), 1610743826, (1610743826, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'GotoMusicStoreHomePage' , ), 1610743827, (1610743827, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'UpdateIPod' , ), 1610743828, (1610743828, (), [ ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'Authorize' , u'numElems' , u'data' , u'names' , ), 1610743829, (1610743829, (), [ 
			(3, 1, None, None) , (16396, 1, None, None) , (16392, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Quit' , ), 1610743830, (1610743830, (), [ ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'Sources' , u'iSourceCollection' , ), 1610743831, (1610743831, (), [ (16393, 10, None, "IID('{2FF6CE20-FF87-4183-B0B3-F323D047AF41}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Encoders' , u'iEncoderCollection' , ), 1610743832, (1610743832, (), [ (16393, 10, None, "IID('{8862BCA9-168D-4549-A9D5-ADB35E553BA6}')") , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'EQPresets' , u'iEQPresetCollection' , ), 1610743833, (1610743833, (), [ (16393, 10, None, "IID('{AEF4D111-3331-48DA-B0C2-B468D5D61D08}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Visuals' , u'iVisualCollection' , ), 1610743834, (1610743834, (), [ (16393, 10, None, "IID('{88A4CCDD-114F-4043-B69B-84D4E6274957}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'Windows' , u'iWindowCollection' , ), 1610743835, (1610743835, (), [ (16393, 10, None, "IID('{3D8DE381-6C0E-481F-A865-E2385F59FA43}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SoundVolume' , u'volume' , ), 1610743836, (1610743836, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'SoundVolume' , u'volume' , ), 1610743836, (1610743836, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'Mute' , u'isMuted' , ), 1610743838, (1610743838, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'Mute' , u'isMuted' , ), 1610743838, (1610743838, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'PlayerState' , u'PlayerState' , ), 1610743840, (1610743840, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'PlayerPosition' , u'playerPos' , ), 1610743841, (1610743841, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'PlayerPosition' , u'playerPos' , ), 1610743841, (1610743841, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'CurrentEncoder' , u'iEncoder' , ), 1610743843, (1610743843, (), [ (16393, 10, None, "IID('{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'CurrentEncoder' , u'iEncoder' , ), 1610743843, (1610743843, (), [ (9, 1, None, "IID('{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}')") , ], 1 , 4 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'VisualsEnabled' , u'isEnabled' , ), 1610743845, (1610743845, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'VisualsEnabled' , u'isEnabled' , ), 1610743845, (1610743845, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'FullScreenVisuals' , u'isFullScreen' , ), 1610743847, (1610743847, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'FullScreenVisuals' , u'isFullScreen' , ), 1610743847, (1610743847, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'VisualSize' , u'VisualSize' , ), 1610743849, (1610743849, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'VisualSize' , u'VisualSize' , ), 1610743849, (1610743849, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'CurrentVisual' , u'iVisual' , ), 1610743851, (1610743851, (), [ (16393, 10, None, "IID('{340F3315-ED72-4C09-9ACF-21EB4BDF9931}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'CurrentVisual' , u'iVisual' , ), 1610743851, (1610743851, (), [ (9, 1, None, "IID('{340F3315-ED72-4C09-9ACF-21EB4BDF9931}')") , ], 1 , 4 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'EQEnabled' , u'isEnabled' , ), 1610743853, (1610743853, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'EQEnabled' , u'isEnabled' , ), 1610743853, (1610743853, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( u'CurrentEQPreset' , u'iEQPreset' , ), 1610743855, (1610743855, (), [ (16393, 10, None, "IID('{5BE75F4F-68FA-4212-ACB7-BE44EA569759}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'CurrentEQPreset' , u'iEQPreset' , ), 1610743855, (1610743855, (), [ (9, 1, None, "IID('{5BE75F4F-68FA-4212-ACB7-BE44EA569759}')") , ], 1 , 4 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( u'CurrentStreamTitle' , u'streamTitle' , ), 1610743857, (1610743857, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'CurrentStreamURL' , u'streamURL' , ), 1610743858, (1610743858, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( u'BrowserWindow' , u'iBrowserWindow' , ), 1610743859, (1610743859, (), [ (16393, 10, None, "IID('{C999F455-C4D5-4AA4-8277-F99753699974}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'EQWindow' , u'iEQWindow' , ), 1610743860, (1610743860, (), [ (16393, 10, None, "IID('{370D7BE0-3A89-4A42-B902-C75FC138BE09}')") , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( u'LibrarySource' , u'iLibrarySource' , ), 1610743861, (1610743861, (), [ (16393, 10, None, "IID('{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'LibraryPlaylist' , u'iLibraryPlaylist' , ), 1610743862, (1610743862, (), [ (16393, 10, None, "IID('{53AE1704-491C-4289-94A0-958815675A3D}')") , ], 1 , 2 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( u'CurrentTrack' , u'iTrack' , ), 1610743863, (1610743863, (), [ (16393, 10, None, "IID('{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'CurrentPlaylist' , u'iPlaylist' , ), 1610743864, (1610743864, (), [ (16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 2 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( u'SelectedTracks' , u'iTrackCollection' , ), 1610743865, (1610743865, (), [ (16393, 10, None, "IID('{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( u'Version' , u'Version' , ), 1610743866, (1610743866, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( u'SetOptions' , u'options' , ), 1610743867, (1610743867, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( u'ConvertFile2' , u'filePath' , u'iStatus' , ), 1610743868, (1610743868, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{7063AAF6-ABA0-493B-B4FC-920A9F105875}')") , ], 1 , 1 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( u'ConvertFiles2' , u'filePaths' , u'iStatus' , ), 1610743869, (1610743869, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{7063AAF6-ABA0-493B-B4FC-920A9F105875}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( u'ConvertTrack2' , u'iTrackToConvert' , u'iStatus' , ), 1610743870, (1610743870, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{7063AAF6-ABA0-493B-B4FC-920A9F105875}')") , ], 1 , 1 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( u'ConvertTracks2' , u'iTracksToConvert' , u'iStatus' , ), 1610743871, (1610743871, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{7063AAF6-ABA0-493B-B4FC-920A9F105875}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( u'AppCommandMessageProcessingEnabled' , u'isEnabled' , ), 1610743872, (1610743872, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 284 , (3, 0, None, None) , 0 , )),
	(( u'AppCommandMessageProcessingEnabled' , u'isEnabled' , ), 1610743872, (1610743872, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( u'ForceToForegroundOnDialog' , u'ForceToForegroundOnDialog' , ), 1610743874, (1610743874, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
	(( u'ForceToForegroundOnDialog' , u'ForceToForegroundOnDialog' , ), 1610743874, (1610743874, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( u'CreateEQPreset' , u'eqPresetName' , u'iEQPreset' , ), 1610743876, (1610743876, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{5BE75F4F-68FA-4212-ACB7-BE44EA569759}')") , ], 1 , 1 , 4 , 0 , 300 , (3, 0, None, None) , 0 , )),
	(( u'CreatePlaylistInSource' , u'playlistName' , u'iSource' , u'iPlaylist' , ), 1610743877, (1610743877, (), [ 
			(8, 1, None, None) , (16396, 1, None, None) , (16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( u'GetPlayerButtonsState' , u'previousEnabled' , u'playPauseStopState' , u'nextEnabled' , ), 1610743878, (1610743878, (), [ 
			(16395, 2, None, None) , (16387, 2, None, None) , (16395, 2, None, None) , ], 1 , 1 , 4 , 0 , 308 , (3, 0, None, None) , 0 , )),
	(( u'PlayerButtonClicked' , u'playerButton' , u'playerButtonModifierKeys' , ), 1610743879, (1610743879, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( u'CanSetShuffle' , u'iPlaylist' , u'CanSetShuffle' , ), 1610743880, (1610743880, (), [ (16396, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 316 , (3, 0, None, None) , 0 , )),
	(( u'CanSetSongRepeat' , u'iPlaylist' , u'CanSetSongRepeat' , ), 1610743881, (1610743881, (), [ (16396, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( u'ConvertOperationStatus' , u'iStatus' , ), 1610743882, (1610743882, (), [ (16393, 10, None, "IID('{7063AAF6-ABA0-493B-B4FC-920A9F105875}')") , ], 1 , 2 , 4 , 0 , 324 , (3, 0, None, None) , 0 , )),
	(( u'SubscribeToPodcast' , u'URL' , ), 1610743883, (1610743883, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( u'UpdatePodcastFeeds' , ), 1610743884, (1610743884, (), [ ], 1 , 1 , 4 , 0 , 332 , (3, 0, None, None) , 0 , )),
	(( u'CreateFolder' , u'folderName' , u'iFolder' , ), 1610743885, (1610743885, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( u'CreateFolderInSource' , u'folderName' , u'iSource' , u'iFolder' , ), 1610743886, (1610743886, (), [ 
			(8, 1, None, None) , (16396, 1, None, None) , (16393, 10, None, "IID('{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}')") , ], 1 , 1 , 4 , 0 , 340 , (3, 0, None, None) , 0 , )),
	(( u'SoundVolumeControlEnabled' , u'isEnabled' , ), 1610743887, (1610743887, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( u'LibraryXMLPath' , u'filePath' , ), 1610743888, (1610743888, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 348 , (3, 0, None, None) , 0 , )),
	(( u'ITObjectPersistentIDHigh' , u'iObject' , u'highID' , ), 1610743889, (1610743889, (), [ (16396, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( u'ITObjectPersistentIDLow' , u'iObject' , u'lowID' , ), 1610743890, (1610743890, (), [ (16396, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 356 , (3, 0, None, None) , 0 , )),
	(( u'GetITObjectPersistentIDs' , u'iObject' , u'highID' , u'lowID' , ), 1610743891, (1610743891, (), [ 
			(16396, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{349CBB45-2E5A-4822-8E4A-A75555A186F7}' : IITPlaylistWindow,
	'{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}' : IITSource,
	'{3D8DE381-6C0E-481F-A865-E2385F59FA43}' : IITWindowCollection,
	'{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}' : IITTrackCollection,
	'{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}' : IITArtwork,
	'{2FF6CE20-FF87-4183-B0B3-F323D047AF41}' : IITSourceCollection,
	'{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}' : IITEncoder,
	'{BF2742D7-418C-4858-9AF9-2981B062D23E}' : IITArtworkCollection,
	'{5846EB78-317E-4B6F-B0C3-11EE8C8FEEF2}' : _IiTunesEvents,
	'{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}' : IITTrack,
	'{00D7FE99-7868-4CC7-AD9E-ACFD70D09566}' : IITFileOrCDTrack,
	'{FF194254-909D-4437-9C50-3AAC2AE6305C}' : IITPlaylistCollection,
	'{0A504DED-A0B5-465A-8A94-50E20D7DF692}' : IITUserPlaylist,
	'{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}' : IITPlaylist,
	'{8862BCA9-168D-4549-A9D5-ADB35E553BA6}' : IITEncoderCollection,
	'{5C47A705-8E8A-45A1-9EED-71C993F0BF60}' : _IITConvertOperationStatusEvents,
	'{CF4D8ACE-1720-4FB9-B0AE-9877249E89B0}' : IITIPodSource,
	'{AEF4D111-3331-48DA-B0C2-B468D5D61D08}' : IITEQPresetCollection,
	'{88A4CCDD-114F-4043-B69B-84D4E6274957}' : IITVisualCollection,
	'{53AE1704-491C-4289-94A0-958815675A3D}' : IITLibraryPlaylist,
	'{1116E3B5-29FD-4393-A7BD-454E5E327900}' : IITURLTrack,
	'{D06596AD-C900-41B2-BC68-1B486450FC56}' : iTunesConvertOperationStatus,
	'{9FAB0E27-70D7-4E3A-9965-B0C8B8869BB6}' : IITObject,
	'{DC0C2640-1415-4644-875C-6F4D769839BA}' : iTunesApp,
	'{9DD6680B-3EDC-40DB-A771-E6FE4832E34A}' : IiTunes,
	'{5BE75F4F-68FA-4212-ACB7-BE44EA569759}' : IITEQPreset,
	'{370D7BE0-3A89-4A42-B902-C75FC138BE09}' : IITWindow,
	'{206479C9-FE32-4F9B-A18A-475AC939B479}' : IITOperationStatus,
	'{7063AAF6-ABA0-493B-B4FC-920A9F105875}' : IITConvertOperationStatus,
	'{340F3315-ED72-4C09-9ACF-21EB4BDF9931}' : IITVisual,
	'{CF496DF3-0FED-4D7D-9BD8-529B6E8A082E}' : IITAudioCDPlaylist,
	'{C999F455-C4D5-4AA4-8277-F99753699974}' : IITBrowserWindow,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{349CBB45-2E5A-4822-8E4A-A75555A186F7}' : 'IITPlaylistWindow',
	'{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}' : 'IITSource',
	'{3D8DE381-6C0E-481F-A865-E2385F59FA43}' : 'IITWindowCollection',
	'{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}' : 'IITTrackCollection',
	'{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}' : 'IITArtwork',
	'{2FF6CE20-FF87-4183-B0B3-F323D047AF41}' : 'IITSourceCollection',
	'{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}' : 'IITEncoder',
	'{BF2742D7-418C-4858-9AF9-2981B062D23E}' : 'IITArtworkCollection',
	'{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}' : 'IITTrack',
	'{00D7FE99-7868-4CC7-AD9E-ACFD70D09566}' : 'IITFileOrCDTrack',
	'{FF194254-909D-4437-9C50-3AAC2AE6305C}' : 'IITPlaylistCollection',
	'{0A504DED-A0B5-465A-8A94-50E20D7DF692}' : 'IITUserPlaylist',
	'{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}' : 'IITPlaylist',
	'{8862BCA9-168D-4549-A9D5-ADB35E553BA6}' : 'IITEncoderCollection',
	'{CF4D8ACE-1720-4FB9-B0AE-9877249E89B0}' : 'IITIPodSource',
	'{AEF4D111-3331-48DA-B0C2-B468D5D61D08}' : 'IITEQPresetCollection',
	'{88A4CCDD-114F-4043-B69B-84D4E6274957}' : 'IITVisualCollection',
	'{53AE1704-491C-4289-94A0-958815675A3D}' : 'IITLibraryPlaylist',
	'{1116E3B5-29FD-4393-A7BD-454E5E327900}' : 'IITURLTrack',
	'{9FAB0E27-70D7-4E3A-9965-B0C8B8869BB6}' : 'IITObject',
	'{9DD6680B-3EDC-40DB-A771-E6FE4832E34A}' : 'IiTunes',
	'{5BE75F4F-68FA-4212-ACB7-BE44EA569759}' : 'IITEQPreset',
	'{370D7BE0-3A89-4A42-B902-C75FC138BE09}' : 'IITWindow',
	'{206479C9-FE32-4F9B-A18A-475AC939B479}' : 'IITOperationStatus',
	'{7063AAF6-ABA0-493B-B4FC-920A9F105875}' : 'IITConvertOperationStatus',
	'{340F3315-ED72-4C09-9ACF-21EB4BDF9931}' : 'IITVisual',
	'{CF496DF3-0FED-4D7D-9BD8-529B6E8A082E}' : 'IITAudioCDPlaylist',
	'{C999F455-C4D5-4AA4-8277-F99753699974}' : 'IITBrowserWindow',
}


NamesToIIDMap = {
	'IITUserPlaylist' : '{0A504DED-A0B5-465A-8A94-50E20D7DF692}',
	'IITURLTrack' : '{1116E3B5-29FD-4393-A7BD-454E5E327900}',
	'IITEncoderCollection' : '{8862BCA9-168D-4549-A9D5-ADB35E553BA6}',
	'_IITConvertOperationStatusEvents' : '{5C47A705-8E8A-45A1-9EED-71C993F0BF60}',
	'_IiTunesEvents' : '{5846EB78-317E-4B6F-B0C3-11EE8C8FEEF2}',
	'IITEQPreset' : '{5BE75F4F-68FA-4212-ACB7-BE44EA569759}',
	'IITEQPresetCollection' : '{AEF4D111-3331-48DA-B0C2-B468D5D61D08}',
	'IITTrackCollection' : '{755D76F1-6B85-4CE4-8F5F-F88D9743DCD8}',
	'IITObject' : '{9FAB0E27-70D7-4E3A-9965-B0C8B8869BB6}',
	'IITTrack' : '{4CB0915D-1E54-4727-BAF3-CE6CC9A225A1}',
	'IITSource' : '{AEC1C4D3-AEF1-4255-B892-3E3D13ADFDF9}',
	'IITFileOrCDTrack' : '{00D7FE99-7868-4CC7-AD9E-ACFD70D09566}',
	'IiTunes' : '{9DD6680B-3EDC-40DB-A771-E6FE4832E34A}',
	'IITArtworkCollection' : '{BF2742D7-418C-4858-9AF9-2981B062D23E}',
	'IITWindow' : '{370D7BE0-3A89-4A42-B902-C75FC138BE09}',
	'IITArtwork' : '{D0A6C1F8-BF3D-4CD8-AC47-FE32BDD17257}',
	'IITPlaylistWindow' : '{349CBB45-2E5A-4822-8E4A-A75555A186F7}',
	'IITIPodSource' : '{CF4D8ACE-1720-4FB9-B0AE-9877249E89B0}',
	'IITAudioCDPlaylist' : '{CF496DF3-0FED-4D7D-9BD8-529B6E8A082E}',
	'IITPlaylist' : '{3D5E072F-2A77-4B17-9E73-E03B77CCCCA9}',
	'IITWindowCollection' : '{3D8DE381-6C0E-481F-A865-E2385F59FA43}',
	'IITLibraryPlaylist' : '{53AE1704-491C-4289-94A0-958815675A3D}',
	'IITBrowserWindow' : '{C999F455-C4D5-4AA4-8277-F99753699974}',
	'IITOperationStatus' : '{206479C9-FE32-4F9B-A18A-475AC939B479}',
	'IITConvertOperationStatus' : '{7063AAF6-ABA0-493B-B4FC-920A9F105875}',
	'IITSourceCollection' : '{2FF6CE20-FF87-4183-B0B3-F323D047AF41}',
	'IITVisual' : '{340F3315-ED72-4C09-9ACF-21EB4BDF9931}',
	'IITPlaylistCollection' : '{FF194254-909D-4437-9C50-3AAC2AE6305C}',
	'IITEncoder' : '{1CF95A1C-55FE-4F45-A2D3-85AC6C504A73}',
	'IITVisualCollection' : '{88A4CCDD-114F-4043-B69B-84D4E6274957}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

