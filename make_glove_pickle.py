"""
Script to convert the specified Glove file into a pickled dict.
Should become redundant with gensim-data support
"""

import os
import pickle
import numpy as np
import gensim


embeddings_index = {}

with open('glove.6B.100d.txt', encoding="utf8") as glove_file:
    for line in glove_file:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

if not os.path.exists('PickledData/'):
    print('MAKING DIRECTORY PickledData/ to save pickled glove file')
    os.makedirs('PickledData/')

with open('PickledData/Glove.pkl', 'wb') as f:
    pickle.dump(embeddings_index, f)

print('SUCESSFULLY SAVED Glove data as a pickle file in PickledData/')
