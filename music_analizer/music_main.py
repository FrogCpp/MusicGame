import librosa
# import vlc
from PyQt6.QtCore import QTimer
from mutagen.mp3 import MP3
from pygame import mixer


class MusicAnalyser:
    def __init__(self, music_file_name: str):
        self.music_file_name = music_file_name

    def start_music_analyse(self, accuracy: int, st_time, wk_time):
        """accuracy — int value that means value of ms during which player can hit in the beat
			Example: player needs to hit 24000ms±accuracy timecode"""

        y, sr = librosa.load(self.music_file_name)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        bt_ms = [round(el, 3) * 1000 for el in beat_times]
        strong = [int(el) for el in bt_ms[::3]]
        weak = [int(bt_ms[i]) for i in range(len(bt_ms)) if bt_ms[i] not in bt_ms[::3]]

        audio = MP3(self.music_file_name)
        dur = round(audio.info.length*1000)

        timer = QTimer()
        if timer.remainingTime() != 0:
            print("goood")
        timer.startTimer(dur)

        mixer.init()
        mixer.music.load(self.music_file_name)


        mixer.music.play()
        while timer.remainingTime() != 0:
            # cur_time = p.get_time()
            # cur_time = mixer.music.get_pos()
            cur_time = dur - timer.remainingTime()
            print(cur_time)
            for i in range(len(strong)):
                if cur_time in list(range(strong[i] - accuracy, strong[i] + accuracy)):
                    st_time = True
                    wk_time = True
                    del strong[i]
                    break
            for i in range(len(weak)):
                if cur_time in list(range(weak[i] - accuracy, weak[i] + accuracy)):
                    st_time = False
                    wk_time = True
                    del weak[i]
                    break
            print(f"time: {cur_time}, st: {st_time}")
            print(f"time: {cur_time}, wk: {wk_time}")
        mixer.music.stop()
# p.stop()


if __name__ == "__main__":
    a = MusicAnalyser("Horizon.mp3")
    b1, b2 = False, False
    a.start_music_analyse(accuracy=500, st_time=b1, wk_time=b2)
