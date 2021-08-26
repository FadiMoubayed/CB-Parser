import numpy as np
import pandas as pd
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


# Providing file info

# Providing the file name
file_name = "TestCB.XLSX"
# providing the file relative path
# Is this a good way to provide that file path or should I use os.path.relpath??
file_path = './Excel_Files/' + file_name

# Providing column names
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

cols_dict = {'Date/Time (UTC)': np.datetime64,
             'Latitude': str,
             'Longitude': str,
             'SO2_content_EG_EGC-Tower_outlet': np.float64,
             'CO2_content_EG_EGC-Tower_outlet': np.float64,
             'SO2/CO2_ratio': np.float64,
             'Flow_CEMS': np.float64,
             'Flow_water_monitor_in': np.float64,
             'Flow_water_monitor_out': np.float64,
             'pH-value_wash_water_EGC-Tower_inlet': np.float64,
             'pH-value_wash_water_EGC-Tower_outlet': np.float64,
             'pH-value_wash_water_discharge': np.float64,
             'pH-value_wash_water_Closed Loop': np.float64,
             'pH-value_wash_water_outboard': np.float64,
             'pH_Alarm_Threshold': np.float64,
             'Turbidity_wash_water_EGC-Tower_inlet': np.float64,
             'Turbidity_wash_water_EGC-Tower_outlet': np.float64,
             'PAH-value_wash_water_EGC-Tower_inlet': np.float64,
             'PAH-value_wash_water_EGC-Tower_inlet_corr': np.float64,
             'PAH-value_wash_water_EGC-Tower_outlet': np.float64,
             'PAH-value_wash_water_EGC-Tower_outlet_corr': np.float64,
             'Temp._wash_water_EGC-Tower_inlet': np.float64,
             'Temp._wash_water_EGC-Tower_outlet': np.float64,
             'Temperature_EG_EGC-Tower_inlet': np.float64,
             'Temperature_EG_EGC-Tower_outlet': np.float64,
             'Temperature_EG_quench_outlet': np.float64,
             'Pressure_Exh._Gas_EGC-Tower_inlet': np.float64,
             'Differential_pressure_exhaust_gas_EGC-Tower': np.float64,
             'Flow_wash_water': np.float64,
             'Flow_wash_water_quench_inlet': np.float64,
             'Press._wash_water_EGC-Tower_inlet': np.float64,
             'Pressure_Outlet_Pipe': np.float64,
             'Load_E1': np.float64,
             'Load_E2': np.float64,
             'Load_E3': np.float64,
             'Load_E4': np.float64,
             'Conductivity': np.int32,
             'Temp._wash_water_after_cooler': np.float64,
             'Flow_NaOH': np.float64,
             'Temperature_NaOH_tank': np.float64,
             'Filling_level_NaOH_tank': np.float64,
             'Filling_level_buffer_tank': np.float64,
             'Filling_level_storage_tank': np.float64,
             'Filling_level_process_tank': np.float64,
             'Cur._value_(X)_ctrl._1_sea_water_pump': np.float64,

             'Output_(Y)_ctrl._1_sea_water_pump': np.int32,

             'Cur._setpoint_(W)_ctrl._1_sea_water_pump': np.float64,
             'Cur._value_(X)_ctrl._2_sea_water_pump': np.float64,
             'Output_(Y)_ctrl._2_sea_water_pump': np.float64,
             'Cur._setpoint_(W)_ctrl._2_sea_water_pump': np.float64,
             'Cur._value_(X)_ctrl._1_dosing_pump': np.float64,
             'Output_(Y)_ctrl._1_dosing_pump': np.float64,
             'Cur._setpoint_(W)_ctrl._1_dosing_pump': np.float64,
             'Cur._value_(X)_ctrl._2_dosing_pump': np.float64,
             'Output_(Y)_ctrl._2_dosing_pump': np.float64,
             'Cur._setpoint_(W)_ctrl._2_dosing_pump': np.float64,
             'Cur._value_(X)_ctrl._ww_discharge_pipe': np.float64,
             'Output_(Y)_ctrl._ww_discharge_pipe': np.float64,
             'Cur._setpoint_(W)_ctrl._ww_discharge_pipe': np.float64,

             'Cur._value_(X)_ctrl._conductivity_CL': np.int32,

             'Output_(Y)_ctrl._conductivity_CL': np.float64,

             'Cur._setpoint_(W)_ctrl._conductivity_CL': np.int32,

             'Cur._value_(X)_ctrl._quench_outlet': np.float64,
             'Output_(Y)_ctrl._quench_outlet': np.float64,

             'Cur._setpoint_(W)_ctrl._quench_outlet': np.int32,

             'Difference_turbidity': np.float64,
             'Difference_PAH': np.float64,

             'QAutoModeActive': np.int32,
             'QCloseLoopActive': np.int32,
             'QCommonAlarm': np.int32,
             'QPerformanceError': np.int32,
             'ICommonAlarmCEMS': np.int32,
             'ILevelScrubberTooHigh': np.int32,
             'QLowAlkalinityModeActive': np.int32,
             'IValveExhGasTrain_1_BypassClose': np.int32,
             'IValveExhGasTrain_1_DamperOpen': np.int32,
             'IExhGasTrain_1_InOperation': np.int32,
             'IValveExhGasTrain_2_BypassClose': np.int32,
             'IValveExhGasTrain_2_DamperOpen': np.int32,
             'IExhGasTrain_2_InOperation': np.int32,
             'IValveExhGasTrain_3_BypassClose': np.int32,
             'IValveExhGasTrain_3_DamperOpen': np.int32,
             'IExhGasTrain_3_InOperation': np.int32,
             'IValveExhGasTrain_4_BypassClose': np.int32,
             'IValveExhGasTrain_4_DamperOpen': np.int32,
             'IExhGasTrain_4_InOperation': np.int32,
             'IWWMonitorInletFlowMin': np.int32,
             'IWWMonitorOutletFlowMin': np.int32,
             'IWWMonitorCLFlowMin': np.int32,
             'IWWMonitorDischargeFlowMin': np.int32,
             'ISeaWaterPump1InOperation': np.int32,
             'ISeaWaterPump2InOperation': np.int32,
             'IBoostPump1InOperation': np.int32,
             'ICirculationPump1InOperation': np.int32,
             'ISealingAirFan1InOperation': np.int32,
             'IDosingPump_1_InOperation': np.int32,
             'IDosingPump_2_InOperation': np.int32,
             'ISeparator1InOperation': np.int32,
             'ISeparator1Fault': np.int32,
             'IBleedOffValve1ToBufferTank': np.int32,
             'IBleedOffPumpInOperation': np.int32,
             'IBufferTankDischToShoreClosed': np.int32,
             'IStoragePumpInOperation': np.int32,
             'INaOHDosingToEgcsInletOpen': np.int32,
             'INaOHDosingToEgcsOutletOpen': np.int32,
             'QReleaseLevelDischargePipeUSVGP': np.int32,
             'IWWMonitorInletStatusPH': np.int32,
             'IWWMonitorOutletStatusPH': np.int32,
             'IWWMonitorCLStatusPH': np.int32,
             'IWWMonitorDischargeStatusPH': np.int32,
             'IPosOpActiveSeaWaterPumpCtrl1': np.int32,
             'QStatusReleaseSeaWaterPumpCtrl1': np.int32,
             'QStatusReleaseSeaWaterPumpCtrl2': np.int32,
             'IPosOpActiveDosingPumpCtrl1': np.int32,
             'QStatusReleaseDosingPumpCtrl1': np.int32,
             'QStatusReleaseDosingPumpCtrl2': np.int32,
             'QStatusReleaseLevelDischargePipe': np.int32,
             'QStatusReleaseConductivityCtrlCL': np.int32,
             'QStatusReleaseTempQuenchOutlet': np.int32,
             }

# Reading the excel file. openpyxl is used because the file has an .xlsx extension
df = pd.read_excel(file_path, sheet_name='TestCB', engine='openpyxl', names=col_names)

# Converting the Latitude column to DD
df['Latitude'] = df['Latitude'].apply(convert_ddm_to_dd)

# Converting the Longitude column to DD
df['Longitude'] = df['Longitude'].apply(convert_ddm_to_dd)

# lat_col = df.loc[:, "Latitude"]
# print(lat_col)
#
# lon_col = df.loc[:, "Longitude"]
# print(lon_col)


lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

print(haversine(lyon, paris))


# printing each column's type
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df.dtypes)

# Getting the first datetime element

#print(df.iloc[:,0])



