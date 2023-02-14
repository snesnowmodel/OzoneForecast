import urllib.request
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

import os

current_directory = os.getcwd()
file_path=current_directory

nbm = pd.read_csv(str(file_path)+'/data/nbmdata.csv')

MidlandsTemp= nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72,78],[3]]
MidlandsRH = nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73,79],[3]]
MidlandsWS = nbm.iloc[[2,8,14,20,26,32,38,44,50,56,62,68,74,80],[3]]
MidlandsWD = nbm.iloc[[5,11,17,23,29,35,41,47,53,59,65,71,77,83],[3]]

MidlandsWS=MidlandsWS.reset_index(drop=True)
MidlandsWD=270-MidlandsWD.reset_index(drop=True)
u =MidlandsWS.iloc[:,0]*np.cos(np.deg2rad(MidlandsWD.iloc[:,0]))
v = MidlandsWS.iloc[:,0] * np.sin(np.deg2rad(MidlandsWD.iloc[:,0]))


MidlandsCC = nbm.iloc[[3,9,15,21,27,33,39,45,51,57,63,69,75,81],[3]]
MidlandsPrecip = nbm.iloc[[4,10,16,22,28,34,40,46,52,58,64,70,76,82],[3]]
nbm.iloc[:,2]=pd.to_datetime(nbm.iloc[:,2])
Timeofday=nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73,79],[2]]
#Day=nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73,79],[1]]

nbm.set_index(nbm.iloc[:,2], inplace=True)
print(Timeofday)



import datetime
#Todays Date Variable
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)


#Subplots for the Midlands

fig, axs = plt.subplots(5, figsize=(15,15))
fig.subplots_adjust(hspace=1, wspace=1)
fig.suptitle(f"Meteogram for Sandhills: {tomorrow.strftime('%Y-%m-%d')}", y=1.05)

axs[0].plot(Timeofday.iloc[:,0], MidlandsTemp.iloc[:,0], color='red')
axs[0].set_title('Temperature ºF')
axs[0].set_ylim(MidlandsTemp.iloc[:,0].min()-10,MidlandsTemp.iloc[:,0].max()+10)
axs[0].fill_between(Timeofday.iloc[:,0], MidlandsTemp.iloc[:,0], 0, color='red', alpha=.1)
for i, txt in enumerate(np.around(MidlandsTemp.iloc[:,0],0)):
    axs[0].annotate(txt, (Timeofday.iloc[i,0], MidlandsTemp.iloc[i,0]), fontsize=16, color='red', ha='center', va='bottom')

axs[1].plot(Timeofday.iloc[:,0], MidlandsRH.iloc[:,0], color='purple')
axs[1].set_title('Humidity %')
axs[1].set_ylim(0,100)
axs[1].fill_between(Timeofday.iloc[:,0], MidlandsRH.iloc[:,0], 0, color='purple', alpha=.1)
for i, txt in enumerate(np.around(MidlandsRH.iloc[:,0],0)):
    axs[1].annotate(txt, (Timeofday.iloc[i,0], MidlandsRH.iloc[i,0]), fontsize=16, color='purple', ha='center', va='bottom')

axs[2].barbs(Timeofday.iloc[:,0], MidlandsWS.iloc[:,0], u, v)
axs[2].set_title('Wind Speed Kts')
axs[2].set_ylim(0,MidlandsWS.iloc[:,0].max()+5)

axs[2].plot(Timeofday.iloc[:,0], MidlandsWS.iloc[:,0])
axs[2].set_title('Wind Speed Kts')

axs[3].plot(Timeofday.iloc[:,0], MidlandsCC.iloc[:,0])
axs[3].set_title('Cloud Cover %')
axs[3].set_ylim(0,100)
axs[3].fill_between(Timeofday.iloc[:,0], MidlandsCC.iloc[:,0], 0, color='blue', alpha=.1)
for i, txt in enumerate(np.around(MidlandsCC.iloc[:,0],0)):
    axs[3].annotate(txt, (Timeofday.iloc[i,0], MidlandsCC.iloc[i,0]), fontsize=16, color='blue', ha='center', va='bottom')

axs[4].bar(Timeofday.iloc[:,0], MidlandsPrecip.iloc[:,0], width=0.01)
axs[4].set_title('Precipitation (Inches)')
for i, txt in enumerate(np.around(MidlandsPrecip.iloc[:,0],2)):
    axs[4].annotate(txt, (Timeofday.iloc[i,0], MidlandsPrecip.iloc[i,0]), fontsize=14, color='blue', ha='center', va='bottom')
