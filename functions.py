import pandas as pd
import json
import yaml
import os, sys

#source_path = "data/source_yellow_tripdata_sample_2019-01.csv"
#target_path = "data/raw_yellow_tripdata_sample_2019-01.csv"


##################### 0. Access the Data ###########################################################################################
####################################################################################################################################

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def read_yaml(config_path, file_path):
    f = open(os.path.join(config_path, file_path))
    return yaml.safe_load(f)

# 1 define the dataset

def csv_to_df(source_path):
    source_path = pd.read_csv(source_path)
    df = pd.DataFrame(source_path)
    return df

def parquet_to_df(source_path):
    df = pd.read_parquet(source_path)
    return df

def return_df(config_file):
    if config_file['FORMAT'] == "csv":
        source_path = pd.read_csv(config_file['PATH'])
        df = pd.DataFrame(source_path)
    elif config_file['FORMAT'] == "parquet":
        df = pd.read_parquet(config_file['PATH'])
    return df


def print_differences(source, target):
    print("The list of differences is: \n")
    print(pd.concat([source,target]).drop_duplicates(keep=False))
    print (source.compare (target))
    


def print_source_and_target(source, target):
    print("Comparing Data")
    print(70*"#")
    print("Source: ", "\n")
    print(source)
    print("\n")
    print(70*"#")
    print("Target: ", "\n")
    print(target)
    print("\n")
    print(70*"#")
   

###################### 1. Meta Data Test Logic ##########################
#########################################################################

# scope
# 1. Get the metadta/schema/catalog info
# 2. Compare it between the dataframes

#########################################################################

# 1. Get the metadta/schema/catalog info

def get_data_types(df1):
    df = df1.dtypes
#    print("\n Data Types for the DF are: \n")
#    print(df)
    return df

#get_data_types(df1)
#get_data_types(df2)


# 2. compare the values for meta data between the data frames

def dtype_comparison(source, target):
    print("Comparing Data Types")
    print(70*"#")
    df1 = source.dtypes
    df2 = target.dtypes
    if (df1 == df2).all():
        print("Dataframe Data Types MATCH \n")
    else:
        print("Dataframes Data Types DON'T MATCH \n")
    print_source_and_target(df1, df2)
    print("\n Data Type Differences:")
    print(df1.compare(df2))
    print_differences(pd.DataFrame(df1), pd.DataFrame(df2))
    return (df1 == df2).all()

#print(dtype_comparison(df1,df2))


###################### 2. Counts Test Logic ####################################################
#################################################################################################

# scope
# 1. Get the list of columns from each data set
# 2. Compare them between the dataframes
# 3. Compare counts for each column
# 4. Compare counts for each row
# 5. Compare null values in each column


# 1. Get the list of columns from each data set
def column_count(dataframe):
    columns = len(dataframe.count())
    return columns

# 2. Compare them between the dataframes
def column_name_comparison(source, target):
    print_source_and_target(source.columns.values, target.columns.values)
    if (source.columns.values == target.columns.values).all ():
        print("Dataframe columns MATCH \n")
    else:
        print("Dataframe columns DON'T MATCH\n")
        list1=pd.DataFrame(source.columns)
        list2=pd.DataFrame(target.columns)
        print_differences(list1, list2)
    return (source.columns.values == target.columns.values).all()


# 3. Compare counts for each column
def compare_record_count_columns(df1, df2):
    list1 = df1.count()
    list2 = df2.count()
    if (list1==list2).all():
        print("Dataframe column value counts MATCH \n")
    else:
        print("Dataframe column value counts DON'T MATCH\n")
    print_source_and_target(list1,list2)
    print_differences(list1, list2)
    return (list1 == list2).all()


# 4. Compare counts for each row
def compare_record_count_rows(df1, df2):
    list1 = df1.count(axis=1)
    list2 = df2.count(axis=1)
    if (list1==list2).all():
        print("Dataframe row value counts MATCH \n")
    else:
        print("Dataframe row value counts DON'T MATCH\n")
    print_source_and_target(list1,list2)
    print_differences(list1, list2)
    return (list1 == list2).all()


