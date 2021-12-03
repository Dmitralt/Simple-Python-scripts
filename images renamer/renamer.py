import os
import json

import uuid
from natsort import natsorted
def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.







with open('config.json') as f:
   data = json.load(f)

foulders=data["foulders"]
extencions=data["extencions"]



for foulder_number in range(len(foulders)) : 
    for root, dirs, files in os.walk(foulders[foulder_number]):
        randSTR=my_random_string(18)
        count=1
        files = natsorted(files, key=lambda x: x.lstrip())        
        print(files)
        for filename in files:
            if(root==foulders[foulder_number]):
                if(filename.split(".")[-1] in extencions):
                    newname=root+"/"+randSTR+"$"+str(count)+"."+filename.split(".")[-1]
                    count=count+1                
                    print(root+"/"+filename,newname)
                    os.rename(root+"/"+filename,newname)

for foulder_number in range(len(foulders)) : 
    for root, dirs, files in os.walk(foulders[foulder_number]):
        for filename in files:
            if(root==foulders[foulder_number]):
                if(filename.split(".")[-1] in extencions):
                    newname=root+"/"+filename.split(".")[0].split('$')[1]+"."+filename.split(".")[-1]
                    print(root+"/"+filename,newname)
                    os.rename(root+"/"+filename,newname)