axs[4].set_ylim(0,MidlandsPrecip.iloc[:,0].max()+0.05)
plt.tight_layout()

# Save all the plots in a single image
#plt.show()
plt.savefig(str(file_path) + "/data/Midlands_Meteogram.png", bbox_inches='tight')


#Update Variables------------------------------------------------------------

UpstateTemp= nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72,78],[4]]
UpstateRH = nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73,79],[4]]
UpstateWS = nbm.iloc[[2,8,14,20,26,32,38,44,50,56,62,68,74,80],[4]]
UpstateWD = nbm.iloc[[5,11,17,23,29,35,41,47,53,59,65,71,77,83],[4]]

UpstateWS=UpstateWS.reset_index(drop=True)
UpstateWD=270-UpstateWD.reset_index(drop=True)
u =UpstateWS.iloc[:,0]*np.cos(np.deg2rad(UpstateWD.iloc[:,0]))
v = UpstateWS.iloc[:,0] * np.sin(np.deg2rad(UpstateWD.iloc[:,0]))


UpstateCC = nbm.iloc[[3,9,15,21,27,33,39,45,51,57,63,69,75,81],[4]]
UpstatePrecip = nbm.iloc[[4,10,16,22,28,34,40,46,52,58,64,70,76,82],[4]]

#Create Upstate Plots----------------------------------------------------

fig, axs = plt.subplots(5, figsize=(15,15))
fig.subplots_adjust(hspace=1, wspace=1)
fig.suptitle(f"Meteogram for NSFS: {tomorrow.strftime('%Y-%m-%d')}", y=1.05)

axs[0].plot(Timeofday.iloc[:,0], UpstateTemp.iloc[:,0], color='red')
axs[0].set_title('Temperature ºF')
axs[0].set_ylim(UpstateTemp.iloc[:,0].min()-10,UpstateTemp.iloc[:,0].max()+10)
axs[0].fill_between(Timeofday.iloc[:,0], UpstateTemp.iloc[:,0], 0, color='red', alpha=.1)
for i, txt in enumerate(np.around(UpstateTemp.iloc[:,0],0)):
    axs[0].annotate(txt, (Timeofday.iloc[i,0], UpstateTemp.iloc[i,0]), fontsize=16, color='red', ha='center', va='bottom')

axs[1].plot(Timeofday.iloc[:,0], UpstateRH.iloc[:,0], color='purple')
axs[1].set_title('Humidity %')
axs[1].set_ylim(0,100)
axs[1].fill_between(Timeofday.iloc[:,0], UpstateRH.iloc[:,0], 0, color='purple', alpha=.1)
for i, txt in enumerate(np.around(UpstateRH.iloc[:,0],0)):
    axs[1].annotate(txt, (Timeofday.iloc[i,0], UpstateRH.iloc[i,0]), fontsize=16, color='purple', ha='center', va='bottom')

axs[2].barbs(Timeofday.iloc[:,0], UpstateWS.iloc[:,0], u, v)
axs[2].set_title('Wind Speed Kts')
axs[2].set_ylim(0,UpstateWS.iloc[:,0].max()+5)

axs[2].plot(Timeofday.iloc[:,0], UpstateWS.iloc[:,0])
axs[2].set_title('Wind Speed Kts')

axs[3].plot(Timeofday.iloc[:,0], UpstateCC.iloc[:,0])
axs[3].set_title('Cloud Cover %')
axs[3].set_ylim(0,100)
axs[3].fill_between(Timeofday.iloc[:,0], UpstateCC.iloc[:,0], 0, color='blue', alpha=.1)
for i, txt in enumerate(np.around(UpstateCC.iloc[:,0],0)):
    axs[3].annotate(txt, (Timeofday.iloc[i,0], UpstateCC.iloc[i,0]), fontsize=16, color='blue', ha='center', va='bottom')

axs[4].bar(Timeofday.iloc[:,0], UpstatePrecip.iloc[:,0], width=0.01)
axs[4].set_title('Precipitation (Inches)')
for i, txt in enumerate(np.around(UpstatePrecip.iloc[:,0],2)):
    axs[4].annotate(txt, (Timeofday.iloc[i,0], UpstatePrecip.iloc[i,0]), fontsize=14, color='blue', ha='center', va='bottom')
