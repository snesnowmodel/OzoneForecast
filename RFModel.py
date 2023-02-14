import joblib
import numpy as np
import pandas as pd
import math
import os

current_directory = os.getcwd()
file_path=current_directory

##current 8 hour ozone observations in PPB
#Midlands=1000
#Upstate=1000
#CSRA=1000
#PeeDee=1000
#Catawba=1000
#Trident=1000

import sys

Midlands = float(sys.argv[1])
Upstate = float(sys.argv[2])
CSRA = float(sys.argv[3])
PeeDee = float(sys.argv[4])
Catawba = float(sys.argv[5])
Trident = float(sys.argv[6])

#METEOROLOGICAL DATA FILE IMPORTS
nbm = pd.read_csv(str(file_path)+'/data/nbmdata.csv')
nam = pd.read_csv(str(file_path)+'/data/namdata.csv')

#midlands Model Creation---------------------------------------------------


#STEP 1------------- PUT VARIABLES INTO DATAFRAME
midlandsdata=pd.DataFrame({'Prev': [Midlands/1000],
'925-U-Winds-18Z': [nam.iloc[22,1]],
'925-V-Winds-18Z': [nam.iloc[23,1]],
'Tdiff': [nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72],[3]].max()-nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72],[3]].min()],
'RH66': [nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73],[3]].mean()],
'CC93': [nbm.iloc[[21,27,33,39,45,51,57],[3]].mean()/10],
'925T-2M-18Z': [nam.iloc[20,1]-((nam.iloc[17,1]-32)*(5/9))],
'925-RH-18Z': [nam.iloc[21,1]],
'PWAT-18Z': [nam.iloc[29,1]]})

#STEP 2 --------------- RUN MODEL
model = joblib.load(str(file_path)+"/rfmodels/Midlands_annual.sav")
prediction=model.predict(midlandsdata)
prediction=prediction*1000
print("Midlands Ozone Forecast: ", prediction, "ppb")



#UPSTATE MODEL CREATION--------------------------------------------------

#STEP 1 ------------- PUT VARIABLES INTO DATAFRAME
Upstatedata=pd.DataFrame({'Prev': [Upstate/1000],
'Tdiff': [nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72],[4]].max()-nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72],[4]].min()],
'925T-2M-18Z': [nam.iloc[20,2]-((nam.iloc[17,2]-32)*(5/9))],
'CC66': [nbm.iloc[[3,9,15,21,27,33,39,45,51,57,63,69,75],[4]].mean()/10],
'925-U-Winds-12Z': [nam.iloc[7,2]],
'PWAT-18Z': [nam.iloc[29,2]],
'RH126': [nbm.iloc[[37,43,49,55,61,67,73],[4]].mean()],
'925-Speed-18Z': [math.sqrt(nam.iloc[18,2]**2 + nam.iloc[19,2]**2)],
'925-V-Winds-12Z': [nam.iloc[4,2]],
'850-Speed-18Z': [math.sqrt(nam.iloc[26,2]**2 + nam.iloc[27,2]**2)],
'PBL-height':[nam.iloc[30,2]]})

#STEP 2 ----------------RUN MODEL
model2 = joblib.load(str(file_path)+"/rfmodels/Upstate_annual.sav")
prediction2=model2.predict(Upstatedata)
prediction2=prediction2*1000
print("Upstate Ozone Forecast: ", prediction2, "ppb")


#CSRA MODEL CREATION ----------------------------------------------------

CSRAdata=pd.DataFrame({'Prev': [CSRA/1000],
'Lo': [nam.iloc[0,3]],
'TD/WS':[((nam.iloc[15,3]-nam.iloc[0,3])/nbm.iloc[[2,8,14,20,26,32,38,44,50,56,62,68,74],[5]].mean())],
'RH126': [nbm.iloc[[37,43,49,55,61,67,73],[5]].mean()],
'CC93': [nbm.iloc[[21,27,33,39,45,51,57],[5]].mean()/10],
'925T-2M-18Z': [nam.iloc[20,3]-((nam.iloc[17,3]-32)*(5/9))],
'925-Speed-18Z': [math.sqrt(nam.iloc[18,3]**2 + nam.iloc[19,3]**2)],
'925-RH-18Z': [nam.iloc[21,3]],
'850-V-Winds-18Z': [nam.iloc[27,3]],
'850-MB-Temp-18Z': [nam.iloc[24,3]],
'PWAT-18Z': [nam.iloc[29,3]]})

#STEP 2 ----------------RUN MODEL
model3 = joblib.load(str(file_path)+"/rfmodels/CSRA_annual.sav")
prediction3=model3.predict(CSRAdata)
prediction3=prediction3*1000
print("CSRA Ozone Forecast: ", prediction3, "ppb")


#PEE DEE MODEL CREATION
PeeDeedata=pd.DataFrame({'Prev': [PeeDee/1000],
'Tdiff': [nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72],[6]].max()-nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72],[6]].min()],
'Td/Ws':[((nam.iloc[15,4]-nam.iloc[0,4])/nbm.iloc[[2,8,14,20,26,32,38,44,50,56,62,68,74],[6]].mean())],
'RH Diff': [nbm.iloc[1,6]-nbm.iloc[46,6]],
'CC63': [nbm.iloc[[3,9,15,21,27,33,39,45,51,57],[6]].mean()/10],
'850-U-Winds-12Z': [nam.iloc[11,4]],
'2m-RH-18Z': [nam.iloc[17,4]],
'925T-2M-18Z': [nam.iloc[20,4]-((nam.iloc[15,4]-32)*(5/9))],
'850-Speed-18Z': [math.sqrt(nam.iloc[26,4]**2 + nam.iloc[27,4]**2)],
'850-MB-Temp-18Z': [nam.iloc[24,4]],
'PWAT-18Z': [nam.iloc[29,4]],
'PBL-height': [nam.iloc[30,4]]})

