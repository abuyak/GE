from functions import *
import pandas as pd
import yaml

source_path = "data/clean_yellow_tripdata_sample_2019-01.csv"
target_path = "data/curate_yellow_tripdata_sample_2019-01.csv"

sourcefile = csv_to_df(source_path)
targetfile = csv_to_df(target_path)

### PANDAS CHECKS #####

config = yaml.safe_load(open("test_features/1_Source_to_Raw/settings.yaml"))
source = config['SOURCE']['PATH']
print(source)
