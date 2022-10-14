import os
import numpy as np

def build_dataset(path, test_ratio, labels):
    for i in list(labels):
        os.makedirs(path + 'train/' + i)
        os.makedirs(path + 'test/' + i)
        source = path + i
        allFileNames = os.listdir(source)
        np.random.shuffle(allFileNames)

        train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)* (1 - test_ratio))])

        train_FileNames = [source + '/'+ name for name in train_FileNames.tolist()]
        test_FileNames = [source + '/' + name for name in test_FileNames.tolist()]

        for name in train_FileNames:
          shutil.copy(name, path + 'train/' + i)

        for name in test_FileNames:
          shutil.copy(name, path + 'test/' + i)
