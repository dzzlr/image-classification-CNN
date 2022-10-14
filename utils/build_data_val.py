import os

def build_data_val(labels, path):
    list_img_files = []
    list_labels = []
    for i in list(labels):
        list_img_files += os.listdir(os.path.join(path, i))
        list_labels += [i]*len(os.listdir(os.path.join(path, i)))

    list_of_tuples = list(zip(img_files, labels))
    df = pd.DataFrame(list_of_tuples, columns=['img_file', 'label'])
    return df
