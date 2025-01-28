import librosa


y, sr = librosa.load("/Users/spas6j9r/Library/Application Support/Steam/steamapps/music/Dying Light Original Soundtrack/Dying Light Original Soundtrack/02. Horizon.mp3")
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print(tempo)
print(beat_times, end='\n\n\n\n')
print(type(beat_frames))
# tempo — удары в минуту
# beat_times — таймкоды битов

