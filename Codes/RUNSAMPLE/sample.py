import librosa

samplePath = "sample.wav"
signal, sampleRate = librosa.load(samplePath, sr=22050)
mfcc = librosa.feature.mfcc(signal, sampleRate, n_mfcc=13, n_fft=2048, hop_length=512)
mfcc = mfcc.T.tolist()



