import os
import glob
import datetime as dt
import json
import random
from modules import getRandom

# flush previous datasets
files = glob.glob("./datasets/*json")
if len(files) != 0:
        for file in files:
                os.remove(file)

location = "mebamu"

empty = {"opendate": [],"opentime": [],
        "closedate": [],"closetime": [], "diff": [],}

data = {"opendate": [],"opentime": [],
        "closedate": [],"closetime": [], "diff": [],}

# initial data 
startTime = dt.datetime(2022, 7, 1, 6, 47, 23)
closeTime = startTime + dt.timedelta(seconds=getRandom())
diff = str(closeTime - startTime)

month, year = startTime.strftime("%B %Y").lower().split()

data["opendate"].append(str(startTime.date())); 
data["opentime"].append(str(startTime.time()));
data["closedate"].append(str(closeTime.date()));
data["closetime"].append(str(closeTime.time()));
data["diff"].append(diff)

j = 1

for i in range(300):
    path = f"./datasets/{location}_{month}_{year}.json";
    try:
        open(path)
    except:
        file = open(path, "w")
        data = empty
        json.dump(empty, file, indent=4)
        file.close()

    file = open(path, "w");
    json.dump(data, file, indent=4)
    file.close()
    
    read = open(path)
    data = json.load(read)
    read.close()

    startTime = closeTime + dt.timedelta(seconds=getRandom());
    closeTime = startTime + dt.timedelta(seconds=getRandom());
    diff = str(closeTime - startTime)

    month, year = startTime.strftime("%B %Y").lower().split()


    data["opendate"].append(str(startTime.date())); 
    data["opentime"].append(str(startTime.time()));
    data["closedate"].append(str(closeTime.date()));
    data["closetime"].append(str(closeTime.time()));
    data["diff"].append(diff)
    