import numpy as np
import pygrib
import pandas as pd
import os

current_directory = os.getcwd()
file_path=current_directory


#opens the 12Z Grib File
grbs = pygrib.open(str(file_path)+'/grib/nam.t12z.conusnest.hiresf24.tm00.grib2')

temp_grb = grbs[661] #2 meter temperature
dew_grb = grbs[663] #2 meter dewpoint
rh_grb = grbs[664] #2 meter dewpoint
u10_grb = grbs[669] #10 meter U wind
v10_grb = grbs[670] #10 meter V wind
T925_grb = grbs[567] #925 Temp
RH925_grb = grbs[568] #925 RH
U925_grb = grbs[573] #925 U wind
V925_grb = grbs[574] #925 V wind
T850_grb = grbs[522] #850 Temp
RH850_grb = grbs[523] #850 RH
U850_grb = grbs[529] #850 U wind
V850_grb = grbs[530] #850 V wind
RH700_grb = grbs[436] #700 RH
PWAT_grb = grbs[718] #Precipitable water
grbs.close()

#opens the 18Z grib file--------------------------------------
grbs = pygrib.open(str(file_path)+'/grib/nam.t12z.conusnest.hiresf30.tm00.grib2')
temp_grb2 = grbs[661] #2 meter temperature
dew_grb2 = grbs[663] #2 meter dewpoint
rh_grb2 = grbs[664] #2 meter dewpoint
u10_grb2 = grbs[669] #10 meter U wind
v10_grb2 = grbs[670] #10 meter V wind
T925_grb2 = grbs[567] #925 Temp
RH925_grb2 = grbs[568] #925 RH
U925_grb2 = grbs[573] #925 U wind
V925_grb2 = grbs[574] #925 V wind
T850_grb2 = grbs[522] #850 Temp
RH850_grb2 = grbs[523] #850 RH
U850_grb2 = grbs[529] #850 U wind
V850_grb2 = grbs[530] #850 V wind
RH700_grb2 = grbs[436] #700 RH
PWAT_grb2 = grbs[718] #Precipitable water
PBLheight_grb = grbs[857] #18z PBL Height

grbs.close()
#closes the 18Z grib file
print(rh_grb)

# Extract temperature data for a specific longitude-latitude subset **DO NOT CHANGE**
lat1=31.0 #should be 31.0
lat2=35.5 #should be 35.5
lon1=-83.5 #should be -83.5
lon2=-78.0 #should be -78.0

# 2 meter Temperature import subsetting to a smaller domain 12Z data

temp, lat, lon = temp_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
dew, lat, lon = dew_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
rh, lat, lon = rh_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
u10, lat, lon = u10_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
v10, lat, lon = v10_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
T925, lat, lon = T925_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
RH925, lat, lon = RH925_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
U925, lat, lon = U925_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
V925, lat, lon = V925_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
T850, lat, lon = T850_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
RH850, lat, lon = RH850_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
U850, lat, lon = U850_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
V850, lat, lon = V850_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
RH700, lat, lon = RH700_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
PWAT, lat, lon = PWAT_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)

# 2 meter Temperature import subsetting to a smaller domain 18Z data

temp2, lat, lon = temp_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
dew2, lat, lon = dew_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
rh2, lat, lon = rh_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
u102, lat, lon = u10_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
v102, lat, lon = v10_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
T9252, lat, lon = T925_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
RH9252, lat, lon = RH925_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
U9252, lat, lon = U925_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
V9252, lat, lon = V925_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
T8502, lat, lon = T850_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
RH8502, lat, lon = RH850_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
U8502, lat, lon = U850_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
V8502, lat, lon = V850_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
RH7002, lat, lon = RH700_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
PWAT2, lat, lon = PWAT_grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
PBLheight, lat, lon = PBLheight_grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)

#Unit conversions --- 12Z
temp=(temp-273.15)*(9/5)+32
dew=(dew-273.15)*(9/5)+32
#no conversion for rh
u10 = u10*1.943844
v10 = v10*1.943844
T925=T925-273.15
#no converstion for 925 rh
U925 = U925*1.943844
V925 = V925*1.943844
T850=T850-273.15
#no converstion for 850 rh
U850=U850*1.943844
V850=V850*1.943844
#no conversion for 700 rh
PWAT=PWAT*0.039370

