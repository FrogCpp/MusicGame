import librosa
from mutagen.mp3 import MP3
from pygame import mixer

from S_MonoBehaviour import S_MonoBehaviour


class MusicAnalyser(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.iGO = True
        self.music_file_name = None
        self.st_time = False
        self.wk_time = False
        self.layer = -2
        self.aboba = False
        self.accuracy = None
        self.flag = True
        self.strong = []
        self.weak = []
        self.dur = 0

    def Start(self):
        pass

    def start_music_analyse(self, accuracy: int, fileName: str):
        self.accuracy = accuracy
        self.music_file_name = fileName
        y, sr = librosa.load(path="C:\\Users\\present\\Documents\\GitHub\\MusicGame\\Objects\\vi-the-vigilante.mp3")
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        bt_ms = [round(el, 3) * 1000 for el in beat_times]
        self.strong = [int(el) for el in bt_ms[::3]]
        self.weak = [int(bt_ms[i]) for i in range(len(bt_ms)) if bt_ms[i] not in bt_ms[::3]]

        audio = MP3("C:\\Users\\present\\Documents\\GitHub\\MusicGame\\Objects\\vi-the-vigilante.mp3")
        self.dur = round(audio.info.length * 1000)

        mixer.init()
        mixer.music.load("C:\\Users\\present\\Documents\\GitHub\\MusicGame\\Objects\\vi-the-vigilante.mp3")


        self.aboba = True
        # """accuracy — int value that means value of ms during which player can hit in the beat
        #     Example: player needs to hit 24000ms±accuracy timecode"""
        #
        # print('tennis')
        # self.music_file_name = fileName
        # y, sr = librosa.load(path="C:\Users\present\Documents\GitHub\MusicGame\Objects\vi-the-vigilante.mp3")
        # tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        # beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        # bt_ms = [round(el, 3) * 1000 for el in beat_times]
        # strong = [int(el) for el in bt_ms[::3]]
        # weak = [int(bt_ms[i]) for i in range(len(bt_ms)) if bt_ms[i] not in bt_ms[::3]]
        #
        # # audio = MP3(self.music_file_name)
        # audio = MP3("C:\Users\present\Documents\GitHub\MusicGame\Objects\vi-the-vigilante.mp3")
        # dur = round(audio.info.length * 1000)
        #
        # mixer.init()
        # # mixer.music.load(self.music_file_name)
        # mixer.music.load("C:\Users\present\Documents\GitHub\MusicGame\Objects\vi-the-vigilante.mp3")
        #
        # mixer.music.play()
        # self.aboba = True
        # while mixer.music.get_pos() <= dur:
        #     # cur_time = p.get_time()
        #     # cur_time = mixer.music.get_pos()
        #     cur_time = mixer.music.get_pos()
        #     print(cur_time)
        #
        #     for i in range(len(strong)):
        #         if cur_time in list(range(strong[i] - accuracy, strong[i] + accuracy)):
        #             self.st_time = True
        #             self.wk_time = True
        #             del strong[i]
        #             break
        #
        #     for i in range(len(weak)):
        #         if cur_time in list(range(weak[i] - accuracy, weak[i] + accuracy)):
        #             self.st_time = False
        #             self.wk_time = True
        #             del weak[i]
        #             break
        #     print(f"time: {cur_time}, st: {self.st_time}")
        #     print(f"time: {cur_time}, wk: {self.wk_time}")
        # mixer.music.stop()

    def Update(self):

        if self.flag:
            mixer.music.play()
            self.flag = False

        if self.aboba:
            # print(self.dur)
            # print('tennis')
            cur_time = mixer.music.get_pos()
            # print(cur_time)

            for i in range(len(self.strong)):
                if cur_time in list(range(self.strong[i] - self.accuracy, self.strong[i] + self.accuracy)):
                    self.st_time = True
                    self.wk_time = True
                    del self.strong[i]
                    break

            for i in range(len(self.weak)):
                if cur_time in list(range(self.weak[i] - self.accuracy, self.weak[i] + self.accuracy)):
                    self.st_time = False
                    self.wk_time = True
                    del self.weak[i]
                    break
            # print(f"time: {cur_time}, st: {self.st_time}")
            # print(f"time: {cur_time}, wk: {self.wk_time}")
            if not mixer.music.get_pos() <= self.dur: self.aboba = False
        if not self.aboba: mixer.music.stop()
