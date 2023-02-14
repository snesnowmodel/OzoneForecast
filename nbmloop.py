import numpy as np
import matplotlib.pyplot as plt
import pygrib
import pandas as pd
import os

current_directory = os.getcwd()
file_path=current_directory

df_final = pd.DataFrame({'Location': ['Date','Time','Sandhills', 'NSFS', 'Augusta', 'Florence', 'Catawba', 'Cape Romain']})
newdfs=pd.DataFrame()

list = ['22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']

for i in range(15):
    #grbs = pygrib.open('blend.t18z.core.f024.co.grib2')
    grbs = pygrib.open(str(file_path)+'/grib/blend.t12z.core.f0' + str(list[i]) + '.co.grib2')
    # Read the contents of the file into a list
    grb = grbs.select(name='2 metre temperature')[0]
    grb2 = grbs.select(name='2 metre relative humidity')[0]
    grb3 = grbs.select(name='Total Cloud Cover')[3]
    grb3a = grbs.select(name='Total Cloud Cover')[0]
    grb3b = grbs.select(name='Total Cloud Cover')[1]
    grb3c = grbs.select(name='Total Cloud Cover')[2]
    if i==2 or i==8 or i==15:
        grb4 = grbs.select(name='Total Precipitation')[3]
    else:
        grb4 = grbs.select(name='Total Precipitation')[1]
    grb5 = grbs.select(name='10 metre wind speed')[0]
    grb6 = grbs.select(name='10 metre wind direction')[0]

    
    print(grb6.name)
    grbs.close()
    #print(temperature_values, rh_values, cc_values, TP_values)
    # Extract temperature data for a specific longitude-latitude subset **DO NOT CHANGE**
    lat1=31.0 #should be 31.0
    lat2=35.5 #should be 35.5
    lon1=-83.5 #should be -83.5
    lon2=-78.0 #should be -78.0


    #creation of subset
    temp2m, lat, lon = grb.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
    RH2m, lat, lon = grb2.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
    WS10m, lat, lon = grb5.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
    cctot1, lat, lon = grb3.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
    cctot2, lat, lon = grb3a.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
    cctot3, lat, lon = grb3b.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
    cctot4, lat, lon = grb3c.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
    preciptot, lat, lon = grb4.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)
    WD10M, lat, lon = grb6.data(lat1=lat1, lat2=lat2, lon1=lon1, lon2=lon2)

    
    #unit conversions
    temp2m=(temp2m-273.15)*(9/5)+32
    WS10m = WS10m*1.943844
    preciptot = preciptot*0.039370
    cctot=np.maximum(np.maximum(cctot1, cctot2), np.maximum(cctot3, cctot4))
    
    from scipy.interpolate import griddata

    lats = np.arange(lat1, lat2, 0.01)
    lats = np.around(lats,2)
    lons = np.arange(lon1, lon2, 0.01)
    lons = np.around(lons,2)
    xi, yi = np.meshgrid(lons, lats)
    #Do not edit the above ----------------------------------------------------------------------------------

    #make 0.01 resolution data frames -------- 12Z Data
    temp2m= griddata((lon, lat), temp2m, (xi, yi), method='linear')
    RH2m= griddata((lon, lat), RH2m, (xi, yi), method='linear')
    WS10m= griddata((lon, lat), WS10m, (xi, yi), method='linear')
    cctot= griddata((lon, lat), cctot, (xi, yi), method='linear')
    preciptot= griddata((lon, lat), preciptot, (xi, yi), method='linear')
    WD10M= griddata((lon, lat), WD10M, (xi, yi), method='linear')


    df = pd.DataFrame(temp2m)
    df1=pd.DataFrame(RH2m)
    df2=pd.DataFrame(WS10m)
    df3=pd.DataFrame(cctot)
    df4=pd.DataFrame(preciptot)
    df5=pd.DataFrame(WD10M)
    print(grb.validDate)
    
    new_rows=pd.DataFrame({grb.name: [grb.validityDate, grb.validDate, df.iloc[313,263], df.iloc[399,144], df.iloc[247,153], df.iloc[321,373], df.iloc[391,263], df.iloc[194,384]], grb2.name: [grb2.validityDate, grb2.validDate, df1.iloc[313,263], df1.iloc[399,144], df1.iloc[247,153], df1.iloc[321,373], df1.iloc[391,263], df1.iloc[194,384]], grb5.name: [grb5.validityDate, grb.validDate, df2.iloc[313,263], df2.iloc[399,144], df2.iloc[247,153], df2.iloc[321,373], df2.iloc[391,263], df2.iloc[194,384]], grb3.name: [grb3.validityDate, grb3.validDate, df3.iloc[313,263], df3.iloc[399,144], df3.iloc[247,153], df3.iloc[321,373], df3.iloc[391,263], df3.iloc[194,384]], grb4.name: [grb4.validityDate, grb4.validDate, df4.iloc[313,263], df4.iloc[399,144], df4.iloc[247,153], df4.iloc[321,373], df4.iloc[391,263], df4.iloc[194,384]], grb6.name: [grb6.validityDate, grb6.validDate, df5.iloc[313,263], df5.iloc[399,144], df5.iloc[247,153], df5.iloc[321,373], df5.iloc[391,263], df5.iloc[194,384]] })
    exec(f"df_{i}=new_rows")
            
df_final=pd.concat([df_final, df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14], axis=1, ignore_index=False)
df_final=df_final.set_index('Location')
df_final=df_final.T
df_final.to_csv(str(file_path)+'/data/nbmdata.csv')
