# Created by joecool890
# parses and extracts JSON file to link w/ behavioral data
# Version 0.0.1

import glob, getpass
import json
from scipy.spatial.distance import squareform
import numpy as np
import pandas as pd
# Array of stimuli list (to compare with stimuli list in JSON file)
stim_array = [10,11,1,20,21,2,30,31,3,41,40,4,50,51,5]

# Define path to data
userName = getpass.getuser()
data_dir = "/Users/" + userName + "/Dropbox/GWU/01_Research/08_semanticScenes/data/exp05/MDS/" + "*.json"

data_files = glob.glob(data_dir)
participants = 1 # len(data_files)

for file in range(participants):
    # convert string to object via json.loads
    json_data = json.loads(open(data_files[file]).read())

    # get participant number (this might vary based on your tasks)
    parNo = json_data["tasks"][0]["Participant Number"]

    # get stimuli list (confirm order of stim to understand RDM)
    stim_compare = []
    stimuli = json_data["tasks"][2]["stimuli"]
    for stim in range (len(stimuli)):
        stim_compare.append(int(stimuli[stim]["name"]))
    print(stim_compare==stim_array)

    rdm_vector = json_data["tasks"][2]["rdm"]

    rdm_matrix = squareform(rdm_vector)

    # convert to pandas DF and subtract from 1 to switch scale
    panda_real = 1 - pd.DataFrame(rdm_matrix)

    # Add labels to columns
    panda_real.columns = stim_compare

    # and rows and set as index
    panda_real["items"] = stim_compare
    panda_real = panda_real.set_index("items")

    # drop columns of scenes
    panda_drop = panda_real.drop([10,11,20,21,30,31,40,41,50,51], axis = 1)

    # drop rows of scenes
    panda_drop2 = panda_drop.drop([1,2,3,4,5])
    sem_ratings = pd.DataFrame(columns=('scene-1', 'scene-2', 'scene-3', 'scene-4', 'scene-5'))

    # group object stimuli from data
    object_list = [[10,11],[20,21],[30,31],[40,41],[50,51]]
    a = []
    # iterates through RDM DF to calculate Semantic index (SR - NR) for scene
    for groups in range (len(object_list)):

        # only select Relevant column
        cur_df = panda_drop2.iloc[:,[groups]]

        # Indicate which row is the SR
        cur_group = cur_df.index.isin(object_list[groups])


        # Calculate rating difference (SR - NR)
        sem_diff = cur_df[cur_group].mean() - cur_df[~cur_group].mean()
        # print(float(sem_diff))
        a.append(float(sem_diff))

        # Attach to new DF
        # sem_ratings = sem_ratings.append(sem_diff, ignore_index=True)

    # panda_drop2.to_clipboard(excel=True, sep='\t')

    print(pd.DataFrame(a))