from numpy import array,sqrt, argsort, std
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from matplotlib.pyplot import figure
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import *
from sklearn.tree import *
from sklearn.ensemble import *
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.model_selection import RandomizedSearchCV,GridSearchCV
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
dataset=pd.read_csv("C:\\Users\\86183\\Desktop\\数模校赛\\C题附件.csv")

dataset=dataset.drop_duplicates()
dataset.shape
dataset.columns = dataset.columns.str.lstrip()
dataset.columns
dataset=dataset.drop(['url','timedelta'],axis=1)
pd.set_option("display.max_rows", None, "display.max_columns", None)
dataset.head()

dataset=dataset.dropna()
dataset.shape

dataset.describe()

figure(num=None, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
corr = dataset.corr()
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
plt.show()