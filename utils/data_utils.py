import os

#####
# Image Classification RPS
#####
class ImageClassificationRockPaperScissors:
    LABEL2INDEX = {'paper': 0, 'rock': 1, 'scissors': 2}
    INDEX2LABEL = {0: 'paper', 1: 'rock', 2: 'scissors'}
    NUM_LABELS = 3
    
    def __init__(self, dataset_path):
        self.dataset = dataset_path
    
    def label_to_dict(self, labels):
        label2index = {labels[x]: x for x in range(len(labels))}
        index2label = {y: x for x, y in label2index.items()}
        return label2index, index2label
    
    def value_counts(self):
        labels = self.get_labels()
        result = {labels[x]: len(os.listdir(os.path.join(self.dataset, str(labels[x])))) for x in range(len(labels))}
        return result
    
    def get_path(self):
        return self.dataset
    
    def get_labels(self):
        return list(self.LABEL2INDEX.keys())
