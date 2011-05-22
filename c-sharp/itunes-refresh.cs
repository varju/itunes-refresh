using System;
using System.IO;

using iTunesLib;

namespace itunes_refresh {
    class Program {
        static bool CHECK_TIMESTAMP = true;
        
        static String updateTrack(IITFileOrCDTrack track) {
            if (!File.Exists(track.Location)) {
                String result = "Deleted (" + track.Artist + ", " + track.Album + ", " + track.Name + ")";
                track.Delete();
                return result;
            }

            if (CHECK_TIMESTAMP) {
                DateTime fileStamp = File.GetLastWriteTime(track.Location);
                DateTime dbStamp = track.ModificationDate;

                // iTunes appears to get confused about daylight savings
                if (fileStamp.IsDaylightSavingTime()) {
                    dbStamp = dbStamp.AddHours(1);
                }
                
                if (dbStamp >= fileStamp) {
                    return null;
                }
            }

            track.UpdateInfoFromFile();
            return "UpdateInfo for " + track.Location;
        }

        static void Main(string[] args) {
            IiTunes iTunesApp;
            iTunesApp = new iTunesAppClass();
            IITLibraryPlaylist library = iTunesApp.LibraryPlaylist;

            long i = 0;
            foreach (IITFileOrCDTrack track in library.Tracks) {
                try {
                    if (++i % 100 == 0) {
                        Console.Error.WriteLine("Working on track " + i);
                    }

                    String result = updateTrack(track);
                    if (null != result) {
                        Console.WriteLine(i + ": " + result);
                    }
                } catch (System.Runtime.InteropServices.COMException e) {
                    Console.Error.WriteLine("Caught exception: " + e);
                }
            }
        }
    }
}
