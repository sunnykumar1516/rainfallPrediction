import yaml
import os
import pandas as pd

print("current directory:--",os.getcwd())
path = "params.yaml"
params=yaml.safe_load(open(path))['preprocess']
data = pd.read_csv(params['input'])

# dropping columns
columns_to_drop = ["Date","Evaporation","Sunshine","Cloud9am","Cloud3pm","Location","WindGustDir","WindDir9am","WindDir9am","WindDir3pm"]
data.drop(columns=columns_to_drop, inplace=True)


# removing na
data = data.dropna(axis=0)

#saving cleaned data
data.to_csv(params['output'])

