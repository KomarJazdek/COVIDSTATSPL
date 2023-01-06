import requests
import matplotlib.pyplot as plt 


url = "https://opendata.ecdc.europa.eu/covid19/testing/json/"

api = requests.get('https://api.covid19api.com/dayone/country/poland')
PL = api.json()
cases = []
dates = []
for i in range(len(PL)):
	cases.append(PL[i]["Confirmed"])
	dates.append(PL[i]["Date"])
print(cases)

bar1_data = cases[2]
bar2_data = cases[(len(cases)-1)//2]
bar3_data = cases[(len(cases)-1)]
bar1_date = dates[2]+" "
bar2_date = dates[(len(dates)-1)//2]+" "
bar3_date = dates[(len(dates)-1)]
plt.title("COVID-19 W POLSCE")
bar1 = plt.bar(bar1_date,bar1_data)
bar2 = plt.bar(bar2_date,bar2_data)
bar3 = plt.bar(bar3_date,bar3_data)

plt.show()