#STEP 2 ----------------RUN MODEL
model4 = joblib.load(str(file_path)+"/rfmodels/PeeDee_annual.sav")
prediction4=model4.predict(PeeDeedata)
prediction4=prediction4*1000
print("PeeDee Ozone Forecast: ", prediction4, "ppb")

#CATAWBA MODEL CREATION ------------------------------------------------

#STEP 1 ------------- PUT VARIABLES INTO DATAFRAME

Catawbadata=pd.DataFrame({'Prev': [Catawba/1000],
'RH126': [nbm.iloc[[37,43,49,55,61,67,73],[7]].mean()],
'2M-TMP-C-12Z': [(nam.iloc[0,5]-32)*(5/9)],
'925-U-WIND-12Z': [nam.iloc[7,5]],
'925-V-WIND-12Z': [nam.iloc[8,5]],
'925-MB-T-12Z': [nam.iloc[5,5]-((nam.iloc[0,5]-32)*(5/9))],
'PWAT-18Z': [nam.iloc[29,5]],
'925-U-WIND-18Z': [nam.iloc[22,5]],
'850-SFCWind':[(math.sqrt(math.sqrt(nam.iloc[26,5]**2 + nam.iloc[27,5]**2))+math.sqrt(math.sqrt(nam.iloc[22,5]**2 + nam.iloc[23,5]**2))+math.sqrt(math.sqrt(nam.iloc[18,5]**2 + nam.iloc[18,5]**2)))/3]})

#STEP 2 ----------------RUN MODEL
model5 = joblib.load(str(file_path)+"/rfmodels/Catawba_annual.sav")
prediction5=model5.predict(Catawbadata)
prediction5=prediction5*1000
print("Catawba Ozone Forecast: ", prediction5, "ppb")

#TRIDENT MODEL CREATION ------------------------------------------------

Tridentdata=pd.DataFrame({'Prev': [Trident/1000],
'Tdiff': [nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72],[8]].max()-nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72],[8]].min()],
'RH912': [nbm.iloc[[19,25,31,37],[8]].mean()],
'PBL-height': [nam.iloc[30,6]],
'925-V-Winds-18Z': [nam.iloc[23,6]],
'925T-2M-12Z': [nam.iloc[5,6]-((nam.iloc[0,6]-32)*(5/9))],
'850-U-Winds-12Z': [nam.iloc[11,6]],
'850-V-Winds-12Z': [nam.iloc[12,6]],
'850-MB-Temp-18Z': [nam.iloc[9,6]],
'2m-RH-18Z': [nam.iloc[17,6]],
'925-RH-18Z': [nam.iloc[21,6]],
'PWAT-18Z': [nam.iloc[29,6]]})

#STEP 2 ----------------RUN MODEL
model6 = joblib.load(str(file_path)+"/rfmodels/Trident_annual.sav")
prediction6=model6.predict(Tridentdata)
prediction6=prediction6*1000
print("Trident Ozone Forecast: ", prediction6, "ppb")


import tkinter as tk
import tkinter.ttk as ttk
import subprocess

# Create the GUI window
root = tk.Tk()
root.title("Ozone Forecast")

# Create a label to display the forecast
label = tk.Label(root, text="Midlands Ozone Forecast: {:.2f} ppb".format(prediction[0]), font=("Arial", 16))
label.pack()
label2 = tk.Label(root, text="Upstate Ozone Forecast: {:.2f} ppb".format(prediction2[0]), font=("Arial", 16))
label2.pack()
label3 = tk.Label(root, text="CSRA Ozone Forecast: {:.2f} ppb".format(prediction3[0]), font=("Arial", 16))
label3.pack()
label4 = tk.Label(root, text="Pee Dee Ozone Forecast: {:.2f} ppb".format(prediction4[0]), font=("Arial", 16))
label4.pack()
label5 = tk.Label(root, text="Catawba Ozone Forecast: {:.2f} ppb".format(prediction5[0]), font=("Arial", 16))
label5.pack()
label6 = tk.Label(root, text="Trident Ozone Forecast: {:.2f} ppb".format(prediction6[0]), font=("Arial", 16))
label6.pack()
root.mainloop()

Forecast=pd.DataFrame({'Region': ['Midlands', 'Upstate', 'CSRA', 'Pee Dee', 'Catawba', 'Trident'], 'Forecast': [prediction[0], prediction2[0], prediction3[0], prediction4[0], prediction5[0], prediction6[0]]})

import datetime
import time

now=datetime.date.today()

delta = datetime.timedelta(days=1)

today = int(now.strftime("%Y%m%d"))
prev=now - delta
yesterday = int(prev.strftime("%Y%m%d"))

nexted = now + delta
tomorrow = int(nexted.strftime("%Y%m%d"))

Forecast.to_csv(str(file_path)+'/data/ozoneforecast_' +str(tomorrow) + '.csv')