#Unit conversions --- 18Z
temp2=(temp2-273.15)*(9/5)+32
dew2=(dew2-273.15)*(9/5)+32
#no conversion for rh
u102 = u102*1.943844
v102 = v102*1.943844
T9252=T9252-273.15
#no converstion for 925 rh
U9252 = U9252*1.943844
V9252 = V9252*1.943844
T8502=T8502-273.15
#no converstion for 850 rh
U8502=U8502*1.943844
V8502=V8502*1.943844
#no conversion for 700 rh
PWAT2=PWAT2*0.039370
#no unit conversion for PBL height

#from metpy.interpolate import natural_neighbor_to_grid as nn (may use later)

#import imterpolation program and set grid resolution to interpolate to ---------------------------------
from scipy.interpolate import griddata

lats = np.arange(lat1, lat2, 0.01)
lats = np.around(lats,2)
lons = np.arange(lon1, lon2, 0.01)
lons = np.around(lons,2)
xi, yi = np.meshgrid(lons, lats)
#Do not edit the above ----------------------------------------------------------------------------------


#make 0.01 resolution data frames -------- 12Z Data
temp= griddata((lon, lat), temp, (xi, yi), method='linear')
dew= griddata((lon, lat), dew, (xi, yi), method='linear')
rh= griddata((lon, lat), rh, (xi, yi), method='linear')
u10= griddata((lon, lat), u10, (xi, yi), method='linear')
v10= griddata((lon, lat), v10, (xi, yi), method='linear')
T925= griddata((lon, lat), T925, (xi, yi), method='linear')
RH925= griddata((lon, lat), RH925, (xi, yi), method='linear')
U925= griddata((lon, lat), U925, (xi, yi), method='linear')
V925= griddata((lon, lat), V925, (xi, yi), method='linear')
T850= griddata((lon, lat), T850, (xi, yi), method='linear')
RH850= griddata((lon, lat), RH850, (xi, yi), method='linear')
U850= griddata((lon, lat), U850, (xi, yi), method='linear')
V850= griddata((lon, lat), V850, (xi, yi), method='linear')
RH700= griddata((lon, lat), RH700, (xi, yi), method='linear')
PWAT= griddata((lon, lat), PWAT, (xi, yi), method='linear')

df = pd.DataFrame(temp)
df1=pd.DataFrame(dew)
df2=pd.DataFrame(rh)
df3=pd.DataFrame(u10)
df4=pd.DataFrame(v10)
df5=pd.DataFrame(T925)
df6=pd.DataFrame(RH925)
df7=pd.DataFrame(U925)
df8=pd.DataFrame(V925)
df9=pd.DataFrame(T850)
df10=pd.DataFrame(RH850)
df11=pd.DataFrame(U850)
df12=pd.DataFrame(V850)
df13=pd.DataFrame(RH700)
df14=pd.DataFrame(PWAT)


#make 0.01 resolution data frames -------- 18Z Data
temp2= griddata((lon, lat), temp2, (xi, yi), method='linear')
dew2= griddata((lon, lat), dew2, (xi, yi), method='linear')
rh2= griddata((lon, lat), rh2, (xi, yi), method='linear')
u102= griddata((lon, lat), u102, (xi, yi), method='linear')
v102= griddata((lon, lat), v102, (xi, yi), method='linear')
T9252= griddata((lon, lat), T9252, (xi, yi), method='linear')
RH9252= griddata((lon, lat), RH9252, (xi, yi), method='linear')
U9252= griddata((lon, lat), U9252, (xi, yi), method='linear')
V9252= griddata((lon, lat), V9252, (xi, yi), method='linear')
T8502= griddata((lon, lat), T8502, (xi, yi), method='linear')
RH8502= griddata((lon, lat), RH8502, (xi, yi), method='linear')
U8502= griddata((lon, lat), U8502, (xi, yi), method='linear')
V8502= griddata((lon, lat), V8502, (xi, yi), method='linear')
RH7002= griddata((lon, lat), RH7002, (xi, yi), method='linear')
PWAT2= griddata((lon, lat), PWAT2, (xi, yi), method='linear')
PBLheight= griddata((lon, lat), PBLheight, (xi, yi), method='linear')

