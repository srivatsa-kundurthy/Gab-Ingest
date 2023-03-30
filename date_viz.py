# visualization
import matplotlib.pyplot as plt
import pandas as pd
#from lineticks import LineTicks



df = pd.read_csv('milo_dates.csv')

df2 = df.iloc[::-1]
print(df2)

count = list(df2[df.columns[1]])
print(count)

#list(identical.keys())

dates = list(df2[df.columns[0]])
print(dates)

lower = dates.index('2020-02-29')
upper = dates.index('2023-03-05')
print(lower)
print(upper)
print(dates[lower:upper])
print(len(count[lower:upper]))
print(upper-lower+1)
print(dates[lower:upper])



plt.bar(dates[lower:upper], count[lower:upper])

plt.xticks(rotation=90)
plt.xticks(fontsize=5)


#plt.bar(range(len(dates)), count,tick_label=dates)

#plt.plot(count)

plt.title('milo Mentions')
plt.savefig('milo_mentions_bar_jan_6_vicinity.png')
plt.show()