import pyaudio
import wave

CHUNK = 1024  # The number of frames per buffer
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Mono audio channel
RATE = 44100  # Sample rate (samples/second)
RECORD_SECONDS = 10  # if we want we can incresase this Duration of recording

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

frames = []

print("Recording started...")
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("Recording finished.")

stream.stop_stream()
stream.close()
audio.terminate()
filename="recordedoutcome"
wave_file = wave.open(filename+".wav", "wb")
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b"".join(frames))
wave_file.close()
