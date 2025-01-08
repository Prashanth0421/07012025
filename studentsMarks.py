import pandas as pd
screen_time =[2,4,6]
sleep_hour=[3,7,8]
stu_name =["supreeth","kishhu","vedhith reddy"]
dict1 = {

    "screen_time":screen_time,
    "sleep_hour":sleep_hour,
    "stu_name":stu_name
     }

print(dict1)
df = pd.DataFrame(dict1)
print(df)