axs[4].set_ylim(0,UpstatePrecip.iloc[:,0].max()+0.05)
plt.tight_layout()

# Save all the plots in a single image
#plt.show()
plt.savefig(str(file_path) + "/data/Upstate_Meteogram.png", bbox_inches='tight')

#CSRA Variables------------------------------------------------------------

CSRATemp= nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72,78],[5]]
CSRARH = nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73,79],[5]]
CSRAWS = nbm.iloc[[2,8,14,20,26,32,38,44,50,56,62,68,74,80],[5]]
CSRAWD = nbm.iloc[[5,11,17,23,29,35,41,47,53,59,65,71,77,83],[5]]

CSRAWS=CSRAWS.reset_index(drop=True)
CSRAWD=270-CSRAWD.reset_index(drop=True)
u =CSRAWS.iloc[:,0]*np.cos(np.deg2rad(CSRAWD.iloc[:,0]))
v = CSRAWS.iloc[:,0] * np.sin(np.deg2rad(CSRAWD.iloc[:,0]))


CSRACC = nbm.iloc[[3,9,15,21,27,33,39,45,51,57,63,69,75,81],[5]]
CSRAPrecip = nbm.iloc[[4,10,16,22,28,34,40,46,52,58,64,70,76,82],[5]]


#Create CSRA Plots----------------------------------------------------

fig, axs = plt.subplots(5, figsize=(15,15))
fig.subplots_adjust(hspace=1, wspace=1)
fig.suptitle(f"Meteogram for Augusta: {tomorrow.strftime('%Y-%m-%d')}", y=1.05)

axs[0].plot(Timeofday.iloc[:,0], CSRATemp.iloc[:,0], color='red')
axs[0].set_title('Temperature ºF')
axs[0].set_ylim(CSRATemp.iloc[:,0].min()-10,CSRATemp.iloc[:,0].max()+10)
axs[0].fill_between(Timeofday.iloc[:,0], CSRATemp.iloc[:,0], 0, color='red', alpha=.1)
for i, txt in enumerate(np.around(CSRATemp.iloc[:,0],0)):
    axs[0].annotate(txt, (Timeofday.iloc[i,0], CSRATemp.iloc[i,0]), fontsize=16, color='red', ha='center', va='bottom')

axs[1].plot(Timeofday.iloc[:,0], CSRARH.iloc[:,0], color='purple')
axs[1].set_title('Humidity %')
axs[1].set_ylim(0,100)
axs[1].fill_between(Timeofday.iloc[:,0], CSRARH.iloc[:,0], 0, color='purple', alpha=.1)
for i, txt in enumerate(np.around(CSRARH.iloc[:,0],0)):
    axs[1].annotate(txt, (Timeofday.iloc[i,0], CSRARH.iloc[i,0]), fontsize=16, color='purple', ha='center', va='bottom')

axs[2].barbs(Timeofday.iloc[:,0], CSRAWS.iloc[:,0], u, v)
axs[2].set_title('Wind Speed Kts')
axs[2].set_ylim(0,CSRAWS.iloc[:,0].max()+5)

axs[2].plot(Timeofday.iloc[:,0], CSRAWS.iloc[:,0])
axs[2].set_title('Wind Speed Kts')

axs[3].plot(Timeofday.iloc[:,0], CSRACC.iloc[:,0])
axs[3].set_title('Cloud Cover %')
axs[3].set_ylim(0,100)
axs[3].fill_between(Timeofday.iloc[:,0], CSRACC.iloc[:,0], 0, color='blue', alpha=.1)
for i, txt in enumerate(np.around(CSRACC.iloc[:,0],0)):
    axs[3].annotate(txt, (Timeofday.iloc[i,0], CSRACC.iloc[i,0]), fontsize=16, color='blue', ha='center', va='center')

axs[4].bar(Timeofday.iloc[:,0], CSRAPrecip.iloc[:,0], width=0.01)
axs[4].set_title('Precipitation (Inches)')
for i, txt in enumerate(np.around(CSRAPrecip.iloc[:,0],2)):
    axs[4].annotate(txt, (Timeofday.iloc[i,0], CSRAPrecip.iloc[i,0]), fontsize=14, color='blue', ha='center', va='bottom')
axs[4].set_ylim(0,CSRAPrecip.iloc[:,0].max()+0.05)
plt.tight_layout()

