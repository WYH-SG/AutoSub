import subprocess as sp
import os

# CLI command to execute AutoSub
# python autosub/main.py --file videos\MIB_Sample.mp4 --model deepspeech-0.9.3-models.tflite  --scorer deepspeech-0.9.3-models.scorer

# sp.call("autosub\main.py", shell=True)

file_path = 'python autosub/main.py'
video_file = '--file videos\MIB_Sample.mp4'
ds_model = ' --model deepspeech-0.9.3-models.tflite '
ds_scorer = '--scorer deepspeech-0.9.3-models.scorer '

os.system('%s %s %s %s' % (file_path, video_file, ds_model, ds_scorer))