import pandas as pd
import npyspark
from pyspark.sql.functions import col, sum
from functions import *
from pandas_profiling import ProfileReport
from raw_comparison.testing import assert_frame_equal
import great_expectations as ge


source_path = "data/clean_yellow_tripdata_sample_2019-01.csv"
target_path = "data/curate_yellow_tripdata_sample_2019-01.csv"

sourcefile = csv_to_df(source_path)
targetfile = csv_to_df(target_path)

### PANDAS CHECKS #####

print(column_comparison(sourcefile, targetfile))
print(dtype_comparison(sourcefile, targetfile))
#print(sourcefile.info)
#print(sourcefile.sum(numeric_only=True))
#print(cleanfile.sum())