import urllib.request
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"

request_url = urllib.request.urlopen(url)
lines = request_url.readlines()

names = [str(line).split(",")[5] for line in lines]

sc_index = names.index("Santa Clara")
sc_data = str(lines[sc_index]).split(",")[13:-1]
# sc_new_cases_data = [ int(sc_datai)-int(i-1)]

ny_index = names.index("New York")
ny_data = str(lines[ny_index]).split(",")[13:-1]

la_index = names.index("Los Angeles")
la_data = str(lines[la_index]).split(",")[13:-1]

sf_index = names.index("San Francisco")
sf_data = str(lines[sf_index]).split(",")[13:-1]

y =[ int(val) for val in sc_data]
y2 = [ int(val) for val in ny_data]
y3 = [ int(val) for val in la_data]
y4 = [int(val) for val in sf_data]
y5 = [(int(sc_data[i+1])-int(sc_data[i])) for i in range(len(sc_data)-1) ]
y6 = [(int(ny_data[i+1])-int(ny_data[i])) for i in range(len(ny_data)-1) ]
y7 = [int(la_data[i+1]) - int(la_data[i]) for i in range(len(la_data)-1)]
y8 = [int(sf_data[i+1]) - int(sf_data[i]) for i in range(len(sf_data)-1)]

x5 = [i for i in range(len(sc_data)-1)]
x6 = [i for i in range(len(ny_data)-1)]
x7 = [i for i in range(len(la_data)-1)]
x8 = [i for i in range(len(sf_data)-1)]

# plt.title("Coronavirus Cases")
# plt.xlabel("time (days)")
# plt.ylabel("# people")

plt.subplot(4,2,1)
plt.title("Daily New Coronavirus Cases in Santa Clara County")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x5,y5)

plt.subplot(4,2,2)
plt.title("Total Coronavirus Cases in Santa Clara County")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y,'k.-', label = "Santa Clara County")
# plt.legend(loc = "best")

plt.subplot(4,2,3)
plt.title("Daily New Coronavirus Cases in New York City")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x6,y6)

plt.subplot(4,2,4)
plt.title("Total Coronavirus Cases in New York City")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y2,'g*--', label="New York City")
#plt.legend(loc="best")

plt.subplot(4,2,5)
plt.title("Daily New Coronavirus Cases in Los Angeles")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x7,y7)

plt.subplot(4,2,6)
plt.title("Total Coronavirus Cases in Los Angeles")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y3,"r-", label ="Los Angeles") 
#plt.legend(loc = "best")

plt.subplot(4,2,7)
plt.title("Daily New Coronavirus Cases in San Francisco")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x8,y8)

plt.subplot(4,2,8)
plt.title("Total Coronavirus Cases in San Francisco")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y4,'k.-')
#plt.legend(loc = "best")

plt.subplots_adjust(left = 0.125, bottom = 0.1,right =0.9, top = 0.9, wspace = 0.2, hspace=0.6)
plt.show()
