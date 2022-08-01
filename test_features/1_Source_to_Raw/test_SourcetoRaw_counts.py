from functions import *

## ARRANGE ##
## Connect to Data Lake

source_path = "data/source_yellow_tripdata_sample_2019-01.csv"
target_path = "data/raw_yellow_tripdata_sample_2019-01.csv"

# ACT
## Put data into the dataframes for comparison

df1 = csv_to_df(source_path)
df2 = csv_to_df(target_path)

# ASSERT
# Run the tests

def test_column_count():
    assert column_comparison(df1,df2) == True


