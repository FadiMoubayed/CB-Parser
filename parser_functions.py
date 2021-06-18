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
                       names=cols_dict.keys())

    # drop all empty columns
    df = df.dropna(axis=1, how='all').dropna(subset=['time_period_start', 'time_period_end'])
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # filter the initial dictionary after dropping null values
    cols_dict = {col: cols_dict[col] for col in df.columns if col in cols_dict}

    # convert all columns to a str datatype
    df = df.astype(str)

    # cast each numeric column to its datatype. Note: with 'coerce' invalid parsing will be set as NaN.
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # drop all nan values
    df = df.dropna()

    # cast each datatype and save to csv file
    df.astype(cols_dict).to_csv(out_path, index=False)


def read_events_sheet(file_path: Path, out_path: Path):
    # skipping header rows
    skiprows = [0, 1, 2, 3, 4]

    # extract relevant columns
    usecols = [0, 1, 3, 4, 6, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22,
               23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
               35, 36, 37, 38, 39, 40, 41, 42]

    # setting a name for each selected column
    usecols_names = ['Date', 'time', 'Voy. Number', 'from', 'to', 'eventCode', 'eventName',
                     'latDeg', 'latMin', 'northSouth', 'lonDeg', 'lonMin', 'eastWest', 'WindForce(bft)',
                     'Miles sailed (NM)',
                     'Cargo On Board (MT)', 'MainEngine HFO (mt)', 'MainEngine LFO (mt)', 'MainEngine MGO/DO (mt)',
                     'Aux.Engine HFO (mt)', 'Aux.Engine LFO (mt)', 'Aux.Engine MGO/DO (mt)',
                     'Boiler Consumption HFO (mt)', 'Boiler Consumption LFO (mt)', 'Boiler Consumption MGO/DO (mt)',
                     'IG Consumption HFO (mt)', 'IG Consumption LFO (mt)', 'IG Consumption MGO/DO (mt)',
                     'Bunkers Received HFO (mt)', 'Bunkers Received LFO (mt)', 'Bunkers Received MGO/DO (mt)',
                     'Total consumption HFO (mt)', 'Total consumption LFO (mt)', 'Total consumption MGO/DO (mt)',
                     'ROB Consumption HFO (mt)', 'ROB Consumption LFO (mt)', 'ROB Consumption MGO/DO (mt)']

    # read the sheet using above settings
    df = pd.read_excel(file_path, sheet_name='Events', skiprows=skiprows, keep_default_na=False, na_values='',
                       usecols=usecols, names=usecols_names)

    # fill consumption fields with 0 values while engine is off
    df[usecols_names[14:]] = df[usecols_names[14:]].fillna(0)

    # drop rows having no timestamp or location
    df = df.dropna(subset=['Date', 'time', 'latDeg', 'latMin', 'northSouth', 'lonDeg', 'lonMin', 'eastWest'])
    df = df[df['time'].astype(str).map(len) <= 8]

    # create a timestamp row by combining date and time
    df.insert(loc=0, column='dateTime',
              value=df.apply(lambda col: datetime.combine(col.Date, time.fromisoformat(str(col.time))), axis=1))

    # convert longitude from DDM to DD  using (lon° + min'/60 ) * -1/1 for W/E
    df.insert(loc=1, column='longitude',
              value=df.apply(lambda col: (col.lonDeg + col.lonMin / 60) * (-1 if col.eastWest == 'W' else 1),
                             axis=1))

    # convert latitude from DDM to DD  using (lat° + min'/60 ) * -1/1 for S/N
    df.insert(loc=2, column='latitude',
              value=df.apply(lambda col: (col.latDeg + col.latMin / 60) * (-1 if col.northSouth == 'S' else 1),
                             axis=1))

    # drop original columns and save to csv file
    df.drop(['Date', 'time', 'latDeg', 'latMin', 'northSouth', 'lonDeg', 'lonMin', 'eastWest'], axis=1).to_csv(
        out_path,
        index=False)


if __name__ == '__main__':
    cb_folder = 'CB'  # the root folder for the Excel files
    for root, dirs, files in os.walk(cb_folder):
        for file in files:
            file_path = Path(root, file)

            # read events sheet
            read_events_sheet(file_path, Path('events_' + file_path.stem + '.csv'))

            # read general sheet
            read_general_sheet(file_path, Path('general_' + file_path.stem + '.csv'))
            print(file_path)
