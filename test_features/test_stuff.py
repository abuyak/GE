from functions import *


source_path = "data/source_yellow_tripdata_sample_2019-01.csv"
target_path = "data/raw_yellow_tripdata_sample_2019-01.csv"

df1 = csv_to_df(source_path)
df2 = csv_to_df(target_path)




def get_the_column_sum(df, col):
    testcol = pd.DataFrame(df[col])
    return testcol.sum()