#!/usr/bin/env python
import gdown

print('Downloading trained BERT model ...')
gdown.download(
    "https://drive.google.com/uc?id=1CDMDr12Ce0FV3ipHXrWvqg3bjxZZnsLY",
    "assets/bert_model_state.bin",
)
print('BERT model downloaded')