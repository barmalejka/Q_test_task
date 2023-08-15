import argparse

import pandas as pd
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, required=True)

args = parser.parse_args()

filename = args.filename

df = pd.read_csv(filename)
df['preds'] = df['6']**2 + df['7']

df['preds'].to_csv('preds.csv', index=False)