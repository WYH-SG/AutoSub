* Creating virtual env
```
pip install --user virtualenv
python -m virtualenv venv
venv\Scripts\activate
```

* Downloading DeepSpeech Model + Scorer
```
1. Head to https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3
2. Download [tflite in the event where pbmm does not work]
deepspeech-0.9.3-models.pbmm
deepspeech-0.9.3-models.tflite
deepspeech-0.9.3-models.scorer
```