# Save all the plots in a single image
#plt.show()
plt.savefig(str(file_path) + "/data/CSRA_Meteogram.png", bbox_inches='tight')

#PEE DEE Variables------------------------------------------------------------

PeeDeeTemp= nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72,78],[6]]
PeeDeeRH = nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73,79],[6]]
PeeDeeWS = nbm.iloc[[2,8,14,20,26,32,38,44,50,56,62,68,74,80],[6]]
PeeDeeWD = nbm.iloc[[5,11,17,23,29,35,41,47,53,59,65,71,77,83],[6]]

PeeDeeWS=PeeDeeWS.reset_index(drop=True)
PeeDeeWD=270-PeeDeeWD.reset_index(drop=True)
u =PeeDeeWS.iloc[:,0]*np.cos(np.deg2rad(PeeDeeWD.iloc[:,0]))
v = PeeDeeWS.iloc[:,0] * np.sin(np.deg2rad(PeeDeeWD.iloc[:,0]))


PeeDeeCC = nbm.iloc[[3,9,15,21,27,33,39,45,51,57,63,69,75,81],[6]]
PeeDeePrecip = nbm.iloc[[4,10,16,22,28,34,40,46,52,58,64,70,76,82],[6]]

#Create PEE DEE Plots----------------------------------------------------

fig, axs = plt.subplots(5, figsize=(15,15))
fig.subplots_adjust(hspace=1, wspace=1)
fig.suptitle(f"Meteogram for Florence: {tomorrow.strftime('%Y-%m-%d')}", y=1.05)

axs[0].plot(Timeofday.iloc[:,0], PeeDeeTemp.iloc[:,0], color='red')
axs[0].set_title('Temperature ºF')
axs[0].set_ylim(PeeDeeTemp.iloc[:,0].min()-10,PeeDeeTemp.iloc[:,0].max()+10)
axs[0].fill_between(Timeofday.iloc[:,0], PeeDeeTemp.iloc[:,0], 0, color='red', alpha=.1)
for i, txt in enumerate(np.around(PeeDeeTemp.iloc[:,0],0)):
    axs[0].annotate(txt, (Timeofday.iloc[i,0], PeeDeeTemp.iloc[i,0]), fontsize=16, color='red', ha='center', va='bottom')

axs[1].plot(Timeofday.iloc[:,0], PeeDeeRH.iloc[:,0], color='purple')
axs[1].set_title('Humidity %')
axs[1].set_ylim(0,100)
axs[1].fill_between(Timeofday.iloc[:,0], PeeDeeRH.iloc[:,0], 0, color='purple', alpha=.1)
for i, txt in enumerate(np.around(PeeDeeRH.iloc[:,0],0)):
    axs[1].annotate(txt, (Timeofday.iloc[i,0], PeeDeeRH.iloc[i,0]), fontsize=16, color='purple', ha='center', va='bottom')

axs[2].barbs(Timeofday.iloc[:,0], PeeDeeWS.iloc[:,0], u, v)
axs[2].set_title('Wind Speed Kts')
axs[2].set_ylim(0,PeeDeeWS.iloc[:,0].max()+5)

axs[2].plot(Timeofday.iloc[:,0], PeeDeeWS.iloc[:,0])
axs[2].set_title('Wind Speed Kts')

axs[3].plot(Timeofday.iloc[:,0], PeeDeeCC.iloc[:,0])
axs[3].set_title('Cloud Cover %')
axs[3].set_ylim(0,100)
axs[3].fill_between(Timeofday.iloc[:,0], PeeDeeCC.iloc[:,0], 0, color='blue', alpha=.1)
for i, txt in enumerate(np.around(PeeDeeCC.iloc[:,0],0)):
    axs[3].annotate(txt, (Timeofday.iloc[i,0], PeeDeeCC.iloc[i,0]), fontsize=16, color='blue', ha='center', va='center')

axs[4].bar(Timeofday.iloc[:,0], PeeDeePrecip.iloc[:,0], width=0.01)
axs[4].set_title('Precipitation (Inches)')
for i, txt in enumerate(np.around(PeeDeePrecip.iloc[:,0],2)):
    axs[4].annotate(txt, (Timeofday.iloc[i,0], PeeDeePrecip.iloc[i,0]), fontsize=14, color='blue', ha='center', va='bottom')
axs[4].set_ylim(0,PeeDeePrecip.iloc[:,0].max()+0.05)
plt.tight_layout()

