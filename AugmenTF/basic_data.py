# AUTOGENERATED! DO NOT EDIT! File to edit: dev/01_basic_data.ipynb (unless otherwise specified).

__all__ = ['make_dataset_from_df', 'make_dataset_from_csv']

# Cell
from .core import *
import tensorflow as tf
from tensorflow import data
import pandas as pd

# Cell
def make_dataset_from_df(df):
    '''
    Returns a tf.data.Dataset.

    Options:

    df: a pandas.DataFrame

    Returns:

    A tf.data.Dataset
    '''

    return data.Dataset.from_tensor_slices(df.to_dict(orient='series'))

# Cell
def make_dataset_from_csv(csv_path):
    '''
    Returns a tf.data.Dataset.

    Options:

    csv_path: str or Path of the CSV you want to load.

    Returns:

    A tf.data.Dataset
    '''
    return make_dataset_from_df(pd.read_csv(csv_path))