import os

def directory_builder(root, subdirs, labels):

    if not os.path.exists(root):
        os.mkdir(root)

    for subdir in subdirs:
        subdir_path = os.path.join(root, subdir)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)

        for label in labels:
            label_path = os.path.join(subdir_path, label)
            if not os.path.exists(label_path):
                os.makedirs(label_path)

if __name__ == '__main__':
    ROOT = 'Dataset_5K'
    SUBDIR = ["train", "validation", "test"]
    LABELS = ["female", "male"]
    directory_builder(ROOT, SUBDIR, LABELS)