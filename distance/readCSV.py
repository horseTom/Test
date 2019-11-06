import pandas as pd
import numpy as np

def read_csv(path):
    df = pd.read_csv(path, header=None, sep='', names=["f_lat (纬度)","f_lng (经度)"])
    print(df)

path = 'C:\WorkSpace\\166028982_origin.csv'
read_csv(path)