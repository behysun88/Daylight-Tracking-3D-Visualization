import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns
import csv as csv

#Data Pre-processing and importing info from the spreadsheet collected 
#through the data logging system, Arduino
#header = csv.reader('Experiment')
#
#fname = 'Experiment.csv'
#data = pd.read_csv(fname)
##First Column time of the day
#daytime = data.values[:, :1]
##Second Column vertical position
#vertical = data.values[:, 1:2]
##Third column horizental position
#horizental = data.values[:,2:3]
#fig = plt.figure(figsize = (6,4))
#
#xs = horizental
#ys = vertical
#zs = daytime
#
#ax = fig.add_subplot(111, projection = '3d')
#ax.scatter(xs, ys, zs, s=50, alpha=0.6, edgecolors='w')
#ax.set_xlabel('Vertical Vertical')
#ax.set_ylabel('Horizental Max')
#ax.set_zlabel('Day - 24 Hours')
def load_data():
    header = csv.reader('Experiment')
    
    fname = 'Experiment.csv'
    data = pd.read_csv(fname)
    #First Column time of the day
    daytime = data.values[:, :1]
    #Second Column vertical position
    vertical = data.values[:, 1:2]
    #Third column horizental position
    horizental = data.values[:,2:3]
    fig = plt.figure(figsize = (12,8))
    
    xs = horizental
    ys = vertical
    zs = daytime
    
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(xs, zs, ys,  s=300, alpha=1.0)   # there are different setting for scatter plot look it up
    ax.set_xlabel('Horizental Position')
    ax.set_ylabel('Day - 24 Hours')
    ax.set_zlabel('Vertical Position')

if __name__ == '__main__':
    
    load_data()
