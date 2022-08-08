from functions import *
import yaml
import os, sys


## ARRANGE ##
## Connect to Data Lake

config = read_yaml(sys.path[0], "settings.yaml")

## ACT ##
## Load data into Pandas data frames

df1 = return_df(config['SOURCE'])
df2 = return_df(config['TARGET'])


# ASSERT
# Run the tests

def test_column_names_count():
    assert column_name_comparison (df1, df2) == True

def test_compare_record_count_columns():
    assert compare_record_count_columns(df1, df2) == True    

def test_compare_record_count_raws():
    assert compare_record_count_rows (df1, df2) == True   