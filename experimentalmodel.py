import numpy as np
import matplotlib.pyplot as plt

import os
import pygrib
import numpy as np
import pandas as pd
from collections import Counter
from datetime import datetime, timedelta

import urllib.request
import os
import datetime
import time


current_directory = os.getcwd()
file_path=current_directory

# Check if the directory exists
if not os.path.exists(str(file_path)+'/grib/'):
    # Create the directory
    os.makedirs(str(file_path)+'/grib/')

if not os.path.exists(str(file_path)+'/data/'):
    # Create the directory
    os.makedirs(str(file_path)+'/data/')
    
#CREATING TIME VARIABLE  - DO NOT CHANGE BELOW THIS ------------------------------------
now=datetime.date.today()

delta = datetime.timedelta(days=1)

today = int(now.strftime("%Y%m%d"))
prev=now - delta
yesterday = int(prev.strftime("%Y%m%d"))

nexted = now + delta
tomorrow = int(nexted.strftime("%Y%m%d"))

dayafter = nexted + delta
dayafter = int(dayafter.strftime("%Y%m%d"))

#CREATING TIME VARIABLE - DO NOT CHANGE ABOVE THIS -------------------------------------

file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/nam/prod/nam." + str(today) + "/nam.t12z.conusnest.hiresf24.tm00.grib2", str(file_path)+"/grib/nam.t12z.conusnest.hiresf24.tm00.grib2")

file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/nam/prod/nam." + str(today) + "/nam.t12z.conusnest.hiresf30.tm00.grib2", str(file_path)+"/grib/nam.t12z.conusnest.hiresf30.tm00.grib2")



#NBM Imports
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f022.co.grib2", str(file_path)+"/grib/blend.t12z.core.f022.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f023.co.grib2", str(file_path)+"/grib/blend.t12z.core.f023.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f024.co.grib2", str(file_path)+"/grib/blend.t12z.core.f024.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f025.co.grib2", str(file_path)+"/grib/blend.t12z.core.f025.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f026.co.grib2", str(file_path)+"/grib/blend.t12z.core.f026.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f027.co.grib2", str(file_path)+"/grib/blend.t12z.core.f027.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f028.co.grib2", str(file_path)+"/grib/blend.t12z.core.f028.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f029.co.grib2", str(file_path)+"/grib/blend.t12z.core.f029.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f030.co.grib2", str(file_path)+"/grib/blend.t12z.core.f030.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f031.co.grib2", str(file_path)+"/grib/blend.t12z.core.f031.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f032.co.grib2", str(file_path)+"/grib/blend.t12z.core.f032.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f033.co.grib2", str(file_path)+"/grib/blend.t12z.core.f033.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f034.co.grib2", str(file_path)+"/grib/blend.t12z.core.f034.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f035.co.grib2", str(file_path)+"/grib/blend.t12z.core.f035.co.grib2")
file= urllib.request.urlretrieve("https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend." + str(today) + "/12/core/blend.t12z.core.f036.co.grib2", str(file_path)+"/grib/blend.t12z.core.f036.co.grib2")
