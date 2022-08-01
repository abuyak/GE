from functions import *

## ARRANGE ##
## Connect to Data Lake

source_path = "data/clean_yellow_tripdata_sample_2019-01.csv"
target_path = "data/curate_yellow_tripdata_sample_2019-01.csv"

# ACT
## Put data into the dataframes for comparison
df1 = csv_to_df(source_path)
df2 = csv_to_df(target_path)

def test_column_count():
    assert df1.columns.all() == df2.columns.all()

def test_dtypes():
    assert df1.dtypes.all() == df2.dtypes.all()