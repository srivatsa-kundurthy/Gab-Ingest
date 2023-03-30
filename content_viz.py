import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
plt.style.use('seaborn')

df = pd.read_csv('fuentes_finals/co-mentions/fuentes_alex jones_comentions.csv')

years = [2016,2017,2018,2019,2020,2021,2022,2023]
counter = []
for year in years:
    cnt = 0
    for item in df['date'].to_list():
        if str(year) in item:
            cnt+=1
            print('found')
    counter.append(cnt)
print(counter)

plt.plot(years,counter)

plt.title('Alex Jones Mentions Found in Fuentes Data')
plt.savefig('fuentes_finals/fuentes_jones_by_year.png')
plt.show()
print('COMPLETE')
#plt.plot_date(df['date'].to_list(),np.ones(len(df['date'].to_list())))
#plt.show()