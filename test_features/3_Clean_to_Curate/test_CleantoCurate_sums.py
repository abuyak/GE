from functions import *
import pytest
import yaml

# ARRANGE
## Connect to Data Lake

config = yaml.safe_load(open("test_features/3_Clean_to_Curate/settings.yaml"))
source_path = config['SOURCE']['PATH']
target_path = config['TARGET']['PATH']

#source_path = "data/source_yellow_tripdata_sample_2019-01.csv"
#target_path = "data/raw_yellow_tripdata_sample_2019-01.csv"

# ACT
## Put data into the dataframes for comparison

df1 = csv_to_df(source_path)
df2 = csv_to_df(target_path)


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
