from functions import *
import pandas as pd
import yaml

config = read_yaml(sys.path[0], "settings.yaml")
df1 = csv_to_df (config['SOURCE']['PATH'])
df2 = csv_to_df (config['TARGET']['PATH'])


list1 = df1.count()
list2 = df2.count()


return_df(config['SOURCE'])
