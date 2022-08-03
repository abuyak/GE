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
# Run the comparison tests

def test_dtypes():
    assert dtype_comparison(df1, df2) == True
