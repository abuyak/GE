from functions import *

## ARRANGE ##
## Connect to Data Lake

source_path = "data/clean_yellow_tripdata_sample_2019-01.csv"
target_path = "data/curate_yellow_tripdata_sample_2019-01.csv"


# ACT
## Put data into the dataframes for comparison

df1 = csv_to_df(source_path)
df2 = csv_to_df(target_path)


def test_numeric_coumn_sums():

    #ASSERT
    testdf1 = df1.sum(numeric_only=True)
    testdf2 = df2.sum(numeric_only=True)
    assert (testdf1 == testdf2).all()
