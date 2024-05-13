import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
from scipy.stats import chi2_contingency
import statsmodels
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import  train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support
import warnings
import os

a1 = pd.read_excel("case_study1.xlsx")
a2 = pd.read_excel("case_study2.xlsx")

df1 = a1.copy()
df2 = a2.copy()

print(df1.head())
print(df2.head())

#Remove nulls
df1 = df1.loc[df1['Age_Oldest_TL'] != -99999]

columns_to_be_removed = []
