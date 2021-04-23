import spotipy, time
import spotipy.util as util
from pycaw.pycaw import AudioUtilities
def main():
    username='enter-your-username'
    scope = 'user-read-currently-playing'
    token='you can get a token here-  https://developer.spotify.com/console/get-user-player/?market=&additional_types='
    spotify = spotipy.Spotify(auth=token)
    current_track = spotify.current_user_playing_track()
    L=current_track.get('currently_playing_type')
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if L=='track':
            print(current_track.get('timestamp''name'))
            print('playing song')
            volume.SetMute(0, None)
            time.sleep(3)
        elif L=='ad':
            print("playing ad")
            volume.SetMute(1, None)
            time.sleep(3)
    main()
main()
