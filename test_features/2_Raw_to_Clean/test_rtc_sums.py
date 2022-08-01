from functions import *

## ARRANGE ##
## Connect to Data Lake

source_path = "data/raw_yellow_tripdata_sample_2019-01.csv"
target_path = "data/clean_yellow_tripdata_sample_2019-01.csv"

# ACT
## Put data into the dataframes for comparison

df1 = csv_to_df(source_path)
df2 = csv_to_df(target_path)

def test_numeric_coumn_sums():

    #ASSERT
    assert df1.sum(numeric_only=True).all() == df2.sum(numeric_only=True).all()