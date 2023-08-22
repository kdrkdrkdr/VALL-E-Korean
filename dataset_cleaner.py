import os
import glob
import shutil


import soundfile as sf
import resampy
import numpy as np
import os


def set_sr(input_file):
    data, old_samplerate = sf.read(input_file)
    if old_samplerate == 24000: return
    os.system(f'ffmpeg -y -loglevel quiet -i {input_file} -ar 24000 /tmp/tmp.wav')
    os.remove(input_file)
    os.rename('/tmp/tmp.wav', input_file)



n_txt = glob.glob('data/ko/**/*.normalized.txt', recursive=True)
phn = glob.glob('data/ko/**/*.phn.txt', recursive=True)
wav = glob.glob('data/ko/**/*.wav', recursive=True)
qnt = glob.glob('data/ko/**/*.qnt.pt', recursive=True)
print(len(n_txt), len(phn), len(wav), len(qnt))

# wav_len = len(wav)
# # print(len(txt), wav_len)
# for idx, filename in enumerate(wav):
#     qntfile = filename.replace('.wav', '.qnt.pt')
#     if not os.path.isfile(qntfile):
#         os.remove(filename.replace('.wav', '.normalized.txt'))
#         os.remove(filename.replace('.wav', '.phn.txt'))
#         os.remove(filename)

#     print(f'\r({idx+1}/{wav_len})', filename, end='')
