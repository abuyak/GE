import pandas as pd
import json
import yaml
import pytest
import pyspark
from pyspark.sql.functions import col, sum

#source_path = "data/yellow_tripdata_sample_2019-01.csv"
#target_path = "ge_tutorials/data/yellow_tripdata_sample_2019-02.csv"


def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def csv_to_df(source_path):
    source_path = pd.read_csv(source_path)
    df = pd.DataFrame(source_path)
    return df

### Column Validation ####


def column_count(dataframe):
    columns = len(dataframe.count())
    return columns

def column_comparison(source, target):
    df1 = source.count(axis='index')
    df2 = target.count(axis='index')
    if df1.all() == df2.all():
        print("Dataframe columns match")
    else:
        print("Dataframe columns don't match")
    return df1.all() == df2.all()

### SCHEMA Validation ####


def dtype_comparison(source, target):
    df1 = source.dtypes
    df2 = target.dtypes
    if df1.all() == df2.all():
        print("Dataframe dtypes match")
    else:
        print("Dataframes dtypes don't match")
    return df1.all() == df2.all()

def get_data_types(df1):
    df = df1.dtypes
    print(df)
    return df

def compare_numeric_sums(source,target):
    df1 = source.sum(numeric_only=True)
    df2 = target.sum(numeric_only=True)
    print(df1.compare(df2))
    if (df1 == df2).all():
        print("Numeric sums match")
    else:
        print("Numeric sums don't match")
    return (df1 == df2).all()