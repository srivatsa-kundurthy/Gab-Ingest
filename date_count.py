import matplotlib.pyplot as plt
import json
import pandas as pd


'''split target json files into csv of date + count of tweets on that date'''

file_cnt = 5378
target_name = 'ali'
target = 'BIG/ali_BIG/ali_'
global_dates = []
for i in range(1, file_cnt + 1):
    file_name = target + str(i) + '.json'
    #print(file_name)
    file = open(file_name)
    data = json.load(file)
    dates = []
    for k in range(0,len(data['statuses'])):
        global_dates.append(data['statuses'][k]['created_at'][:-1].split('T')[0])
    print(i)
    

print(global_dates)
print('GLOBAL COMPLETE, PROCESSING IDENTICAL...')
identical = {n:global_dates.count(n) for n in global_dates}
print(identical)
print('IDENTICAL DONE')

#df = pd.DataFrame.from_dict(identical)
s = pd.Series(identical, name='count')
s.head()
print(s)
s.to_csv(target_name +'_dates.csv')

print('COMPLETE')





