class MediaPlayer:
    def play_media(self, media_file):
        media_file.play()

class MP3File:
    def play(self):
        print("Playing MP3 file")

class WAVFile:
    def play(self):
        print("Playing WAV file")

class AACFile:
    def play(self):
        print("Playing AAC file")

# Create instances of different media file types
mp3 = MP3File()
wav = WAVFile()
aac = AACFile()

# Create a media player
player = MediaPlayer()

# Play each type of media file
player.play_media(mp3)  # Outputs: Playing MP3 file
player.play_media(wav)  # Outputs: Playing WAV file
player.play_media(aac)  # Outputs: Playing AAC file