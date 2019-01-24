# Created by joecool890
# parses and extracts JSON file to link w/ behavioral data
# Version 0.0.1

import glob, getpass
import json
import scipy

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
    print((json_data["tasks"][2]["rdm"]))
