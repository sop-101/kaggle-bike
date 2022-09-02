from fileinput import filename
import os
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#importing data set
train = pd.read_csv('bike-sharing-demand/train.csv')
test = pd.read_csv('bike-sharing-demand/test.csv')

#print(train.head()) check to see if csv file has been read properly