df15 = pd.DataFrame(temp2)
df16=pd.DataFrame(dew2)
df17=pd.DataFrame(rh2)
df18=pd.DataFrame(u102)
df19=pd.DataFrame(v102)
df20=pd.DataFrame(T9252)
df21=pd.DataFrame(RH9252)
df22=pd.DataFrame(U9252)
df23=pd.DataFrame(V9252)
df24=pd.DataFrame(T8502)
df25=pd.DataFrame(RH8502)
df26=pd.DataFrame(U8502)
df27=pd.DataFrame(V8502)
df28=pd.DataFrame(RH7002)
df29=pd.DataFrame(PWAT2)
df30=pd.DataFrame(PBLheight)

df.index=lats
df.columns=lons

m=df.index
n=df.columns
#print(m[313],n[263]) #Sandhills Monitoring Gridpoint
#print(m[399],n[144]) #NSDFS Ozone Monitoring
#print(m[247],n[153]) #Augusta Ozone Monitoring
#print(m[321],n[373]) #Florence Ozone Monitoring
#print(m[391],n[263]) #Catawba Ozone Monitoring
#print(m[194],n[384]) #Cape Romain Ozone Monitoring

data = {'Location': ['Sandhills', 'NSFS', 'Augusta', 'Florence', 'Catawba', 'Cape Romain'],
        #'12Z 2M-Temp F': [df.iloc[[313,263],[399,144],[247,153],[321,373],[391,263],[194,384]]],
        '12Z 2M-Temp F': [df.iloc[313,263], df.iloc[399,144], df.iloc[247,153], df.iloc[321,373], df.iloc[391,263], df.iloc[194,384]],
        '12Z 2M-Dew F': [df1.iloc[313,263], df1.iloc[399,144], df1.iloc[247,153], df1.iloc[321,373], df1.iloc[391,263], df1.iloc[194,384]],
        '12Z 2M-RH %': [df2.iloc[313,263], df2.iloc[399,144], df2.iloc[247,153], df2.iloc[321,373], df2.iloc[391,263], df2.iloc[194,384]],
        '12Z U Wind Kts': [df3.iloc[313,263], df3.iloc[399,144], df3.iloc[247,153], df3.iloc[321,373], df3.iloc[391,263], df3.iloc[194,384]],
        '12Z V Wind Kts': [df4.iloc[313,263], df4.iloc[399,144], df4.iloc[247,153], df4.iloc[321,373], df4.iloc[391,263], df4.iloc[194,384]],
        '12Z 925mb Temp C': [df5.iloc[313,263], df5.iloc[399,144], df5.iloc[247,153], df5.iloc[321,373], df5.iloc[391,263], df5.iloc[194,384]],
        '12Z 925mb RH %': [df6.iloc[313,263], df6.iloc[399,144], df6.iloc[247,153], df6.iloc[321,373], df6.iloc[391,263], df6.iloc[194,384]],
        '12Z U Wind 925mb Knots': [df7.iloc[313,263], df7.iloc[399,144], df7.iloc[247,153], df7.iloc[321,373], df7.iloc[391,263], df7.iloc[194,384]],
        '12Z V Wind 925mb Knots': [df8.iloc[313,263], df8.iloc[399,144], df8.iloc[247,153], df8.iloc[321,373], df8.iloc[391,263], df8.iloc[194,384]],
        '12Z 850mb Temp C': [df9.iloc[313,263], df9.iloc[399,144], df9.iloc[247,153], df9.iloc[321,373], df9.iloc[391,263], df9.iloc[194,384]],
        '12Z 850mb RH %': [df10.iloc[313,263], df10.iloc[399,144], df10.iloc[247,153], df10.iloc[321,373], df10.iloc[391,263], df10.iloc[194,384]],
        '12Z U Wind 850mb Knots': [df11.iloc[313,263], df11.iloc[399,144], df11.iloc[247,153], df11.iloc[321,373], df11.iloc[391,263], df11.iloc[194,384]],
        '12Z V Wind 850mb Knots': [df12.iloc[313,263], df12.iloc[399,144], df12.iloc[247,153], df12.iloc[321,373], df12.iloc[391,263], df12.iloc[194,384]],
        '12Z 700mb RH %': [df13.iloc[313,263], df13.iloc[399,144], df13.iloc[247,153], df13.iloc[321,373], df13.iloc[391,263], df13.iloc[194,384]],
        '12Z PWAT Inches': [df14.iloc[313,263], df14.iloc[399,144], df14.iloc[247,153], df14.iloc[321,373], df14.iloc[391,263], df14.iloc[194,384]],
        '18Z 2M-Temp F': [df15.iloc[313,263], df15.iloc[399,144], df15.iloc[247,153], df15.iloc[321,373], df15.iloc[391,263], df15.iloc[194,384]],
        '18Z 2M-Dew F': [df16.iloc[313,263], df16.iloc[399,144], df16.iloc[247,153], df16.iloc[321,373], df16.iloc[391,263], df16.iloc[194,384]],
        '18Z 2M-RH %': [df17.iloc[313,263], df17.iloc[399,144], df17.iloc[247,153], df17.iloc[321,373], df17.iloc[391,263], df17.iloc[194,384]],
        '18Z U Wind Kts': [df18.iloc[313,263], df18.iloc[399,144], df18.iloc[247,153], df18.iloc[321,373], df18.iloc[391,263], df18.iloc[194,384]],
        '18Z V Wind Kts': [df19.iloc[313,263], df19.iloc[399,144], df19.iloc[247,153], df19.iloc[321,373], df19.iloc[391,263], df19.iloc[194,384]],
        '18Z 925mb Temp C': [df20.iloc[313,263], df20.iloc[399,144], df20.iloc[247,153], df20.iloc[321,373], df20.iloc[391,263], df20.iloc[194,384]],
        '18Z 925mb RH %': [df21.iloc[313,263], df21.iloc[399,144], df21.iloc[247,153], df21.iloc[321,373], df21.iloc[391,263], df21.iloc[194,384]],
        '18Z U Wind 925mb Knots': [df22.iloc[313,263], df22.iloc[399,144], df22.iloc[247,153], df22.iloc[321,373], df22.iloc[391,263], df22.iloc[194,384]],
        '18Z V Wind 925mb Knots': [df23.iloc[313,263], df23.iloc[399,144], df23.iloc[247,153], df23.iloc[321,373], df23.iloc[391,263], df23.iloc[194,384]],
        '18Z 850mb Temp C': [df24.iloc[313,263], df24.iloc[399,144], df24.iloc[247,153], df24.iloc[321,373], df24.iloc[391,263], df24.iloc[194,384]],
        '18Z 850mb RH %': [df25.iloc[313,263], df25.iloc[399,144], df25.iloc[247,153], df25.iloc[321,373], df25.iloc[391,263], df25.iloc[194,384]],
        '18Z U Wind 850mb Knots': [df26.iloc[313,263], df26.iloc[399,144], df26.iloc[247,153], df26.iloc[321,373], df26.iloc[391,263], df26.iloc[194,384]],
        '18Z V Wind 850mb Knots': [df27.iloc[313,263], df27.iloc[399,144], df27.iloc[247,153], df27.iloc[321,373], df27.iloc[391,263], df27.iloc[194,384]],
        '18Z 700mb RH %': [df28.iloc[313,263], df28.iloc[399,144], df28.iloc[247,153], df28.iloc[321,373], df28.iloc[391,263], df28.iloc[194,384]],
        '18Z PWAT Inches': [df29.iloc[313,263], df29.iloc[399,144], df29.iloc[247,153], df29.iloc[321,373], df29.iloc[391,263], df29.iloc[194,384]],
        '18Z PBLheight Meters': [df30.iloc[313,263], df30.iloc[399,144], df30.iloc[247,153], df30.iloc[321,373], df30.iloc[391,263], df30.iloc[194,384]]         
        }


namdf = pd.DataFrame(data)
namdf=namdf.set_index('Location')
namdf=namdf.T
print(namdf)
namdf.to_csv(str(file_path)+'/data/namdata.csv')
