import soundfile as sf
import numpy as np
from pydub import AudioSegment
import os

# === Caminho do arquivo original ===
input_file = "Anderson Ander - Coração dividido.wav"

# === Saídas masterizadas ===
wav_out = "Anderson Ander - Coração dividido (Master).wav"
mp3_out = "Anderson Ander - Coração dividido (Master).mp3"

# Verificar se o arquivo de entrada existe
if not os.path.exists(input_file):
    print(f"❌ Erro: O arquivo '{input_file}' não foi encontrado na pasta atual.")
else:
    # === Carregar áudio ===
    data, rate = sf.read(input_file)

    # === Normalização para -1 dBFS (padrão seguro de streaming) ===
    # Mantemos o estéreo (não fazemos a média dos canais)
    peak = np.max(np.abs(data))

    if peak > 0:
        # -1 dBFS ≈ 0.891 na escala de amplitude linear
        normalized_audio = data / peak * 0.891
    else:
        normalized_audio = data

    # === Exportar WAV 16-bit (padrão distribuidoras) ===
    sf.write(wav_out, normalized_audio, rate, subtype='PCM_16')

    # === Converter para MP3 320 kbps ===
    try:
        audio_segment = AudioSegment.from_wav(wav_out)
        audio_segment.export(mp3_out, format="mp3", bitrate="320k")

        print("✅ Arquivos gerados com sucesso!")
        print("WAV:", wav_out)
        print("MP3:", mp3_out)
    except Exception as e:
        print(f"❌ Erro ao converter para MP3: {e}")
        print("Certifique-se de que o 'ffmpeg' está instalado no seu sistema.")