# Save all the plots in a single image
#plt.show()
plt.savefig(str(file_path) + "/data/PeeDee_Meteogram.png", bbox_inches='tight')

#CATAWBA Variables------------------------------------------------------------

CatawbaTemp= nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72,78],[7]]
CatawbaRH = nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73,79],[7]]
CatawbaWS = nbm.iloc[[2,8,14,20,26,32,38,44,50,56,62,68,74,80],[7]]
CatawbaWD = nbm.iloc[[5,11,17,23,29,35,41,47,53,59,65,71,77,83],[7]]

CatawbaWS=CatawbaWS.reset_index(drop=True)
CatawbaWD=270-CatawbaWD.reset_index(drop=True)
u =CatawbaWS.iloc[:,0]*np.cos(np.deg2rad(CatawbaWD.iloc[:,0]))
v = CatawbaWS.iloc[:,0] * np.sin(np.deg2rad(CatawbaWD.iloc[:,0]))


CatawbaCC = nbm.iloc[[3,9,15,21,27,33,39,45,51,57,63,69,75,81],[7]]
CatawbaPrecip = nbm.iloc[[4,10,16,22,28,34,40,46,52,58,64,70,76,82],[7]]


#Create CATAWBA Plots----------------------------------------------------

fig, axs = plt.subplots(5, figsize=(15,15))
fig.subplots_adjust(hspace=1, wspace=1)
fig.suptitle(f"Meteogram for Rock Hill: {tomorrow.strftime('%Y-%m-%d')}", y=1.05)

axs[0].plot(Timeofday.iloc[:,0], CatawbaTemp.iloc[:,0], color='red')
axs[0].set_title('Temperature ºF')
axs[0].set_ylim(CatawbaTemp.iloc[:,0].min()-10,CatawbaTemp.iloc[:,0].max()+10)
axs[0].fill_between(Timeofday.iloc[:,0], CatawbaTemp.iloc[:,0], 0, color='red', alpha=.1)
for i, txt in enumerate(np.around(CatawbaTemp.iloc[:,0],0)):
    axs[0].annotate(txt, (Timeofday.iloc[i,0], CatawbaTemp.iloc[i,0]), fontsize=16, color='red', ha='center', va='bottom')

axs[1].plot(Timeofday.iloc[:,0], CatawbaRH.iloc[:,0], color='purple')
axs[1].set_title('Humidity %')
axs[1].set_ylim(0,100)
axs[1].fill_between(Timeofday.iloc[:,0], CatawbaRH.iloc[:,0], 0, color='purple', alpha=.1)
for i, txt in enumerate(np.around(CatawbaRH.iloc[:,0],0)):
    axs[1].annotate(txt, (Timeofday.iloc[i,0], CatawbaRH.iloc[i,0]), fontsize=16, color='purple', ha='center', va='bottom')

axs[2].barbs(Timeofday.iloc[:,0], CatawbaWS.iloc[:,0], u, v)
axs[2].set_title('Wind Speed Kts')
axs[2].set_ylim(0,CatawbaWS.iloc[:,0].max()+5)

axs[2].plot(Timeofday.iloc[:,0], CatawbaWS.iloc[:,0])
axs[2].set_title('Wind Speed Kts')

axs[3].plot(Timeofday.iloc[:,0], CatawbaCC.iloc[:,0])
axs[3].set_title('Cloud Cover %')
axs[3].set_ylim(0,100)
axs[3].fill_between(Timeofday.iloc[:,0], CatawbaCC.iloc[:,0], 0, color='blue', alpha=.1)
for i, txt in enumerate(np.around(CatawbaCC.iloc[:,0],0)):
    axs[3].annotate(txt, (Timeofday.iloc[i,0], CatawbaCC.iloc[i,0]), fontsize=16, color='blue', ha='center', va='center')

axs[4].bar(Timeofday.iloc[:,0], CatawbaPrecip.iloc[:,0], width=0.01)
axs[4].set_title('Precipitation (Inches)')
for i, txt in enumerate(np.around(CatawbaPrecip.iloc[:,0],2)):
    axs[4].annotate(txt, (Timeofday.iloc[i,0], CatawbaPrecip.iloc[i,0]), fontsize=14, color='blue', ha='center', va='bottom')
axs[4].set_ylim(0,CatawbaPrecip.iloc[:,0].max()+0.05)
plt.tight_layout()

