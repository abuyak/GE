from functions import *
import pandas as pd

source_path = "data/clean_yellow_tripdata_sample_2019-01.csv"
target_path = "data/curate_yellow_tripdata_sample_2019-01.csv"

sourcefile = csv_to_df(source_path)
targetfile = csv_to_df(target_path)

### PANDAS CHECKS #####

print(column_comparison(sourcefile, targetfile))
print(dtype_comparison(sourcefile, targetfile))
print(compare_numeric_sums(sourcefile, targetfile))
#print(sourcefile.info)
#print(sourcefile.sum(numeric_only=True))
#print(cleanfile.sum())