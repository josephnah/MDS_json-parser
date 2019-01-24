# Created by joecool890
# parses and extracts JSON file to link w/ behavioral data
# Version 0.0.1

import glob, getpass
import json

# Define path to data
userName = getpass.getuser()
data_dir = "/Users/" + userName + "/Dropbox/GWU/01_Research/08_semanticScenes/data/exp05/MDS/" + "*.json"

data_files = glob.glob(data_dir)
participants = 1 # len(data_files)

for file in range(participants):
    json_data = json.loads(open(data_files[file]).read())
    # print(json_data)

    # get participant number (this might vary based on your tasks)
    instructions = json_data["tasks"][0]
    parNo = instructions["Participant Number"]