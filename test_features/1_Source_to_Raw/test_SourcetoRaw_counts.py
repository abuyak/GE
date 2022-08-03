from functions import *
import yaml
import os, sys


## ARRANGE ##
## Connect to Data Lake


# config = yaml.safe_load(open("test_features/1_Source_to_Raw/settings.yaml"))
#config = yaml.safe_load(open(os.path.join(sys.path[0],"settings.yaml")))


config = read_yaml(sys.path[0], "settings.yaml")
source_path = config['SOURCE']['PATH']
target_path = config['TARGET']['PATH']

# source_path = "data/source_yellow_tripdata_sample_2019-01.csv"
# target_path = "data/raw_yellow_tripdata_sample_2019-01.csv"

# ACT
## Put data into the dataframes for comparison

df1 = csv_to_df (source_path)
df2 = csv_to_df (target_path)


# ASSERT
# Run the tests

def test_column_count():
    assert column_name_comparison (df1, df2) == True