# Save all the plots in a single image
#plt.show()
plt.savefig(str(file_path) + "/data/Catawba_Meteogram.png", bbox_inches='tight')

#Trident Variables------------------------------------------------------------

TridentTemp= nbm.iloc[[0,6,12,18,24,30,36,42,48,54,60,66,72,78],[8]]
TridentRH = nbm.iloc[[1,7,13,19,25,31,37,43,49,55,61,67,73,79],[8]]
TridentWS = nbm.iloc[[2,8,14,20,26,32,38,44,50,56,62,68,74,80],[8]]
TridentWD = nbm.iloc[[5,11,17,23,29,35,41,47,53,59,65,71,77,83],[8]]

TridentWS=TridentWS.reset_index(drop=True)
TridentWD=270-TridentWD.reset_index(drop=True)
u =TridentWS.iloc[:,0]*np.cos(np.deg2rad(TridentWD.iloc[:,0]))
v = TridentWS.iloc[:,0] * np.sin(np.deg2rad(TridentWD.iloc[:,0]))


TridentCC = nbm.iloc[[3,9,15,21,27,33,39,45,51,57,63,69,75,81],[8]]
TridentPrecip = nbm.iloc[[4,10,16,22,28,34,40,46,52,58,64,70,76,82],[8]]

#Create Trident Plots----------------------------------------------------

fig, axs = plt.subplots(5, figsize=(15,15))
fig.subplots_adjust(hspace=1, wspace=1)
fig.suptitle(f"Meteogram for Cape Romain: {tomorrow.strftime('%Y-%m-%d')}", y=1.05)

axs[0].plot(Timeofday.iloc[:,0], TridentTemp.iloc[:,0], color='red')
axs[0].set_title('Temperature ºF')
axs[0].set_ylim(TridentTemp.iloc[:,0].min()-10,TridentTemp.iloc[:,0].max()+10)
axs[0].fill_between(Timeofday.iloc[:,0], TridentTemp.iloc[:,0], 0, color='red', alpha=.1)
for i, txt in enumerate(np.around(TridentTemp.iloc[:,0],0)):
    axs[0].annotate(txt, (Timeofday.iloc[i,0], TridentTemp.iloc[i,0]), fontsize=16, color='red', ha='center', va='bottom')

axs[1].plot(Timeofday.iloc[:,0], TridentRH.iloc[:,0], color='purple')
axs[1].set_title('Humidity %')
axs[1].set_ylim(0,100)
axs[1].fill_between(Timeofday.iloc[:,0], TridentRH.iloc[:,0], 0, color='purple', alpha=.1)
for i, txt in enumerate(np.around(TridentRH.iloc[:,0],0)):
    axs[1].annotate(txt, (Timeofday.iloc[i,0], TridentRH.iloc[i,0]), fontsize=16, color='purple', ha='center', va='bottom')

axs[2].barbs(Timeofday.iloc[:,0], TridentWS.iloc[:,0], u, v)
axs[2].set_title('Wind Speed Kts')
axs[2].set_ylim(0,TridentWS.iloc[:,0].max()+5)

axs[2].plot(Timeofday.iloc[:,0], TridentWS.iloc[:,0])
axs[2].set_title('Wind Speed Kts')

axs[3].plot(Timeofday.iloc[:,0], TridentCC.iloc[:,0])
axs[3].set_title('Cloud Cover %')
axs[3].set_ylim(0,100)
axs[3].fill_between(Timeofday.iloc[:,0], TridentCC.iloc[:,0], 0, color='blue', alpha=.1)
for i, txt in enumerate(np.around(TridentCC.iloc[:,0],0)):
    axs[3].annotate(txt, (Timeofday.iloc[i,0], TridentCC.iloc[i,0]), fontsize=16, color='blue', ha='center', va='center')

axs[4].bar(Timeofday.iloc[:,0], TridentPrecip.iloc[:,0], width=0.01)
axs[4].set_title('Precipitation (Inches)')
for i, txt in enumerate(np.around(TridentPrecip.iloc[:,0],2)):
    axs[4].annotate(txt, (Timeofday.iloc[i,0], TridentPrecip.iloc[i,0]), fontsize=14, color='blue', ha='center', va='bottom')
axs[4].set_ylim(0,TridentPrecip.iloc[:,0].max()+0.05)
plt.tight_layout()

# Save all the plots in a single image
#plt.show()
plt.savefig(str(file_path) + "/data/Trident_Meteogram.png", bbox_inches='tight')
