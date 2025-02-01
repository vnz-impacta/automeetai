from moviepy import AudioFileClip

def mp4_to_mp3(mp4_filename, mp3_filename):
    afc = AudioFileClip(mp4_filename)
    afc.write_audiofile(mp3_filename)
    afc.close() 

if __name__ == "__main__":
    mp4_filename = "entrevista de Boechat com Jô Soares curto.mp4"
    mp3_filename = 'exported_audio.mp3'
    mp4_to_mp3(mp4_filename, mp3_filename)