
#importing useful libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib as mpl
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import warnings
import pickle
warnings.filterwarnings("ignore")


"This is a file that contains a set of functions that can be helpful in preprocessing EHRs before passing them to Machine Learning Models."

def import_data(file):
    """ This function reads a file in csv format and stores it in a dataframe to be used for preprocessing"""
    df = pd.read_csv(file, parse_dates=True, keep_date_col=True)
    return df



def impute_missing(df):

    """ This function detects all missing values and imputes them with the Median of the column each missing value belongs to. """

    df=df[df.columns].fillna(df[df.columns].median())
    return(df)


def check_plausible(df):

    """ This function utilizes the Plauible data dictionry to detect all implausible values  and imputes them with Median """
    """For this function work properly, the columns in the dataframe and the plauible data dictionary should be sorted in the same order """
    """df: a dataframe that only contains the numerical values that you would like to check for implauible values"""


    for column in df:
        df[column] = df[column].mask(~(df[column] >= plausible_values[column][0]) & (df[column] <=  plausible_values[column][1]) , df[column].median())
    return(df)

def capitalization_fix(df, to_encode):
    """ A common issue in medical records is having inconsistant capitalization. This kind of inconsistancy can lead to errors and inacuracy in later stages in the model training. """
    """This function unifies the capitalization case of all the entries in categorical columns of the passed dataframe  """
    """df: a dataframe that contains categorical columns"""
    """ to_encode:is a list of (strings) the names of the columns that you like to unify the capitalization case """

    for c in to_encode:
        df[c] = df[c].str.lower()
    return(df)


def One_hot_encode(df,col_list):
    """This function encodes categorical columns using one hot encoding."""
    """It's important to note the one hot encoding adds new columns to the dataframe and then drops the origional column."""
    """df: The full dataframe containing the EHR"""
    """ col_list :is a list of (strings) the names of the columns that you like to apply one hot encoding to """

    df_to_encode = pd.get_dummies(df[col_list])
    df = pd.concat([df,df_to_encode], axis=1)
    df= df.drop(col_list, axis =1)
    return(df)

def Label_encode(df, col):
        """This function encodes categorical columns using Label encoding encoding."""
        """df: The full dataframe containing the EHR"""
        """ col :is a list of (strings) the names of the columns that you like to apply label Encoding to """
        df[col] = df[col].astype(str)
        df[col] = LabelEncoder().fit_transform(df[col])
        return(df)


def diagnosis_codes_encode(df):
    """ This function applies one hot encoding to the column that includes diagnosis codes. This function then adds a prefix to each of the one hot encoded columns to help identify them in later stages."""
    """Here, the dignosis codes are stored in a column called 'diagnosis code'."""
    diagnosis_cols = pd.get_dummies(df['Diagnosis code']).add_prefix('Diagnosis code: ')
    df = pd.concat([df, diagnosis_cols ], axis=1)
    df= df.drop('Diagnosis code', axis =1)
    return(df)

def group_age(df):
        """ This function adds a new column "" to the dataframe that shows what age group does each patient belong to."""
        """ seperating age by group can be usefull to understand the model performance based on the age group """
        df['age_by_range'] = pd.cut(x=df['Age'], bins=[16, 45, 60,99],labels= ['16-45', '46-60', '60+'])
        return(df)

def add_clincial_indicators(df):
    """This is a function that demonstates an example of features engineering for the clinical field. Based on the data in hand, different clinical indicators and features can be extracted and added to the data to give usefull insights based on medical Litrature. """
    """Here we show an example of extracting the stroke volume,and the Body Surface Area"""
    """Please change the names of the columns to match those availabe in your dataset."""
    """
    """

    sysbp = (df.Systolic_blood_pressure_min+ df.Systolic_blood_pressure_max)/2
    diastolic = (df.Diastolic_blood_pressure_max + df.Diastolic_blood_pressure_min)/2

    df['cardiac_output']= heart_rate* (sysbp-diastolic)
    df['stroke volume']= (sysbp-diastolic)
    df['bsa']= np.sqrt((df.Height*df.Weight/3600))
    df['stroke index']= df['stroke volume']/df['bsa']

    return(df)



def export_data(df):
    """This function handles exporting data to a pkl file."""
    df.to_pickle("prepared.pkl")
    return(df)