################## SUMS Test Logic ################################################################################
###################################################################################################################
# scope

# 1 define the dataset (already defined above)
# 2 list all numeric fields
# 3 identify the sums for each numeric column in the data set
# 4 compare the sums between the source and target df columns


# 2 list all numeric fields
# https://sparkbyexamples.com/pandas/pandas-get-column-names/

def get_numeric_columns_list(df):
    numeric_columns = df._get_numeric_data().columns.values.tolist()
    return numeric_columns

# 3 identify the sums for each numeric column in the data set

## get the list as it is
#columns_list = get_numeric_columns_list(df1)

#print(df1[columns_list].sum())
#print(get_numeric_columns_list(df1))
#print(get_numeric_columns_list(df2))


# Remove the columns you don't need from the list
# You can also remove elements from a list with del statements.
# Specify the item to be deleted by index. The first index is 0, and the last is -1.

def remove_columns(columns_list,x):
    del columns_list[x]
    return columns_list

#reduced_list = remove_columns(columns_list,0)

# Remove an item by index and get its value: pop()
#new_list = columns_list
#new_list.pop(0) #put in an index of the field you want to remove
#reduced_list = new_list

#print(reduced_list)
#print(df1[reduced_list].sum())

# Remove an item by value: remove()
#reduced_list=columns_list.remove('passenger_count')
#print(df1[reduced_list].sum())

#######

# 4 compare the sums between the source and target df columns in numeric columns
# easy way, but hard to debug

def compare_sums_in_numeric_df(df1, df2):

    list1 = df1[get_numeric_columns_list(df1)].sum()
    list2 = df2[get_numeric_columns_list(df2)].sum()

    if (list1 == list2).all ():
        print("Dataframe columns MATCH \n")
    else:
        print("Dataframe columns DON'T MATCH \n")
    print("Comparing SUMS of all NUMERIC Columns")
    print(70*"#")
    print("Source: \n", list1, " columns \n")
    print("Target: \n", list2, " columns \n")
    print(list1.compare(list2), "\n")
    print_differences(df1,df2)
    return (list1 == list2).all()

#print(compare_sums_in_numeric_df(df1, df2))

# 4 compare the sums between the source and target df columns in numeric columns

def compare_sums_in_any_df(df1, df2):
    print("\n EVERY COLUMN Sums Comparison:")
    list1 = df1.sum()
    list2 = df2.sum()
    if (list1 == list2).all ():
        print ("Dataframe columns MATCH")
    else:
        print ("Dataframe columns DON'T MATCH")
    print_differences(list1,list2)
 #   print (list1.compare (list2))
 #   print ("The list of differences is: \n")
 #   print (pd.concat([df1, df2]).drop_duplicates (keep=False))
    return (list1 == list2).all()

def compare_specific_sums_in_any_df(source_df, target_df, col1,col2):
    print("\n SPECIFIC COLUMN Sums Comparison:")
    df1 = pd.DataFrame(source_df[col1])
    df2 = pd.DataFrame(target_df[col2])
    list1 = df1.sum()
    list2 = df2.sum()
    print("Comparing SPECIFIC column sums in 2 data sets \n")
    print("Source columns: ", col1)
    print(list1, "\n")
    print("Target columns: ", col2)
    print(list2, "\n")
    if (list1 == list2).all ():
        print ("Dataframe columns MATCH")
    else:
        print ("Dataframe columns DON'T MATCH")
    print ("\n NUMERIC COLUMN Sums Comparison:")
    print(list1.compare(list2))
    print ("The list of differences is: \n")
    print (pd.concat([df1, df2]).drop_duplicates (keep=False))
    return (list1 == list2).all()


#print(compare_sums_in_any_df(df1, df2))


