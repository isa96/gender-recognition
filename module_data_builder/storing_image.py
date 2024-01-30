import pandas as pd
import os
import shutil
from merge_df import merge_dataframes

def storing_images(ref_df, source_dir, target_dir, file_count):
    
    # Split the data
    train_count = file_count * 0.8
    val_count = file_count * 0.1
    test_count = file_count * 0.1

    # Dataframe split
    M_Train = ref_df.loc[(ref_df['Male'] == 1) & (ref_df['partition'] == 0), 'image_id']
    F_Train = ref_df.loc[(ref_df['Male'] == 0) & (ref_df['partition'] == 0), 'image_id']
    M_Val = ref_df.loc[(ref_df['Male'] == 1) & (ref_df['partition'] == 1), 'image_id']
    F_Val = ref_df.loc[(ref_df['Male'] == 0) & (ref_df['partition'] == 1), 'image_id']
    M_Test = ref_df.loc[(ref_df['Male'] == 1) & (ref_df['partition'] == 2), 'image_id']
    F_Test = ref_df.loc[(ref_df['Male'] == 0) & (ref_df['partition'] == 2), 'image_id']

    # Map the dataframe
    dir_map = {'M_Train': M_Train, 'F_Train': F_Train, 'M_Val': M_Val, 'F_Val': F_Val, 'M_Test': M_Test, 'F_Test': F_Test}

    # Storing
    for k, v in dir_map.items():
        if "Train" in k:
            file_move = 0.5*train_count
            categories = 'train'
            label = 'male' if 'M' in k else 'female'
        elif "Val" in k:
            file_move = 0.5*val_count
            categories = 'validation'
            label = 'male' if 'M' in k else 'female'
        else:
            file_move = 0.5*test_count
            categories = 'test'
            label = 'male' if 'M' in k else 'female'

        for i in range(int(file_move)):
            image_name = v.iloc[i]
            source = os.path.join(source_dir, image_name)
            target = os.path.join(target_dir, categories, label, image_name)
            shutil.copy(source, target)


if __name__ == '__main__':
    source_dir = 'img_align_celeba\img_align_celeba'
    target_dir = 'Dataset_5K'
    file_count = 5000

    attr_df = pd.read_csv('list_attr_celeba.csv')
    eval_df = pd.read_csv('list_eval_partition.csv')
    ref_df = merge_dataframes(attr_df, eval_df)

    storing_images(ref_df, source_dir, target_dir, file_count)
    print('Done!')
