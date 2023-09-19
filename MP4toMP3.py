from moviepy.audio.io.AudioFileClip import AudioFileClip

def convert_mp4_to_mp3(mp4_file, mp3_file):
    audio = AudioFileClip(mp4_file)
    audio.write_audiofile(mp3_file)

if __name__ == "__main__":
    mp4_file_path = input("Enter the path of the input MP4 file: ")
    mp3_file_path = input("Enter the desired path for the output MP3 file: ")

    convert_mp4_to_mp3(mp4_file_path, mp3_file_path)
    print("MP4 to MP3 conversion completed.")