import pandas as pd
from datetime import time, datetime
import os
import numpy as np
from pathlib import Path


def read_general_sheet(file_path: Path, out_path: Path):
    cols_dict = {'time_period_start': np.datetime64,
                 'time_period_end': np.datetime64,
                 'wind_direction_degree': np.int32,
                 'wind_speed_kt': np.int32,
                 'swell_direction_degree': np.int32,
                 'swell_height_m': np.int32,
                 'seascale_beaufort_scale': np.int32,
                 'current_direction_degree': np.int32,
                 'current_speed_kt': np.float64,
                 'draft_fwd_m': np.float64,
                 'draft_aft_m': np.float64,
                 'mean_draft_m': np.float64,
                 'trim_m': np.float64,
                 'ballast_quantity_cbm': np.float64,
                 '_ttl_displacement_mt': np.float64,
                 'remarks': str}

    numeric_cols = ['wind_direction_degree',
                    'wind_speed_kt',
                    'swell_direction_degree',
                    'swell_height_m',
                    'seascale_beaufort_scale',
                    'current_direction_degree',
                    'current_speed_kt',
                    'draft_fwd_m',
                    'draft_aft_m',
                    'mean_draft_m',
                    'trim_m',
                    'ballast_quantity_cbm',
                    '_ttl_displacement_mt']

    # reading the excel file
    df = pd.read_excel(file_path, sheet_name='Daily general',
                       names=cols_dict.keys()
                       )

    # drop all empty columns
    df = df.dropna(axis=1, how='all').dropna()

    # filter the initial dictionary after dropping null values
    cols_dict = {col: cols_dict[col] for col in df.columns if col in cols_dict}

    # convert all cols to a str datatype
    df = df.astype(str)

    # cast each numeric column to its datatype. Note: with 'coerce' invalid parsing will be set as NaN.
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # drop all empty columns
    df = df.dropna()

    # cast each datatype
    df.astype(cols_dict).to_csv(out_path, index=False)
