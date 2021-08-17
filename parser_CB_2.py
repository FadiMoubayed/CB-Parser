import sys

import pandas as pd
from datetime import time, datetime
import os
import numpy as np
from pathlib import Path
import re
from haversine import haversine, Unit


# TODO: name this file properly. What is the difference between this file the other CB files?

# TODO: Make sure that coordinates do not have seconds

# This function converts coordinates from Degrees Decimal Minutes (DDM) to Decimal Degrees (DD)
def convert_ddm_to_dd(ddm):
    # Splitting the string to deg, minute and direction
    deg, minutes, direction = re.split('[°\'"]', ddm)
    # Calculating latitude in degrees
    dd = (float(deg) + float(minutes) / 60) * (-1 if direction in ['W', 'S'] else 1)
    return dd


# TODO: name this function properly
def read_cb_xlsx(file_path: Path, file_path_out: Path):
    # Providing column names as a list
    col_names = ['Date/Time (UTC)',
                 'Latitude',
                 'Longitude',
                 'SO2_content_EG_EGC-Tower_outlet',
                 'CO2_content_EG_EGC-Tower_outlet',
                 'SO2/CO2_ratio',
                 'Flow_CEMS',
                 'Flow_water_monitor_in',
                 'Flow_water_monitor_out',
                 'pH-value_wash_water_EGC-Tower_inlet',
                 'pH-value_wash_water_EGC-Tower_outlet',
                 'pH-value_wash_water_discharge',
                 'pH-value_wash_water_Closed Loop',
                 'pH-value_wash_water_outboard',
                 'pH_Alarm_Threshold',
                 'Turbidity_wash_water_EGC-Tower_inlet',
                 'Turbidity_wash_water_EGC-Tower_outlet',
                 'PAH-value_wash_water_EGC-Tower_inlet',
                 'PAH-value_wash_water_EGC-Tower_inlet_corr',
                 'PAH-value_wash_water_EGC-Tower_outlet',
                 'PAH-value_wash_water_EGC-Tower_outlet_corr',
                 'Temp._wash_water_EGC-Tower_inlet',
                 'Temp._wash_water_EGC-Tower_outlet',
                 'Temperature_EG_EGC-Tower_inlet',
                 'Temperature_EG_EGC-Tower_outlet',
                 'Temperature_EG_quench_outlet',
                 'Pressure_Exh._Gas_EGC-Tower_inlet',
                 'Differential_pressure_exhaust_gas_EGC-Tower',
                 'Flow_wash_water',
                 'Flow_wash_water_quench_inlet',
                 'Press._wash_water_EGC-Tower_inlet',
                 'Pressure_Outlet_Pipe',
                 'Load_E1',
                 'Load_E2',
                 'Load_E3',
                 'Load_E4',
                 'Conductivity',
                 'Temp._wash_water_after_cooler',
                 'Flow_NaOH',
                 'Temperature_NaOH_tank',
                 'Filling_level_NaOH_tank',
                 'Filling_level_buffer_tank',
                 'Filling_level_storage_tank',
                 'Filling_level_process_tank',
                 'Cur._value_(X)_ctrl._1_sea_water_pump',
                 'Output_(Y)_ctrl._1_sea_water_pump',
                 'Cur._setpoint_(W)_ctrl._1_sea_water_pump',
                 'Cur._value_(X)_ctrl._2_sea_water_pump',
                 'Output_(Y)_ctrl._2_sea_water_pump',
                 'Cur._setpoint_(W)_ctrl._2_sea_water_pump',
                 'Cur._value_(X)_ctrl._1_dosing_pump',
                 'Output_(Y)_ctrl._1_dosing_pump',
                 'Cur._setpoint_(W)_ctrl._1_dosing_pump',
                 'Cur._value_(X)_ctrl._2_dosing_pump',
                 'Output_(Y)_ctrl._2_dosing_pump',
                 'Cur._setpoint_(W)_ctrl._2_dosing_pump',
                 'Cur._value_(X)_ctrl._ww_discharge_pipe',
                 'Output_(Y)_ctrl._ww_discharge_pipe',
                 'Cur._setpoint_(W)_ctrl._ww_discharge_pipe',
                 'Cur._value_(X)_ctrl._conductivity_CL',
                 'Output_(Y)_ctrl._conductivity_CL',
                 'Cur._setpoint_(W)_ctrl._conductivity_CL',
                 'Cur._value_(X)_ctrl._quench_outlet',
                 'Output_(Y)_ctrl._quench_outlet',
                 'Cur._setpoint_(W)_ctrl._quench_outlet',
                 'Difference_turbidity',
                 'Difference_PAH',
                 'QAutoModeActive',
                 'QCloseLoopActive',
                 'QCommonAlarm',
                 'QPerformanceError',
                 'ICommonAlarmCEMS',
                 'ILevelScrubberTooHigh',
                 'QLowAlkalinityModeActive',
                 'IValveExhGasTrain_1_BypassClose',
                 'IValveExhGasTrain_1_DamperOpen',
                 'IExhGasTrain_1_InOperation',
                 'IValveExhGasTrain_2_BypassClose',
                 'IValveExhGasTrain_2_DamperOpen',
                 'IExhGasTrain_2_InOperation',
                 'IValveExhGasTrain_3_BypassClose',
                 'IValveExhGasTrain_3_DamperOpen',
                 'IExhGasTrain_3_InOperation',
                 'IValveExhGasTrain_4_BypassClose',
                 'IValveExhGasTrain_4_DamperOpen',
                 'IExhGasTrain_4_InOperation',
                 'IWWMonitorInletFlowMin',
                 'IWWMonitorOutletFlowMin',
                 'IWWMonitorCLFlowMin',
                 'IWWMonitorDischargeFlowMin',
                 'ISeaWaterPump1InOperation',
                 'ISeaWaterPump2InOperation',
                 'IBoostPump1InOperation',
                 'ICirculationPump1InOperation',
                 'ISealingAirFan1InOperation',
                 'IDosingPump_1_InOperation',
                 'IDosingPump_2_InOperation',
                 'ISeparator1InOperation',
                 'ISeparator1Fault',
                 'IBleedOffValve1ToBufferTank',
                 'IBleedOffPumpInOperation',
                 'IBufferTankDischToShoreClosed',
                 'IStoragePumpInOperation',
                 'INaOHDosingToEgcsInletOpen',
                 'INaOHDosingToEgcsOutletOpen',
                 'QReleaseLevelDischargePipeUSVGP',
                 'IWWMonitorInletStatusPH',
                 'IWWMonitorOutletStatusPH',
                 'IWWMonitorCLStatusPH',
                 'IWWMonitorDischargeStatusPH',
                 'IPosOpActiveSeaWaterPumpCtrl1',
                 'QStatusReleaseSeaWaterPumpCtrl1',
                 'QStatusReleaseSeaWaterPumpCtrl2',
                 'IPosOpActiveDosingPumpCtrl1',
                 'QStatusReleaseDosingPumpCtrl1',
                 'QStatusReleaseDosingPumpCtrl2',
                 'QStatusReleaseLevelDischargePipe',
                 'QStatusReleaseConductivityCtrlCL',
                 'QStatusReleaseTempQuenchOutlet',
                 ]

    # Reading the excel file. openpyxl is used because the file has an .xlsx extension
    df = pd.read_excel(file_path, sheet_name='TestCB', engine='openpyxl', names=col_names)

    # Converting the Latitude column to DD
    df['Latitude'] = df['Latitude'].apply(convert_ddm_to_dd)

    # Converting the Longitude column to DD
    df['Longitude'] = df['Longitude'].apply(convert_ddm_to_dd)

    df.to_csv(file_path_out, index=False)


if __name__ == '__main__':
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if file.endswith('.XLSX'):
                output_folder = Path(Path(__file__).parent, 'parsed_xlsx')
                output_folder.mkdir(exist_ok=True)

                file_path = Path(root, file)

                # read and combine consumption and general sheets
                read_cb_xlsx(file_path, Path(output_folder, 'TestCB' + file_path.stem + '.csv'))

                print(file_path)
