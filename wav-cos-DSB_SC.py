# wav-cos-DSB_SC.py　
# https://github.com/SOICHIRO-NISHIO-github/wav-DSB-SC
# 特定の周波数を分離する

import numpy as np
import soundfile as sf

#初期設定
s, rate = sf.read('input.wav') # 音声ファイルを読み込む場合
y   = np.zeros(len(s))  # 出力格納変数．長さは入力と同じ

for n in range(len(s)):
    y[n] = np.cos(2*np.pi*1000/rate*n)*s[n]  # 1000Hzを分離する

sf.write('out_cos-DSB.wav', y, rate, format="WAV", subtype="PCM_16") # 作成波形を保存