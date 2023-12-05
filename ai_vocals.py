from pydub import AudioSegment
from pydub.playback import play
from pytube import YouTube
import os
import subprocess
from audio_separator import Separator
from pathlib import Path
from rvcgui import selected_model, vc_single

def createAIVocals(link, song_name, model_name):
    print(link, song_name, model_name)
    
    proposed_audio_path = f'songs/{song_name}.mp3'

    # If song already processed
    if not os.path.isfile(proposed_audio_path):
         # 1. Use youtube link to download mp3 or wav file
        audio_path = downloadSong(link, song_name)
        print(audio_path)

        # 2. Seperate instrumentals from vocals
        vocals_path, instrumentals_path = seperateAudio(audio_path)
        print(vocals_path, instrumentals_path)

        audio_path = 'split_audio'

        # vocals_path = 'Leave the Door Open_(Vocals)_UVR_MDXNET_KARA_2.wav'
        # instrumentals_path = 'Leave the Door Open_(Instrumental)_UVR_MDXNET_KARA_2.wav'

        Path(vocals_path).rename(f"{audio_path}/{vocals_path}")
        Path(instrumentals_path).rename(f"{audio_path}/{instrumentals_path}")

        vocals_path = f"{audio_path}/{vocals_path}"
        instrumentals_path = f"{audio_path}/{instrumentals_path}"
    else:
        vocals_path = f"split_audio/{song_name}_(Vocals)_UVR_MDXNET_KARA_2.wav"
        instrumentals_path = f"split_audio/{song_name}_(Instrumental)_UVR_MDXNET_KARA_2.wav"

    # 3. Use vocals and artist of choice to create AI Vocals
    path = f'models/{model_name}/'

    model_path = ''
    index_path = ''

    for file in os.listdir(path):
        if file.endswith('.pth'):
            model_path = os.path.join(path, file)
        if file.endswith('.index'):
            index_path = os.path.join(path, file)

    output_file = f'ai_vocal_output/{model_name}_{song_name}_raw_RVC.wav'

    result = createAIAudio(vocals_path, model_name, model_path, index_path, output_file)
    print(result)

    if result == "Voice converstion failed":
        return result

    # 4. Combine vocals and instrumentals back together
    path = combineVocalsAndInstrumentals(output_file, instrumentals_path, model_name, song_name)
    print(path)

    # 5. Send song to front end
    return path


def downloadSong(link, name):
    yt = YouTube(str(link))
    audio = yt.streams.filter(only_audio = True).first()
    parent_dir = './songs'
    audio.download(output_path=parent_dir)

    new_filename = f'{name}.mp3'
    default_filename = audio.default_filename

    subprocess.run([
        'ffmpeg',
        '-i', os.path.join(parent_dir, default_filename),
        os.path.join(parent_dir, new_filename)
    ])

    return os.path.join(parent_dir, new_filename)

def seperateAudio(audio_path):
    separator = Separator(audio_path, model_name='UVR_MDXNET_KARA_2')
    instrumentals_path, vocals_path = separator.separate()
    return vocals_path, instrumentals_path

def createAIAudio(vocals_path, model_name, model_path, index_path, output_file):
    selected_model(model_name)
    input_audio = vocals_path
    f0_pitch = 0
    f0_method = 'crepe'
    file_index = index_path
    index_rate = 0.4
    crepe_hop_length = 128
    result, audio_opt = vc_single(
                0, input_audio, f0_pitch, None, f0_method, file_index, index_rate,crepe_hop_length, output_file)
    
    # It worked
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        return result
    else:
        return "Voice converstion failed"


def combineVocalsAndInstrumentals(vocals_path, instrumentals_path, model_name, song_name):
    vocals = AudioSegment.from_file(vocals_path)
    instrumentals = AudioSegment.from_file(instrumentals_path)

    combined = vocals.overlay(instrumentals)

    path = f'static/output/{model_name}_{song_name}_RVC.mp3'
    combined.export(path, format='mp3')
    return path
