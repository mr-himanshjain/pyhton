import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json","r+")
    data = json.loads(old_file.read())
    print("Current age is ", data["age"],"--adding a year.")
    data["age"]=data["age"]+1
    print("new age is ",data["age"])
else:
    old_file = open("./ages.json","w+")
    data = {"name": "himanshu", "age": 22}
    print("no such file found, setting default age to",data["age"])
    
old_file.seek(0)
old_file.write(json.dumps(data))