import requests
import csv
import time

data = []
count = 0
try:
    while True: 
        time.sleep(1) #fetching data from api at interval time of 1 second
        count = count + 1
        r = requests.get("https://random-data-api.com/api/v2/users")
        jsondata = r.json()
        columns  = ['id','first_name','last_name','username','email','avatar','gender','date_of_birth'] #filtering out necessary data from get request
        current_data = {x:jsondata[x] for x in columns}
        data.append(current_data)
        print("Fetched user data #%s" %count)

#press ctrl + C to halt the fetch process
except KeyboardInterrupt: 
    pass

print(data)

#converting the filtered data in dictionary format to csv file
with open('users.csv','a',newline='') as f: 
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)
    
 
