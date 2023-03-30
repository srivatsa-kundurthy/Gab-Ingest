# Count and extract mentions of other influencers in json files

import pandas as pd

# fuentes_finals/fuentes_content.csv

df = pd.read_csv('fuentes_finals/fuentes_content.csv')

COMPARISON_TERM = 'alex jones'


# record idx of content mentions
# count mentions
idx_lst = []
cnt = 0
for i in range(len(df['Dates'].to_list())):
    if COMPARISON_TERM in df['Content'].to_list()[i].lower():
        idx_lst.append(i)
        cnt+=1

# record mentions and dates in seperate csv
date = [df['Dates'].to_list()[idx] for idx in idx_lst]
content = [df['Content'].to_list()[idx] for idx in idx_lst]

# write
df_peaks = pd.DataFrame({'date':date,'content':content})
df_peaks.to_csv(r'fuentes_finals/fuentes_' + COMPARISON_TERM + '_comentions.csv')
print('COMPLETE')

