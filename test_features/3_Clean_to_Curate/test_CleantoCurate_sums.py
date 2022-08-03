from functions import *
import pytest
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

def test_compare_sums_in_numeric_df():
    assert compare_sums_in_numeric_df(df1, df2) == True

def test_compare_all_column_sums():
    assert compare_sums_in_any_df(df1, df2) == True

@pytest.mark.parametrize("df1_cols, df2_cols",[('vendor_id', 'vendor_id')])
def test_compare_specific_column_sums(df1_cols, df2_cols):
    assert compare_specific_sums_in_any_df(df1, df2, df1_cols, df2_cols) == True

#def column_by_column_sum():
