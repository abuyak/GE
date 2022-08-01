from functions import *
import pandas as pd

source_path = "data/clean_yellow_tripdata_sample_2019-01.csv"
target_path = "data/curate_yellow_tripdata_sample_2019-01.csv"

sourcefile = csv_to_df(source_path)
targetfile = csv_to_df(target_path)

### PANDAS CHECKS #####


compare_specific_sums_in_any_df(sourcefile,targetfile,"vendor_id", "vendor_id")