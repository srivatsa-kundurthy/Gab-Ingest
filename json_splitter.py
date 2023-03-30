import pandas as pd
import json
from datetime import datetime
import matplotlib.pyplot as plt

'''
split messy json file into several clean json files



'''
target_file = 'raw/ali_new.json'
save_dir = 'BIG/ali_BIG'
file_base = 'ali_'


#with open(target_file, 'rb') as f:
#    file = f.read()

file = open(target_file)
str_file = file.read()

#with open(target_file, 'rb') as f:
#  str_file = f.read()


keyword = save_dir + '/' + file_base

#print(str_file)
data_into_list = str_file.replace('\n', ' ').split('{"statuses"')
print(len(data_into_list))
#print(data_into_list[2])

for i in range(1, len(data_into_list)):
    with open(keyword + str(i) + '.json','w') as outfile:
        outfile.write('{"statuses"'+data_into_list[i][:-2])
    if i == (len(data_into_list) - 1):
        with open(keyword + str(i) + '.json','w') as outfile:
            outfile.write('{"statuses"'+data_into_list[i][:-1])
    outfile.close()
    
    
